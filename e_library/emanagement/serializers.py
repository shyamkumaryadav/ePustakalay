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
        fields = ['id', 'name']

class BookAuthorSerializers(serializers.HyperlinkedModelSerializer):
    '''
    The system.models.Book `Serializer`
    '''

    genre = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.BookAuthor
        fields = '__all__'


class BookPublishSerializers(serializers.HyperlinkedModelSerializer):
    '''
    The system.models.Book `Serializer`
    '''

    genre = serializers.StringRelatedField(many= True)

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
        fields = '__all__'

class IssueSerializers(serializers.HyperlinkedModelSerializer):
    '''
    The system.models.Book `Serializer`
    '''
    book = serializers.StringRelatedField(many= False, read_only=True)
    user = serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        model = models.Issue
        fields = '__all__'
        read_only_fields = ['due_date']
        # exclude = ['user']
