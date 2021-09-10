from django import forms
from django.forms import fields
from .models import Category

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        exclude =["categoryID"]
        widgets = {
            'categoryName' : forms.TextInput(),
            'categoryDesc' : forms.Textarea(),
            
        },
        labels ={
            'categoryName': 'Category Name',
            'categoryDesc': 'Category Description',
        }