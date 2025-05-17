from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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
    if request.user.is_authenticated:
        return redirect('core:index')

    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect('core:index')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'core/login.html', {'form': form})


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('core:index')

    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Signup successful.")
            return redirect('core:index')
        else:
            messages.error(request, "Signup failed. Please correct the errors below.")

    return render(request, 'core/login_signup.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('login')


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

def terms_conditions_page_view(request):
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
