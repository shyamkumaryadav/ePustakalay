'''
All Serializers For Book Management

1. `BookSerializers`
'''
from rest_framework import serializers
from django.contrib.auth import get_user_model
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

    genre_list = serializers.StringRelatedField(source="genre", many=True, read_only=True)

    class Meta:
        model = models.BookAuthor
        fields = '__all__'

class BookPublishSerializers(serializers.HyperlinkedModelSerializer):
    '''
    The system.models.Book `Serializer`
    '''

    genre_list = serializers.StringRelatedField(source="genre", many=True, read_only=True)

    class Meta:
        model = models.BookPublish
        fields = '__all__'




class BookSerializers(serializers.HyperlinkedModelSerializer):
    '''
    The system.models.Book `Serializer`
    '''
    genre_list = serializers.StringRelatedField(source="genre", many=True, read_only=True)
    author = serializers.StringRelatedField(many=False, read_only=True)
    author_url = serializers.HyperlinkedRelatedField(source='author', many=False, read_only=True, view_name='bookauthor-detail')
    publish = serializers.StringRelatedField(many=False, read_only=True)
    publish_url = serializers.HyperlinkedRelatedField(source='publish', many=False, read_only=True, view_name='bookpublish-detail')

    class Meta:
        model = models.Book
        # fields = '__all__'
        exclude = ['genre', 'language']
   
    
class IssueSerializers(serializers.HyperlinkedModelSerializer):
    '''
    The system.models.Book `Serializer`
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