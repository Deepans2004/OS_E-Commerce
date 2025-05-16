from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.index_view, name='home'),
    path("index/", views.index_view, name='index'),
    path("men/", views.men_view, name='men'),
    path("about/", views.about_view, name='about'),
    path("contact/", views.contact_view, name='contact'),
]