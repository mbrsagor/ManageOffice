import datetime
from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from utils.employee_info import Types, Roles, GENDER, MARITAL
from office.models import Bank, Department, BaseEntity


class Profile(BaseEntity):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee')
    departments = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department', blank=True,
                                    null=True)
    designations = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='designation', blank=True,
                                     null=True)
    bank_name = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='employeeBank', blank=True, null=True)
    bank_account_number = models.CharField(max_length=20, blank=True, null=True)
    bank_branch_name = models.CharField(max_length=20, blank=True, null=True)
    employee_type = models.IntegerField(choices=Types.employee_types(), default=Types.FULLTIME.value)
    role = models.IntegerField(choices=Roles.select_role(), default=Roles.EMPLOYEE.value)
    gender = models.IntegerField(choices=GENDER.select_gender(), default=GENDER.MALE.value)
    marital_status = models.IntegerField(choices=MARITAL.select_status(), default=MARITAL.UNMARRIED.value)
    address = models.TextField(blank=True)
    phn_num = models.CharField(max_length=14, blank=True, null=True)
    emergency_phn_num = models.CharField(max_length=14, blank=True, null=True)
    reference_name = models.CharField(max_length=20, blank=True, null=True)
    salary = models.IntegerField(default=0)
    date_of_birth = models.DateField(blank=True, null=True, default=now)
    documents = models.FileField(upload_to='documents', blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile', blank=True, null=True)

    def __str__(self):
        return self.user.username

    @property
    def get_photo_url(self):
        if self.profile_picture and hasattr(self.profile_picture, 'url'):
            return self.profile_picture.url
        else:
            return "/static/images/avatar.jpg"

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
