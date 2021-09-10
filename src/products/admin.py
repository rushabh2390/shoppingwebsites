from django.contrib import admin

# Register your models here.
from .models import Product,ProductsImage
admin.site.register(Product)
admin.site.register(ProductsImage)