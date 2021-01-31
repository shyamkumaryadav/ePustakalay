'''
All Serializers For Book Management

1. `BookSerializers`
'''
from rest_framework import serializers
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.encoding import force_text
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.utils.http import urlsafe_base64_decode as uid_decoder
from django.contrib.auth.tokens import default_token_generator
from django.http import Http404
from emanagement import models
from django.utils.translation import ugettext_lazy as _

UserModel = get_user_model()

class  IssueSetSerializers(serializers.ModelSerializer):
    book_name = serializers.SlugRelatedField(source="book", many= False, read_only=True, slug_field="name")
    is_return = serializers.SerializerMethodField()


    class Meta:
        model = models.Issue
        fields = ['book_name', 'is_return', 'date', 'due_date',]
    
    def get_is_return(self, obj):
        return obj.due_date_end

class UserSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(read_only=True, view_name="user-detail", lookup_field='username')
    update = serializers.HyperlinkedIdentityField(read_only=True, view_name="user-update-user", lookup_field='username')
    setpassword = serializers.HyperlinkedIdentityField(read_only=True, view_name="user-change-password", lookup_field='username')
    issue_set = IssueSetSerializers( many=True, read_only=True)
    
    class Meta:
        model = UserModel
        fields = ['url', 'id', 'username', 'first_name', 'middle_name', 'last_name', 'email', 'phone_number', 'date_of_birth', 'country', 'state', 'city', 'pincode', 'full_address', 'is_defaulter', 'profile', 'groups', 'user_permissions','is_superuser', 'last_login', 'is_superuser', 'is_active', 'is_staff', 'date_joined', 'update', 'setpassword', 'issue_set']

class UserCreateSerializers(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type': 'password', 'autocomplete': 'new-password'}, write_only=True, required=True,) # validators=[validate_password])
    url = serializers.HyperlinkedIdentityField(read_only=True, view_name="user-detail", lookup_field='username')
    issue_set = IssueSetSerializers( many=True, read_only=True)

    class Meta(UserSerializer.Meta):
        fields = ['url', 'username', 'email', 'password', 'confirm_password', 'is_superuser', 'profile', 'last_login', 'date_joined', 'issue_set', ]
        read_only_fields = ['is_superuser', 'last_login', 'date_joined',]
        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': True,
                'style': {
                    'input_type': 'password',
                    'autocomplete': 'new-password'
                },
                'validators': [validate_password]
            },
        }

    def validate_confirm_password(self, value):
        if self.initial_data.get('password') == value:
            return value
        raise serializers.ValidationError("The two password fields didn’t match.")
            
    def create(self, validated_data):
        return self.Meta.model.objects.create_user(**validated_data)
    
class UserUpdateSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(read_only=True, view_name="user-detail", lookup_field='username')
    update = serializers.HyperlinkedIdentityField(read_only=True, view_name="user-update-user", lookup_field='username')
    setpassword = serializers.HyperlinkedIdentityField(read_only=True, view_name="user-change-password", lookup_field='username')
    issue_set = IssueSetSerializers( many=True, read_only=True)

    class Meta(UserSerializer.Meta):
        read_only_fields = ['last_login', 'is_superuser', 'is_active', 'is_staff', 'date_joined', 'username', 'is_defaulter', 'user_permissions', 'groups', 'password', 'issue_set',]



# https://github.com/Tivix/django-rest-auth 

class PasswordResetSerializer(serializers.Serializer):
    """
    Serializer for requesting a password reset e-mail.
    """
    email = serializers.EmailField(style={'autocomplete': 'email'})

    password_reset_form_class = PasswordResetForm

    def get_email_options(self):
        """Override this method to change default e-mail options"""
        return {}

    def validate_email(self, value):
        # Create PasswordResetForm with the serializer
        self.reset_form = self.password_reset_form_class(data=self.initial_data)
        if not self.reset_form.is_valid():
            raise serializers.ValidationError(self.reset_form.errors)

        return value

    def save(self):
        request = self.context.get('request')
        # Set some values to trigger the send_email method.
        opts = {
            'use_https': request.is_secure(),
            'from_email': getattr(settings, 'DEFAULT_FROM_EMAIL'),
            'request': request,
        }

        opts.update(self.get_email_options())
        self.reset_form.save(**opts)


class PasswordResetConfirmSerializer(serializers.Serializer):
    """
    Serializer for requesting a password reset e-mail.
    """
    new_password1 = serializers.CharField(max_length=128, style={'input_type': 'password', 'autocomplete': 'new-password'}, label="password")
    new_password2 = serializers.CharField(max_length=128, style={'input_type': 'password', 'autocomplete': 'new-password'}, label="confirm password")
    uid = serializers.CharField()
    token = serializers.CharField()

    set_password_form_class = SetPasswordForm

    def custom_validation(self, attrs):
        pass

    def validate(self, attrs):
        self._errors = {}

        # Decode the uidb64 to uid to get User object
        try:
            uid = force_text(uid_decoder(attrs['uid']))
            self.user = UserModel._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
            raise serializers.ValidationError({'uid': ['Invalid value']})

        self.custom_validation(attrs)
        # Construct SetPasswordForm instance
        self.set_password_form = self.set_password_form_class(
            user=self.user, data=attrs
        )
        if not self.set_password_form.is_valid():
            raise serializers.ValidationError(self.set_password_form.errors)
        if not default_token_generator.check_token(self.user, attrs['token']):
            raise serializers.ValidationError({'token': ['Invalid value']})

        return attrs

    def save(self):
        return self.set_password_form.save()


class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=128, style={'input_type': 'password', 'autocomplete' : 'current-password'})
    new_password1 = serializers.CharField(max_length=128, style={'input_type': 'password', 'autocomplete': 'new-password'}, label="New password")
    new_password2 = serializers.CharField(max_length=128, style={'input_type': 'password', 'autocomplete': 'new-password'}, label="Confirm password")

    set_password_form_class = SetPasswordForm

    def __init__(self, *args, **kwargs):
        self.old_password_field_enabled = getattr(
            settings, 'OLD_PASSWORD_FIELD_ENABLED', False
        )
        self.logout_on_password_change = getattr(
            settings, 'LOGOUT_ON_PASSWORD_CHANGE', False
        )
        super(PasswordChangeSerializer, self).__init__(*args, **kwargs)

        if not self.old_password_field_enabled:
            self.fields.pop('old_password')

        self.request = self.context.get('request')
        self.user = getattr(self.request, 'user', None)

    def validate_old_password(self, value):
        invalid_password_conditions = (
            self.old_password_field_enabled,
            self.user,
            not self.user.check_password(value)
        )

        if all(invalid_password_conditions):
            err_msg = _("Your old password was entered incorrectly. Please enter it again.")
            raise serializers.ValidationError(err_msg)
        return value

    def validate(self, attrs):
        self.set_password_form = self.set_password_form_class(
            user=self.user, data=attrs
        )

        if not self.set_password_form.is_valid():
            raise serializers.ValidationError(self.set_password_form.errors)
        return attrs

    def save(self):
        self.set_password_form.save()
        if not self.logout_on_password_change:
            from django.contrib.auth import update_session_auth_hash
            update_session_auth_hash(self.request, self.user)


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
        

    def get_is_return(self, obj):
        return obj.due_date_end

   
    