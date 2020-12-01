from django.contrib import admin
from management import models


admin.site.register(models.Book)
admin.site.register(models.BookAuthor)
admin.site.register(models.BookPublish)
admin.site.register(models.Genre)
