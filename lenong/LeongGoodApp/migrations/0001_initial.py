# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gtitle', models.CharField(max_length=20)),
                ('gpic', models.ImageField(upload_to='static/media')),
                ('gprice', models.DecimalField(max_digits=5, decimal_places=2)),
                ('isDelete', models.BooleanField(default=False)),
                ('gclick', models.IntegerField(default=0)),
                ('gunit', models.CharField(max_length=20, default='550g')),
                ('gjianjie', models.TextField()),
                ('gpub_date', models.DateTimeField(default=datetime.datetime(2018, 5, 15, 3, 23, 27, 995761))),
                ('gpubj_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Typeinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ttitle', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='g_type',
            field=models.ForeignKey(to='LeongGoodApp.Typeinfo'),
        ),
    ]
