"""
URLPATTERNS for e_library project.
"""
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework import routers
from django.utils.translation import gettext as _, gettext_lazy


class SimpleRouterEx(routers.SimpleRouter):
    include_root_view = True
    include_format_suffixes = True
    default_schema_renderers = None
    
    routes = [
        # routers.Route(
        #     url=r'^{prefix}$',
        #     mapping={'get': 'list'},
        #     name='{basename}-list',
        #     detail=False,
        #     initkwargs={'suffix': 'List'}
        # ),
        routers.Route(
            url=r'^{prefix}/{lookup}$',
            mapping={'get': 'retrieve'},
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        ),
        routers.DynamicRoute(
            url=r'^{prefix}/{lookup}/{url_path}$',
            name='{basename}-{url_name}',
            detail=True,
            initkwargs={}
        ),
        routers.DynamicRoute(
            url=r'^{prefix}/{url_path}/{lookup}$',
            name='{basename}-{url_name}',
            detail=False,
            initkwargs={}
        )
    ]

# Root Url Of DRF
router = routers.DefaultRouter()
# router.APIRootView = APIRootView
router.APIRootView.api_root_dict = {'ref':'reftoken'}
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
    path('auth/token/', TokenObtainPairView.as_view(), name="gettoken"),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name="reftoken"),
    path('auth/token/verify/', TokenVerifyView.as_view(), name="vertoken"),
    path('updatexfcBQRdMgeNr/', man_views.update),
]