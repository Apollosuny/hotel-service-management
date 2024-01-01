from django import forms
from booking.models import *
from room.models import *

class BookingForm(forms.Form):
    class PaymentStatus(models.TextChoices):
        UNPAID = 'UNPAID'
        PARTIALLY_PAID = 'PARITIALLY_PAID'
        FULLY_PAID = 'FULLY_PAID'
        DEPOSIT = 'DEPOSIT'

    choices = Service.objects.all()
    checkin_date = forms.DateField(label='Check-in')
    checkout_date = forms.DateField(label='Check-out')
    services = forms.ModelMultipleChoiceField(queryset=choices, widget=forms.CheckboxSelectMultiple, required=False)
    rooms = forms.ModelMultipleChoiceField(queryset=Room.objects.all(), widget=forms.CheckboxSelectMultiple, required = False)
    total_price = forms.DecimalField(label='Total Price')
    status = forms.CharField(
        widget=forms.Select(choices=Booking.PaymentStatus.choices),
    )
    def __init__(self, *args, **kwargs):
        room_type = kwargs.pop('room_type', None)
        selected_services = kwargs.pop('selected_services', None)
        super(BookingForm, self).__init__(*args, **kwargs)

        if room_type:
            all_rooms = Room.objects.filter(room_type__name=room_type, status="EMPTY")
            self.fields['rooms'].queryset = all_rooms
            self.fields['rooms'].label_from_instance = lambda obj: f"{obj.room_number} {obj.room_type.name} {obj.status}"

        
        if selected_services:
            selected_service_ids = [service.id for service in selected_services]
            all_services = Service.objects.exclude(id__in=selected_service_ids)
            self.fields['services'].queryset = all_services
            self.fields['services'].label_from_instance = lambda obj: obj.name
    
