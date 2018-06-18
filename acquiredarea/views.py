from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import KairiParcels, Acquiredarea
# Create your views here.
class HomePageView(TemplateView):
	"""docstring for ClassName"""
	template_name = 'index.html'
def kairiparceldata(request):
	karparc = serialize('geojson', KairiParcels.objects.all())
	return HttpResponse(karparc, content_type = 'json')
def acquiredarea(request):
	acqarea = serialize('geojson', Acquiredarea.objects.all())
	return HttpResponse(acqarea, content_type='json')
