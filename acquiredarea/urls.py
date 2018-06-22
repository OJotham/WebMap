from django.conf.urls import url, include
from acquiredarea.views import HomePageView, ChartView, kairiparceldata, acquiredarea

# Registering the various view as urls
urlpatterns = [
    url(r'^$', HomePageView.as_view(), name = 'home'),
    url(r'^chart/$', ChartView.as_view(), name = 'charts' ),
    url(r'^kairiparc/$', kairiparceldata, name = 'kairiparcel' ),
    url(r'^acqarea/$', acquiredarea, name = 'acquarea'),
]