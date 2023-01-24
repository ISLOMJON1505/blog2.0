from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_from = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name', 'age', 'city' ,'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields' : ('age','city',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields' : ('age','city',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)