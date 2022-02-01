from django.contrib import admin
from .models import User


class UserAdminManager(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'pin', 'employee', 'role', 'is_superuser']
    search_fields = ['username', 'pin']
    list_filter = ['username', 'email', 'pin']
    list_display_links = ['username', ]


admin.site.register(User, UserAdminManager)
