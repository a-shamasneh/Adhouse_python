from django.forms import ModelForm

from django import forms
from models import Advs

class ThingForm(ModelForm):
    class Meta:
        model = Advs
        fields = ('name', 'description',)

class AdvForm(forms.Form):
    #to take the input of Adv
    name = forms.CharField(max_length=100)
    # to take the input of email
    description = forms.CharField(max_length=100)
    # to take the input of password
    phone = forms.CharField(max_length=100)
    cat = forms.CharField(max_length=100)
    img = forms.CharField(max_length=100)
      
