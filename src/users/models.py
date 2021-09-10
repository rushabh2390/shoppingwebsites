from django.db import models

# Create your models here.
from django.db import models
from django.db.models.fields import AutoField, BooleanField
from django.core.validators import RegexValidator
phone_regex = RegexValidator(
        regex=r'^\d{10}$',
        message="Please enter 10 digits mobiel number"
    )
# Create your models here.
class User(models.Model):
    userID = models.AutoField(primary_key=True)
    userFirstName = models.CharField(max_length = 200)
    userLastName = models.CharField(max_length = 200)
    userEmail = models.EmailField(max_length= 300)
    userPwd = models.CharField(max_length=200)
    userAddress = models.TextField(max_length=300)
    userShipmentAddress = models.TextField(max_length = 300)
    userContactNo = models.CharField(validators=[phone_regex], max_length=60,
                             null=True, blank=True)
    isSeller = models.BooleanField(default=False)
    profilephoto = models.ImageField(upload_to='profile/',blank=True, null=True)

    @staticmethod
    def get_user_for_login(email,password):
        try:
            return User.objects.get(userEmail = email,userPwd = password)
        except:
            return False
    
    def get_user(email):
        try:
            return User.objects.get(userEmail = email)
        except:
            return False
            
    @staticmethod
    def is_duplicate(email):
        try:
            return User.objects.get(userEmail = email)
        except:
            return False
    
    @staticmethod
    def updateisseller(custid):
        try:
           user = User.objects.get(userID = custid)
           user.isSeller = True
           user.save()
        except:
            raise

class Seller(models.Model):
    userID = models.ForeignKey(User,on_delete=models.CASCADE)
    companyName = models.CharField(max_length = 200)
    companyGSTIN = models.CharField(max_length=200)
    panNumber = models.CharField(max_length=10)
    registeredAddress = models.CharField(max_length=300)
    pickupAddress = models.CharField(max_length=300)
    aadharCopy = models.ImageField(upload_to='aadhar/',blank=True, null=True)
    gstincertificate = models.ImageField(upload_to='GSTIN/',blank=True, null=True)
    panCopy = models.ImageField(upload_to='pancard/',blank=True, null=True)
    bankAccountNumber = models.IntegerField()
    bankIFSCCode = models.CharField(max_length=20)

    @staticmethod
    def get_user_for_login(email,password):
        try:
            return User.objects.get(userEmail = email,userPwd = password)
        except:
            return False
            
    @staticmethod
    def is_duplicate(email):
        try:
            return User.objects.get(userEmail = email)
        except:
            return False
    