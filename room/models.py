from django.db import models

# Create your models here.

class RoomType(models.Model):

    class Meta: 
        db_table = 'room-type'

    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    num_adults = models.IntegerField()
    num_children = models.IntegerField()

class Room(models.Model):

    class Meta:
        db_table = 'room'
    
    class Status(models.TextChoices):
        EMPTY = 'EMPTY'
        CLEAN = 'CLEAN'
        BOOKED = 'BOOKED'

    room_number = models.CharField(max_length=10)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.EMPTY)

    # relations
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)

class Service(models.Model):

    class Meta:
        db_table = 'service'

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name + ' - ' + str(self.price)

