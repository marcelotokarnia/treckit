from django.db import connection
from django.contrib.gis.gdal import DataSource
from utils.gis_utils import f2geom, f2kml
from core.models import TrailRecord, TrackPoint, WayPoint

def gis_to_kml():
    kml = open('/tmp/xpto.kml', 'w')
    kml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    kml.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
    kml.write('<Document>\n')
    kml.write('<Placemark>\n')
    with connection.cursor() as cursor:
        cursor.execute("SELECT ST_AsKML(wkb_geometry), name FROM waypoints")
        waypoint = cursor.fetchone()
        while waypoint:
            kml.write('<name>%s</name>\n' % waypoint[1])
            kml.write(waypoint[0] + '\n')
            kml.write('</Placemark>\n')
            kml.write('<Placemark>\n')
            waypoint = cursor.fetchone()
        cursor.execute("SELECT ST_AsKML(ST_MakeLine(wkb_geometry)) FROM track_points")
        kml.write(cursor.fetchone()[0] + '\n')
    kml.write('</Placemark>\n')
    kml.write('</Document>\n')
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
    kml = open(filepath, 'w')
    kml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    kml.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
    kml.write('<Document>\n')
    kml.write('<Placemark>\n')
    for waypoint in datasource['waypoints']:
        kml.write('<name>%s</name>\n' % waypoint['name'].value)
        kml.write(f2kml(waypoint) + '\n')
        kml.write('</Placemark>\n')
        kml.write('<Placemark>\n')
    track = datasource['tracks'][0]
    kml.write('<name>%s</name>\n' % track['name'].value)
    kml.write(f2kml(track) + '\n')
    kml.write('</Placemark>\n')
    kml.write('</Document>\n')
    kml.write('</kml>')
    kml.close()
    return filepath
