from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User

class AccountAdmin(UserAdmin):  # This class is used to make sure that the hashed password is not shown in django admin and show other features like is active, date joined etc
    list_display = ('email', 'full_name', 'phone', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('full_name', 'phone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'phone', 'password1', 'password2', 'groups'),
        }),
    )
    search_fields = ('email', 'full_name', 'phone')
    ordering = ('email',)
    filter_horizontal = ('groups',)


admin.site.register(User, AccountAdmin)