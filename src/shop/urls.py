from django.urls import path

from shop.views import cart, get_products

app_name = "shop"

urlpatterns = [
    path("", get_products, name="get_products"),
    path("cart/", cart, name="cart"),
]
