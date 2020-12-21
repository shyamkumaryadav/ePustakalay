from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, Group
from .models import User
from django.utils.translation import gettext, gettext_lazy as _

admin.site.unregister(Group)



@admin.register(User)
class UserAdmins(UserAdmin):
    readonly_fields = ('image_tag', 'id')
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_defaulter')
    list_filter = ('is_defaulter', 'is_superuser', 'is_active', 'country')
    fieldsets = (
        (None, {'fields': (('image_tag', 'profile'), 'username', 'password')}),
        (_('Personal info'), {
            'classes': ('collapse',),
            'fields': ('first_name', 'middle_name', 'last_name', 'email', 'date_of_birth')
        }),
        (_('More info'), {
            'classes': ('collapse',),
            'fields': ('phone_number', 'country', 'state', 'city', 'pincode', 'full_address',)
        }),
        (_('Permissions'), {
            'classes': ('collapse',),
            'fields': ('is_defaulter', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {
            'classes': ('collapse',),
            'fields': ('last_login', 'date_joined')
        }),
    )
   
