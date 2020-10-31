from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView



urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('book/', include('system.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)