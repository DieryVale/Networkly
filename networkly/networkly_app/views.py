from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'networkly_app/home.html')


def products(request):
    return render(request, 'networkly_app/products.html')
