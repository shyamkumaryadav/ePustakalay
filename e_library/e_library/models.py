import uuid
import data_list
from django.db import models
from django.contrib.auth.models import AbstractUser as BaseAbstractUser
from django.core import validators
from django.utils.html import mark_safe, escape
from django.utils.translation import gettext_lazy as _
from emanagement import utils



class AbstractUser(BaseAbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
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
                                        regex=r"^\d{1,5}[4-9]\d{9}$", message=_("Enter Valid Phone Number.")), ],
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
