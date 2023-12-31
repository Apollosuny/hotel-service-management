from django.db import models
from user.models import Customer
from room.models import Service, Room

# Create your models here.
class Booking(models.Model):

    class Meta:
        db_table = 'booking'

    class PaymentStatus(models.TextChoices):
        UNPAID = 'UNPAID'
        PARTIALLY_PAID = 'PARITIALLY_PAID'
        FULLY_PAID = 'FULLY_PAID'
        DEPOSIT = 'DEPOSIT'

    checkin_date = models.DateField()
    checkout_date = models.DateField()
    room_type = models.CharField(max_length=50, default='Mini Suite')
    total_price = models.FloatField()
    status = models.CharField(max_length=20, choices=PaymentStatus.choices, default=PaymentStatus.UNPAID)

    #relation
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    services = models.ManyToManyField(Service, null=True)
    rooms = models.ManyToManyField(Room, null=True)
    
class Payment(models.Model):

    class Meta: 
        db_table = 'payment'

    class PaymentMethod(models.TextChoices):
        CREDIT = 'CREDIT'
        CASH = 'CASH'

    amount = models.FloatField()
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=20, choices=PaymentMethod.choices)
    note = models.CharField(max_length=100)

    # relations
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)

    def __str__(self):
        return {
            'amount': self.amount,
            'payment-date': self.payment_date,
            'payment-method': self.payment_method
        }