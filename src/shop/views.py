from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from shop.models import Category, Product


def get_products(request: HttpRequest) -> HttpResponse:
    category_id = request.GET.get("category_id")
    products = Product.objects.filter(active=True)
    if category_id:
        products = products.filter(category_id=category_id)
    categories = Category.objects.filter(active=True)
    return render(request, "shop/product/products.html", {"products": products, "categories": categories})


def cart(request: HttpRequest) -> HttpResponse:
    cart_data = request.session.get("cart", {})

    if request.method == "POST":
        product_id = request.POST["product_id"]
        if product_id in cart_data:
            cart_data[product_id] = cart_data[product_id] + 1
        else:
            cart_data[product_id] = 1
        request.session["cart"] = cart_data
        return redirect(reverse("shop:cart"))

    cart = {
        "products": [],
        "total": 0,
    }

    for product_id, count in cart_data.items():
        product = Product.objects.get(pk=product_id)
        if product:
            product.count = count
            product.total = product.price * count
            cart["products"].append(product)
            cart["total"] = product.total
    return render(request, "shop/cart/cart.html", {"cart": cart})
