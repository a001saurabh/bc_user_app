# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Users


def index(request):
    user_list = Users.objects.all[:]
    output = ', '.join([q.user_id for q in user_list])
    return HttpResponse(output)

def user_details(request, user_id):
    return HttpResponse("%s." % Users.name)
