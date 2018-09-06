# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from datetime import datetime
from django.utils import timezone

from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

#картинка в админке
from django.utils.safestring import mark_safe

# Добавление категорий

class Category(models.Model):
	class Meta():
		db_table = 'category'
		ordering = ['nomer_id']
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

	name = models.CharField(max_length=150, unique=True, verbose_name='Категория')
	categoryslug = models.SlugField(verbose_name='Транслит', null=True)
	image = models.ImageField (u'Фото категории', null=True, blank=True)
	template_name = models.CharField(
		('Выбор шаблона'),
		max_length=70,
		blank=True,
		help_text=(
			"Пример: 'flatpages/contact_page.html'. Если не указано,  "
			"система будет использовать 'flatpages/default.html'."
		),
	)
	nomer_id = models.IntegerField(u'Номер сортировки', null=True, blank=True)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.categoryslug:
			lastid = Category.objects.latest('id')
			self.categoryslug =  createslug(self.name)
		super(Category, self).save(*args, **kwargs)

	# слуг url
	def get_absolute_url(self):
		return ('view_blog_category', None, { 'categoryslug': self.categoryslug })

	# картинка в админке
	def image_img(self,):
		if self.image:
			return mark_safe('<a href="{0}" target="_blank"><img src="{0}" width="100" /></a>' .format(self.image.url))
		else:
			return '(Нет изображения)'
	image_img.short_description = 'Картинка'




class Svetofor(models.Model):
	name_block = models.CharField(u'Цвет', max_length=255, null=True, blank=True)
	class_block = models.CharField(u'Название Класса', max_length=255, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="Created at")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")



	def __str__(self):
		return self.name_block

	# переопределение названий
	class Meta:
		verbose_name = "Светофор"
		verbose_name_plural = "Светофор"
		ordering = ["-created_at"]


# Страницы

class Stranica(models.Model):
	name_block = models.CharField(u'Название', max_length=255, null=True, blank=True)
	text_block = RichTextUploadingField(verbose_name='Контент страницы',default='')
	image = models.ImageField(u'Фото', null=True, blank=True)
	active = models.BooleanField(default=True,verbose_name='Активность',)
	nomer_id = models.IntegerField(u'Номер сортировки',  null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="Created at")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")
	slug = models.SlugField(unique=True, verbose_name='Url', db_index=True)
	categorypost = models.ForeignKey(Category, verbose_name='Категория', blank=True, null=True,on_delete=models.CASCADE,)
	svetofor = models.ForeignKey(Svetofor, verbose_name='Светофор', blank=True, null=True,on_delete=models.CASCADE,)
	template_name = models.CharField(
		('Выбор шаблона'),
		max_length=70,
		blank=True,
		help_text=(
			"Пример: 'flatpages/contact_page.html'. Если не указано,  "
			"система будет использовать 'flatpages/default.html'."
		),
	)
	title_us = models.CharField(u'Тайтл', max_length=255, null=True, blank=True)
	description = models.TextField(u'Дескрипшон', null=True, blank=True )
	keywords = models.CharField(u'Кейвордс', max_length=255, null=True, blank=True)

	def __str__(self):
		return self.name_block

	# переопределение названий
	class Meta:
		verbose_name = "Страницы"
		verbose_name_plural = "Страницы"
		ordering = ["nomer_id"]


	#слуг url
	 # def get_absolute_url(self):
	 # 	return ('post_single', (), {
	 # 		'categoryslug': self.categorypost.categoryslug,
	 # 		'post_slug': self.slug,	
	 # 	})

	def get_absolute_url(self):
		return "/%s/%s.html" % (self.categorypost.categoryslug, self.slug)
	



	def save(self, *args, **kwargs):
		if not self.slug:
			lastid = Stranica.objects.latest('id')
			self.slug =  createslug(self.name_block)
		super(Stranica, self).save(*args, **kwargs)

	# картинка в админке
	def image_img(self,):
		if self.image:
			return mark_safe('<a href="{0}" target="_blank"><img src="{0}" width="100" /></a>' .format(self.image.url))
		else:
			return '(Нет изображения)'
	image_img.short_description = 'Картинка'


# Доступы

class Dostup(models.Model):
	name_block = models.CharField(u'Название', max_length=255, null=True, blank=True)
	# поля
	podkluchenie = RichTextUploadingField(verbose_name='Подключение SSHFS',default='')
	adminka = RichTextUploadingField(verbose_name='Админка сайта',default='')
	yandex = RichTextUploadingField(verbose_name='Яндекс почта',default='')
	google = RichTextUploadingField(verbose_name='Google почта',default='')
	phpmyadmin = RichTextUploadingField(verbose_name='Phpmyadmin',default='')
	ftp = RichTextUploadingField(verbose_name='Фтп доступ',default='')
	billing = RichTextUploadingField(verbose_name='Биллинг панель',default='')
	isp = RichTextUploadingField(verbose_name='SMM',default='')
	registrator = RichTextUploadingField(verbose_name='Регистратор домена',default='')
	drugoe = RichTextUploadingField(verbose_name='Доступы другие',default='')
	# 
	slug = models.SlugField(unique=True, verbose_name='Url', db_index=True)

	def __str__(self):
		return self.name_block

	# переопределение названий
	class Meta:
		verbose_name = "Доступы страницы"
		verbose_name_plural = "Доступы"

	def get_absolute_url(self):
		return "/%s" % (self.slug)

	def save(self, *args, **kwargs):
		if not self.slug:
			lastid = Dostup.objects.latest('id')
			self.slug =  createslug(self.name_block)
		super(Dostup, self).save(*args, **kwargs)

