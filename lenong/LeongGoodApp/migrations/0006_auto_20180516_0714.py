# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('LeongGoodApp', '0005_auto_20180516_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='gjianjie',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gpic',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gpub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 16, 7, 14, 27, 489432)),
        ),
    ]
