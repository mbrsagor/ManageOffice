import datetime
from django.db import models
from django.contrib.auth.models import User

from utils.employee_info import Pay, Status, Evolution


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


class Project(BaseEntity):
    name = models.CharField(max_length=100)
    description = models.TextField()
    budget = models.IntegerField()
    client_name = models.CharField(max_length=30)
    client_phn_num = models.CharField(max_length=14)
    client_email = models.EmailField(blank=True)
    reference_name = models.CharField(max_length=30, blank=True, null=True)
    date_line = models.DateField()
    payment_status = models.IntegerField(choices=Status.pay_status(), default=Status.ADVANCE.value)
    is_active = models.BooleanField(default=True)
    status = models.IntegerField(choices=Evolution.task_status(), default=Evolution.PROGRESS.value)
    document = models.FileField(upload_to='project', blank=True, null=True)
    image = models.ImageField(upload_to='project', blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def start_day(self):
        day = datetime.date.today() - self.date_line
        return int(day.days / 365.25)


class Task(BaseEntity):
    task_name = models.CharField(max_length=120)
    project_name = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project')
    assigned_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='taskOwner', blank=True)
    assigned_users = models.ManyToManyField(User, related_name='taskMember')
    assigned_date = models.DateField()
    status = models.IntegerField(choices=Evolution.task_status(), default=Evolution.PROGRESS.value)

    def __str__(self):
        return self.task_name[:50]

    @property
    def total_working_day(self):
        day = Project.date_line - self.assigned_date
        return day
