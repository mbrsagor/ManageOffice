import datetime
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from office.models import Bank, Department, BaseEntity
from utils.employee_info import Types, Roles, GENDER, MARITAL


class Profile(BaseEntity):
    salary = models.IntegerField(default=0)
    address = models.TextField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phn_num = models.CharField(max_length=14, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True, default=now)
    designation = models.CharField(max_length=150, blank=True, null=True)
    reference_name = models.CharField(max_length=20, blank=True, null=True)
    bank_branch_name = models.CharField(max_length=20, blank=True, null=True)
    emergency_phn_num = models.CharField(max_length=14, blank=True, null=True)
    bank_account_number = models.CharField(max_length=20, blank=True, null=True)
    bank_name = models.ForeignKey(Bank, on_delete=models.CASCADE, blank=True, null=True)
    role = models.IntegerField(choices=Roles.select_role(), default=Roles.EMPLOYEE.value)
    gender = models.IntegerField(choices=GENDER.select_gender(), default=GENDER.MALE.value)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    employee_type = models.IntegerField(choices=Types.employee_types(), default=Types.FULLTIME.value)
    marital_status = models.IntegerField(choices=MARITAL.select_status(), default=MARITAL.UNMARRIED.value)
    documents = models.FileField(upload_to='documents/%y/%m', blank=True, null=True)
    avatar = models.ImageField(upload_to='profile/%y/%m', blank=True, null=True)

    def __str__(self):
        return self.user.username

    @property
    def get_photo_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        else:
            return "/static/images/avatar.svg"

    def calculate_age(self):
        age = datetime.date.today() - self.date_of_birth
        return int(age.days / 365.25)

    @property
    def make_full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = Profile.objects.get_or_create(user=instance)
        return profile


post_save.connect(create_user_profile, sender=User)
