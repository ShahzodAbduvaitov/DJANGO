from django.contrib import admin

from products.models import Category, ProductModel


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name']
    search_fields = ['category_name']
    list_filter = ['id']


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'created_at']
    search_fields = ['product_name']
    list_filter = ['id']