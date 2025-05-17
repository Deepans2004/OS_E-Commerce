from django.shortcuts import render
from django.http import HttpResponse


def index_view(request):
    return render(request, 'core/index.html')

def men_view(request):
    return render(request, 'core/men.html')  # This loads the men/index.html template

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

def profile_view(request):
    return render(request, 'core/profile.html')


def order_history_view(request):
    # You can add logic here to fetch order history for the user
    return render(request, 'core/order_history.html')

def edit_profile_view(request):
    # Your logic here (e.g., show a form to edit user profile)
    return render(request, 'core/edit_profile.html')
