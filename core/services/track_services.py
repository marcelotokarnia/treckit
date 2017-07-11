from core.models import Track

def list_tracks():
    return Track.objects.all()


def get_track(pk):
    return Track.objects.get(pk=pk)