"""
URLPATTERNS for e_library project.
"""
from django.urls import path, include, re_path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.schemas import get_schema_view
from django.views.generic.base import RedirectView, TemplateView
from django.utils.translation import gettext as _, gettext_lazy

# `Django Admin`
# Text to put at the end of each page's <title>.
admin.AdminSite.site_title = gettext_lazy('E-Pustakalay')

# Text to put in each page's <h1>.
admin.AdminSite.site_header = gettext_lazy('E-Pustakalay Management System API')

# Text to put at the top of the admin index page.
admin.AdminSite.index_title = gettext_lazy('App List')

# URL for the "View site" link at the top of each admin page.
admin.AdminSite.site_url = '/' # 'https://elibrarymanagementsystem.herokuapp.com/'

admin.AdminSite.enable_nav_sidebar = False

admin.AdminSite.empty_value_display = '<i>undefined</i>'



urlpatterns = [
    path('api/', include('emanagement.urls')),
    path('admin/', admin.site.urls),
    path('doc/open/', get_schema_view(
        title="E-Pustakalay",
        urlconf="emanagement.urls",
    ), name="openapi-schema"),
    path('doc/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
    path('', TemplateView.as_view(template_name="index.html"), name='home'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
# urlpatterns += [re_path(r'^(?:.*)/?$', TemplateView.as_view(template_name="emanagement/index.html"), name='home')] 
# else:
#     urlpatterns += [re_path(r'^(?:.*)/?$', TemplateView.as_view(template_name="emanagement/index.html"), name='home')] 