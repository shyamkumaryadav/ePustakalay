'''
All Serializers For Book Management

1. `BookSerializers`
'''
from rest_framework import serializers
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.encoding import force_text
from django.contrib.auth import password_validation
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.utils.http import urlsafe_base64_decode as uid_decoder
from django.contrib.auth.tokens import default_token_generator
from django.http import Http404
from emanagement import models
from django.utils.translation import ugettext_lazy as _


UserModel = get_user_model()
password_help_text = '<br>'.join([str(elem) for elem in password_validation.password_validators_help_texts()])

class IssueSetSerializers(serializers.ModelSerializer):
    book_name = serializers.SlugRelatedField(source="book", many= False, read_only=True, slug_field="name")
    is_return = serializers.SerializerMethodField()


    class Meta:
        model = models.Issue
        fields = ['book_name', 'is_return', 'date', 'due_date',]
    
    def get_is_return(self, obj):
        return obj.due_date_end

class UserSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(read_only=True, view_name="user-detail", lookup_field='pk')
    setpassword = serializers.HyperlinkedIdentityField(read_only=True, view_name="user-change-password", lookup_field='pk')
    issue_set = IssueSetSerializers( many=True, read_only=True)
    
    class Meta:
        model = UserModel
        fields = ['url', 'id', 'username', 'first_name', 'middle_name', 'last_name', 'email', 'phone_number', 'date_of_birth', 'country', 'state', 'city', 'pincode', 'full_address', 'is_defaulter', 'profile', 'groups', 'user_permissions','is_superuser', 'last_login', 'is_superuser', 'is_active', 'is_staff', 'date_joined', 'setpassword', 'issue_set']
        read_only_fields = ['last_login', 'is_superuser', 'is_active', 'is_staff', 'date_joined', 'username', 'is_defaulter', 'user_permissions', 'groups', 'password', 'issue_set',]
    
    

class UserCreateSerializers(serializers.ModelSerializer):
    confirm_password = serializers.CharField(help_text=_("Enter the same password as before, for verification."), style={'input_type': 'password', 'autocomplete': 'new-password'}, write_only=True, required=True,) # validators=[validate_password])
    url = serializers.HyperlinkedIdentityField(read_only=True, view_name="user-detail", lookup_field='pk')
    setpassword = serializers.HyperlinkedIdentityField(read_only=True, view_name="user-change-password", lookup_field='pk')

    class Meta(UserSerializer.Meta):
        fields = ['id', 'url', 'username', 'email', 'password', 'confirm_password', 'profile', 'date_joined', 'is_active', 'setpassword']
        read_only_fields = ['id', 'is_superuser', 'last_login', 'date_joined',]
        extra_kwargs = {
            'is_active': {'read_only': True},
            'password': {
                'write_only': True,
                'required': True,
                'style': {
                    'input_type': 'password',
                    'autocomplete': 'new-password'
                },
                'help_text': password_help_text,
                'validators': [password_validation.validate_password]
            },
        }

    def validate_confirm_password(self, value):
        if self.initial_data.get('password') != value:
            raise serializers.ValidationError(_("The two password fields didn’t match."))
        return value
            
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        return self.Meta.model.objects.create_user(**validated_data)


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
    new_password1 = serializers.CharField(max_length=128, style={'input_type': 'password', 'autocomplete': 'new-password'}, label="password", help_text=password_validation.password_validators_help_texts())
    new_password2 = serializers.CharField(max_length=128, style={'input_type': 'password', 'autocomplete': 'new-password'}, label="confirm password", help_text=_('Enter the same password as before, for verification.'))
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
        fields = [ 'url', 'id', 'name',]

class BookAuthorSerializers(serializers.HyperlinkedModelSerializer):
    '''
    The Serializer of `emanagement.models.BookAuthor`  
    '''

    genre = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=models.Genre.objects.all())

    class Meta:
        model = models.BookAuthor
        fields = ('url', 'id', 'first_name', 'middle_name', 'last_name', 'date_of_birth', 'died', 'aboutAuthor', 'genre', 'profile')
        # extra_kwargs = {'genre': {'write_only': True}}

class BookPublishSerializers(serializers.HyperlinkedModelSerializer):
    '''
    The Serializer of `emanagement.models.BookPublish`
    '''
    
    genre = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=models.Genre.objects.all())

    class Meta:
        model = models.BookPublish
        fields = ('url', 'id', 'company_name', 'website', 'genre')

class BookSerializers(serializers.HyperlinkedModelSerializer):
    '''
    The Serializer of `emanagement.models.Book`
    '''
    genre = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=models.Genre.objects.all())
    # serializers.PrimaryKeyRelatedField
    author = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=models.BookAuthor.objects.all())
    publish = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=models.BookPublish.objects.all())
    author_name = serializers.StringRelatedField(source='author', many=False, read_only=True)
    publish_by = serializers.StringRelatedField(source='publish', many=False, read_only=True)

    class Meta:
        model = models.Book
        fields = ['url', 'id', 'slug', 'name', 'genre', 'author', 'publish', 'update_date', 'author_name', 'publish_by', 'date', 'language', 'edition', 'cost', 'page', 'description', 'stock', 'in_stock', 'today_stock', 'rating', 'profile']
        extra_kwargs = {
            'author': {'write_only': True},
            'publish': {'write_only': True},
        }

class IssueSerializers(serializers.HyperlinkedModelSerializer):
    '''
    The Serializer of `emanagement.models.Issue`
    '''
    book = serializers.PrimaryKeyRelatedField(many= False, queryset=models.Book.objects.filter(in_stock=True))
    user = serializers.PrimaryKeyRelatedField(many= False, queryset=models.User.objects.filter(is_defaulter=False))
    is_return = serializers.SerializerMethodField()

    class Meta:
        model = models.Issue
        fields = ['url', 'id', 'book', 'user', 'is_return', 'date', 'due_date',]
        
        

    def get_is_return(self, obj):
        return obj.due_date_end
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)