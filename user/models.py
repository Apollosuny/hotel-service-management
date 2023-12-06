from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from datetime import date

class Roles(models.TextChoices):
    SUPERADMIN = 'SUPERADMIN'
    STAFF = 'STAFF'
    USER = 'USER'

class CustomUserManager(BaseUserManager):

    def create_superuser(self, username, email, password, **other_fields):

        other_fields.setdefault('role', Roles.SUPERADMIN)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')

        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        if other_fields.get('role') != Roles.SUPERADMIN:
            raise ValueError(
                'Superuser must be assigned to role=SUPERADMIN.')

        return self.create_user(username, email, password, **other_fields)

    def create_user(self, username, email, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):

    class Meta:
        db_table = 'user'

    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    role = models.CharField(max_length=10, choices=Roles.choices, default=Roles.USER)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username + ' - ' + self.email

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'USER' and not instance.is_superuser:
        Customer.objects.create(user=instance)
    elif created and instance.role == 'STAFF' and not instance.is_superuser:
        Staff.objects.create(user=instance)

class Customer(models.Model):

    class Meta:
        db_table = 'customer'

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12, null=True)
    national_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # relations
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Staff(models.Model):
    
    class Meta:
        db_table = 'staff'

    class Position(models.TextChoices):
        MANAGER = 'MANAGER'
        RECEPTIONIST = 'RECEPTIONIST'

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField(null=True)
    phone = models.CharField(max_length=12, null=True)
    address = models.CharField(max_length=100)
    avatar = models.ImageField(default='default.jpg')
    position = models.CharField(max_length=20, choices=Position.choices, default=Position.RECEPTIONIST)
    national_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # relations
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' - ' + self.position



