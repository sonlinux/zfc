# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-04 02:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_sponser_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='JuvenilePlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number', models.IntegerField()),
                ('img', models.ImageField(upload_to='player_img%Y-%m-%d')),
            ],
        ),
        migrations.CreateModel(
            name='SeniorPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number', models.IntegerField()),
                ('img', models.ImageField(upload_to='player_img%Y-%m-%d')),
            ],
        ),
        migrations.CreateModel(
            name='VeteranPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number', models.IntegerField()),
                ('img', models.ImageField(upload_to='player_img%Y-%m-%d')),
            ],
        ),
    ]
