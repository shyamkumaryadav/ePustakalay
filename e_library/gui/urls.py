'''
Urls of GUI App
'''
from django.urls import path
from gui import views


urlpatterns = [
    path('', views.index),
]