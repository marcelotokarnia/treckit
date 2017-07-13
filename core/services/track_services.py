from core.models import Track
from core.adapter import postgis_adapter

def list_tracks():
    return Track.objects.all()


def get_track(pk):
    return Track.objects.get(pk=pk)


def save_trail_record(track_id, filepath):
    track = Track.objects.get(pk=track_id)
    postgis_adapter.gpx_to_gis(filepath, track)