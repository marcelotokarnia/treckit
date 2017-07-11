# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20170711_1742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trailrecord',
            name='start',
        ),
        migrations.AddField(
            model_name='trailrecord',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 11, 17, 41, 16, 619686, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trailrecord',
            name='created_by',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trailrecord',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 11, 17, 41, 38, 566274, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trailrecord',
            name='votes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='textrecord',
            name='track',
            field=models.ForeignKey(to='core.Track', related_name='texts'),
        ),
        migrations.AddField(
            model_name='imagerecord',
            name='track',
            field=models.ForeignKey(to='core.Track', related_name='images'),
        ),
        migrations.AddField(
            model_name='trailrecord',
            name='track',
            field=models.ForeignKey(default=1, related_name='trail_records', to='core.Track'),
            preserve_default=False,
        ),
    ]