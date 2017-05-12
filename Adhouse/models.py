# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from mongoengine import *
# Create your models here.
class User(models.Model):
    
    u_name = StringField(max_length=50)
    u_pass = StringField(max_length=50)
    u_email= StringField(required=True)
    
