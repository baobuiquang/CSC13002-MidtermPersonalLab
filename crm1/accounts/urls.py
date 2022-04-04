from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/<str:customer_id>/', views.customer, name='customer'),
    
    path('create_order/', views.createOrder, name='create_order'),
    path('update_order/<str:order_id>/', views.updateOrder, name='update_order'),
    path('delete_order/<str:order_id>/', views.deleteOrder, name='delete_order'),

    path('create_order/<str:customer_id>/', views.createOrderForACustomer, name='create_order_for_a_customer'),
]