"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from Adhouse import views
urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^Add/', include('Adhouse.urls')),
    # The new URL entries we're adding:
   
    url(r'^things/(?P<id>[-\w]+)/$', views.thing_detail, 
        name='thing_detail'),
    url(r'^things/(?P<id>[-\w]+)/edit/$', views.editadv,
    	name='editadv'), 
    url(r'^accounts/', 
        include('registration.backends.simple.urls')),

    url(r'^admin/', admin.site.urls),
]
