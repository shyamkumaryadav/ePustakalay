'''
All Serializers For Book Management

1. `BookSerializers`
'''
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.http import Http404
from emanagement import models

class  IssueSetSerializers(serializers.ModelSerializer):
    book_name = serializers.SlugRelatedField(source="book", many= False, read_only=True, slug_field="name")
    is_return = serializers.SerializerMethodField()


    class Meta:
        model = models.Issue
        fields = ['book_name', 'is_return', 'date', 'due_date',]
    
    def get_is_return(self, obj):
        return obj.due_date_end

class UserSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(read_only=True, view_name="user-detail")
    update = serializers.HyperlinkedIdentityField(read_only=True, view_name="user-update-user")
    setpassword = serializers.HyperlinkedIdentityField(read_only=True, view_name="user-set-password")
    issue_set = IssueSetSerializers( many=True, read_only=True)
    
    class Meta:
        model = get_user_model()
        fields = ['url', 'id', 'username', 'first_name', 'middle_name', 'last_name', 'email', 'phone_number', 'date_of_birth', 'country', 'state', 'city', 'pincode', 'full_address', 'is_defaulter', 'profile', 'groups', 'user_permissions','is_superuser', 'last_login', 'is_superuser', 'is_active', 'is_staff', 'date_joined', 'update', 'setpassword', 'issue_set']

class UserCreateSerializers(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True, required=True, validators=[validate_password])
    url = serializers.HyperlinkedIdentityField(read_only=True, view_name="user-detail")
    issue_set = IssueSetSerializers( many=True, read_only=True)

    class Meta(UserSerializer.Meta):
        fields = ['url', 'username', 'email', 'password', 'confirm_password', 'is_superuser', 'profile', 'last_login', 'date_joined', 'issue_set', ]
        read_only_fields = ['is_superuser', 'last_login', 'date_joined',]
        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': True,
                'style': {
                    'input_type': 'password'
                },
                'validators': [validate_password]
            },
        }

    # def validate_password(self, value):
    #     validate_password(value)
    #     return value
    
    # def validate(self, data):
    #     if data['password'] != data.pop('confirm_password'):
    #         raise serializers.ValidationError({"confirm_password": "Password not mathc!"})
    #     else:
    #         return data
    
    def create(self, validated_data):
        return self.Meta.model.objects.create_user(**validated_data)

class UserUpdateSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(read_only=True, view_name="user-detail")
    update = serializers.HyperlinkedIdentityField(read_only=True, view_name="user-update-user")
    setpassword = serializers.HyperlinkedIdentityField(read_only=True, view_name="user-set-password")
    issue_set = IssueSetSerializers( many=True, read_only=True)

    class Meta(UserSerializer.Meta):
        read_only_fields = ['last_login', 'is_superuser', 'is_active', 'is_staff', 'date_joined', 'username', 'is_defaulter', 'user_permissions', 'groups', 'password', 'issue_set',]

class UserPasswordSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True, required=True)
    old_password = serializers.CharField(style={'input_type': 'password'}, write_only=True, required=True)
    url = serializers.HyperlinkedIdentityField(read_only=True, view_name="user-detail")

    class Meta(UserSerializer.Meta):
        fields = ['url', 'old_password', 'password', 'confirm_password',]
        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': True,
                'style': {
                    'input_type': 'password'
                },
            },
        }
    def validate_password(self, value):
        validate_password(value)
        return value
    
    def validate(self, data):
        if data['password'] != data.pop('confirm_password'):
            raise serializers.ValidationError({"confirm_password": "Password not mathc!"})
        else:
            return data
        
    def validate_old_password(self, value):
        if self.context.get('request').user.check_password(value):
            return value
        raise serializers.ValidationError("Old Password wrong!!!")
            
        
    def update(self, instance, validated_data):
        instance.set_password(validated_data.get('password')).save()
        return instance




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
    bookname = serializers.SlugRelatedField(source="book", many= False, read_only=True, slug_field="name")
    username = serializers.SlugRelatedField(source="user", many= False, read_only=True, slug_field="username")
    user = serializers.SlugRelatedField(many= False, queryset=models.User.objects.filter(is_defaulter=False), write_only=True, slug_field="username")
    is_return = serializers.SerializerMethodField()

    class Meta:
        model = models.Issue
        fields = '__all__'
        # read_only_fields = ['due_date', 'book', 'user']
        # extra_kwargs = {
        #     'book': {'lookup_field': 'author'},
        # }

    def get_is_return(self, obj):
        return obj.due_date_end

   
    