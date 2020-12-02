from django_filters import rest_framework as filters
from emanagement import models

class BookFilter(filters.FilterSet):

    class Meta:
        model = models.Book
        fields = {
            'name': ['contains', 'exact'],
            'genre__name': ['exact', 'contains'],
        }