# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('LeongGoodApp', '0003_auto_20180516_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='gpub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 16, 2, 15, 51, 212219)),
        ),
    ]
