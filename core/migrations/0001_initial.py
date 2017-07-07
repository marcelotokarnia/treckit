# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrackPoint',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('time', models.DateTimeField()),
                ('ele', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TrailRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=1024)),
                ('kml', models.CharField(max_length=512)),
                ('gpx', models.CharField(max_length=512)),
                ('start', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('simplified_track', django.contrib.gis.db.models.fields.MultiLineStringField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='WayPoint',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('ele', models.IntegerField()),
                ('name', models.CharField(max_length=1024)),
                ('trail_record', models.ForeignKey(related_name='waypoints', to='core.TrailRecord')),
            ],
        ),
        migrations.AddField(
            model_name='trackpoint',
            name='trail_record',
            field=models.ForeignKey(related_name='trackpoints', to='core.TrailRecord'),
        ),
    ]
