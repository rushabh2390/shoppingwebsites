def categories(request):
    from categories.models import Category
    return {'categories': Category.objects.all().order_by("categoryName")}

def products(request):
    from products.models import Product
    return {'products': Product.objects.all()}
     