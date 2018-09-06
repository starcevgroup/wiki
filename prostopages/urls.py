#coding: utf-8
from django.conf.urls import url 

#############################
#from django.core.urlresolvers import reverse
##################################
#from stranica import views

from prostopages.views import *

urlpatterns = [

#url(r'^pages/(?P<slug>[-\w]+)/$', prostopages, name='prostopages'),

url(r'^pages/(?P<slug>[-\w]+)/$', Prostopages_single.as_view()),

]
