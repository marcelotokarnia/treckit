from django.contrib.gis.db import models
from django.contrib.gis.geos import GEOSGeometry


class TrailRecord(models.Model):
    name = models.CharField(max_length=1024)
    start = models.PointField()
    accumulated_heights = models.IntegerField()
    accumulated_depths = models.IntegerField()
    simplified_track = models.MultiLineStringField()

    def to_marker(self):
        return {
            'title': self.name,
            'coords': {
                'latitude': self.start.y,
                'longitude': self.start.x
            },
            'id': self.id,
            'distance': self.simplified_distance,
            'accumulated_heights': self.accumulated_heights,
            'accumulated_depths': self.accumulated_depths
        }

    @property
    def simplified_distance(self):
        geometry = GEOSGeometry(self.simplified_track)
        geometry.transform(3857)
        return geometry.length


class TrackPoint(models.Model):
    point = models.PointField()
    time = models.DateTimeField()
    ele = models.IntegerField()
    trail_record = models.ForeignKey(TrailRecord, related_name='trackpoints')

    def to_gpx(self):
        return '<trkpt lat="%s" lon="%s"><ele>%s</ele><time>%s</time></trkpt>' % (
            self.point.y, self.point.x, self.ele, self.time.strftime('%Y-%m-%dT%H:%M:%SZ'))


class WayPoint(models.Model):
    point = models.PointField()
    ele = models.IntegerField()
    name = models.CharField(max_length=1024)
    trail_record = models.ForeignKey(TrailRecord, related_name='waypoints')

    def to_gpx(self):
        return '<wpt lat="%s" lon="%s"><ele>%s</ele><name>%s</name></wpt>' % (
            self.point.y, self.point.x, self.ele, self.name
        )