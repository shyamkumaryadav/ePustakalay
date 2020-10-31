from django.urls import path, include
from rest_framework import routers
from system import views

router = routers.DefaultRouter()
router.register('Books', views.BookViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]