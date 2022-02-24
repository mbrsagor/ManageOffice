from django.db import models
from django.contrib.auth.models import User

from utils.employee_info import Pay, Status


class BaseEntity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Department(BaseEntity):
    name = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Designation(BaseEntity):
    name = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Bank(BaseEntity):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Payment(BaseEntity):
    title = models.CharField(max_length=120)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='paymentEmployee')
    bank_name = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='paymentBank')
    pay_purpose = models.IntegerField(choices=Pay.payment_types(), default=Pay.SALARY.value)
    status = models.IntegerField(choices=Status.pay_status(), default=Status.REGULAR.value)
    amount = models.IntegerField(default=0)
    month = models.DateField()

    def __str__(self):
        return self.title[:50]
