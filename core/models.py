from django.contrib.gis.db import models


class TrailRecord(models.Model):
    name = models.CharField(max_length=1024)
    kml = models.CharField(max_length=512)
    gpx = models.CharField(max_length=512)
    start = models.PointField()
    simplified_track = models.MultiLineStringField()


class TrackPoint(models.Model):
    point = models.PointField()
    time = models.DateTimeField()
    ele = models.IntegerField()
    trail_record = models.ForeignKey(TrailRecord, related_name='trackpoints')


class WayPoint(models.Model):
    point = models.PointField()
    ele = models.IntegerField()
    name = models.CharField(max_length=1024)
    trail_record = models.ForeignKey(TrailRecord, related_name='waypoints')