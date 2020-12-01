from rest_framework import viewsets


'''
System view Config
'''

from system import serializers, models, permissions


class BookViewSet(viewsets.ModelViewSet):
    """
    
    """
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializers
    permission_classes = [permissions.IsAdminUserOrReadOnly]
