"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index_view, name='index'),  # root URL mapped directly
    path("index/", views.index_view, name='home'),
    path("men/", views.men_view, name='men'),
    path("about/", views.about_view, name='about'),
    path("contact/", views.contact_view, name='contact'),
    path("product-detail/", views.product_detail_view, name='product-detail'),
    path("cart/", views.cart_view, name='cart'),
    path("checkout/", views.checkout_view, name='checkout'),
    path("order-complete/", views.order_complete_view, name='order-complete'),
    path("add-to-wishlist/", views.add_to_wishlist_view, name='add-to-wishlist'),
    path("women/", views.women_view, name='women'),
    path("terms_conditions_page/", views.terms_conditions_page_view, name='terms_conditions_page'),
    path("profile/", views.profile_view, name='profile'),
    path('orders/', views.order_history_view, name='order-history'),
    path('edit-profile/', views.edit_profile_view, name='edit-profile'),
]

if settings.DEBUG:
   urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
   urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)