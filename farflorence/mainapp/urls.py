from django.contrib import admin
from django.urls import path,register_converter
from .views import howfar,main
from . import converters
register_converter(converters.FloatUrlParameterConverter, 'float')

urlpatterns = [
    path('far/<float:lon>/<float:lat>/', howfar, name='howfar'),
     path('', main, name='main'),
]