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

# Страницы

class Prostopage(models.Model):
	name_block = models.CharField(u'Название', max_length=255, null=True, blank=True)
	text_block = RichTextUploadingField(verbose_name='Контент страницы',default='')
	image = models.ImageField(u'Фото', null=True, blank=True)
	active = models.BooleanField(default=True,verbose_name='Активность',)
	nomer_id = models.IntegerField(u'Номер сортировки',  null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="Created at")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")
	slug = models.SlugField(max_length=255, unique=True, verbose_name='Url', db_index=True, null=True, blank=True,)
	template_name = models.CharField(
		('Выбор шаблона'),
		max_length=70,
		blank=True,
		help_text=(
			"Пример: 'prostopages/prostopages2.html'. Если не указано,  "
			"система будет использовать 'prostopages/prostopages.html'."
		),
	)
	title_us = models.CharField(u'Тайтл', max_length=255, null=True, blank=True)
	description = models.TextField(u'Дескрипшон', null=True, blank=True )
	keywords = models.CharField(u'Кейвордс', max_length=255, null=True, blank=True)

	def __str__(self):
		return self.name_block

	# переопределение названий
	class Meta:
		verbose_name = "Простые страницы"
		verbose_name_plural = "Простые страницы"
		ordering = ["nomer_id"]

	def get_absolute_url(self):
		return "/%s/" % (self.slug)
	
	def save(self, *args, **kwargs):
		if not self.slug:
			lastid = Prostopage.objects.latest('id')
			self.slug =  createslug(self.name_block)
		super(Prostopage, self).save(*args, **kwargs)

	# картинка в админке
	def image_img(self,):
		if self.image:
			return mark_safe('<a href="{0}" target="_blank"><img src="{0}" width="100" /></a>' .format(self.image.url))
		else:
			return '(Нет изображения)'
	image_img.short_description = 'Картинка'
