# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trailrecord',
            name='gpx',
        ),
        migrations.RemoveField(
            model_name='trailrecord',
            name='kml',
        ),
        migrations.AddField(
            model_name='trailrecord',
            name='accumulated_depths',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trailrecord',
            name='accumulated_heights',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
