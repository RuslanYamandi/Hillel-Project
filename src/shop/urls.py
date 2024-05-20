from django.urls import path
from shop.views import ListProductsView, CreateProductsView

app_name = 'shop'

urlpatterns = [
    path("products/", ListProductsView.as_view(), name="get_products"),
    path("create/", CreateProductsView.as_view(), name="create_product"),
]
