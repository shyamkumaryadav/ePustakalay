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
            'language': ['exact'],
            'in_stock': ['exact'],
            'edition': ['exact'],
            'genre__name': ['contains'],
            'description': ['contains'],
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
        
class GenreFilter(filters.FilterSet):
    '''
    FilterSet of emanagement.models.Genre
    '''

    class Meta:
        model = models.Genre
        fields = {
            'name': ['contains'],
            'id': ['exact'],
        }