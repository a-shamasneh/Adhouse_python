# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from Adhouse.models import Advs
# Create your views here.
from forms import ThingForm


#def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    #user=User.objects.create(
    	#email="pedro.kong@company.com",
    	#first_name="Pedro",
    	#last_name="Kong"

    	#)
    #user.save()

def index(request):
    things = Advs.objects.all()

    return render(request, 'index.html', {
        'things': things,
    })

    # our new view
def thing_detail(request, id):
    # grab the object...
    thing = Advs.objects.get(id=id)

    # and pass to the template
    return render(request,'thing_detail.html', {
        'thing': thing,
    })

    #edit ad
def editadv(request, id):
	# grab the object
    thing = Advs.objects.get(id=id)
    # set the form we're using
    form_class = ThingForm

    # if we're coming to this view from a submitted form
    if request.method == 'POST':
        # grab the data from the submitted form and apply to
        # the form
        form = form_class(data=request.POST, instance=thing)
        if form.is_valid():
            # save the new data
            form.save()
            return redirect('thing_detail', id=thing.id)
    # otherwise just create the form
    else:
        form = form_class(instance=thing)

    # and render the template
    return render(request,'editadv.html', {
        'thing': thing,
        'form': form,
    })

    