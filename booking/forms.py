from django import forms
from booking.models import *
from room.models import *

class BookingForm(forms.Form):
    choices = Service.objects.all()
    all_rooms = Room.objects.all()
    checkin_date = forms.DateField(label='Check-in')
    checkout_date = forms.DateField(label='Check-out')
    services = forms.ModelMultipleChoiceField(queryset=choices, widget=forms.CheckboxSelectMultiple)
    rooms = forms.ModelMultipleChoiceField(queryset=all_rooms, widget=forms.CheckboxSelectMultiple)
