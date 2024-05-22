from django.contrib import admin

from shop.models import Category, Order, OrderItem, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "active")
    list_display_links = ("name",)
    search_fields = ("name",)
    ordering = ("id",)

    actions = ["make_active", "make_inactive"]

    @admin.action(description="Activate selected Categories")
    def make_active(self, request, queryset):
        queryset.update(active=True)
        category = queryset.first()
        Product.objects.filter(category=category).update(active=True)

    @admin.action(description="Deactivate selected Categories")
    def make_inactive(self, request, queryset):
        queryset.update(active=False)
        category = queryset.first()
        Product.objects.filter(category=category).update(active=False)


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "price", "active")
    list_display_links = ("name",)
    list_filter = ("category", "active")
    search_fields = ("name",)
    ordering = ("id",)

    actions = ["make_active", "make_inactive"]

    @admin.action(description="Activate selected Products")
    def make_active(self, request, queryset):
        queryset.update(active=True)

    @admin.action(description="Deactivate selected Products")
    def make_inactive(self, request, queryset):
        queryset.update(active=False)


admin.site.register(Product, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "user", "total")
    list_display_links = ("id",)
    search_fields = ("user",)
    ordering = ("id",)


admin.site.register(Order, OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "product", "quantity")
    list_display_links = ("id", "order")
    search_fields = ("order",)
    ordering = ("id",)


admin.site.register(OrderItem, OrderItemAdmin)
