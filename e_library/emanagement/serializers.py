'''
All Serializers For Book Management

1. `BookSerializers`
'''
from rest_framework import serializers
from emanagement import models



class GenreSerializers(serializers.HyperlinkedModelSerializer):
    '''
    The system.models.Book `Serializer`
    '''
    class Meta:
        model = models.Genre
        fields = '__all__'

class BookAuthorSerializers(serializers.HyperlinkedModelSerializer):
    '''
    The system.models.Book `Serializer`
    '''

    genre = GenreSerializers(many= True)

    class Meta:
        model = models.BookAuthor
        fields = '__all__'


class BookPublishSerializers(serializers.HyperlinkedModelSerializer):
    '''
    The system.models.Book `Serializer`
    '''

    genre = GenreSerializers(many= True)
    
    class Meta:
        model = models.BookPublish
        fields = '__all__'




class BookSerializers(serializers.HyperlinkedModelSerializer):
    '''
    The system.models.Book `Serializer`
    '''
    genre = GenreSerializers(many= True)
    author = BookAuthorSerializers(many= False)
    publish = BookPublishSerializers(many= False)

    class Meta:
        model = models.Book
        fields = ['id', 'name', 'genre', 'author', 'publish', 'publish_date', 'date', 'language', 'edition', 'cost', 'page', 'description', 'stock', 'today_stock', 'rating', 'profile']
