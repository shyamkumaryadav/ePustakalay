from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    prefix_default_language=False
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)