from django.urls import path, include
from .views import *

urlpatterns = [
    path('add_cart/<int:id>', add_cart_view),
    path('cart', cart_list),
    path('changing_quantity', changing_quantity),
    path('cart_item_delete/<int:item_id>', deleting_cart_item),
    path('login', login),
]
