from django_filters import rest_framework as filters
from emanagement import models

class BookFilter(filters.FilterSet):
    '''
    FilterSet of emanagement.models.Book
    '''

    class Meta:
        model = models.Book
        fields = {
            'name': ['contains'],
            'cost': ['range'],
            'rating': ['range'],
            'genre__name': ['contains'],
            'author__first_name': ['contains'],
            'publish__company_name': ['contains'],
        }