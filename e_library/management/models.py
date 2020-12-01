import uuid
from django.db import models
import data_list
from django.conf import global_settings
from management import utils
from django.core import validators
from django.contrib.auth import get_user_model


UserModel = get_user_model()

class Genre(models.Model):
    name = models.IntegerField(choices=[
                               (None, "Select Language")] + data_list.BOOK_GENRE)
    # objects = GenreManager()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class BookAuthor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(verbose_name="First Name", max_length=100)
    middle_name = models.CharField(verbose_name="Middle Name", max_length=100)
    last_name = models.CharField(verbose_name="Last Name", max_length=100)
    date_of_birth = models.DateField(null=True)
    died = models.DateField(verbose_name='Died', null=True, blank=True)
    aboutAuthor = models.TextField(max_length=250)
    genre = models.ManyToManyField(
        Genre, verbose_name="Genre", help_text='Hold down “Control”, or “Command” on a Mac, to select more than one.')

    class Meta:
        ordering = ['date_of_birth']
        unique_together = ('first_name', 'last_name',)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    # @property
    # def get_update_url(self):
    #     return reverse_lazy('system:authormanagementupdate', kwargs={
    #         'pk': self.pk
    #     })




class BookPublish(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_name = models.CharField(max_length=100, unique=True,
                            error_messages={
                                "unique": "This name is already exists."
                            }
                            )
    website = models.TextField(unique=True,)
    genre = models.ManyToManyField(
        Genre, verbose_name="Genre", help_text='Hold down “Control”, or “Command” on a Mac, to select more than one.')

    class Meta:
        ordering = ['company_name']

    def __str__(self):
        return self.company_name

class Book(models.Model):
    """
    Management all book Data

    filds = ['id', 'name', 'genre', 'author']
    """
    id = models.UUIDField(verbose_name="Book ID",
                          primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120, verbose_name="Name", unique=True)
    genre = models.ManyToManyField(
        Genre, verbose_name="Genre", help_text='Hold down “Control”, or “Command” on a Mac, to select more than one.')
    author = models.ForeignKey(
        BookAuthor, on_delete=models.CASCADE, verbose_name="Author Name")
    publish = models.ForeignKey(BookPublish, on_delete=models.CASCADE,
                                verbose_name="Publisher Name")
    publish_date = models.DateField(
        validators=[], verbose_name="Publish Date")
    date = models.DateTimeField(auto_now=True, verbose_name="Date", editable=False)
    language = models.CharField(max_length=12, verbose_name="Language", choices=[
                                (None, "Select Language")] + global_settings.LANGUAGES)
    edition = models.IntegerField(verbose_name="Edition", choices=[
                                  (None, "Select Edition")] + data_list.BOOK_EDITION)
    cost = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="Book Cost(per unit)")
    page = models.PositiveIntegerField(verbose_name="Total Page")
    description = models.TextField(verbose_name="Book Description")
    stock = models.PositiveIntegerField(verbose_name="Stock")
    today_stock = models.PositiveIntegerField(
        verbose_name="Current stock", null=True, blank=True)
    rating = models.DecimalField(
        max_digits=2, decimal_places=1, verbose_name="Rating")
    profile = models.FileField(
        upload_to=utils.pic_upload, verbose_name="Book cover",
        default="default.jpg", blank=True,
        validators=[validators.FileExtensionValidator(
                allowed_extensions=validators.get_available_image_extensions(),
                message="Select valid Cover Image.")
        ],
    )

    class Meta:
        ordering = ['name']
        permissions = [('is_defaulter', 'User in defaulter list')]

    def __str__(self):
        return self.name

class Issue(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, editable=False)
    due_date = models.DateField()

    class Meta:
        unique_together = ('user', 'book',)

    def __str__(self):
        return f"{self.user} <---> {self.book}"

