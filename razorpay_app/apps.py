from django.apps import AppConfig


class RazorpayAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'razorpay_app'
    def ready(self):
        from . import siganls
