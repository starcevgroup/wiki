# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render



from django.conf import settings
from stranica.models import *

from django.http import Http404, HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

from django.shortcuts import render_to_response
from django.template.loader import get_template


from django.views.generic import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

from django.db.models import Count
# class PostDetailView(DetailView): # детализированное представление модели
#     model = Stranica
from django.template import loader
DEFAULT_TEMPLATE = 'stranica/stranica_detail1.html'
DEFAULT_TEMPLATE2 = 'stranica/category.html'
# class StranicaListView(ListView):
    # model = Stranica
    # queryset = Stranica.objects.filter(active=True).order_by('name_block')
    # paginate_by = 3
	# context_object_name = 'cat'
	# template_name = 'stranica/stranica_list.html'


#Мониторинг
#import urllib, socket, smtplib
#import urllib2
import urllib.request
import socket
from django.core.mail import send_mail

# поиск
from .forms import *
import json




class SearchTag(View):
# 	""" Search tags with autocomplete (live search) """

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
# 	""" Search tags with autocomplete (live search) json data"""
	def get(self, request):
		q = request.GET.get('q', '')
		taglist = []
		tags = Stranica.objects.filter(name_block__icontains=q)
		for tag in tags:
			# new = {'q' : tag.name_block, }
			new = {'q' : tag.name_block, 'url' : tag.categorypost.categoryslug, 'url2' : tag.slug}
			taglist.append(new)
		return HttpResponse(json.dumps(taglist), content_type="application/json")





# ///////////////////////


class Post_list(View):


	def get(self, request):
		# 
		cat = Category.objects.all().order_by('nomer_id').annotate(count_post = Count('stranica'))
		paginator = Paginator(cat, 24)
		page = request.GET.get('page')
		try:
			cat = paginator.page(page)
		except PageNotAnInteger:
			cat = paginator.page(1)
		except EmptyPage:
			cat = paginator.page(paginator.num_pages)
		# 
		form = SearchTagForm()
		context = {'searchtag' : form, 'page': page,"cat": cat}
		return render(request, 'stranica/stranica_list.html', context)

	def post(self,request):
		# 
		cat = Category.objects.all().order_by('nomer_id').annotate(count_post = Count('stranica'))
		paginator = Paginator(cat, 24)
		page = request.GET.get('page')
		try:
			cat = paginator.page(page)
		except PageNotAnInteger:
			cat = paginator.page(1)
		except EmptyPage:
			cat = paginator.page(paginator.num_pages)
		#
		q = request.POST['q']
		form = SearchTagForm()
		tags = Stranica.objects.filter(name_block__icontains=q)
		context = {'tags' : tags, 'searchtag' : form, 'page': page,"cat": cat}
		return render(request, 'stranica/stranica_list.html', context)









class Category_list(View):


	def get(self, request, categoryslug, timeout=5 ):
		# 
		category = get_object_or_404(Category, categoryslug=categoryslug)
		post = Stranica.objects.filter(active=True, categorypost=category)
		cat = Category.objects.all().annotate(count_post = Count('stranica'))
		dostup = Dostup.objects.all()
		paginator = Paginator(post, 20)


		page = request.GET.get('page')
		try:
			post = paginator.page(page)
		except PageNotAnInteger:
			post = paginator.page(1)
		except EmptyPage:
			post = paginator.page(paginator.num_pages)

		if category.template_name:
			template = loader.select_template((category.template_name, DEFAULT_TEMPLATE2))
		else:
			template = loader.get_template(DEFAULT_TEMPLATE2)
		# 
		form = SearchTagForm()

		if category.id == 26:
			############ Мониторинг ###############
			def check_url( url, timeout=5 ):
				try:
					#return  urllib2.urlopen(url,timeout=timeout).getcode() == 200
					request = urllib.request.urlopen(url,timeout=timeout).getcode() == 200
					return "{0} {1} - {2}".format('<div class="monitoring"><img src="/media/on.jpg" style="width:80px" alt="" />' , url, "Работает</div>")
				except urllib.request.URLError as e:
					return "{0} {1} - {2}".format('<div class="monitoring"><img src="/media/off.jpg" style="width:80px" alt="" />' , url, "Не работает</div>")
				except socket.timeout as e:
					print (False)
			#Фруктовый дизайн
			monitoring1 = check_url("https://starcev.biz") 
			monitoring2 = check_url("http://fruitdesign.ru") 
			#ковка
			monitoring3 = check_url("https://skctroy.ru/") 
			monitoring4 = check_url("http://moskvadez.ru/") 
			monitoring5 = check_url("http://podolskmaster.ru/")
			#Фифа
			monitoring6 = check_url("https://myfifasalon.ru/")
			#Репетиторша
			monitoring7 = check_url("https://repetitorstudio.ru/")
			#Паркетэссе
			monitoring8 = check_url("http://parket-esse.ru/")
			#Бетон
			monitoring9 = check_url("http://beton-pd.ru/")
			monitoring10 = check_url("http://beton-ch.ru/")
			monitoring11 = check_url("http://betonlarec.ru/")
			#Женя ремонт
			monitoring12 = check_url("http://classikaremonta.ru/")
			#тест
			monitoring13 = check_url("http://old.classikaremonta.ru/")
			monitoring14 = check_url("http://test1.betonlarec.ru/")
			################# мониторинг конец ##########################
			context = {'searchtag' : form, 'page': page,"cat": cat, 'post': post, 'dostup': dostup, 'category': category, 
			'monitoring1': monitoring1,
			'monitoring2': monitoring2,
			'monitoring3': monitoring3,
			'monitoring4': monitoring4,
			'monitoring5': monitoring5,
			'monitoring6': monitoring6,
			'monitoring7': monitoring7,
			'monitoring8': monitoring8,
			'monitoring9': monitoring9,
			'monitoring10': monitoring10,
			'monitoring11': monitoring11,
			'monitoring12': monitoring12,
			'monitoring13': monitoring13,
			'monitoring14': monitoring14,
			}
			response = HttpResponse(template.render(context, request))
			return response
		else:
			context = {'searchtag' : form, 'page': page,"cat": cat, 'post': post, 'dostup': dostup, 'category': category, 
			}
			response = HttpResponse(template.render(context, request))
			return response


	def post(self, request, categoryslug):
		# 
		category = get_object_or_404(Category, categoryslug=categoryslug)
		post = Stranica.objects.filter(active=True, categorypost=category)
		cat = Category.objects.all().annotate(count_post = Count('stranica'))
		dostup = Dostup.objects.all()
		paginator = Paginator(post, 20)

		page = request.GET.get('page')
		try:
			post = paginator.page(page)
		except PageNotAnInteger:
			post = paginator.page(1)
		except EmptyPage:
			post = paginator.page(paginator.num_pages)

		if category.template_name:
			template = loader.select_template((category.template_name, DEFAULT_TEMPLATE2))
		else:
			template = loader.get_template(DEFAULT_TEMPLATE2)

		#
		q = request.POST['q']
		form = SearchTagForm()
		tags = Stranica.objects.filter(name_block__icontains=q)
		context = {'tags' : tags, 'searchtag' : form, 'page': page,"cat": cat, 'post': post, 'dostup': dostup, 'category': category,}
		response = HttpResponse(template.render(context, request))
		return response









