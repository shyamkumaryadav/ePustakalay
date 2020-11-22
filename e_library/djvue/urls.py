from django.urls import path
from djvue import views

urlpatterns = [
    path('', views.index),
    path('about/', views.index),
]