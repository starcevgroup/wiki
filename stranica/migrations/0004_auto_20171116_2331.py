# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-16 23:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stranica', '0003_auto_20171116_1814'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['nomer_id'], 'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f', 'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438'},
        ),
        migrations.AlterField(
            model_name='category',
            name='nomer_id',
            field=models.IntegerField(blank=True, max_length=255, null=True, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0432\u043b\u043e\u0436\u0435\u043d\u043d\u043e\u0441\u0442\u0438'),
        ),
    ]
