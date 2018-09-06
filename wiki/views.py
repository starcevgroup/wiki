# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
#from django.contrib.auth.decorators import login_required
from stranica.models import *
from django.db.models import Count
#@login_required(login_url='/svg_admin/')
def home(request):
    return render(request, 'index.html', {})


# Страницы списков
def dostup(request):
    cat = Category.objects.all().order_by('nomer_id').annotate(count_post = Count('stranica'))
    return render(request, 'page/dostup.html', {"cat": cat})
def sayts(request):
    cat = Category.objects.all().order_by('nomer_id').annotate(count_post = Count('stranica'))
    return render(request, 'sayts.html', {"cat": cat})






def prodvizhenie(request):
    return render(request, 'page/prodvizhenie.html', {})
def htmlcss(request):
    return render(request, 'page/html-css.html', {})
def django(request):
    return render(request, 'page/django.html', {})
def postgresql(request):
    return render(request, 'page/postgresql.html', {})
def gulp(request):
    return render(request, 'page/gulp.html', {})
def sass(request):
    return render(request, 'page/sass.html', {})
def apache_nginx(request):
    return render(request, 'page/apache-nginx.html', {})
def linux(request):
    return render(request, 'page/linux.html', {})
def photoshop(request):
    return render(request, 'page/photoshop.html', {})
def sublime(request):
    return render(request, 'page/sublime.html', {})
def bitrix(request):
    return render(request, 'page/bitrix.html', {})
def wordpress(request):
    return render(request, 'page/wordpress.html', {})
def git(request):
    return render(request, 'page/git.html', {})
def java(request):
    return render(request, 'page/java.html', {})
def mysql(request):
    return render(request, 'page/mysql.html', {})
def opencart(request):
    return render(request, 'page/opencart.html', {})
def jquery(request):
    return render(request, 'page/jquery.html', {})
def php(request):
    return render(request, 'page/php.html', {})
def advego(request):
    return render(request, 'page/advego.html', {})
def centos(request):
    return render(request, 'page/centos.html', {})
def direkt(request):
    return render(request, 'page/direkt.html', {})

#обычные страницы
def django_apache(request):
    return render(request, 'str/django-apache.html', {})
def django_nginx(request):
    return render(request, 'str/django-nginx.html', {})
def django_prilozhenie(request):
    return render(request, 'str/django-prilozhenie.html', {})
def django_plugins(request):
    return render(request, 'str/django-plugins.html', {})
def postgresql(request):
    return render(request, 'str/postgresql.html', {})
def gulp_ustanovka(request):
    return render(request, 'str/gulp-ustanovka.html', {})
def html5(request):
    return render(request, 'str/html5.html', {})
def obnulenie_stiley(request):
    return render(request, 'str/obnulenie-stiley.html', {})
def div_nazvaniya(request):
    return render(request, 'str/div-nazvaniya.html', {})
def adaptivnostmobile(request):
    return render(request, 'str/adaptivnostmobile.html', {})
def pagespeed(request):
    return render(request, 'str/pagespeed.html', {})
def commands(request):
    return render(request, 'str/commands.html', {})
def zadacha(request):
    return render(request, 'str/zadacha.html', {})
def ioncube(request):
    return render(request, 'str/ioncube.html', {})
def uvelichenie_vremeni(request):
    return render(request, 'str/uvelichenie-vremeni.html', {})
def ustanovka_programm(request):
    return render(request, 'str/ustanovka-programm.html', {})
def linux_commands(request):
    return render(request, 'str/linux-commands.html', {})
def host(request):
    return render(request, 'str/host.html', {})
def option_sayt(request):
    return render(request, 'str/option-sayt.html', {})
def ftp_server(request):
    return render(request, 'str/ftp-server.html', {})
def bootstrap(request):
    return render(request, 'str/bootstrap.html', {})
def redirect(request):
    return render(request, 'str/redirect.html', {})
def https(request):
    return render(request, 'str/https.html', {})
def verstki(request):
    return render(request, 'str/verstki.html', {})
def wordpressstr(request):
    return render(request, 'str/wordpressstr.html', {})
def menuwordpress(request):
    return render(request, 'str/menuwordpress.html', {})
def woocommerce(request):
    return render(request, 'str/woocommerce.html', {})
def table_adaptive(request):
    return render(request, 'str/table-adaptive.html', {})
