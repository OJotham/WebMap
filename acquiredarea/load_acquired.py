import os
from django.contrib.gis.utils import LayerMapping 
from .models import Acquiredarea

acquiredarea_mapping = {
    'objectid' : 'OBJECTID',
    'name' : 'Name',
    'area' : 'Area',
    'rem_area' : 'Rem_Area',
    'shape_leng' : 'SHAPE_Leng',
    'shape_area' : 'SHAPE_Area',
    'geom' : 'MULTIPOLYGON',
}

acquired_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Data', 'Acquired_Area.shp'),)

def run(verbose = True):
	lm = LayerMapping(
         Acquiredarea, acquired_shp, acquiredarea_mapping,
         transform=True, encoding = 'iso-8859-1',
		)
	lm.save(strict = True, verbose=verbose)
