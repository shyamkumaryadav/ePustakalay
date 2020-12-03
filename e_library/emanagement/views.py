"""
views for management apps.
"""
from rest_framework import viewsets, versioning, permissions
from emanagement import serializers, models, filters


class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class BookAPI(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing `Book` Model.
    """
    queryset = models.Book.objects.all()
    permission_classes = [permissions.IsAdminUser|ReadOnly]
    serializer_class = serializers.BookSerializers
    # filter_backends = (filters.DjangoFilterBackend,)
    # filterset_fields = ('name', 'author', 'publish')
    filterset_class = filters.BookFilter
    
class BookAuthorAPI(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing `BookAuthor` Model.
    """
    queryset = models.BookAuthor.objects.all()
    permission_classes = [permissions.IsAdminUser|ReadOnly]
    serializer_class = serializers.BookAuthorSerializers
      
class BookPublishAPI(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing `BookPublish` Model.  
    """
    # name = "Book Puasblish"
    queryset = models.BookPublish.objects.all()
    permission_classes = [permissions.IsAdminUser|ReadOnly]
    serializer_class = serializers.BookPublishSerializers

     
class GenreAPI(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing `Genre` Model.
    """
    queryset = models.Genre.objects.all()
    permission_classes = [permissions.IsAdminUser|ReadOnly]
    serializer_class = serializers.GenreSerializers

class IssueAPI(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing `Issue` Model.
    """
    # queryset = models.Issue.objects.filter(user=request.user)
    serializer_class = serializers.IssueSerializers
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        return self.request.user.issue_set.all()