class Post_single(View):

	def get(self, request, post_slug, categoryslug):
		# 
		cat = Category.objects.select_related().all().order_by('nomer_id').annotate(count_post = Count('stranica'))
		stranica = get_object_or_404(Stranica.objects.filter(active=True), slug=post_slug, categorypost__categoryslug=categoryslug)
		if stranica.template_name:
			template = loader.select_template((stranica.template_name, DEFAULT_TEMPLATE))
		else:
			template = loader.get_template(DEFAULT_TEMPLATE)
		# 
		form = SearchTagForm()
		context = {'searchtag' : form, "stranica": stranica, "cat": cat,}
		return render(request, 'stranica/stranica_detail1.html', context)

	def post(self,request, post_slug, categoryslug):
		# 
		cat = Category.objects.select_related().all().order_by('nomer_id').annotate(count_post = Count('stranica'))
		stranica = get_object_or_404(Stranica.objects.filter(active=True), slug=post_slug, categorypost__categoryslug=categoryslug)
		if stranica.template_name:
			template = loader.select_template((stranica.template_name, DEFAULT_TEMPLATE))
		else:
			template = loader.get_template(DEFAULT_TEMPLATE)
		#
		q = request.POST['q']
		form = SearchTagForm()
		tags = Stranica.objects.filter(name_block__icontains=q)
		context = {'tags' : tags, 'searchtag' : form, "stranica": stranica, "cat": cat,}
		return render(request, 'stranica/stranica_detail1.html', context)






# def post_list(request ):
# 	cat = Category.objects.all().order_by('nomer_id').annotate(count_post = Count('stranica'))
# 	paginator = Paginator(cat, 24)
# 	page = request.GET.get('page')
# 	try:
# 		cat = paginator.page(page)
# 	except PageNotAnInteger:
# 		cat = paginator.page(1)
# 	except EmptyPage:
# 		cat = paginator.page(paginator.num_pages)
# 	return render(request, 'stranica/stranica_list.html', {'page': page,"cat": cat})



# def category(reguest, categoryslug):

# 	category = get_object_or_404(Category, categoryslug=categoryslug)
# 	post = Stranica.objects.filter(active=True, categorypost=category)
# 	cat = Category.objects.all().annotate(count_post = Count('stranica'))
# 	paginator = Paginator(post, 20)

# 	page = reguest.GET.get('page')
# 	try:
# 		post = paginator.page(page)
# 	except PageNotAnInteger:
# 		post = paginator.page(1)
# 	except EmptyPage:
# 		post = paginator.page(paginator.num_pages)
# 	return render(reguest, 'stranica/category.html', {
# 		'category': category,
# 		'page': page,
# 		'post': post,
# 		'cat': cat,

# 		})



# def dostup(request, slug ):
# 	cat = Category.objects.select_related().all().order_by('nomer_id').annotate(count_post = Count('stranica'))
# 	dostup = get_object_or_404(Dostup, slug=slug, )
# 	return render(request, 'stranica/dostup.html', {"dostup": dostup,"cat": cat,})




# def post_single(request, post_slug, categoryslug):
# 	cat = Category.objects.select_related().all().order_by('nomer_id').annotate(count_post = Count('stranica'))
# 	stranica = get_object_or_404(Stranica.objects.filter(active=True), slug=post_slug, categorypost__categoryslug=categoryslug)
# 	if stranica.template_name:
# 		template = loader.select_template((stranica.template_name, DEFAULT_TEMPLATE))
# 	else:
# 		template = loader.get_template(DEFAULT_TEMPLATE)
# 	response = HttpResponse(template.render({"stranica": stranica, "cat": cat, }, request))
# 	return response





