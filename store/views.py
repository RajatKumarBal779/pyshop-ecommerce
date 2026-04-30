from django.shortcuts import render,redirect
from .models import Product,Category,Profile
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm, UpdateUserForm, ChangePassword,UserInfoForm
from django.db.models import Q
import json
from cart.cart import Cart
from payment.forms import ShippingForm
from payment.models import ShippingAddress
# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request,'testapp/home.html',{'products':products})
def about(request):
    return render(request,'testapp/about.html')
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # html name attribute
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            
            # Do some shopping cart stuff
            current_user = Profile.objects.get(user__id=request.user.id)
            # Get saved data from database
            saved_cart=current_user.old_cart
            # Convert datebase string to python dict
            if saved_cart:
                converted_cart = json.loads(saved_cart)
                # add the loaded cart dictionary to our session
                # Get the cart
                cart = Cart(request)
                # Loop through the cart and add the items from the database
                for key,value in converted_cart.items():
                    cart.db_add(product=key,quantity=value)
            
            messages.success(request,(f'Welcome Back, {user.username}!'))
            return redirect('home')
        else:
            messages.error(request,"Invalid Username Or Password.")
            return redirect('login')
    return render (request,'testapp/login.html')
def logout_user(request):
    logout(request)
    messages.success(request,("You have been logged out successfully. See you again!"))
    return redirect ('home')
def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #Login User.
            user = authenticate(request, username=username, password=password)
            login(request, user)

            messages.success(request, "Username Created - Please Fill Out Your User Info.")
            return redirect('update_info')

        else:
            messages.error(request, "Something went wrong. Please try again.")
            return redirect('register')

    else:
        form = SignUpForm()

    return render(request, 'testapp/register.html', {'form': form})
def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request,'testapp/product.html',{'product':product})
def category(request,cat):
    try:
        category = Category.objects.get(name = cat)
        products = Product.objects.filter(category=category)
        return render(request,'testapp/category.html',{'category':category,"products":products})
    except:
        messages.success(request,("This Category Doesn't Exist!!!"))
        return redirect('home')
def category_summary(request):
    categories = Category.objects.all()
    return render(request,'testapp/category_summary.html',{'categories':categories})
def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)
        if user_form.is_valid():
            user_form.save()
            
            login(request,current_user)
            messages.success(request,('User Has Been Updated!'))
            return redirect('home')
        return render(request,'testapp/update_user.html',{'user_form':user_form})
    else:
        messages.success(request,('You Must Be Logged In To Update Profile.'))
        return redirect('home')
def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        # Did they fill out the form
        if request.method == 'POST':
            form = ChangePassword(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,("Your Password Has Been Changed. Login Again."))
                return redirect('login')
            else:
                for error in list(form.errors.values()):
                    messages.error(request,(error[0]))    
                return redirect('update_password')
        else:
            form = ChangePassword(current_user)
            return render(request,'testapp/update_password.html',{'form':form})
    else:
        messages.success(request,('You Must Be Logged In To Update Password.'))
        return redirect('home')
def update_info(request):
    if request.user.is_authenticated:
        
        current_user = Profile.objects.get(user__id=request.user.id)
        # Get current users shipping info.
        shipping_user = ShippingAddress.objects.get(shipping_user__id=request.user.id)
        
        form = UserInfoForm(request.POST or None, instance=current_user)
        # Get users shipping form
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        if form.is_valid() or shipping_form.is_valid():
            form.save()
            shipping_form.save()
            messages.success(request,("Your Info Has Been Updated."))
            return redirect('home')
        return render(request,'testapp/update_info.html',{'form':form,'shipping_form':shipping_form})
    else:
        messages.error(request,('You Must Be Logged In To Change User Info.'))
        return redirect('home')
def search(request):
    if request.method == 'POST':
        searched = request.POST.get('searched', '').strip()

        #  Check empty input
        if searched == "":
            return render(request, 'testapp/search.html', {})

        #  Filter products
        results = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))

        #  No results
        if not results:
            messages.error(request, "No product found.")
            return render(request, 'testapp/search.html', {})

        #  Send results
        return render(request, 'testapp/search.html', {'searched': results})

    return render(request, 'testapp/search.html', {})
        