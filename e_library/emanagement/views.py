"""
views for management apps.
"""
from rest_framework import viewsets
from emanagement import serializers, models, filters


class BookAPI(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing `Book` Model.
    """
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializers
    # filter_backends = (filters.DjangoFilterBackend,)
    # filterset_fields = ('name', 'author', 'publish')
    filterset_class = filters.BookFilter
    
class BookAuthorAPI(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing `BookAuthor` Model.
    """
    queryset = models.BookAuthor.objects.all()
    serializer_class = serializers.BookAuthorSerializers
      
class BookPublishAPI(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing `BookPublish` Model.
    """
    queryset = models.BookPublish.objects.all()
    serializer_class = serializers.BookPublishSerializers

     
class GenreAPI(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing `Genre` Model.
    """
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializers


