from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

# System Config
from system import serializers, models, authentication



class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializers
    permission_classes = [permissions.IsAdminUser]
