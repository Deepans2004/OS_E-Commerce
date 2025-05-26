from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.decorators.cache import cache_page
from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from .models import Product, WishlistItem


# ----------------------------
# Home Page (Protected)
# ----------------------------
@login_required(login_url=reverse_lazy('login'))
def index_view(request):
    return render(request, 'core/index.html')

# ----------------------------
# Authentication Views
# ----------------------------

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"{username} logged in successfully!")
            return redirect('index')  # or your home page
        else:
            error = "Invalid username or password"
            return render(request, 'core/login.html', {'error': error})
    else:
        return render(request, 'core/login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'core/login_signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'core/login_signup.html')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        messages.success(request, "Account created successfully!")
        return redirect('core/login.html')  # URL name of your login view

    return render(request, 'core/login_signup.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'core/login_signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'core/login_signup.html')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        messages.success(request, "Account created successfully!")
        return redirect('login')  # URL name of your login view

    return render(request, 'core/login_signup.html')

def logout_view(request):
    logout(request)
    return redirect('login')


# ----------------------------
# Public Views
# ----------------------------

def men_view(request):
    products = Product.objects.all()  # get all products
    return render(request, 'core/men.html', {'products': products})

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

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item, created = WishlistItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        wishlist_item.quantity += 1
        wishlist_item.save()
    return redirect('wishlist')


@login_required
def wishlist_page(request):
    items = WishlistItem.objects.filter(user=request.user)
    total = sum(item.total_price() for item in items)
    return render(request, 'core/add-to-wishlist.html', {'items': items, 'total': total})


@login_required
def remove_from_wishlist(request, item_id):
    item = get_object_or_404(WishlistItem, id=item_id, user=request.user)
    item.delete()
    return redirect('wishlist')




def women_view(request):
    return render(request, 'core/women.html')

def terms_conditions_page(request):
    return render(request, 'core/terms_conditions_page.html')

# ----------------------------
# Protected Views (Login Required)
# ----------------------------

@login_required(login_url=reverse_lazy('login'))
def profile_view(request):
    return render(request, 'core/profile.html')

@login_required(login_url=reverse_lazy('login'))
def order_history_view(request):
    return render(request, 'core/order_history.html')

@login_required(login_url=reverse_lazy('login'))
def edit_profile_view(request):
    return render(request, 'core/edit-profile.html')

def offline_view(request):
    return render(request, 'core/offline.html')


def about(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # AJAX request - return partial HTML (content only)
        return render(request, 'core/about_content.html')
    else:
        # Normal page load - return full page
        return render(request, 'core/about.html')

def contact(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'core/contact_content.html')
    else:
        return render(request, 'core/contact.html')

@cache_page(60 * 1)  # cache for 10 minutes
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'core/product_detail.html', {'product': product})

#product buying

@login_required
def wishlist_view(request):
    items = WishlistItem.objects.filter(user=request.user)
    return render(request, 'core/wishlist.html', {'items': items})

