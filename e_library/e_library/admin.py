from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, Group
from .models import User, City, Countrie, State
from django.utils.translation import gettext, gettext_lazy as _

admin.site.unregister(Group)

@admin.register(City)
class CityAdmins(admin.ModelAdmin):
    pass

@admin.register(Countrie)
class CountrieAdmins(admin.ModelAdmin):
    pass

@admin.register(State)
class StateAdmins(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmins(UserAdmin):
    # readonly_fields = ('image_tag', 'id')
    list_display = ('username', 'email', 'first_name', 'last_name', 'email')
    list_filter = ('is_defaulter', 'is_superuser', 'is_active', 'country')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {
            'classes': ('collapse',),
            'fields': ('first_name', 'middle_name', 'last_name', 'email', 'date_of_birth')
        }),
        (_('More info'), {
            'classes': ('collapse',),
            'fields': ('phone_number', 'country', 'state', 'city', 'pincode', 'full_address', 'profile')
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
   
