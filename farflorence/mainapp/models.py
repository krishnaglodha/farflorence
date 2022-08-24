from django.db import models

# Create your models here.
from django.contrib.gis.db import models # this will override the default models import


class countries(models.Model):
    name = models.CharField(max_length=24)
    geometry = models.PolygonField(srid=4326)


    def __str__(self):
        return self.name

