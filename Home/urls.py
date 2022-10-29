

from django.urls import path,include
from .views import *


urlpatterns = [
    path('', Home_page),
    path('search', Search),
    path('about/<name>-<id>/', about,name='some place'),
    path('api/city/', CityApi.as_view()),
    path('api/type/', TypeApi.as_view()),
    path('api/search/', SearchApi.as_view()),
    path('api/about/<id>/', About.as_view(),name='some place'),
]