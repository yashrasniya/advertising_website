from django.urls import path,include
from .views import *


urlpatterns = [
    path('create_payment_link/<hording_id>', create_payment_link),
    path('payment_verify', verify_payment),
    path('book_cart', book_cart)

]
