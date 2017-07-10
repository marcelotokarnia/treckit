from core.models import TrailRecord

def list_trails():
    return TrailRecord.objects.all()