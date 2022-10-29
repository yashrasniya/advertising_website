from django.shortcuts import render, redirect
from django.http import *
from .models import *
from Home.models import *
from Home.views import *
import json
import datetime


# Create your views here.
def login(request):
    return render(request, 'html/login.html')


def add_cart_view(request, id):
    if request.user.is_authenticated:
        o = Hoarding.objects.filter(id=id)
        if len(o) != 0:
            car = cart.objects.get(user=request.user)
            too_many_value = Time.objects.filter(cart=car, hoarding=o[0])
            if len(too_many_value) > 0:
                value = Time.objects.get(id=too_many_value[0].id)
                value.quantity = 1 + too_many_value[0].quantity
                value.save()


            else:
                time = Time(cart=car, hoarding=o[0])
                time.save()
            return redirect(Home_page)
        else:
            return Http404()
    else:
        return redirect(login)


def cart_list(request):
    if request.user.is_authenticated:
        cart_obj = cart.objects.filter(user=request.user)
        time_obj = Time.objects.filter(cart=cart_obj[0])
        if len(time_obj):
            return render(request, 'html/cart.html', {'data': time_obj})
    else:
        return redirect(login)


def changing_quantity(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            print(request.body)
            print(request.body.decode("utf-8"))

            js = json.loads(request.body.decode("utf-8"))
            obj_id = js['id']
            quantity = int(js['quantity'])
            obj = Time.objects.get(id=obj_id)
            if quantity < 1:
                return JsonResponse({'data': 'quantity must be greater then zero!!!'})

            obj.quantity = quantity
            obj.save()
            return JsonResponse({'data': 'done'})

        else:
            return JsonResponse({'data': 'Get request is not allowed'})


    else:
        return redirect(login)


def deleting_cart_item(request, item_id):
    if request.user.is_authenticated:
        obj = Time.objects.filter(id=item_id)
        obj.delete()
        return redirect(cart_list)
    else:
        return redirect(login)
