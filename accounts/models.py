from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from Home.models import *


# Create your models here.

class cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hording = models.ManyToManyField(Hoarding, through='Time')


class Time(models.Model):
    cart = models.ForeignKey(cart, on_delete=models.CASCADE)
    hoarding = models.ForeignKey(Hoarding, on_delete=models.CASCADE)
    time_stamp = models.TimeField(auto_created=True,auto_now_add=True)
    quantity = models.IntegerField(blank=False, null=True,default=1)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        cart.objects.create(user=instance)



