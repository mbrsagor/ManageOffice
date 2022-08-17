from django.contrib import admin
from .models import Department, Designation, Bank, Payment, Project, Task, Client

admin.site.register([Department, Designation, Bank, Payment, Project, Task, Client])
