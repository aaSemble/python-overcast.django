# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.conf import settings
from django.db import migrations


def import_snapshotfiles(apps, schema_editor):
    SnapshotFile = apps.get_model("mirrorsvc", "SnapshotFile")
    recursive_import_snapshotfiles(SnapshotFile, settings.MIRRORSVC_BASE_PATH)


def recursive_import_snapshotfiles(SnapshotFile, path):
    if os.path.isdir(path):
        for f in os.listdir(path):
            recursive_import_snapshotfiles(SnapshotFile, os.path.join(path, f))
    else:
        base_url = settings.MIRRORSVC_BASE_URL
        url_path = path[len(settings.MIRRORSVC_BASE_PATH) + 1:]
        SnapshotFile.objects.create(url='%s%s' % (base_url, url_path), orig_path=url_path)


class Migration(migrations.Migration):
    dependencies = [
        ('mirrorsvc', '0016_snapshotfile'),
    ]

    operations = [
        migrations.RunPython(import_snapshotfiles, migrations.RunPython.noop)
    ]
