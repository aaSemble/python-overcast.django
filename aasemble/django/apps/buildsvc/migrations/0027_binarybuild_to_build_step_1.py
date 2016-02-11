# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

import aasemble.django.apps.buildsvc.models.build


class Migration(migrations.Migration):

    dependencies = [
        ('buildsvc', '0026_auto_20160208_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='binarypackageversion',
            name='build',
            field=models.ForeignKey(to='buildsvc.Build', null=True),
        ),
        migrations.AddField(
            model_name='build',
            name='architecture',
            field=models.ForeignKey(default=aasemble.django.apps.buildsvc.models.build.get_default_architecture_pk, to='buildsvc.Architecture', null=True),
        ),
        migrations.AddField(
            model_name='build',
            name='build_type',
            field=models.SmallIntegerField(default=0, choices=[(0, b'Source+Binary'), (1, b'Source'), (2, b'Binary')]),
        ),
        migrations.AddField(
            model_name='build',
            name='source_package_version',
            field=models.ForeignKey(to='buildsvc.SourcePackageVersion', null=True),
        ),
        migrations.AlterField(
            model_name='build',
            name='source',
            field=models.ForeignKey(to='buildsvc.PackageSource', null=True),
        ),
    ]
