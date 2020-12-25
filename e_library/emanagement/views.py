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
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import viewsets, versioning, permissions, mixins, decorators
from emanagement import serializers, models, filters, utils
import json

@require_http_methods(['POST'])
@csrf_exempt
def update(request):
    _ = request.headers.get('X-Hub-Signature')
    if _:
        repo = git.Repo(os.path.dirname(settings.BASE_DIR))
        o = repo.remotes.origin
        o.pull()
        os.system("/home/elibrarymanagementsystemapi/.virtualenvs/e-library-management-system-api-W9LeGc9Z/bin/python /home/elibrarymanagementsystemapi/e-library-management-system-api/e_library/manage.py collectstatic --noinput")
        os.system("touch /var/www/elibrarymanagementsystemapi_pythonanywhere_com_wsgi.py")
        return HttpResponse("Update on Pythonanywhere is Done!")
    else:
        raise Http404

def handler404(request, exception):
    return HttpResponse(f"<h1 style='text-align: center;'>404 <a style='text-decoration: none;' title='Send me Email' href='mailto:shyamkumaryadav2003@gmail.com'>Send me an email</a><br><a style='text-decoration: none;' href='/' title='API Home Page' style='color:red;'>Go back</a></h1><br><p style='text-align: center;'>The requested resource was not found on this server.</p><hr>")

def handler500(request):
    return HttpResponse(f"<h1 style='text-align: center;'>500 error handler! contect admin <a href='mailto:shyamkumaryadav2003@gmail.com'>shyamkumaryadav2003@gmail.com</a></h1>")


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.AllowAny&utils.IsAuthor]
    queryset = get_user_model().objects.all()

    def list(self, request, *args, **kwargs):
        if request.user.is_authenticated and not request.user.is_staff:
            return HttpResponseRedirect(reverse('user-detail', kwargs={'pk': self.request.user.id}))
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        headers = ''
        useris = self.get_serializer(request.user)
        if useris:
            headers = self.get_success_headers(useris.data)
        return Response(serializer.data, headers=headers)
       

    def get_queryset(self):
        if self.request.user.is_staff:
            return super(UserViewSet, self).get_queryset()
        return get_user_model().objects.filter(username=self.request.user.username)
    
    @decorators.action(detail=False, methods=['post'], serializer_class=serializers.UserCreateSerializers)
    def create_user(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)
        # serializer = self.get_serializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors, status=404)
    
    @decorators.action(detail=True, methods=['post'], serializer_class=serializers.UserPasswordSerializer)
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=404)


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
