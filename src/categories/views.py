from django.shortcuts import render, redirect

from .forms import CategoryForm
from .models import Category
from products.models import Product
# Create your views here.
def add_category(request):
    context = {}
    form = CategoryForm(request.POST or None)
    error_message =None
    success_message = None
    if form.is_valid():
        catname = form["categoryName"].value()
        category = Category.is_duplicate(catname)
        if category:
            error_message= "Category is already exists."
        else:
            form.save()
            success_message = "Category Added Sucessfully"
        
    context['form'] = form
    context['errors'] = error_message
    context["sucess"] = success_message
    return render(request, "addcategory.html",context)

def view_category(request):
    context = {}
    error_message =None
    context["categorylist"] = None
    Categorylist = Category.get_category()
    if len(Categorylist) > 0:
        context["categorylist"] = Categorylist
    else:
        error_message = "No category exist"
    context['errors'] = error_message
    return render(request, "category.html",context)


def catergory_list(request):
    if request.GET.get("category"):
        context = {}
        categoryName = request.GET.get("category")
        category = Category.get_category_by_name(categoryName)
        product= Product.get_product_by_category(category.categoryID)
        if product:
            context["products"] = product
            return render(request,"category_list.html",context)
        else:
            return redirect("/")
    else:
            return redirect("/")