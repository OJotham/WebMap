import os
from django.contrib.gis.utils import LayerMapping 
from .models import KairiParcels

# Auto-generated `LayerMapping` dictionary for Parcels model
parcels_mapping = {
    'kairi_parc' : 'kairi_parc',
    'name' : 'NAME',
    'owner_name' : 'OWNER_NAME',
    'remm_area' : 'Remm_Area',
    'area' : 'Area',
    'geom' : 'MULTIPOLYGON',
}
kairiparc_shp = os.path.abspath( os.path.join(os.path.dirname(__file__), 'Data', 'Kairi_Parcels.shp'),)

def run(verbose=True): 
	lm = LayerMapping( 
		KairiParcels, kairiparc_shp, parcels_mapping, 
		transform=True, encoding='iso-8859-1',
	)
	lm.save(strict=True, verbose=verbose)