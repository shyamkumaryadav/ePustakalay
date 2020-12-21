from django.contrib import admin
from emanagement import models


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'author', 'publish', 'in_stock', 'cost',)
    fieldsets = (
        (None, {'fields': ('id', 'name', 'author')}),
        ('Information', {
            'classes': ('wide','extrapretty',),
            'fields': ('in_stock', 'date', 'update_date', 'today_stock', 'genre', 'publish', 'language', 'edition', 'cost', 'page', 'description', 'stock', 'rating', 'profile')}),
    )
    search_fields = ('name',)
    readonly_fields = ('today_stock', 'id', 'date', 'in_stock', 'update_date')
    ordering = ('name',)
    list_filter = ('in_stock', 'edition', 'language', 'date')

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
