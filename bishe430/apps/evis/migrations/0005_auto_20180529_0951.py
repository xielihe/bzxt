# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-29 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evis', '0004_auto_20180528_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devshapeevi',
            name='originalUrl',
            field=models.ImageField(blank=True, null=True, upload_to='image/devShapeEvi/original/', verbose_name='原始图像文件路径'),
        ),
    ]