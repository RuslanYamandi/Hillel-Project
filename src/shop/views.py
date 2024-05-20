from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from shop.forms import ProductForm
from shop.models import Product, Category


class ListProductsView(ListView):
    model = Product
    template_name = 'shop/product/products.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(active=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(active=True)
        return context


class CreateProductsView(CreateView):
    template_name = "shop/product/create.html"
    form_class = ProductForm
    success_url = reverse_lazy("shop:get_products")
