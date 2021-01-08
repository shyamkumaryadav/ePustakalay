'''
All Models of Emanagement  

1. Genre ['id', 'name']
2. BookAuthor ['id', 'first_name', 'middle_name', 'last_name', 'date_of_birth', 'died', 'aboutAuthor', 'genre']
3. BookPublish ['id', 'company_name', 'website', 'genre']
4. Book ['id', 'name', 'genre', 'author', 'publish', 'publish_date', 'date', 'language', 'edition', 'cost', 'page', 'description', 'stock', 'today_stock', 'rating', 'profile']
5. Issue ['id', 'user', 'book', 'date', 'due_date']
'''
import uuid
from django.db import models
import data_list
from django.conf import global_settings
from emanagement import utils
from django.core import validators
from django.contrib.auth.models import AbstractUser as BaseAbstractUser
from django_extensions.db.fields import AutoSlugField
from django.utils.html import mark_safe, escape
from django.utils import timezone
from django.utils.translation import gettext_lazy as _



class AbstractUser(BaseAbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_('email address'), unique=True)
    middle_name = models.CharField(
        verbose_name=_("Middle Name"),
        max_length=20,
        validators=[
            validators.RegexValidator(regex=r"^[A-Za-z ]+$", message=_("Enter Valid Middle Name."))],
        null=True,blank=True,
    )
    
    date_of_birth = models.DateField(
        verbose_name=_("Data of Birth"),
        null=True,blank=True,
        validators=[utils.age]
    )
    phone_number = models.CharField(verbose_name=_("Phone Number"),
                                    max_length=13,
                                    null=True,blank=True,
                                    validators=[validators.RegexValidator(
                                        regex=r"^[4-9]\d{9}$", message=_("Enter Valid Phone Number.")), ],
                                    help_text=_("Enter Your Number without <b>country code.</b>")
                                    )
    country = models.CharField(max_length=25, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    pincode = models.CharField(verbose_name=_("Pincode"), max_length=6,
                               null=True,blank=True
                               )
    full_address = models.TextField(verbose_name=_("Full Address"),
                                    null=True,
                                    blank=True,
                                    max_length=50,
                                    )
    is_defaulter = models.BooleanField(default=False, help_text=_('User in defaulter list'))
    profile = models.FileField(upload_to=utils.pic_upload,
                               default='user.jpg', blank=True,null=True,
                               validators=[validators.FileExtensionValidator(
                                   allowed_extensions=validators.get_available_image_extensions(),
                                   message=_(
                                       "Select valid Cover Image.")
                               ), utils.profile_size
                               ],)

    def image_tag(self):
        return mark_safe('<img src="{}" width="200px" />'.format(escape(self.profile.url)))
    image_tag.short_description = 'USER IMAGE'
    image_tag.allow_tags = True
   
    class Meta(BaseAbstractUser.Meta):
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True


class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.
    Username and password are required. Other fields are optional.
    """
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class Genre(models.Model):
    '''
    E-Management `Genre` Model

    fields = ['id', 'name']
    '''
    name = models.CharField(max_length=50, unique=True, editable=False, choices=[
                               (None, "Select Genre")] + data_list.BOOK_GENRE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class BookAuthor(models.Model):
    '''
    E-Management `BookAuthor` Model

    fields = ['id', 'first_name', 'middle_name', 'last_name', 'date_of_birth', 'died', 'aboutAuthor', 'genre']
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(verbose_name="First Name", max_length=100)
    middle_name = models.CharField(verbose_name="Middle Name", max_length=100)
    last_name = models.CharField(verbose_name="Last Name", max_length=100)
    date_of_birth = models.DateField(null=True)
    died = models.DateField(verbose_name='Died', null=True, blank=True)
    aboutAuthor = models.TextField(max_length=250)
    genre = models.ManyToManyField(
        Genre, verbose_name="Genre", help_text='Hold down “Control”, or “Command” on a Mac, to select more than one.')
    profile = models.FileField(
        upload_to=utils.pic_upload, verbose_name="Author Profile",
        default="user.jpg", blank=True,
        validators=[validators.FileExtensionValidator(
                allowed_extensions=validators.get_available_image_extensions(),
                message="Select valid Cover Image."), utils.profile_size
        ],
    )

    class Meta:
        ordering = ['date_of_birth']
        unique_together = ('first_name', 'last_name',)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    # @property
    # def get_update_url(self):
    #     return reverse_lazy('system:authormanagementupdate', kwargs={
    #         'pk': self.pk lol xd
    #     })




class BookPublish(models.Model):
    """
    E-Management `BookPublisher` Model

    fields = ['id', 'company_name', 'website', 'genre']
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_name = models.CharField(max_length=100, unique=True,
                            error_messages={
                                "unique": "This name is already exists."
                            }
                            )
    website = models.URLField(unique=True,)
    genre = models.ManyToManyField(
        Genre, verbose_name="Genre", help_text='Hold down “Control”, or “Command” on a Mac, to select more than one.')

    class Meta:
        unique_together = ('company_name', 'website',)
        ordering = ['company_name']

    def __str__(self):
        return f"{self.company_name}"

class Book(models.Model):
    '''
    E-Management `BookAuthor` Model

    fields = [
        'id',
        'name',
        'genre',
        'author',
        'publish',
        'update_date',
        'date',
        'language',
        'edition',
        'cost',
        'page',
        'description',
        'stock',
        'in_stock',
        'today_stock',
        'rating',
        'profile',
        'slug',
    ]
    '''
    id = models.UUIDField(verbose_name="Book ID",
                          primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120, verbose_name="Name", unique=True)
    genre = models.ManyToManyField(
        Genre, verbose_name="Genre", help_text='Hold down “Control”, or “Command” on a Mac, to select more than one.')
    author = models.ForeignKey(
        BookAuthor, on_delete=models.CASCADE, verbose_name="Author Name")
    publish = models.ForeignKey(BookPublish, on_delete=models.CASCADE,
                                verbose_name="Publisher Name")
    update_date = models.DateTimeField(auto_now=True, verbose_name="Last Update")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Date")
    language = models.CharField(max_length=12, verbose_name="Language", choices=[
                                (None, "Select Language")] + global_settings.LANGUAGES)
    edition = models.IntegerField(verbose_name="Edition", choices=[
                                  (None, "Select Edition")] + data_list.BOOK_EDITION)
    cost = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="Book Cost(per unit)")
    page = models.PositiveIntegerField(verbose_name="Total Page")
    description = models.TextField(verbose_name="Book Description")
    stock = models.PositiveIntegerField(verbose_name="Stock")
    in_stock = models.BooleanField(default=True, editable=False)
    today_stock = models.PositiveIntegerField(
        verbose_name="Current stock", editable=False)
    rating = models.DecimalField(
        max_digits=3, decimal_places=1, verbose_name="Rating", validators=[utils.validate_rating])
    profile = models.FileField(
        upload_to=utils.pic_upload, verbose_name="Book cover",
        default="elibrary.jpg", blank=True,
        validators=[validators.FileExtensionValidator(
                allowed_extensions=validators.get_available_image_extensions(),
                message="Select valid Cover Image."), utils.profile_size
        ],
    )
    slug = AutoSlugField(populate_from=['name', 'author'])

    class Meta:
        ordering = ['name']
        unique_together = ('name', 'author',)
        

    def __str__(self):
        return f"{self.name}"
    
    def image_tag(self):
        return mark_safe('<img src="{}" width="200px" />'.format(escape(self.profile.url)))
    image_tag.short_description = 'BOOK COVER'
    image_tag.allow_tags = True
    

class Issue(models.Model):
    '''
    E-Management book issue by user `Issue` Model

    fields = ['id', 'user', 'book', 'date', 'due_date']
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_active': True, })
    book = models.ForeignKey(Book, on_delete=models.CASCADE, limit_choices_to={'in_stock': True})
    date = models.DateTimeField(auto_now_add=True, editable=False,
        help_text=_("The date book is issue by user."),
    )
    due_date = models.DateTimeField(
        default=timezone.now() + timezone.timedelta(days=7),
        help_text=_("By defualt date is 7 days"),
    )

    class Meta:
        unique_together = ('user', 'book',)

    def __str__(self):
        return f"{self.user} take {self.book}"
    
    def _due_date_end(self):
        return self.due_date <= timezone.now()

    _due_date_end.boolean = True
    due_date_end = property(_due_date_end)



