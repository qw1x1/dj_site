from django.urls import path, include
from .views import *

urlpatterns = [
    path('orders/', OrdersShow.as_view(), name='orders'),
]   