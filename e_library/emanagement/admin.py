from django.contrib import admin
from emanagement import models


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'author', 'publish', 'stock', 'today_stock')
    fieldsets = (
        (None, {'fields': ('id', 'name', 'author')}),
        ('Information', {
            'classes': ('collapse',),
            'fields': ('date', 'today_stock', 'genre', 'publish', 'language', 'edition', 'cost', 'page', 'description', 'stock', 'rating', 'profile')}),
    )
    search_fields = ('name',)
    readonly_fields = ('today_stock', 'id', 'date')
    ordering = ('name',)
    # actions = ['apply_discount', ]
    list_filter = ('edition', 'language', 'date')

admin.site.register(models.BookAuthor)
admin.site.register(models.BookPublish)
admin.site.register(models.Genre)
