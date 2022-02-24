from django.contrib import admin
from .models import Department, Designation, Bank, Payment

admin.site.register(Department)
admin.site.register(Designation)
admin.site.register(Bank)
admin.site.register(Payment)
