from django.db import models
from products.models import Product
from users.models import User

# Create your models here.
class Cart(models.Model):
    cartID = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    productQty = models.IntegerField(max_length=1000)
    productTax = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey(User,on_delete=models.CASCADE)