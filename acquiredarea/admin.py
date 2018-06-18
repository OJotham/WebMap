from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin
#from django.contrib.gis import admin
from . import models as acquiredarea_parc

# Register your models here.
class KairiParcelsAdmin(LeafletGeoAdmin):
	# Remaining_Area = 'remm_area' 
	list_display = ( 'name','kairi_parc','remm_area')

admin.site.register(acquiredarea_parc.Acquiredarea, LeafletGeoAdmin)
admin.site.register(acquiredarea_parc.KairiParcels, KairiParcelsAdmin)
#admin.site.register(Acq_Area, admin.GeoModelAdmin)

