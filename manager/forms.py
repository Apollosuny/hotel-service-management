from django import forms
from room.models import *

class RoomTypeForm(forms.Form):
    name = forms.CharField(label='Name Room Type', max_length='50')
    description = forms.CharField(label='Description', max_length='200')
    price = forms.DecimalField(label='Price')
    numb_adults = forms.IntegerField(label='Number of adults')
    numb_children = forms.IntegerField(label='Number of children')
    banner = forms.CharField(label='Banner', required=False, max_length=200)

class RoomForm(forms.Form):
    room_number = forms.CharField(label='Room Number')
    room_type = forms.ModelChoiceField(
        queryset=RoomType.objects.all(), 
        to_field_name='name', 
        widget=forms.Select(attrs={'class': 'form-control'})
    )

class UpdateRoomForm(forms.Form):
    room_number = forms.CharField(label="Room number")
    room_type = forms.ModelChoiceField(
        queryset=RoomType.objects.all(), 
        to_field_name='name', 
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    status = forms.CharField(label="Status")

class ServiceForm(forms.Form):
    name = forms.CharField(label='Name Service', max_length=50)
    description = forms.CharField(label='Description', max_length=200)
    price = forms.DecimalField(label='Price')
