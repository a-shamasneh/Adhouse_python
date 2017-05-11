# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from mongoengine import *
# Create your models here.
class User(Document):
    
    u_name = StringField(max_length=50)
    u_pass = StringField(max_length=50)
    u_email= StringField(required=True)
    u_phone= StringField(required=True)
    