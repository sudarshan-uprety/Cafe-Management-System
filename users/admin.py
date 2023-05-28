from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User

class AccountAdmin(UserAdmin):  # This class is used to make sure that the hashed password is not shown in django admin and show other features like is active, date joined etc
    list_display = (
        "email",
        "full_name",
        "last_login",
        "date_joined",
        "is_active",
    )
    list_display_links = ("email", "full_name")
    readonly_fields = ("last_login", "date_joined")
    ordering = ("-date_joined",)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User, AccountAdmin)