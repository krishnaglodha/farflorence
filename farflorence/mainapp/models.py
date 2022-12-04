from django.db import models

# Create your models here.
from django.contrib.gis.db import models # this will override the default models import



class post(models.Model):
    title = models.CharField( max_length=50)
    active = models.BooleanField(default=True)
    description = models.TextField()    


    def __str__(self):
        return self.title

class countries(models.Model):
    name = models.CharField(max_length=24)
    geometry = models.PolygonField(srid=4326)


    def __str__(self):
        return self.name

