from django.contrib import admin
from .models import User


class UserAdminManager(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'pin', 'is_superuser']
    list_display_links = ['username', ]


admin.site.register(User, UserAdminManager)
