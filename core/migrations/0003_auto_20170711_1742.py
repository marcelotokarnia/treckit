# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_auto_20170711_0228'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageRecord',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('image', models.CharField(max_length=1024)),
                ('votes', models.IntegerField()),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TextRecord',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('record', models.TextField()),
                ('votes', models.IntegerField()),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=1024)),
                ('start', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VideoRecord',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(max_length=128)),
                ('link', models.CharField(max_length=1024)),
                ('votes', models.IntegerField()),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('track', models.ForeignKey(to='core.Track', related_name='videos')),
            ],
            options={
                'abstract': False,
            },
        ),

    ]
