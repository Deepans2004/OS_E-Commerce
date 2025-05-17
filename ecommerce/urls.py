from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views

urlpatterns = [
    # Admin Panel
    path("admin/", admin.site.urls),

    # Home Page
    path("", views.index_view, name="index"),

    # Auth routes from core app
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup_view, name="login_signup"),
    path("logout/", views.logout_view, name="logout"),

    # Core Pages
    path("men/", views.men_view, name="men"),
    path("women/", views.women_view, name="women"),
    path("about/", views.about_view, name="about"),
    path("contact/", views.contact_view, name="contact"),
    path("product-detail/", views.product_detail_view, name="product-detail"),
    path("cart/", views.cart_view, name="cart"),
    path("checkout/", views.checkout_view, name="checkout"),
    path("order-complete/", views.order_complete_view, name="order-complete"),
    path("add-to-wishlist/", views.add_to_wishlist_view, name="add-to-wishlist"),
    path("terms-conditions/", views.terms_conditions_page_view, name="terms-conditions"),

    # User Profile & Orders
    path("profile/", views.profile_view, name="profile"),
    path("orders/", views.order_history_view, name="order-history"),
    path("edit-profile/", views.edit_profile_view, name="edit-profile"),
]

# Static & Media files handling (development only)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
