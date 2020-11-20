'''
Views of Gui
'''

from django.shortcuts import render

def index(request, *args, **kwargs):
    """
    This render gui/index.html templates
    """
    context = {}

    return render(request, 'gui/index.html', context=context)
