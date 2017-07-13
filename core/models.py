from django.contrib.gis.db import models
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.auth.models import User
from utils.models_utils import BaseModel


class Track(BaseModel):
    name = models.CharField(max_length=1024)
    start = models.PointField()

    def to_marker(self):
        trail_record = self.trail_records.first()
        return {
            'name': self.name,
            'coords': {
                'latitude': self.start.y,
                'longitude': self.start.x
            },
            'id': self.id,
            'distance': trail_record.simplified_length,
            'accumulated_heights': trail_record.accumulated_heights,
            'accumulated_depths': trail_record.accumulated_depths
        }

    def to_dict_json(self):
        dictj = {
            'name': self.name,
            'coords': {
                'latitude': self.start.y,
                'longitude': self.start.x
            }
        }
        best_image = self.images.order_by('-votes').first()
        if best_image:
            dictj['best_image'] = best_image.to_dict_json()
        else:
            dictj['best_image'] = {}
        best_video = self.videos.order_by('-votes').first()
        if best_video:
            dictj['best_video'] = best_video.to_dict_json()
        else:
            dictj['best_video'] = {}
        best_text = self.texts.order_by('-votes').first()
        if best_text:
            dictj['best_text'] = best_text.to_dict_json()
        else:
            dictj['best_text'] = {}
        return dictj


class TextRecord(BaseModel):
    created_by = models.ForeignKey(User)
    record = models.TextField()
    votes = models.IntegerField(default=0)
    track = models.ForeignKey(Track, related_name="texts")


class ImageRecord(BaseModel):
    created_by = models.ForeignKey(User)
    image = models.CharField(max_length=1024)
    votes = models.IntegerField(default=0)
    track = models.ForeignKey(Track, related_name="images")


class VideoRecord(BaseModel):
    created_by = models.ForeignKey(User)
    type = models.CharField(max_length=128)
    link = models.CharField(max_length=1024)
    votes = models.IntegerField(default=0)
    track = models.ForeignKey(Track, related_name="videos")


class TrailRecord(BaseModel):
    created_by = models.ForeignKey(User)
    name = models.CharField(max_length=1024)
    votes = models.IntegerField(default=0)
    accumulated_heights = models.IntegerField()
    accumulated_depths = models.IntegerField()
    simplified_track = models.MultiLineStringField()
    track = models.ForeignKey(Track, related_name="trail_records")

    @property
    def simplified_length(self):
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