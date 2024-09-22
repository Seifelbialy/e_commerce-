from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Product

def home_view(request):
    return render(request, 'home.html')  # This should match exactly with the template name

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')
from django.shortcuts import render, get_object_or_404
from .models import Product

def product_detail_view(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})

def all_products_view(request):
    products = Product.objects.all()
    return render(request, 'products/all_products.html', {'products': products})