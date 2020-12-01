'''
All Serializers For Book Management

1. `BookSerializers`
'''
from rest_framework import serializers
from management import models


class BookSerializers(serializers.HyperlinkedModelSerializer):
    '''
    The system.models.Book `Serializer`
    '''
    class Meta:
        model = models.Book
        fields = '__all__'


class BookAuthorSerializers(serializers.HyperlinkedModelSerializer):
    '''
    The system.models.Book `Serializer`
    '''
    class Meta:
        model = models.BookAuthor
        fields = '__all__'


class BookPublishSerializers(serializers.HyperlinkedModelSerializer):
    '''
    The system.models.Book `Serializer`
    '''
    class Meta:
        model = models.BookPublish
        fields = '__all__'


class GenreSerializers(serializers.HyperlinkedModelSerializer):
    '''
    The system.models.Book `Serializer`
    '''
    class Meta:
        model = models.Genre
        fields = ['url', 'id', 'name',]
