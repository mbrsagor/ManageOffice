from datetime import date, datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.core.validators import MinValueValidator, MaxValueValidator

from utils.role_type import Roles, Types, GENDER
from .manager import UserManager


class DomainEntity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(AbstractUser):
    pin = models.CharField(max_length=15, unique=True)
    employee = models.IntegerField(choices=Types.employee_types(), default=Types.FULLTIME.value)
    role = models.IntegerField(choices=Roles.select_role(), default=Roles.EMPLOYEE.value)

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'pin']

    def __str__(self):
        return self.pin


class Profile(DomainEntity):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    date_of_birth = models.DateField(default=datetime.now)
    gender = models.IntegerField(choices=GENDER.select_gender(), default=GENDER.MALE.value)
    nid_number = models.IntegerField(unique=True, validators=[MinValueValidator(13), MaxValueValidator(17)], blank=True,
                                     null=True)
    phn_num = models.IntegerField(unique=True, blank=True, null=True,
                                  validators=[MinValueValidator(11), MaxValueValidator(14)])
    emergency_phn_num = models.IntegerField(unique=True, blank=True, null=True,
                                            validators=[MinValueValidator(11), MaxValueValidator(14)])
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
