"""
URLPATTERNS for e_library project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework import routers
from django.utils.translation import gettext as _, gettext_lazy


# Text to put at the end of each page's <title>.
admin.AdminSite.site_title = gettext_lazy('shyamkumar')

# Text to put in each page's <h1>.
admin.AdminSite.site_header = gettext_lazy('E-library Management System')

# Text to put at the top of the admin index page.
admin.AdminSite.index_title = gettext_lazy('App List')

# URL for the "View site" link at the top of each admin page.
admin.AdminSite.site_url = '/' # 'https://elibrarymanagementsystem.herokuapp.com/'

admin.AdminSite.enable_nav_sidebar = False

admin.AdminSite.empty_value_display = '<i>undefined</i>'


# Root Url Of DRF
router = routers.DefaultRouter()
router.APIRootView.__doc__ = """
```python
print("Hello world")

from emanagement import views
```
"""

# All management Views
from emanagement import views as man_views
router.register('books', man_views.BookAPI)
router.register('book-authors', man_views.BookAuthorAPI)
router.register('book-publish', man_views.BookPublishAPI)
router.register('book-genres', man_views.GenreAPI)
router.register('book-issue', man_views.IssueAPI, basename="issue")


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/token/', TokenObtainPairView.as_view()),
    path('auth/token/refresh/', TokenRefreshView.as_view()),
    path('auth/token/verify/', TokenVerifyView.as_view()),
    path('updatexfcBQRdMgeNr/', man_views.update),
    path('favicon.ico', RedirectView.as_view(
        url=staticfiles_storage.url('favicon.ico')))

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


handler404 = 'emanagement.views.handler404'
handler500 = 'emanagement.views.handler500'
