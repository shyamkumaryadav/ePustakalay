"""
URLPATTERNS for e_library project.
"""
from django.contrib import admin
# from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('admin/', admin.site.urls),
    # path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('management/', include('management.urls')),
    path('system/', include('system.urls')),
    path('api/auth/ojwt', obtain_jwt_token),
    path('api/auth/rjwt', refresh_jwt_token),
    path('favicon.ico', RedirectView.as_view(
        url=staticfiles_storage.url('favicon.ico')))

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
