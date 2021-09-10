from django.db import models
from django.db.models.deletion import CASCADE

from users.models import User

# Create your models here.
class Order(models.Model):
    orderID = models.BigAutoField(primary_key=True)
    orderCustomerID = models.ForeignKey(User,on_delete=models.CASCADE)
    orderDate = models.DateField()
    orderShippedDate = models.DateField()
    isOrderReturns = models.BooleanField(default=False)
    orderReturnsReason = models.TextField(max_length= 200, null = True)
    orderTrackingNumber = models.TextField(max_length=200)
