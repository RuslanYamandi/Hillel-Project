from django.urls import include, path
from rest_framework import routers

from api.views import *

app_name = "api"
router = routers.DefaultRouter()
router.register("categories", CategoryViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("products/", ProductListView.as_view(), name="products-list"),
    path("products/create", ProductCreateView.as_view(), name="products-create"),
    path("products/<int:pk>/", ProductDetailsView.as_view(), name="products-details"),
    path("products/<int:pk>/update", ProductUpdateView.as_view(), name="products-update"),
    path("products/<int:pk>/delete", ProductDeleteView.as_view(), name="products-delete"),
]
