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
    permission_classes = [utils.IsAuthor]
    serializer_class = serializers.UserSerializer
    queryset = get_user_model().objects.all()
    # lookup_field = 'username'

    def list(self, request, *args, **kwargs):
        if request.user.is_authenticated and not request.user.is_staff:
            return HttpResponseRedirect(reverse('user-detail', kwargs = {'pk': self.request.user.id}))
        elif request.user.is_authenticated and request.user.is_staff:
            return super(UserViewSet, self).list(request, *args, **kwargs)
        else:
            raise Http404
    
    def create(self, request, *args, **kwargs):
        raise Http404

    @decorators.action(detail=True, methods = ['POST'], serializer_class=serializers.PasswordChangeSerializer, permission_classes = [utils.IsAuthor])
    def change_password(self, request, pk=None):
        '''
        Accepts the following POST parameters: old_password, new_password1, new_password2  
        Returns the success/fail message.
        '''
        user = self.get_object()
        serializer = self.get_serializer(user, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": _("New password has been saved.")})
        return Response(serializer.errors, status=404)
    
    # the detail is False and permission_classes AllowAny to call
    @decorators.action(detail = False, methods = ['POST'], serializer_class=serializers.UserCreateSerializers)
    def create_user(self, request, *args, **kwargs):
        '''
        # A form that creates a user, with no privileges, from the given username, email, password and confirm_password.  
        `profile not required`
        '''
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)
    
    
    @decorators.action(detail=False, methods=['POST'], serializer_class=serializers.PasswordResetSerializer)
    def reset_password(self, request, pk=None):
        '''
        Accepts the following POST parameters: email
        Returns the success and visit url.
        '''
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        # Return the success message with OK HTTP status
        return Response(
            {"detail": "Password reset e-mail has been sent.", 'visit' : request.build_absolute_uri(reverse('user-password-reset-confirm'))},
            status=200
        )

    @decorators.action(detail=False, methods=['POST'], serializer_class=serializers.PasswordResetConfirmSerializer)
    def password_reset_confirm(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"detail": "Password has been reset with the new password."}
        )    
    
class BookAPI(viewsets.ModelViewSet):
    """
    E-Management `Book` ViewSet  
    fields = [
        'id',
        'name',
        'genre_',
        'author_',
        'publish_',
        'update_date+now',
        'date+now_add',
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
    """
    queryset = models.Book.objects.all()
    permission_classes = [permissions.IsAdminUser|utils.ReadOnly]
    serializer_class = serializers.BookSerializers
    filterset_class = filters.BookFilter

    @decorators.action(detail=False, methods=['GET'])
    def lang_list(self, request):
        res = dict(models.Book.language.field.choices)
        return Response(res) 
    
class BookAuthorAPI(viewsets.ModelViewSet):
    """
    E-Management `BookAuthor` ViewSet
    fields = ['id', 'first_name', 'middle_name', 'last_name', 'date_of_birth', 'died', 'aboutAuthor', 'genre_']
    """
    queryset = models.BookAuthor.objects.all()
    permission_classes = [permissions.IsAdminUser|utils.ReadOnly]
    serializer_class = serializers.BookAuthorSerializers
    filterset_class = filters.BookAuthorFilter
      
class BookPublishAPI(viewsets.ModelViewSet):
    """
    E-Management `BookPublish` ViewSet  
    fields = ['id', 'company_name', 'website', 'genre_']
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
    filterset_class = filters.GenreFilter

class IssueAPI(viewsets.ModelViewSet):
    """
    E-Management `Issue` ViewSet  
    fields = ['id', 'user_', 'book_', 'date+now', 'due_date+7']
    """
    # queryset = models.Issue.objects.filter(user=request.user)
    serializer_class = serializers.IssueSerializers
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        return self.request.user.issue_set.all()
        # except:
            # raise Http404
