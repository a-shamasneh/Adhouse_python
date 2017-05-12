# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Advs(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    phone = models.CharField(max_length=255)
    cat = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    #relation one to many
    user = models.ForeignKey(User, on_delete=models.CASCADE)




    