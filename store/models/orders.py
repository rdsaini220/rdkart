from django.db import models
from .product import Product
from .customer import Customer
from django.utils import timezone
import datetime

# Create your models here.
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=200,default='')
    phone = models.CharField(max_length=13,default='')
    date = models.DateTimeField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return "%s" % self.product
    
    def placeOrder(self):
        self.save()

    @staticmethod 
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')