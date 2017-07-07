from django.contrib.gis.geos import GEOSGeometry


def f2geom(feat):
    return GEOSGeometry(str(feat.geom))


def f2kml(feat):
    return GEOSGeometry(str(feat.geom)).kml
