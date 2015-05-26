# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('xid', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('update_date', models.DateField()),
                ('created_date', models.DateField()),
            ],
        ),
    ]
