from django.contrib import admin
from .models import *


# Register your models here.


class admin_Images(admin.TabularInline):
    model = Image2


class admin_Hoarding(admin.ModelAdmin):
    inlines = [admin_Images]
    list_display = ['name', 'city', 'hoarding_type']

    class Meta:
        model = Hoarding


admin.site.register(Hoarding, admin_Hoarding)


@admin.register(City)
class admin_City(admin.ModelAdmin):
    pass


@admin.register(Type)
class admin_Type(admin.ModelAdmin):
    pass


@admin.register(Image)
class admin_Image(admin.ModelAdmin):
    pass
