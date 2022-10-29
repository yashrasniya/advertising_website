from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(razorpay_gateway_detail)
class admin_razorpay_gateway_detail(admin.ModelAdmin):
    pass


@admin.register(Create_payment_link)
class admin_razorpay_gateway_detail(admin.ModelAdmin):
    pass
