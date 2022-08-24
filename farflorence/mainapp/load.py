from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import countries

world_mapping = {
    'name' : 'NAME',
    'geometry' : 'POLYGON',
}

world_shp = Path(__file__).resolve().parent / 'data' / 'countries.shp'

def run(verbose=True):
    lm = LayerMapping(countries, world_shp, world_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)