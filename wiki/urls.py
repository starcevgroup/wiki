# -*- coding: utf-8 -*-
"""wiki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include

from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views
#приложения
from stranica.views import *
#карта сайта
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap
sitemaps = {
    'static': StaticViewSitemap,
    }
#Переопределение названий
from django.contrib import admin
admin.site.site_title = "Wiki"
admin.site.site_header = "Wiki" 
admin.site.site_url = "/" 




urlpatterns = [
	#url(r'^$', views.home,  name='home'),
    url(r'^svg_admin/', admin.site.urls),

    # поиск
    url(r'^search/hashtag$', SearchTag.as_view()),
    url(r'^hashtag.json$', TagJson.as_view()),


    #страницы разделов
    #url(r'^dostup/$', views.dostup,  name='dostup'),
    url(r'^sayts/$', views.sayts,  name='sayts'),


    url(r'^', include('stranica.urls')),
    url(r'^', include('prostopages.urls')),
    #############

    url(r'^robots.txt', include('robots.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')), #загрузка в editor



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


Handler404 = 'repetitor.views.my_custom_page_not_found_view'
Handler500 = 'repetitor.views.my_custom_error_view'
Handler403 = 'repetitor.views.my_custom_permission_denied_view'
Handler400 = 'repetitor.views.my_custom_bad_request_view'
