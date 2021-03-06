# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-17 07:35
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stranica', '0005_auto_20171116_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='nomer_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0438'),
        ),
        migrations.AlterField(
            model_name='stranica',
            name='active',
            field=models.BooleanField(default=True, verbose_name='\u0410\u043a\u0442\u0438\u0432\u043d\u043e\u0441\u0442\u044c'),
        ),
        migrations.AlterField(
            model_name='stranica',
            name='nomer_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0438'),
        ),
        migrations.AlterField(
            model_name='stranica',
            name='text_block',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='', verbose_name='\u041a\u043e\u043d\u0442\u0435\u043d\u0442 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b'),
        ),
    ]
