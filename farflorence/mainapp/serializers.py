from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import countries
class countriesSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = countries
        geo_field = "geometry"

        # you can also explicitly declare which fields you want to include
        # as with a ModelSerializer.
        fields = ('name',)