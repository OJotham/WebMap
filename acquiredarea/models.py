from __future__ import unicode_literals
from django.contrib.gis.db import models

# Create your models here
class KairiParcels(models.Model):
    Initial_Area = models.FloatField()
    parcelID = models.IntegerField()
    owner_name = models.CharField(max_length=50)
    Remaining_Area = models.FloatField()
    Acquired_Area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
	    return self.owner_name

class Acquiredarea(models.Model):
    objectid = models.IntegerField()
    name = models.IntegerField()
    area = models.FloatField()
    rem_area = models.FloatField()
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    def _unicode_(self):
    	return self.name
