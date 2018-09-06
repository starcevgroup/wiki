# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
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


class StranicaAdmin(SortableAdminMixin, admin.ModelAdmin):
    fieldsets = [
        ('Основные',        {'fields': ['name_block', 'slug', 'categorypost',   'svetofor', 'image', 'text_block',   'active','template_name' ,]}),
        ('Сео оптимизация', {'fields': ['title_us','description',]}),
    ]
    list_display = ["active",'image_img',"nomer_id",'svetofor',   "name_block",'categorypost', "created_at",]
    list_display_links = ["name_block",'image_img',]
    list_editable = ['active', 'categorypost', 'svetofor', ]
    list_filter = ['categorypost',"active","created_at",]
    search_fields = ["name_block"]
    #автозаполнение slug
    prepopulated_fields = {"slug": ("name_block",)}

    actions = [all_post, complete_post, incomplete_post]

    class Meta:
        model = Stranica


#//////////////////////////////
class SvetoforAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name_block', 'class_block', ]}),
    ]
    list_display = ['name_block', 'class_block',]
    list_editable = [ 'class_block',]



#//////////////////////////////
class CategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'categoryslug', 'image',   'template_name' ,]}),
    ]
    list_display = ['name', 'nomer_id', 'image_img', 'categoryslug', ]
    list_editable = [ 'categoryslug', ]
    prepopulated_fields = {'categoryslug': ('name',)}
    search_fields = ["name"]
    list_filter = ['name',]
# /////////////////////////////
class DostupAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name_block', 'slug','podkluchenie','adminka','yandex','google','isp', 'phpmyadmin', 
            'billing','registrator','drugoe' ]}),
    ]
    list_display = ['name_block', 'slug', ]
    prepopulated_fields = {'slug': ('name_block',)}

# ////////////////////////////

admin.site.register(Stranica, StranicaAdmin, )
admin.site.register(Category, CategoryAdmin, )
admin.site.register(Svetofor, SvetoforAdmin, )
admin.site.register(Dostup, DostupAdmin, )
