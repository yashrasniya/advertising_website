from django.db import models


# Create your models here.
class Company_details(models.Model):
    Company_name = models.CharField(max_length=50, blank=False, null=False)
    Company_logo = models.ImageField(blank=False, null=False, upload_to='upload/logo')
    Company_description = models.TextField(max_length=400, blank=False, null=False)
    Company_phone_number = models.CharField(max_length=12, blank=False, null=False)
    Company_whatsapp_number = models.CharField(max_length=12, blank=False, null=False)
    Company_email = models.EmailField(blank=False, null=False)
    Company_facebook_link = models.URLField(max_length=50, blank=False, null=False)
    Company_instagram_link = models.URLField(max_length=50, blank=False, null=False)
    Company_address = models.TextField(max_length=500, blank=False, null=False)
    Company_latitude = models.CharField(max_length=10, blank=False, null=False)
    Company_longitude = models.CharField(max_length=10, blank=False, null=False)

