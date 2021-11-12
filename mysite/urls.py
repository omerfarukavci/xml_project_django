from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from xml_project import views


urlpatterns = [
    path('', TemplateView.as_view(template_name="xml_project/index.html")),
    path('upload/', views.upload, name='upload'),
    path('', views.upload, name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)