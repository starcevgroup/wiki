# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from django.conf import settings
from stranica.models import *

from django.http import Http404, HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render_to_response
from django.views.generic import *

# # поиск
from stranica.forms import *
import json



class SearchTag(View):
	""" Search tags with autocomplete (live search) """

	def get(self, request):
		form = SearchTagForm()
		context = {'searchtag' : form}
		return render(request, 'search_tags.html', context)

	def post(self,request):
		q = request.POST['q']
		form = SearchTagForm()
		tags = Stranica.objects.filter(name_block__icontains=q)
		context = {'tags' : tags, 'searchtag' : form}
		return render(request, 'search_tags.html', context)



class TagJson(View):
	""" Search tags with autocomplete (live search) json data"""
	def get(self, request):
		q = request.GET.get('q',)
		taglist = []
		tags = Stranica.objects.filter(name_block__icontains=q)
		for tag in tags:
			# new = {'q' : tag.name_block, }
			new = {'q' : tag.name_block, }
			taglist.append(new)
		return HttpResponse(json.dumps(taglist), content_type="application/json")


# ///////////////////////