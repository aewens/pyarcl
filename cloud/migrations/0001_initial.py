# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 04:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_type', models.CharField(max_length=16)),
                ('file_name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='ItemList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('group', models.CharField(max_length=128)),
                ('link', models.CharField(max_length=1024)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='item_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cloud.ItemList'),
        ),
    ]
