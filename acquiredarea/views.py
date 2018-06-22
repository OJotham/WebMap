from django.db.models import Sum, Avg, Max, Min, Count
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import KairiParcels, Acquiredarea

# Creating the frontend for users to visualize the data.
class HomePageView(TemplateView):
	"""docstring for ClassName"""
	template_name = 'index.html'

# A view to display the chart and carry out queries on the database
class ChartView(View):
	def get(self, request, *args, **kwargs):
		no_parce = Acquiredarea.objects.all().aggregate(Number_of_Parcels_acquired = Count('name'))
		sum_area = Acquiredarea.objects.all().aggregate(Total_Area_Acquired   = Sum('area'))
		avg_area = Acquiredarea.objects.all().aggregate(Average_Area_Acquired = Avg('area'))
		max_area = Acquiredarea.objects.all().aggregate(Maximum_Area_Acquired = Max('area'))
		min_area = Acquiredarea.objects.all().aggregate(Maximum_Area_Acquired = Min('area'))
		#sdv_area = Acquiredarea.objects.all().aggregate(Std_Deviation = Stddev('area'))
		return render(request, 'charts.html', {
			'sum':sum_area,
			'average':avg_area,
			'max':max_area,
			'parcel_num':no_parce,
			'min':min_area
			}
			)
# A view to convert the parcel data into geojson format		
def kairiparceldata(request):
	karparc = serialize('geojson', KairiParcels.objects.all())
	return HttpResponse(karparc, content_type = 'json')

# A view to convert the acquired parcel data into geojson format	
def acquiredarea(request):
	acqarea = serialize('geojson', Acquiredarea.objects.all())
	return HttpResponse(acqarea, content_type='json')
