from django.db import connection
from django.contrib.gis.gdal import DataSource
from utils.gis_utils import f2geom, f2kml
from core.models import TrailRecord, TrackPoint, WayPoint

def gis_to_kml():
    kml = open('/tmp/xpto.kml', 'w')
    kml.write('<?xml version="1.0" encoding="UTF-8"?>')
    kml.write('<kml xmlns="http://www.opengis.net/kml/2.2">')
    kml.write('<Document>')
    kml.write('<Placemark>')
    with connection.cursor() as cursor:
        cursor.execute("SELECT ST_AsKML(wkb_geometry), name FROM waypoints")
        waypoint = cursor.fetchone()
        while waypoint:
            kml.write('<name>%s</name>' % waypoint[1])
            kml.write(waypoint[0])
            kml.write('</Placemark>')
            kml.write('<Placemark>')
            waypoint = cursor.fetchone()
        cursor.execute("SELECT ST_AsKML(ST_MakeLine(wkb_geometry)) FROM track_points")
        kml.write(cursor.fetchone()[0])
    kml.write('</Placemark>')
    kml.write('</Document>')
    kml.write('</kml>')
    kml.close()


def gpx_to_gis(filepath):
    # ogr2ogr -append -update -f PostgreSQL "PG:dbname='treckit'" /home/tokarnia/Downloads/cachoeira-do-tabuleiro.gpx
    datasource = DataSource(filepath)
    track = datasource['tracks'][0]
    first_point = datasource['track_points'][0]
    tr = TrailRecord(simplified_track=f2geom(track), start=f2geom(first_point), gpx=filepath,
                     kml=gpx_to_kml(datasource), name=track['name'].value)
    tr.save()
    for point in datasource['track_points']:
        TrackPoint(point=f2geom(point), time=point['time'].value, ele=point['ele'].value, trail_record=tr).save()
    for waypoint in datasource['waypoints']:
        WayPoint(point=f2geom(waypoint), ele=waypoint['ele'].value, name=waypoint['name'].value, trail_record=tr).save()


def gpx_to_kml(datasource):
    filepath = '/tmp/xpto.kml'
    with open(filepath, 'w') as kml:
        kml.write('<?xml version="1.0" encoding="UTF-8"?>')
        kml.write('<kml xmlns="http://www.opengis.net/kml/2.2">')
        kml.write('<Document>')
        kml.write('<Placemark>')
        for waypoint in datasource['waypoints']:
            kml.write('<name>%s</name>' % waypoint['name'].value)
            kml.write(f2kml(waypoint))
            kml.write('</Placemark>')
            kml.write('<Placemark>')
        track = datasource['tracks'][0]
        kml.write('<name>%s</name>' % track['name'].value)
        kml.write(f2kml(track))
        kml.write('</Placemark>')
        kml.write('</Document>')
        kml.write('</kml>')
    return filepath


def gis_to_gpx(trail_record_points, trail_record_waypoints):
    filepath = '/tmp/xpto.gpx'
    with open(filepath, 'w') as gpx:
        gpx.write('<?xml version="1.0" encoding="UTF-8"?><gpx creator="TRECKIT" version="1.1" xmlns="http://www.topografix.com/GPX/1/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd">')
        waypoints = WayPoint.objects.filter(trail_record__in=trail_record_waypoints)
        for wpt in waypoints:
            gpx.write(wpt.to_gpx())
        for trail_record in trail_record_points:
            gpx.write('<trk><name>%s</name><trkseg>' % trail_record.name)
            trail_points = TrackPoint.objects.filter(trail_record=trail_record).order_by('time')
            for trkpt in trail_points:
                gpx.write(trkpt.to_gpx())
            gpx.write('</trkseg></trk>')
        gpx.write('</gpx>')
    return filepath