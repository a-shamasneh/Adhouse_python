# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import User
# Create your views here.
from django.http import HttpResponse


def index(request):
    user=User.objects.create(
    	email="a.ashamasneh@gmail.com",
    	first_name="Ahmad",
    	last_name="Shamasneh"

    	)
    user.save()
    return HttpResponse("Hello, world. You're at the polls index.")


