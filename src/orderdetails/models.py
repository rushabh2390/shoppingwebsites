from django.db import models

from orders.models import Order
from products.models import Product
# Create your models here.
class OrderDetail(models.Model):
    orderDetailsID = models.BigAutoField(primary_key = True)
    orderDetailsorderID = models.ForeignKey(Order,on_delete=models.CASCADE)
    orderDetailsProductID = models.ForeignKey(Product, on_delete=models.CASCADE)
    orderDetailsProductPrice = models.DecimalField(max_digits=10, decimal_places=2)
    orderDetailsDiscount = models.DecimalField(max_digits=5, decimal_places=2)
    oredrDetailsOrderQty = models.DecimalField(max_digits= 5, decimal_places=2)