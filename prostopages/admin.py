# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *


# Функции фильтрации для массовой публикации/снятия с публикации новостей.
def all_post(modeladmin, reguest, queryset):
    for qs in queryset:
        print (qs.title)

def complete_post(modeladmin, reguest, queryset):
    queryset.update(active=True)
complete_post.short_description = 'Опубликовать новости'

def incomplete_post(modeladmin, reguest, queryset):
    queryset.update(active=False)
incomplete_post.short_description = 'Снять с публикации'
# ////////////////////////////////////////////


class ProstopageAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Основные',        {'fields': ['name_block', 'slug', 'image', 'text_block','nomer_id','active','template_name' ,]}),
        ('Сео оптимизация', {'fields': ['title_us','description','keywords',]}),
    ]
    list_display = ['image_img',"name_block","active",'slug', "nomer_id","created_at",]
    list_display_links = ["name_block",'image_img',]
    list_editable = ['active', 'slug', 'nomer_id',]
    list_filter = ["active","created_at",]
    search_fields = ["name_block"]
    #автозаполнение url
    prepopulated_fields = {"slug": ("name_block",)}

    actions = [all_post, complete_post, incomplete_post]

    class Meta:
        model = Prostopage

# ////////////////////////////

admin.site.register(Prostopage, ProstopageAdmin, )

