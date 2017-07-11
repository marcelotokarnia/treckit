# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '00035_semi_auto_20170711_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagerecord',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='textrecord',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='trailrecord',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='videorecord',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
