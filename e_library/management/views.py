"""
views for management apps.
"""
from django.shortcuts import render


def index(request):
    '''
    Index view of management
    '''
    context = {}
    return render(request, 'management/index.html', context=context)
