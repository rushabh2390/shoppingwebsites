from django import forms
from django.db import models
from django.forms import fields
from .models import Product
from django.forms import ModelChoiceField
from datetime import datetime

class CategoryModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return (obj.categoryID,obj.categoryName)

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude =["productID","productSKU","sellerID"] 
        widgets = {
            'productName': forms.TextInput(),
            'productPrice': forms.NumberInput(),
            'productName': forms.TextInput(),
            'productWeight': forms.NumberInput(),
            'productCartDesc':forms.Textarea(),
            'productShortDesc':forms.TextInput(),
            'productLongDesc' : forms.TextInput(),
            'productStocks' : forms.TextInput(),
            'productsDiscount' : forms.NumberInput(),
            'isProductAvailable' : forms.NumberInput(),
            'productCategory' : forms.Select(),
            'productCoverImage': forms.ImageField()
        },
        labels ={
            'productName': 'Product Name',
            'productPrice': 'Product Price',
            'productWeight': 'Product Weight',
            'productCartDesc':'Product Cart Description',
            'productShortDesc':'Short Description',
            'productLongDesc' : 'Long Description',
            'productStocks' : 'stocks',
            'productPrice' : 'Price',
            'productsDiscount' : 'Discount',
            'isProductAvailable' :  'Is Available',
            'productCategory' : 'Product Category',
            'productUpdateDate': 'Date',
            'productCoverImage': 'Cover Image'
        }
    def __init__(self, *args, **kwargs):
        super(ProductsForm, self).__init__(*args, **kwargs)
        self.fields['productUpdateDate'].disabled = True
        self.fields['productUpdateDate'].initial = datetime.now().strftime('%d-%m-%Y')

