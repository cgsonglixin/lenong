# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('LeongGoodApp', '0002_auto_20180515_0332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='gjianjie',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gpub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 16, 1, 41, 34, 662214)),
        ),
    ]
