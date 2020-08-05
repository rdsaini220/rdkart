from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from store.models.product import Product
from store.models.orders import Order
from store.models.customer import Customer
# from store.middleware.auth import auth_middleware
# from django.utils.decorators import method_decorator
# Create your views here.

class OrdersView(View):
    # @method_decorator(auth_middleware)
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        return render(request, 'orders/order.html',{'orders':orders})
        
