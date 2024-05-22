from django.forms import ModelForm, NumberInput, Select, Textarea, TextInput

from shop.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "category", "price", "description", "image"]
        widgets = {
            "name": TextInput(attrs={"class": "form-control"}),
            "category": Select(attrs={"class": "form-control"}),
            "price": NumberInput(attrs={"class": "form-control"}),
            "description": Textarea(attrs={"class": "form-control"}),
        }
