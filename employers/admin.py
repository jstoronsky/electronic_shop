from django.contrib import admin
from employers.models import Employee
# Register your models here.


@admin.register(Employee)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'phone', 'last_login', 'is_active')
