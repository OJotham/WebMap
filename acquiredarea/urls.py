from django.conf.urls import url, include
from acquiredarea.views import HomePageView, kairiparceldata, acquiredarea

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name = 'home'),
    url(r'^kairiparc/$', kairiparceldata, name = 'kairiparcel' ),
    url(r'^acqarea/$', acquiredarea, name = 'acquarea')
]