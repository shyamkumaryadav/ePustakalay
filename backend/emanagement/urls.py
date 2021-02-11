"""
URLPATTERNS for e_library project.
"""
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from rest_framework import routers
from django.utils.translation import gettext as _, gettext_lazy


# Root Url Of DRF
router = routers.DefaultRouter()
router.APIRootView.__doc__ =''' ```python
print("Hello world")
from emanagement import views
```
'''

# All management Views
from emanagement import views as man_views
router.register('user', man_views.UserViewSet)
router.register('books', man_views.BookAPI)
router.register('book-authors', man_views.BookAuthorAPI)
router.register('book-publish', man_views.BookPublishAPI)
router.register('book-genres', man_views.GenreAPI)
router.register('book-issue', man_views.IssueAPI, basename="issue")


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token/obtain/', TokenObtainPairView.as_view(), name="gettoken"),
    path('token/refresh/', TokenRefreshView.as_view(), name="reftoken"),
    path('token/verify/', TokenVerifyView.as_view(), name="vertoken"),
    path('updatexfcBQRdMgeNr/', man_views.update),
]