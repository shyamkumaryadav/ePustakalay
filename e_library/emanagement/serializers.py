'''
All Serializers For Book Management

1. `BookSerializers`
'''
from rest_framework import serializers
from django.contrib.auth import get_user_model
from emanagement import models



class GenreSerializers(serializers.HyperlinkedModelSerializer):
    '''
    The Serializer of `emanagement.models.Genre`
    '''
    class Meta:
        model = models.Genre
        fields = '__all__'

class BookAuthorSerializers(serializers.HyperlinkedModelSerializer):
    '''
    The Serializer of `emanagement.models.BookAuthor`  
    '''

    genre_list = serializers.StringRelatedField(source="genre", many=True, read_only=True)

    class Meta:
        model = models.BookAuthor
        fields = '__all__'
        extra_kwargs = {'genre': {'write_only': True}}

class BookPublishSerializers(serializers.HyperlinkedModelSerializer):
    '''
    The Serializer of `emanagement.models.BookPublish`
    '''

    genre_list = serializers.StringRelatedField(source="genre", many=True, read_only=True)

    class Meta:
        model = models.BookPublish
        fields = ('url', 'company_name', 'website', 'genre_list', 'genre')
        extra_kwargs = {'genre': {'write_only': True}}





class BookSerializers(serializers.HyperlinkedModelSerializer):
    '''
    The Serializer of `emanagement.models.Book`
    '''
    genre_list = serializers.StringRelatedField(source="genre", many=True, read_only=True)
    # author = serializers.StringRelatedField(many=False, read_only=True)
    author_name = serializers.StringRelatedField(source='author', many=False, read_only=True)
    # publish = serializers.StringRelatedField(many=False, read_only=True)
    publish_by = serializers.StringRelatedField(source='publish', many=False, read_only=True)

    class Meta:
        model = models.Book
        fields = '__all__'
        # exclude = ['genre', 'language']
        extra_kwargs = {
            'genre': {'write_only': True},
            'author': {'write_only': True},
            'publish': {'write_only': True},
        }
        # depth = 1
   
    
class IssueSerializers(serializers.HyperlinkedModelSerializer):
    '''
    The Serializer of `emanagement.models.Issue`
    '''
    book = serializers.StringRelatedField(many= False, read_only=True)
    user = serializers.SlugRelatedField(many= False, read_only=True, slug_field="username")
    _return = serializers.SerializerMethodField()

    class Meta:
        model = models.Issue
        fields = '__all__'
        read_only_fields = ['due_date', 'book', 'user']
        # extra_kwargs = {
        #     'book': {'lookup_field': 'author'},
        # }

    def get__return(self, obj):
        return obj.due_date_end