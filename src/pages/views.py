from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request,*args, **kwargs):
    # return HttpResponse("<h1>Hello Rushabh Doshi</h1>")
    return render(request,"index.html",{})

# def signup_view(request, *args, ** kwargs):
#     return render(request,"signup.html",{})

def contact_view(request,*args, **kwargs):
    # return HttpResponse("<h1>Hello Rushabh Doshi</h1>")
    return render(request,"contact.html",{})
