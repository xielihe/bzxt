# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-23 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0002_auto_20180515_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='devshapesample',
            name='middleResultUrl',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='第一次文件路径'),
        ),
        migrations.AlterField(
            model_name='devshapesample',
            name='blackWhiteUrl',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='黑白图像路径'),
        ),
        migrations.AlterField(
            model_name='devshapesample',
            name='featureUrl',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='特征文件路径'),
        ),
        migrations.AlterField(
            model_name='devshapesample',
            name='interColorUrl',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='中间彩色图像路径'),
        ),
        migrations.AlterField(
            model_name='devshapesample',
            name='nomUrl',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='归一化图像文件路径'),
        ),
        migrations.AlterField(
            model_name='devshapesample',
            name='originalUrl',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='原始图像文件路径'),
        ),
        migrations.AlterField(
            model_name='devshapesample',
            name='resultFileUrl',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='结果文件形式路径'),
        ),
        migrations.AlterField(
            model_name='devshapesample',
            name='resultPicUrl',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='结果图像形式路径'),
        ),
    ]