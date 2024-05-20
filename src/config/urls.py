from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from config.settings import dev as settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('shop.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
