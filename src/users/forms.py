from django import forms
from django.forms import fields
from .models import User
from .models import Seller

class UsersForm(forms.ModelForm):

    class Meta:
        model = User
        exclude =["userID","isSeller"]
        widgets = {
            'userFirstName': forms.TextInput(),
            'userLastName': forms.TextInput(),
            'userEmail': forms.TextInput(),
            'userPwd': forms.TextInput(),
            'userAddress': forms.Textarea(),
            'usershipmentAddress': forms.Textarea(),
            'userContactNo': forms.TextInput(),
            'profilephoto': forms.ImageField()
        },
        labels ={
            'userFirstName': 'First Name',
            'userLastName': 'Last Name',
            'userEmail':'Email',
            'userPwd':'Password',
            'userAddress': 'Address',
            'usershipmentAddress': 'Shipment Address',
            'userContactNo': 'Contact Number',
            'profilephoto': "Profile Photo"
        }

class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields =["userEmail", "userPwd"]
        widgets = {
            'userEmail': forms.TextInput(),
            'userPwd': forms.PasswordInput()
        },
        labels ={
            'userEmail':'Email',
            'userPwd':'Password'
        }


class SellersForm(forms.ModelForm):

    class Meta:
        model = Seller
        exclude =["userID"]
        widgets = {
            'companyName': forms.TextInput(),
            'companyGSTIN':forms.TextInput(),
            'panNumber': forms.TextInput(),
            'registeredAddres': forms.TextInput(),
            'pickupAddress' : forms.TextInput(),
            'aadharCopy': forms.ImageField(),
            'gstincertificate': forms.ImageField(),
            'panCopy':forms.ImageField(),
            'bankAccountNumber':forms.NumberInput(),
            'bankIFSCCode':forms.TextInput(),
        },
        labels ={
            'companyName': 'Company Name',
            'companyGSTIN': 'GSTIN number',
            'panNumber':'Pan Number',
            'registeredAddres':'Registered Address',
            'AadharCopy': 'Aadhar Image',
            'gstincertificate': 'GSTIn certificate',
            'panCopy': 'Pan Image',
            'bankAccountNumber': 'Bank Account Number',
            'bankIFSCCode': 'IFSC Code'
        }