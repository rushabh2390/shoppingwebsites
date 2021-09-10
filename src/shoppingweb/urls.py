"""shoppingweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from pages.views import home_view, contact_view
from users.views import login_request, signup_view, logout_request,seller_view
from categories.views import add_category,view_category, catergory_list
from products.views import add_product,product_view,product_list,updateproduct,deleteproduct
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('contact', contact_view, name='contact'),
    path('signup_view', signup_view, name='sign_up'),
    path('addcategory', add_category, name='add_category'),
    path("login", login_request, name="login"),
    path("logout", logout_request, name="logout"),
    path('category',view_category,name="view_category"),
    path('category/list',catergory_list,name="view_category"),
    path('addproduct',add_product,name="add_product"),
    path('becomeseller',seller_view, name='seller'),
    path('productdetails', product_view, name='product view'),
    path('updateproduct', updateproduct, name='product view'),
    path('deleteproduct', deleteproduct, name='product view'),
    path('myproduct', product_list, name='product list'),    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
