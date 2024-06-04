from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

import api.views as views

app_name = "api"
router = routers.DefaultRouter()
router.register("categories", views.CategoryViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-redoc"),
    path("", include(router.urls)),
    path("auth/", include("djoser.urls.jwt")),
    path("products/", views.ProductListView.as_view(), name="products_list"),
    path("products/create", views.ProductCreateView.as_view(), name="products_create"),
    path("products/<int:pk>/", views.ProductDetailsView.as_view(), name="products_details"),
    path("products/<int:pk>/update", views.ProductUpdateView.as_view(), name="products_update"),
    path("products/<int:pk>/delete", views.ProductDeleteView.as_view(), name="products_delete"),
]
