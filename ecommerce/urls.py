from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import views
from django.contrib import admin


app_name = "core"

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Your existing app URLs
    # Home Page
    path('', views.index_view, name='index'),

    # Offline Page
    path('offline.html', views.offline_view, name='offline'),

    # Authentication
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='login_signup'),
    path('logout/', views.logout_view, name='logout'),

    # Core Pages
    path('men/', views.men_view, name='men'),
    path('women/', views.women_view, name='women'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('product-detail/', views.product_detail_view, name='product-detail'),
    path('cart/', views.cart_view, name='cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('order-complete/', views.order_complete_view, name='order-complete'),
    path('add-to-wishlist/<int:product_id>/', views.add_to_wishlist, name='add-to-wishlist'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('terms-conditions/', views.terms_conditions_page, name='terms_conditions_page'),

    # Profile & Orders (require login)
    path('profile/', views.profile_view, name='profile'),
    path('orders/', views.order_history_view, name='order-history'),
    path('edit-profile/', views.edit_profile_view, name='edit-profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)