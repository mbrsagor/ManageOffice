from datetime import date, datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

from utils.role_type import Roles, Types


class DomainEntity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(AbstractUser, DomainEntity):
    pin = models.CharField(max_length=15, unique=True)
    employee = models.ForeignKey(Types, on_delete=models.CASCADE, related_name='employee_type')
    role = models.ForeignKey(Roles, on_delete=models.CASCADE, related_name='user_role')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'pin']

    def __str__(self):
        return self.pin


class Profile(DomainEntity):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    date_of_birth = models.DateField(default=datetime.now)
    nid_number = models.IntegerField(unique=True, max_length=15, blank=True, null=True)
    phone_number = models.IntegerField(unique=True, max_length=11)
    emergency_phone_number = models.IntegerField(unique=True, max_length=11, blank=True, null=True)
    address = models.TextField(default='')
    bank_account = models.CharField(max_length=20, blank=True, null=True)
    bank_name = models.TextField(default='')
    eduction = models.TextField(help_text='add your education qualification')
    documents = models.FileField(upload_to='documents/%y/%m', blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile/%y/%m', blank=True, null=True)

    def __str__(self):
        return self.user.username

    @property
    def current_age(self):
        today = date.today()
        return (today - self.date_of_birth).days


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = Profile.objects.get_or_create(user=instance)
        return profile


post_save.connect(create_user_profile, sender=User)
