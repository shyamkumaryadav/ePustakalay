"""
views for management apps.
"""
from rest_framework import viewsets
from management import serializers, models


class BookAPI(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing `Book` Model.
    """
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializers
    
class BookAuthorAPI(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing `BookAuthor` Model.
    """
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookAuthorSerializers
      
class BookPublishAPI(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing `BookPublish` Model.
    """
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookPublishSerializers

     
class GenreAPI(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing `Genre` Model.
    """
    queryset = models.Book.objects.all()
    serializer_class = serializers.GenreSerializers


