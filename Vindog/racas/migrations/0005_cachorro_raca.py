# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2023-06-22 21:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('racas', '0004_auto_20230622_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='cachorro',
            name='raca',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='racas.Raca'),
        ),
    ]
