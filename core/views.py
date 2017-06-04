import json
from django.http.response import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import auth
# from core.models import Camera
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


@ajax_login_required
def list_cameras(request):
    return JsonResponse([], safe=False)


def _user2dict(user):
    return {
        'username': user.username,
        'name': user.first_name,
        'permissions':{
            'ADMIN': user.is_superuser,
            'STAFF': user.is_staff,
        }
    }