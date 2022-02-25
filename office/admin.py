from django.contrib import admin
from .models import Department, Designation, Bank, Payment, Project, Task, Client

admin.site.register(Department)
admin.site.register(Designation)
admin.site.register(Bank)
admin.site.register(Payment)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Client)
