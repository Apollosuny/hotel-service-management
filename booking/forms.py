from django import forms
from booking.models import *
from room.models import *

class BookingForm(forms.Form):
    choices = Service.objects.all()
    checkin_date = forms.DateField(label='Check-in')
    checkout_date = forms.DateField(label='Check-out')
    services = forms.ModelMultipleChoiceField(queryset=choices, widget=forms.CheckboxSelectMultiple, required=False)
    rooms = forms.ModelMultipleChoiceField(queryset=Room.objects.all(), widget=forms.CheckboxSelectMultiple, required = False)
    total_price = forms.DecimalField(label='Total Price')
    def __init__(self, *args, **kwargs):
        room_type = kwargs.pop('room_type', None)
        super(BookingForm, self).__init__(*args, **kwargs)

        if room_type:
            all_rooms = Room.objects.filter(room_type__name=room_type)
            self.fields['rooms'].queryset = all_rooms
            self.fields['rooms'].label_from_instance = lambda obj: f"{obj.room_number} {obj.room_type.name} {obj.status}"

    
