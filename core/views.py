from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User  # if you use User anywhere
# from .forms import CustomUserCreationForm
from .forms import SignUpForm

# ----------------------------
# ✅ Home Page (Protected)
# ----------------------------
@login_required(login_url='/login/')
def index_view(request):
    return render(request, 'core/index.html')


# ----------------------------
# ✅ Authentication Views
# ----------------------------

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  # bind data to form
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Make sure 'home' is the name of your home URL pattern
        else:
            messages.error(request, 'Invalid credentials')
    else:
        form = AuthenticationForm()  # empty form for GET request

    return render(request, 'core/login.html', {'form': form})



def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after signup
            return redirect('index')  # Change 'home' to your home URL name
    else:
        form = SignUpForm()
    return render(request, 'core/login_signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # or any page you want after logout


# ----------------------------
# ✅ Public Views
# ----------------------------

def men_view(request):
    return render(request, 'core/men.html')

def about_view(request):
    return render(request, 'core/about.html')

def contact_view(request):
    return render(request, 'core/contact.html')

def product_detail_view(request):
    return render(request, 'core/product-detail.html')

def cart_view(request):
    return render(request, 'core/cart.html')

def checkout_view(request):
    return render(request, 'core/checkout.html')

def order_complete_view(request):
    return render(request, 'core/order-complete.html')

def add_to_wishlist_view(request):
    return render(request, 'core/add-to-wishlist.html')

def women_view(request):
    return render(request, 'core/women.html')

def terms_conditions_page(request):
    return render(request, 'core/terms_conditions_page.html')


# ----------------------------
# ✅ Protected Views (Login Required)
# ----------------------------

@login_required(login_url='/login/')
def profile_view(request):
    return render(request, 'core/profile.html')

@login_required(login_url='/login/')
def order_history_view(request):
    return render(request, 'core/order_history.html')

@login_required(login_url='/login/')
def edit_profile_view(request):
    return render(request, 'core/edit_profile.html')
