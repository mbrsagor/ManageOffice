import datetime
from django.db import models
from django.contrib.auth.models import User

from utils.employee_info import Pay, Status, Evolution


class BaseEntity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        abstract = True


class Department(BaseEntity):
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Designation(BaseEntity):
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Bank(BaseEntity):
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Payment(BaseEntity):
    month = models.DateField()
    amount = models.IntegerField(default=0)
    title = models.CharField(max_length=120)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    pay_purpose = models.IntegerField(choices=Pay.payment_types(), default=Pay.SALARY.value)
    status = models.IntegerField(choices=Status.pay_status(), default=Status.REGULAR.value)

    def __str__(self):
        return self.title[:50]


class Client(BaseEntity):
    address = models.TextField()
    email = models.EmailField(blank=True)
    name = models.CharField(max_length=30)
    phn_num = models.CharField(max_length=14)
    organization = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return self.name


class Project(BaseEntity):
    name = models.CharField(max_length=100)
    description = models.TextField()
    budget = models.IntegerField()
    date_line = models.DateField()
    is_active = models.BooleanField(default=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True)
    reference_name = models.CharField(max_length=30, blank=True, null=True)
    document = models.FileField(upload_to='project/%y/%m', blank=True, null=True)
    image = models.ImageField(upload_to='project/%y/%m', blank=True, null=True)
    payment_status = models.IntegerField(choices=Status.pay_status(), default=Status.ADVANCE.value)
    status = models.IntegerField(choices=Evolution.task_status(), default=Evolution.PROGRESS.value)

    def __str__(self):
        return self.name

    @property
    def start_day(self):
        day = datetime.date.today() - self.date_line
        return int(day.days / 365.25)


class Task(BaseEntity):
    assigned_date = models.DateField()
    task_name = models.CharField(max_length=120)
    users = models.ManyToManyField(User, related_name='taskMember')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project')
    status = models.IntegerField(choices=Evolution.task_status(), default=Evolution.PROGRESS.value)
    assigned_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='taskOwner', blank=True)

    def __str__(self):
        return self.task_name[:50]

    @property
    def total_working_day(self):
        day = Project.date_line - self.assigned_date
        return day
