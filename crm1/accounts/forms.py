from django.forms import ModelForm
from .models import *

class OrderForm(ModelForm):
    class Meta:
        model = Order
        # fields = ['customer', 'product', 'date_created', 'status']
        fields = '__all__'
