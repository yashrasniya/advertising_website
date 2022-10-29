from django.urls import path
from .mymodel import *

urlpatterns = [
    path('e/login/', login),
    path('e/account/', user_info),
    path('e/register/', register),

]
