from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes
from django.contrib.gis.geos import  LineString
from .models import countries, post
from .serializers import countriesSerializer, PostSerializer
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets


# Create your views here.

def main(request):
    return render(request, 'mainapp/map.html')



class PostViewSet(viewsets.ModelViewSet):
    queryset = post.objects.all()
    serializer_class = PostSerializer



@api_view(['GET'])
def howfar(request,lon,lat):
    if request.method == 'GET':
        st_line = LineString((11.246530,43.777776), (lon, lat), srid=4326)
        queryset = countries.objects.filter(geometry__intersects=st_line)
        serlialized_output = countriesSerializer(queryset, many=True)
        return Response(serlialized_output.data)

