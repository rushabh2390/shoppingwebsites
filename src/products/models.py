import os
from typing import Text
from django.db import models

from categories.models import Category
from users.models import User

# Create your models here.
class Product(models.Model):
    productID = models.BigAutoField(primary_key=True)
    productSKU = models.CharField(max_length = 200)
    productName = models.CharField(max_length= 300)
    productPrice = models.DecimalField(max_digits=8, decimal_places=2)
    productWeight =  models.DecimalField(max_digits=8, decimal_places=2)
    productCartDesc = models.TextField()
    productShortDesc = models.TextField()
    productLongDesc = models.TextField()
    productCoverImage = models.ImageField(upload_to="image/",null=True,blank=True)
    productCategory = models.ForeignKey(Category,on_delete=models.CASCADE)
    productUpdateDate = models.TextField()
    productStocks = models.FloatField(null=True)
    productsDiscount= models.FloatField(null=True)
    isProductAvailable = models.BooleanField()
    sellerID = models.ForeignKey(User, on_delete=models.CASCADE)
    productTax = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)

    @staticmethod
    def is_duplicate(product_name):
        try:
            return Product.objects.get(productName = product_name)
        except:
            return False
    
    @staticmethod
    def get_product_info(id):
        try:
            return Product.objects.get(productID=id)
        except:
            return False
    
    @staticmethod
    def get_product_by_category(id):
        try:
            return Product.objects.filter(productCategory=id)
        except:
            return False
    
    @staticmethod
    def get_product_by_seller(id):
        try:
            return Product.objects.filter(sellerID=id)
        except:
            return False
    
    @staticmethod
    def delete_product_by_id(id):
        image=Product.objects.filter(pk=id).values('productCoverImage').first()
        if os.path.isfile('media/'+image["productCoverImage"]):
            os.remove('media/'+image["productCoverImage"])
        Product.objects.filter(pk=id).delete()

class ProductsImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="image/",null=True,blank=True)

    @staticmethod
    def get_product_images_by_productid(id):
        try:
            return ProductsImage.objects.filter(product=id)
        except:
            return False
    
    @staticmethod
    def delete_product_images_by_id(id):
        ProductsImage.objects.filter(pk=id).delete()

    @staticmethod
    def delete_product_images_by_productid(id):
        print("id",id)
        productimage=ProductsImage.objects.filter(product=id).values('image')
        print(productimage)
        for img in productimage:
            print(img)
            print(img["image"])
            if os.path.isfile('media/'+img["image"]):
                os.remove('media/'+img["image"])
        ProductsImage.objects.filter(product=id).delete()
    