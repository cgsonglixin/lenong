# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('LeongGoodApp', '0006_auto_20180516_0714'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('utitle', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gpub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 22, 8, 2, 30, 320849)),
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='g_User',
            field=models.ForeignKey(to='LeongGoodApp.Userinfo', default=1),
            preserve_default=False,
        ),
    ]
