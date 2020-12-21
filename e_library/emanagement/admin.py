from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, Group
from emanagement import models
from django.utils.translation import gettext_lazy as _

admin.site.unregister(Group)

@admin.register(models.User)
class UserAdmins(UserAdmin):
    readonly_fields = ('image_tag', 'id', 'last_login', 'date_joined')
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
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', ('image_tag', 'profile')),
        }),
    )
   


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'author', 'publish', 'in_stock', 'cost',)
    fieldsets = (
        (None, {'fields': (('image_tag', 'profile'), 'name', 'author')}),
        ('Information', {
            'classes': ('wide','extrapretty',),
            'fields': ('in_stock', 'date', 'update_date', 'today_stock', 'genre', 'publish', 'language', 'edition', 'cost', 'page', 'description', 'stock', 'rating')}),
    )
    search_fields = ('name',)
    readonly_fields = ('today_stock', 'id', 'date', 'in_stock', 'update_date', 'image_tag')
    ordering = ('name',)
    list_filter = ('in_stock', 'date')

admin.site.register(models.BookAuthor)
admin.site.register(models.BookPublish)

@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'id')
    readonly_fields = ('name',)

@admin.register(models.Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user', 'book', '_due_date_end',)
    list_filter = ('date',)
    readonly_fields = ('date','_due_date_end')
