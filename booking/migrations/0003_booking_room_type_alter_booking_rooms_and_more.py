# Generated by Django 4.2.7 on 2023-12-24 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_alter_service_status'),
        ('booking', '0002_booking_rooms'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='room_type',
            field=models.CharField(default='Mini Suite', max_length=50),
        ),
        migrations.AlterField(
            model_name='booking',
            name='rooms',
            field=models.ManyToManyField(null=True, to='room.room'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='services',
            field=models.ManyToManyField(null=True, to='room.service'),
        ),
    ]
