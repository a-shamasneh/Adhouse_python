# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from Adhouse.models import Advs
# Create your views here.
from forms import ThingForm
from forms import AdvForm
# to get current user id 




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
 
def Add(request):
    if request.method == 'POST':  # if the form has been filled

        form = AdvForm(request.POST)

        if form.is_valid():  # All the data is valid
            name = request.POST.get('name', '')
            description = request.POST.get('description', '')
            phone = request.POST.get('phone', '')
            cat = request.POST.get('cat', '')
            img = request.POST.get('img', '')
            userid=request.POST.get('userid', '')

        # creating an user object containing all the data
        ok = Advs(name=name, description=description, phone=phone,cat=cat,img=img,user_id=userid)
        # saving all the data in the current object into the database
        ok.save()
        things = Advs.objects.all()
        return render(request, 'index.html', {'things': things,'is_registered':True }) # Redirect after POST

    else:
        form = AdvForm()  # an unboundform

        return render(request, 'create_thing.html', {'form': form})

#the function executes with the showdata url to display the list of registered users
#the function executes with the showdata url to display the list of registered users
def showdata(request):
    things = Advs.objects.all()
    return render(request, 'index.html', {'things': things, })