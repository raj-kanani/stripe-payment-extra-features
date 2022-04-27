from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'file', 'url']


admin.site.register(Product)
