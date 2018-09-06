#coding: utf-8
from django.conf.urls import url 

#############################
#from django.core.urlresolvers import reverse
##################################
#from stranica import views
from stranica import views
from stranica.views import *

urlpatterns = [

#url(r'^$', views.post_list, name='list'),
#url(r'^(?P<categoryslug>[-\w]+)/$', views.category, name='category'),
#url(r'^(?P<categoryslug>[^\.]+)/(?P<post_slug>[-\w]+).html', views.post_single, name='post_single'),
#url(r'^(?P<slug>[-\w]+)/$', views.dostup, name='dostup'),


url(r'^$', Post_list.as_view()),
url(r'^(?P<categoryslug>[-\w]+)/$', Category_list.as_view()),

url(r'^(?P<categoryslug>[^\.]+)/(?P<post_slug>[-\w]+).html', Post_single.as_view()),


]
