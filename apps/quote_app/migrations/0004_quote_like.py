# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-26 20:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote_app', '0003_auto_20180926_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='like',
            field=models.ManyToManyField(related_name='liked_quotes', to='quote_app.User'),
        ),
    ]