from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin
#from django.contrib.gis import admin
from . import models as acquiredarea_parc

# Register your models here.
class KairiParcelsAdmin(LeafletGeoAdmin):
	# Remaining_Area = 'remm_area' 
	list_display = ( 'parcelID', 'owner_name', 'Initial_Area', 'Remaining_Area')

admin.site.register(acquiredarea_parc.Acquiredarea, LeafletGeoAdmin)
#admin.site.register(acquiredarea_parc.KairiParcels, LeafletGeoAdmin)
admin.site.register(acquiredarea_parc.KairiParcels, KairiParcelsAdmin)
#admin.site.register(acquiredarea_parc.Acquiredarea, admin.GeoModelAdmin)
#admin.site.register(acquiredarea_parc.KairiParcels, admin.GeoModelAdmin)

