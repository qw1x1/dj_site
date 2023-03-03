from django.urls import path, include
from .views import *

app_name = 'cart'

urlpatterns = [
    path('cart', include([
    path('<slug:slug>/add/', add, name='add'),
    # path('<slug:slug>/add/', ShopCart.as_view(), name='add'),
    path('<slug:slug>/remove/', remove, name='remove'),
    path('order/', order, name='order'),
    ]))
]