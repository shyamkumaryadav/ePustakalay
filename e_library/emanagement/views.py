"""
views for management apps.
"""
import git
import os
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from rest_framework import viewsets, versioning, permissions
from emanagement import serializers, models, filters, utils


@csrf_exempt
def update(request):
    if request.method == "POST":
        repo = git.Repo(os.path.dirname(settings.BASE_DIR))
        o = repo.remotes.origin
        o.pull()
        return HttpResponse(str(dict(request.POST)))
    return HttpResponseRedirect('/')

def handler404(request, exception):
    return HttpResponse(f"<h1>Not Found</h1><br><p>The requested resource was not found on this server.</p><hr>")

def handler500(request):
    return HttpResponse(f"500 error handler!")

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
    permission_classes = [permissions.IsAdminUser|utils.ReadOnly&utils.IsDefaulter]


    def get_queryset(self):
        return self.request.user.issue_set.all()
