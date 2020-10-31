from django.shortcuts import render
from rest_framework import viewsets


# System Config
from system import serializers, models, permissions



class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializers
    permission_classes = [permissions.IsAdminUserOrReadOnly]
