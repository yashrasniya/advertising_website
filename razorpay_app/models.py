from django.db import models

from Home.models import *
import razorpay

client = razorpay.Client(auth=("rzp_test_vlK7qms1BtJdXt", "GmrIdfs0XYoLWtXsY2E7D5pk"))


# Create your models here.

class Create_payment_link(models.Model):
    choice = [('Paid', 'Paid',), ('Pending', 'Pending',), ('Failed', 'Failed')]
    user_name = models.CharField(blank=True, null=True, max_length=32)
    user_contact = models.CharField(blank=True, null=True, max_length=32)
    user_email = models.CharField(blank=True, null=True, max_length=32)
    Amount = models.IntegerField(blank=True, null=True)
    description = models.TextField(max_length=300, blank=False, null=False)
    Hoarding_id = models.ManyToManyField(Hoarding)
    status = models.CharField(choices=choice, default='Pending', max_length=32)
    short_url = models.URLField(blank=False, null=False)
    payment_link_id = models.CharField(blank=False, null=False, max_length=32)
    payment_link_status = models.CharField(blank=False, null=False, max_length=32)
    razorpay_payment_id = models.CharField(blank=False, null=False, max_length=32)
    razorpay_signature = models.CharField(blank=False, null=False, max_length=32)



class razorpay_gateway_detail(models.Model):
    razorpay_id = models.CharField(blank=False, null=False, max_length=50)
    razorpay_SECRET = models.CharField(blank=False, null=False, max_length=50)
    call_back_url = models.URLField(blank=False, null=False)
