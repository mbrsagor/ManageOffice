from django.contrib import admin
from .models import User


class UserAdminManager(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'pin', 'role', 'is_superuser', 'last_login']
    search_fields = ['username', 'pin']
    list_filter = ['username', 'email', 'pin']
    list_display_links = ['username', ]


admin.site.register(User, UserAdminManager)
