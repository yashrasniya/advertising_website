from django.shortcuts import render, redirect
from .models import *
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializers import Hoarding_data


# Create your views here.
class CityApi(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        city = City.objects.all().values()
        return Response({'status': True, 'city': city})


class TypeApi(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        type = Type.objects.all().values()
        return Response({'status': True, 'type': type})


class SearchApi(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        if request.GET.get('city', '') and request.GET.get('type', ''):
            c = request.GET['city']
            t = request.GET['type']
            ci = City.objects.filter(city_name=c)
            ty = Type.objects.filter(type_name=t)
            print(ci,ty,City.objects.all(),Type.objects.all())
            if ci and ty:
                Hoarding_data = Hoarding.objects.all().filter(city=ci[0].id, hoarding_type_id=ty[0].id)
            else:
                return Response({'status': False, 'error': 'not found'})

            return Response({'status': True, 'Hoarding_data': Hoarding_data.values()})
        else:

            return Response({'status': False, 'error': 'query not found'})

class About(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id):
        Hoarding_data_ = Hoarding.objects.get(id=id)
        # if len(Hoarding_data_)==0:
        #     return Response({'status': False,'error':'id not found'})
        print(Hoarding_data_)
        ser=Hoarding_data(Hoarding_data_)
        return Response({'status': True, 'hoarding_data': ser.data})


def Home_page(request):
    city = City.objects.all()
    t = Type.objects.all()
    return render(request, 'html/pages/home.html', {'city': city, 'Type': t})


def Search(request):
    city = City.objects.all()
    type_ = Type.objects.all()
    Hoarding_data = ''
    if request.method == 'GET':
        c = request.GET['city']
        t = request.GET['type']
        ci = City.objects.filter(city_name=c)
        ty = Type.objects.filter(type_name=t)
        if ci and ty:
            Hoarding_data = Hoarding.objects.all().filter(city=ci[0].id, hoarding_type_id=ty[0].id)
        else:
            Hoarding_data = 'Not found'
    print(Hoarding_data)
    return render(request, 'html/pages/home.html', {'city': city, 'Type': type_, 'Hoarding_data': Hoarding_data})


def about(request, name, id):
    Hoarding_data_ = Hoarding.objects.all().filter(name=name, id=id)
    Hoarding_data = Hoarding_data_.values()[0]
    Hoarding_data['images'] = Hoarding_data_.all()[0].images
    Hoarding_data['active'] = 0
    return render(request, 'html/pages/about.html', Hoarding_data)
