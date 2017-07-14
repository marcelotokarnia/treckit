from django.contrib.gis.geos import GEOSGeometry


def geom2kml(geom):
    return GEOSGeometry(geom).kml


def f2geom(feat):
    return GEOSGeometry(str(feat.geom))


def f2kml(feat):
    return GEOSGeometry(str(feat.geom)).kml
