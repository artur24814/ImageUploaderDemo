from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from core.settings import DEBUG

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('imageuploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if DEBUG:
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")),)

urlpatterns += staticfiles_urlpatterns()
