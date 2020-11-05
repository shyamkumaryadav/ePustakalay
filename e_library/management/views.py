"""
views for management apps.
"""
from django.shortcuts import HttpResponse


def index(request):
    '''
    Index view of management
    '''
    return HttpResponse("<h1>Management index file<h1>", status=200)
