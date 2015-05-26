# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote_in_action', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bills',
            name='description',
            field=models.TextField(),
        ),
    ]
