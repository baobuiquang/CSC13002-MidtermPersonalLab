from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    return render(
        request, 'accounts/dashboard.html',
        {
            # Objects
            'orders': orders,
            'customers': customers,
            # Stat
            'total_orders': orders.count(),
            'delivered_orders': orders.filter(status='Delivered').count(),
            'pending_orders': orders.filter(status='Pending').count(),
            'total_customers': customers.count(),
        }
    )

def products(request):
    products = Product.objects.all()
    return render(
        request, 'accounts/products.html',
        {
            'products': products,
        }
    )

def customer(request):
    return render(request, 'accounts/customer.html')