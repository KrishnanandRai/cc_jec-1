# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-17 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('c_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='branch',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='user',
            name='contact',
            field=models.IntegerField(default=0, max_length=128),
        ),
        migrations.AddField(
            model_name='user',
            name='semester',
            field=models.IntegerField(default=0, max_length=128),
        ),
        migrations.AddField(
            model_name='user',
            name='town',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default='', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='', max_length=128),
        ),
    ]
