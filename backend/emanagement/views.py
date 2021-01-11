"""
views for management apps.
"""
import git
import os
from django.http import HttpResponse, HttpResponseRedirect, Http404
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.conf import settings
from django.http import Http404
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import viewsets, versioning, permissions, mixins, decorators
from emanagement import serializers, models, filters, utils
from django.utils.translation import ugettext_lazy as _
import json

@require_http_methods(['POST'])
@csrf_exempt
def update(request):
    _ = request.headers.get('X-Hub-Signature')
    if _:
        repo = git.Repo(os.path.dirname(settings.BASE_DIR))
        o = repo.remotes.origin
        o.pull()
        os.system("/home/elibrarymanagementsystemapi/.virtualenvs/e-library-management-system-api-W9LeGc9Z/bin/python -m pip install -r /home/elibrarymanagementsystemapi/e-library-management-system-api/requirements.txt")
        os.system("/home/elibrarymanagementsystemapi/.virtualenvs/e-library-management-system-api-W9LeGc9Z/bin/python /home/elibrarymanagementsystemapi/e-library-management-system-api/e_library/manage.py collectstatic --noinput")
        os.system("/home/elibrarymanagementsystemapi/.virtualenvs/e-library-management-system-api-W9LeGc9Z/bin/python /home/elibrarymanagementsystemapi/e-library-management-system-api/e_library/manage.py makemigrations emanagement")
        os.system("/home/elibrarymanagementsystemapi/.virtualenvs/e-library-management-system-api-W9LeGc9Z/bin/python /home/elibrarymanagementsystemapi/e-library-management-system-api/e_library/manage.py migrate")
        os.system("touch /var/www/elibrarymanagementsystemapi_pythonanywhere_com_wsgi.py")
        return HttpResponse("Update on Pythonanywhere is Done!")
    else:
        return HttpResponse("urlencoded is Fix!")

def handler404(request, exception):
    return HttpResponse(f"<h1 style='text-align: center;'>404 <a style='text-decoration: none;' title='Send me Email' href='mailto:shyamkumaryadav2003@gmail.com'>Send me an email</a><br><a style='text-decoration: none;' href='/' title='API Home Page' style='color:red;'>Go back</a></h1><br><p style='text-align: center;'>The requested resource was not found on this server.</p><hr>")

def handler500(request):
    return HttpResponse(f"<h1 style='text-align: center;'>500 error handler! contect admin <a href='mailto:shyamkumaryadav2003@gmail.com'>shyamkumaryadav2003@gmail.com</a></h1>")


class UserViewSet(viewsets.ModelViewSet):
    '''
    User View
    '''
    allowed_methods = ['GET', 'HEAD', 'OPTIONS']
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.AllowAny]
    queryset = get_user_model().objects.all()

    def list(self, request, *args, **kwargs):
        headers = {}
        if request.user.is_authenticated and not request.user.is_staff:
            return HttpResponseRedirect(reverse('user-detail', kwargs={'pk': self.request.user.id}))
        elif request.user.is_staff:
            return super(UserViewSet, self).list(request, *args, **kwargs)
        else:
            raise Http404
       

    def create(self, request, *args, **kwargs):
        raise Http404
    
    @decorators.action(detail=False, methods=['POST'], serializer_class=serializers.UserCreateSerializers, allowed_methods=['POST','HEAD', 'OPTIONS'], permission_classes=[permissions.AllowAny])
    def create_user(self, request, *args, **kwargs):
        '''
        A form that creates a user, with no privileges, from the given username, email and password.
        '''
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)
    
    @decorators.action(detail=True, methods=['GET', 'POST', 'PUT'], serializer_class=serializers.UserUpdateSerializer, allowed_methods=['GET', 'PUT', 'HEAD', 'OPTIONS'])
    def update_user(self, request, *args, **kwargs):
        '''
        A form that Update a user.
        '''
        if request.method == 'PUT':
            return self.update(request, *args, **kwargs)
        return self.retrieve(request, *args, **kwargs)
    
    @decorators.action(detail=True, methods=['POST'], serializer_class=serializers.PasswordChangeSerializer, allowed_methods=['POST', 'HEAD', 'OPTIONS'])
    def change_password(self, request, pk=None):
        '''
        Accepts the following POST parameters: old_password, new_password1, new_password2  
        Returns the success/fail message.
        '''
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=404)
    
    @decorators.action(detail=False, methods=['POST'], serializer_class=serializers.PasswordResetSerializer, allowed_methods=['POST', 'HEAD', 'OPTIONS'])
    def reset_password(self, request, pk=None):
        '''
        Accepts the following POST parameters: email
        Returns the success/fail message.
        '''
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        # Return the success message with OK HTTP status
        return Response(
            {"detail": _("Password reset e-mail has been sent.")},
            status=200
        )

    @decorators.action(detail=False, methods=['POST'], serializer_class=serializers.PasswordResetConfirmSerializer, allowed_methods=['POST', 'HEAD', 'OPTIONS'])
    def password_reset_confirm(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"detail": _("Password has been reset with the new password.")}
        )
    
    
    
class BookAPI(viewsets.ModelViewSet):
    """
    E-Management `Book` ViewSet
    """
    queryset = models.Book.objects.all()
    permission_classes = [permissions.IsAdminUser|utils.ReadOnly]
    serializer_class = serializers.BookSerializers
    # filter_backends = (filters.DjangoFilterBackend,)
    # filterset_fields = ('name', 'author', 'publish')
    filterset_class = filters.BookFilter
    
class BookAuthorAPI(viewsets.ModelViewSet):
    """
    E-Management `BookAuthor` ViewSet
    """
    queryset = models.BookAuthor.objects.all()
    permission_classes = [permissions.IsAdminUser|utils.ReadOnly]
    serializer_class = serializers.BookAuthorSerializers
    filterset_class = filters.BookAuthorFilter
      
class BookPublishAPI(viewsets.ModelViewSet):
    """
    E-Management `BookPublish` ViewSet
    """
    # name = "Book Puasblish"
    queryset = models.BookPublish.objects.all()
    permission_classes = [permissions.IsAdminUser|utils.ReadOnly]
    serializer_class = serializers.BookPublishSerializers
    filterset_class = filters.BookPublishFilter

     
class GenreAPI(viewsets.ModelViewSet):
    """
    E-Management `Genre` ViewSet

    fields  
    - id : id of genre  
    - name : Name of genre  
    """
    queryset = models.Genre.objects.all()
    permission_classes = [utils.ReadOnly]
    serializer_class = serializers.GenreSerializers

class IssueAPI(viewsets.ModelViewSet):
    """
    E-Management `Issue` ViewSet
    """
    # queryset = models.Issue.objects.filter(user=request.user)
    serializer_class = serializers.IssueSerializers
    permission_classes = [permissions.IsAdminUser|utils.ReadOnly]


    def get_queryset(self):
        return self.request.user.issue_set.all()
