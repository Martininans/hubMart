from django.contrib import admin
from django.contrib.auth.admin import  UserAdmin as BaseUserAdmin
from . models import Customer

# Register your models here.
@admin.register(Customer)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "usable_password", "password1", "password2","user_name"),
            },
        ),
    )