# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2023-06-20 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Raca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('descricao', models.TextField()),
            ],
        ),
    ]
