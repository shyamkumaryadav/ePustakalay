from django.template.defaultfilters import filesizeformat
from rest_framework import permissions
from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_rating(value):
    if value < 0.0 or value > 10:
        raise ValidationError(f'Ensure that {value} in 0 to 10.')

def pic_upload(instance, filename):
    return f"{instance._meta.app_label}/{instance._meta.model_name}_{instance.id}_{instance.__str__()}.{filename.split('.')[-1]}"

def age(value):
    today = timezone.now()
    year = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if year < 18:
        raise ValidationError(f"Your age not 18+, as i think you are {year} year old.")

def profile_size(value):
    if value.size > 1024 * 1024 * 0.5:
        raise ValidationError(f"Image size is {filesizeformat(value.size)} required size {filesizeformat(1024 * 1024 * 0.5)}")

class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
    
    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS

class IsDefaulter(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #  Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user

class IsAuthor(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user.is_authenticated
        )
    
    def has_object_permission(self, request, view, obj):
        return bool(request.method in permissions.SAFE_METHODS or request.user.is_authenticated and request.user == obj)