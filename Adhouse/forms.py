from django.forms import ModelForm

from models import Advs

class ThingForm(ModelForm):
    class Meta:
        model = Advs
        fields = ('name', 'description',)