from django.urls import path
from .views import home_view, about_view, contact_view, product_detail_view, all_products_view

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('product/<int:id>/', product_detail_view, name='product_detail'),
    path('products/', all_products_view, name='all_products'),
]