from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from client.views import *

urlpatterns = [
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('articles/', include('articles.urls')),
    path('old/', include('pages.urls')),
    path('', include('front.urls')),
    path('client/', include("client.urls"), name="client"),
    path('thanks/', thanks, name="thanks"),
    path('med/', BlogListView.as_view(), name="client"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)