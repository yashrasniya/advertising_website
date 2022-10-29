from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Hoarding(models.Model):
    name = models.CharField(max_length=32, blank=False, null=False)
    images = models.ManyToManyField('Image', through='Image2')
    map_link = models.URLField(blank=True, null=True)
    city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True)
    hoarding_type = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True)
    price = models.CharField(max_length=32, blank=False, null=False)
    size = models.CharField(max_length=32, blank=False, null=False)


class Image(models.Model):
    img_name = models.CharField(max_length=32, blank=False, null=False)
    img = models.ImageField(upload_to='upload/img')

    def __str__(self):
        if self.img:

            return  str(self.img.url)


class Image2(models.Model):
    img = models.ForeignKey('Image', on_delete=models.CASCADE)
    hoarding = models.ForeignKey('Hoarding', on_delete=models.CASCADE)


class City(models.Model):
    city_name = models.CharField(max_length=32, blank=False, null=False)

    def __str__(self):
        return self.city_name


class Type(models.Model):
    type_name = models.CharField(max_length=32, blank=False, null=False)

    def __str__(self):
        return self.type_name
