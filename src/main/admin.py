from django.contrib import admin

from main.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "email", "is_active", "is_staff", "is_superuser")
    list_display_links = ("id", "email")
    ordering = ("id",)
    list_filter = ("is_active", "is_staff")
    search_fields = ("first_name", "last_name", "phone", "email")
    list_editable = ("is_active", "is_staff", "is_superuser")
    fieldsets = (
        ("Personal information", {"fields": ("first_name", "last_name", "email")}),
        ("Additional information", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )

    actions = ['make_active', 'make_inactive']

    @admin.action(description='Activate selected Users')
    def make_active(self, request, queryset):
        queryset.update(is_active=True)

    @admin.action(description='Deactivate selected Users')
    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)


admin.site.register(User, UserAdmin)
