# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-22 07:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbour', '0005_auto_20181020_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighbour',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
