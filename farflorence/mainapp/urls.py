from django.contrib import admin
from django.urls import path,register_converter
from .views import howfar,main, PostViewSet
from . import converters
from rest_framework import routers

register_converter(converters.FloatUrlParameterConverter, 'float')
router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('far/<float:lon>/<float:lat>/', howfar, name='howfar'),
     path('', main, name='main'),
]
