from django.shortcuts import render
from django.http import HttpResponse


def index_view(request):
    return render(request, 'core/index.html')

def men_view(request):
    return render(request, 'core/men.html')

def about_view(request):
    return render(request, 'core/about.html')

def contact_view(request):
    return render(request, 'core/contact.html')