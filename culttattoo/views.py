from django.shortcuts import render
from .models import *
from django.contrib import auth
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

def get_data(request):
    return json.loads(request.body.decode("utf-8"))

@csrf_exempt
def get_up_master(request):
    up = UserProfile.objects.all()[0]
    response = json.dumps({'first_name': up.get_first_name(),
                               'last_name': up.get_last_name(),
                               'adress': up.get_adress(),
                               'rating': up.get_rating(),
                               'about': up.get_about()})
    return HttpResponse(response)