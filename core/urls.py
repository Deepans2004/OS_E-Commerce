from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.index_view, name='index'),
    path("index/", views.index_view, name='index'),
    path('men/', views.men_view, name='men'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('product-detail/', views.product_detail_view, name='product-detail'),
    path('cart/', views.cart_view, name='cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path("order-complete/", views.order_complete_view, name='order-complete'),
    path("add-to-wishlist/", views.add_to_wishlist_view, name='add-to-wishlist'),
    path("women/", views.women_view, name='women'),
    path("terms_conditions_page/", views.terms_conditions_page_view, name='terms_conditions_page'),
    path("profile/", views.profile_view, name='profile'),
    path('orders/', views.order_history_view, name='order-history'),
    path('edit-profile/', views.edit_profile_view, name='edit-profile'),
]