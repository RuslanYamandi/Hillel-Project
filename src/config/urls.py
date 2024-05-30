from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from config.settings import dev as settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("account.urls")),
    path("", include("shop.urls")),
    path("api/", include("api.urls")),
    path("api-auth/", include("rest_framework.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
