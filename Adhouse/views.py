# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import mongoengine
from django.shortcuts import render
from models import User
# Create your views here.
from django.http import HttpResponse


#def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    #user=User.objects.create(
    	#email="pedro.kong@company.com",
    	#first_name="Pedro",
    	#last_name="Kong"

    	#)
    #user.save()

def index(request): 
   
    number=6
    return render(request, 'index.html',{
    	"number":number,
    	})
