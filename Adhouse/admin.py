# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.


# import your model
from Adhouse.models import Advs

class AdvAdmin(admin.ModelAdmin):
    model = Advs
    list_display = ('id','name', 'description','date','phone','cat','img')



admin.site.register(Advs, AdvAdmin)