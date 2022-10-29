from django.contrib import admin
from .models import *


# Register your models here.
class hording_table_admin(admin.TabularInline):
    model = Time


@admin.register(cart)
class accounts_admin(admin.ModelAdmin):
    inlines = [hording_table_admin]
    list_display = ['user']

    class Meta:
        model = cart
