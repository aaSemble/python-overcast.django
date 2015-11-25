# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserActionLogger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action_type', models.CharField(max_length=10, choices=[(b'API', b'API'), (b'WEBUI', b'Web UI')])),
                ('time_action_created', models.DateTimeField(auto_now_add=True)),
                ('http_method_used', models.CharField(max_length=15, null=True, choices=[(b'GET', b'GET'), (b'POST', b'POST'), (b'PUT', b'PUT'), (b'PATCH', b'PATCH'), (b'DELETE', b'DELETE')])),
                ('method_url', models.URLField(null=True)),
                ('remote_addr', models.IPAddressField(null=True)),
                ('view_function', models.CharField(max_length=200, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
