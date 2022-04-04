from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory

from .models import *
from .forms import *
from .filters import *

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

def customer(request, customer_id):
    cstm = Customer.objects.get(id=customer_id)
    ords = cstm.order_set.all()

    myFilter = OrderFilter(
        request.GET,
        queryset = ords,
    ) # from filters.py
    ords = myFilter.qs

    return render(
        request, 'accounts/customer.html',
        {
            'customer': cstm,
            'orders': ords,
            'orders_count': ords.count(),
            'myFilter': myFilter,
        }
    )

def createOrder(request):

    ord_form = OrderForm()

    if request.method == 'POST':
        print(f">> {request.POST}")
        ord_form = OrderForm(request.POST)
        if ord_form.is_valid():
            ord_form.save()
            return redirect('/')
    else:
        return render(
            request, 'accounts/order_form.html',
            {
                'ord_form': ord_form,
            }
        )

def createOrderForACustomer(request, customer_id):

    OrderFormSet = inlineformset_factory(
        Customer, Order,
        fields = ('product', 'status'),
        extra = 5,
    )

    cstm = Customer.objects.get(id = customer_id)

    # ord_form = OrderForm(
    #     initial = {'customer': cstm}  # same as createOrder, but pre-fill here
    # )
    ord_formset = OrderFormSet(
        instance = cstm,                 # This will pre-fill, even with customer's old orders
        queryset = Order.objects.none(), # This will hide the old orders
    )

    if request.method == 'POST':
        print(f">> {request.POST}")
        # ord_form = OrderForm(request.POST)
        ord_formset = OrderFormSet(
            request.POST,
            instance = cstm,
        )
        if ord_formset.is_valid():
            ord_formset.save()
            return redirect('/')
    else:
        return render(
            request, 'accounts/order_form.html',
            {
                'ord_form': ord_formset,
            }
        )

def updateOrder(request, order_id):

    ord = Order.objects.get(id = order_id)
    ord_form = OrderForm(instance = ord)     # same as create order but pre-fill the info of this order

    if request.method == 'POST':
        print(f">> {request.POST}")
        ord_form = OrderForm(request.POST, instance = ord)
        if ord_form.is_valid():
            ord_form.save()
            return redirect('/')
    else:
        return render(
            request, 'accounts/order_form.html',
            {
                'ord_form': ord_form,
            }
        )

def deleteOrder(request, order_id):
    ord = Order.objects.get(id = order_id)
    # ord_form = OrderForm(instance = ord)     # same as create order but pre-fill the info of this order

    if request.method == 'POST':
        print(f">> {request.POST}")
        ord.delete()
        return redirect('/')
    else:
        return render(
            request, 'accounts/delete_order.html',
            {
                'ord': ord,
            }
        )