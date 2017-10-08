import json
from django.http.response import JsonResponse, HttpResponse
from django.contrib import auth
from core.services import track_services
from core.decorators import ajax_login_required


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    user_dict = None
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            user_dict = _user2dict(user)
    return JsonResponse(user_dict)


def logout(request):
    auth.logout(request)
    return JsonResponse({})


def whoami(request):
    i_am = {
        'user': _user2dict(request.user),
        'authenticated': True,
    } if request.user.is_authenticated() else {'authenticated': False}
    return JsonResponse(i_am)


def get_user_details(request):
    username = request.GET['username']
    user = auth.get_user_model().objects.get(username=username)
    user_dict = _user2dict(user)
    return JsonResponse(user_dict)


def list_tracks(request):
    tracks = track_services.list_tracks()
    return JsonResponse([t.to_marker() for t in tracks], safe=False)


def get_track_details(request):
    track_id = request.GET.get('track_id') or request.POST.get('track_id')
    track = track_services.get_track(track_id)
    return JsonResponse(track.to_dict_json())


def get_track_kml(request):
    track_id = request.GET.get('track_id') or request.POST.get('track_id')
    name, kml = track_services.get_track_kml(track_id)
    response = HttpResponse(kml, content_type='application/vnd.google-earth.kml+xml')
    response['Content-Disposition'] = 'attachment; filename=%s' % name
    return response


def _user2dict(user):
    return {
        'username': user.username,
        'name': user.first_name,
        'permissions':{
            'ADMIN': user.is_superuser,
            'STAFF': user.is_staff,
        }
    }
