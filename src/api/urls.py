from django.urls import include, path
from rest_framework import routers

import api.views as views

app_name = "api"
router = routers.DefaultRouter()
router.register("categories", views.CategoryViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("products/", views.ProductListView.as_view(), name="products-list"),
    path("products/create", views.ProductCreateView.as_view(), name="products-create"),
    path("products/<int:pk>/", views.ProductDetailsView.as_view(), name="products-details"),
    path("products/<int:pk>/update", views.ProductUpdateView.as_view(), name="products-update"),
    path("products/<int:pk>/delete", views.ProductDeleteView.as_view(), name="products-delete"),
]
