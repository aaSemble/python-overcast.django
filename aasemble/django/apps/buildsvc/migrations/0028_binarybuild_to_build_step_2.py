# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

from aasemble.django.apps.buildsvc.models.build import Build as RealBuild


def convert_binary_build_to_build(apps, schema_editor):
    BinaryBuild = apps.get_model('buildsvc', 'BinaryBuild')
    Build = apps.get_model('buildsvc', 'Build')
    for bb in BinaryBuild.objects.all():
        b = Build(version=bb.source_package_version.version,
                  source_package_version=bb.source_package_version,
                  state=RealBuild.UNKNOWN)
        b.save()
        for bpv in bb.binarypackageversion_set.all():
            bpv.build = b
            bpv.save()


class Migration(migrations.Migration):

    dependencies = [
        ('buildsvc', '0027_binarybuild_to_build_step_1'),
    ]

    operations = [
        migrations.RunPython(convert_binary_build_to_build)
    ]
