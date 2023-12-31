from django import forms
from booking.models import *
from room.models import *

class UpdateRoomForm(forms.Form):
    room_number = forms.CharField(label="Room number")
    status = forms.CharField(label="Status")

    
