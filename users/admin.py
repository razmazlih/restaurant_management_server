from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'address', 'phone_number', 'loyalty_points')}),
    )

    readonly_fields = ('is_staff_member',)  # Make is_staff_member read-only in admin

    def save_model(self, request, obj, form, change):
        # Ensure the role logic applies in the admin save as well
        if obj.role != 'customer':
            obj.is_staff_member = True
        else:
            obj.is_staff_member = False
        super().save_model(request, obj, form, change)

admin.site.register(CustomUser, CustomUserAdmin)