from os import error
from django.db.models import query

from django.forms import modelformset_factory
from django.shortcuts import render, get_object_or_404
from categories.models import Category
from users.models import User
from django.shortcuts import redirect, render
from .forms import ProductsForm
from .models import Product,ProductsImage
from categories.models import Category
# Create your views here.
def add_product(request):
    context = {}
    ImageFormset = modelformset_factory(ProductsImage,fields=('image',),extra=4)
    data = {
        'form-TOTAL_FORMS': '2',
        'form-INITIAL_FORMS': '0',
    }
    categories =  Category.objects.all()
    error_message = []
    success_message = None
    if request.method == 'POST':
        form = ProductsForm(request.POST, request.FILES)
        formimageset = ImageFormset(request.POST or None,request.FILES or None)
      
        if form.is_valid() and formimageset.is_valid():
            productdata = form.save(commit=False)
            user = User.get_user(request.session['user_email'])
            productdata.sellerID = user
            productdata.save()
            for f in formimageset:
                try:
                    if f.is_valid() and request.FILES and  f.cleaned_data != {}:
                        photo = ProductsImage(product=productdata,image=f.cleaned_data["image"])
                        photo.save()
                except Exception as e:
                    raise
            success_message = "Product Added Sucessfully"
        else:
            if form.errors:
                error_message = form.errors  
            else:
                error_message = formimageset.errors 
    else:
        form = ProductsForm(None)
        formimageset = ImageFormset(queryset=ProductsImage.objects.none())
    
    context['form'] = form
    context["formimageset"] =formimageset
    context['errors'] = error_message
    context["success"] = success_message
    context["categories"] = categories
    return render(request, "addproduct.html",context)

def product_view(request):
    if request.GET.get("productid",False):
        context = {}
        id = request.GET.get("productid")
        categories = Category.objects.all().order_by("categoryName")
        context["categories"] = categories
        product= Product.get_product_info(id)
        productImage = ProductsImage.get_product_images_by_productid(id)
        if product:
            context["product"] = product
            if productImage:
                context["productImage"] = productImage
            return render(request,"product_details.html",context)
        else:
            return redirect("/")
    else:
            return redirect("/")

def product_list(request):
    context = {}
    if request.session.get('user_id', False):
        id = request.session.get('user_id')
        products = Product.get_product_by_seller(id)
        context["products"] = products
        return render(request,"productlist.html",context)

    else:
            return redirect("/")

def updateproduct(request):
    if request.GET.get("productid",False):
        context = {}
        id = request.GET.get("productid")
        product = Product.get_product_info(id)
        productImage = ProductsImage.get_product_images_by_productid(id)
        ImageFormset = modelformset_factory(ProductsImage,fields=('image',),extra=4)
        data = {
            'form-TOTAL_FORMS': '2',
            'form-INITIAL_FORMS': '0',
        }
        categories =  Category.objects.all()
        error_message = []
        success_message = None
        if request.method == 'POST':
            form = ProductsForm(request.POST, request.FILES)
            formimageset = ImageFormset(request.POST or None,request.FILES or None)
            if form.is_valid() and formimageset.is_valid():
                obj = form.save(commit=False)
                user = User.get_user(request.session['user_email'])
                obj.productID=id
                obj.sellerID = user
                if form.cleaned_data["productCoverImage"] is None :
                    obj.productCoverImage = product.productCoverImage
                if(request.POST.get("deleted_image_list",False)):
                    delids = request.POST.get("deleted_image_list")
                    if delids !="[]":
                        delids = delids.strip('][').split(',')
                        for delid in delids:
                            ProductsImage.delete_product_images_by_id(int(delid.replace('"','')))
                    
                obj.save()
                for f in formimageset:
                    try:
                        if f.is_valid() and request.FILES and  f.cleaned_data != {}:
                            photo = ProductsImage(product=obj,image=f.cleaned_data["image"])
                            photo.save()
                    except Exception as e:
                        formimageset = ImageFormset(queryset=ProductsImage.objects.none())
                product = Product.get_product_info(id)
                productImage = ProductsImage.get_product_images_by_productid(id)
                form = ProductsForm(instance=product)
                success_message = "Product Updated Sucessfully"
            else:
                if form.errors:
                    error_message = form.errors  
                else:
                    error_message = formimageset.errors 
        else:
            if product:
                form = ProductsForm(instance=product)
                formimageset = ImageFormset(queryset=ProductsImage.objects.none())
            else:
                return redirect("/")
        
        context['form'] = form
        context["formimageset"] = formimageset
        context["productimage"] =productImage
        context['errors'] = error_message
        context["success"] = success_message
        context["categories"] = categories
        return render(request, "updateproduct.html",context)    
    else:
            return redirect("myproduct/")
    
def deleteproduct(request):
    if request.GET.get("productid",False):
        id = request.GET.get("productid")
        ProductsImage.delete_product_images_by_productid(id)
        Product.delete_product_by_id(id)        
        return redirect("/myproduct")
    else:
        return redirect("/myproduct")