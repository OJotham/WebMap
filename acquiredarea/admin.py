from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin
#from django.contrib.gis import admin
from . import models as acquiredarea_parc

# Register your models here.
class KairiParcelsAdmin(LeafletGeoAdmin):
	list_display = ( 'parcelID', 'owner_name', 'Initial_Area', 'Remaining_Area')

admin.site.register(acquiredarea_parc.Acquiredarea, LeafletGeoAdmin)
#admin.site.register(acquiredarea_parc.KairiParcels, LeafletGeoAdmin)
admin.site.register(acquiredarea_parc.KairiParcels, KairiParcelsAdmin)


