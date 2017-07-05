from django.db import connection

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

def gpx_to_gis():
    pass
    # ogr2ogr -append -update -f PostgreSQL "PG:dbname='treckit'" /home/tokarnia/Downloads/cachoeira-do-tabuleiro.gpx