from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import *
@receiver(post_save, sender=Create_payment_link)
def on_transaction_create(sender, instance, created, **kwargs):  # GENERATING THE KEY FOR OTP.

    if created:
        # instance.get_verify()
        pass