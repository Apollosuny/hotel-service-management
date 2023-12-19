from django import forms
from room.models import *

class RoomTypeForm(forms.Form):
    name = forms.CharField(label='Name', max_length='50')
    description = forms.CharField(label='Description', max_length='100')
    price = forms.DecimalField(label='Price')
    numb_adults = forms.IntegerField(label='Number of adults')
    numb_children = forms.IntegerField(label='Number of children')

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_type', 'room_number']

class ServiceForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50)
    description = forms.CharField(label='Description', max_length=100)
    price = forms.DecimalField(label='Price')
