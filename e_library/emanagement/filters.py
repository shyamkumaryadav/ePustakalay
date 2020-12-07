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


class BookPublishFilter(filters.FilterSet):
    '''
    FilterSet of emanagement.models.BookPublish
    '''

    class Meta:
        model = models.BookPublish
        fields = {
            'company_name': ['contains'],
            'genre__name': ['contains'],
        }


class BookAuthorFilter(filters.FilterSet):
    '''
    FilterSet of emanagement.models.BookAuthor
    '''

    class Meta:
        model = models.BookAuthor
        fields = {
            'first_name': ['contains'],
            'genre__name': ['contains'],
        }