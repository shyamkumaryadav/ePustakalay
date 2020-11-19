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
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('', include('gui.urls')),
    path('admin/', admin.site.urls),
    # path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('management/', include('management.urls')),
    path('system/', include('system.urls')),
    path('api/auth/token/', TokenObtainPairView.as_view()),
    path('api/auth/token/refresh/', TokenRefreshView.as_view()),
    path('api/auth/token/verify/', TokenVerifyView.as_view()),
    path('favicon.ico', RedirectView.as_view(
        url=staticfiles_storage.url('favicon.ico')))

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
