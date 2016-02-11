# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildsvc', '0029_binarybuild_to_build_step_3'),
    ]

    operations = [
        migrations.CreateModel(
            name='BinaryBuild',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('buildsvc.build',),
        ),
        migrations.CreateModel(
            name='SourceBuild',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('buildsvc.build',),
        ),
        migrations.AlterField(
            model_name='binarypackageversion',
            name='build',
            field=models.ForeignKey(to='buildsvc.Build'),
        ),
    ]
