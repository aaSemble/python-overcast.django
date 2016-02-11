# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buildsvc', '0028_binarybuild_to_build_step_2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='binarybuild',
            name='architecture',
        ),
        migrations.RemoveField(
            model_name='binarybuild',
            name='source_package_version',
        ),
        migrations.RemoveField(
            model_name='binarypackageversion',
            name='binary_build',
        ),
        migrations.DeleteModel(
            name='BinaryBuild',
        ),
    ]
