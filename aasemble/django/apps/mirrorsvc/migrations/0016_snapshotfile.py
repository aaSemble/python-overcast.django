# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mirrorsvc', '0015_change_visible_to_v1_column_to_false'),
    ]

    operations = [
        migrations.CreateModel(
            name='SnapshotFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orig_path', models.CharField(max_length=255)),
                ('url', models.URLField(max_length=255)),
                ('snapshots', models.ManyToManyField(to='mirrorsvc.Snapshot')),
            ],
        ),
    ]
