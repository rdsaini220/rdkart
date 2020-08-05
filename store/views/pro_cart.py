from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password,check_password
from django.views import View
from store.models.product import Product


# Create your views here.
class ProductCart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        return render(request, 'orders/cart.html', {'products': products})


        
        
