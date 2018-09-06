# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from django.conf import settings
from stranica.models import *
from prostopages.models import *

from django.http import Http404, HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404


from django.shortcuts import render_to_response
from django.template.loader import get_template


from django.views.generic import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

from django.db.models import Count
# class PostDetailView(DetailView): # детализированное представление модели
#     model = Stranica
from django.template import loader
DEFAULT_TEMPLATE = 'prostopages/prostopages.html'


# поиск
from stranica.forms import *
import json





class Prostopages_single(View):

	# def prostopages(request, slug):
	
	# 	cat = Category.objects.all().order_by('nomer_id').annotate(count_post = Count('stranica'))
	# 	prostopage = get_object_or_404(Prostopage, slug=slug)
	
	
	# 	context = { "prostopage": prostopage, "cat": cat,}
	# 	return render(request, 'prostopages/prostopages.html', context)


	def get(self, request, slug):
		# 
		cat = Category.objects.all().order_by('nomer_id').annotate(count_post = Count('stranica'))
		prostopage = get_object_or_404(Prostopage, slug=slug)
		# 
		form = SearchTagForm()
		context = {'searchtag' : form, "prostopage": prostopage, "cat": cat,}
		return render(request, 'prostopages/prostopages.html', context)


	def post(self,request, slug):
		# 
		cat = Category.objects.all().order_by('nomer_id').annotate(count_post = Count('stranica'))
		prostopage = get_object_or_404(Prostopage, slug=slug)
		#
		q = request.POST['q']
		form = SearchTagForm()
		tags = Stranica.objects.filter(name_block__icontains=q)
		context = {'tags' : tags, 'searchtag' : form, "prostopage": prostopage, "cat": cat,}
		return render(request, 'prostopages/prostopages.html', context)