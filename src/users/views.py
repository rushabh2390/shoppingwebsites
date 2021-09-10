from django.shortcuts import redirect, render

from .models import User,Seller
from .forms import UsersForm, LoginForm, SellersForm

# Create your views here.
# Create your views here.
def signup_view(request):
    context ={}
    error_message = None
    success_message = None
    if request.method == 'POST':
        form = UsersForm(request.POST, request.FILES)
        if form.is_valid():
            email = form["userEmail"].value()
            user =User.get_user(email)
            if user:
                error_message ="Email is already exist"
            else:
                form.save()
                success_message = "Registration is Sucessfully"
    else:
        form = UsersForm(None)
    
    context['form'] = form
    context["errors"] = error_message
    context["success"] = success_message
    return render(request, "signup.html",context)

def login_request(request):
    context ={}
    form = LoginForm(request.POST or None)
    error_message =None
    if form.is_valid():
        email = form["userEmail"].value()
        password = form["userPwd"].value()
        user = User.get_user_for_login(email,password)
        if user:
            print(user.userID)
            request.session['user_id'] = user.userID
            request.session['user_email'] = user.userEmail
            request.session['isseller'] = user.isSeller
            return render(request, "index.html")
        else:
            error_message ="Email or password is incorrect"
        
    
    context['form'] = form
    context["error"] = error_message
    return render(request, "login.html",context)

def logout_request(request):
    if request.session.get('user_id', False):
        del request.session["user_id"]
        del request.session["user_email"]
        return redirect("/")

def seller_view(request):
    if request.session.get('user_email', False):
        context ={}
        error_message = None
        success_message = None
        if request.method == 'POST':
            form = SellersForm(request.POST,request.FILES)
            if form.is_valid() and request.FILES and  form.cleaned_data != {}:
                User.updateisseller(request.session['user_id'])
                user= User.get_user(request.session['user_email'])
                request.session['isseller'] = user.isSeller
                seller = form.save(commit=False)
                seller.userID= user
                seller.save()
                success_message="Congratulation Now you are seller"
            else:
                error_message = form.errors
        else:
            form = SellersForm(None)
        
        context['form'] = form
        context["errors"] = error_message
        context["success"] = success_message
        return render(request, "sellerregistration.html",context)
    else:
        return redirect("/login")