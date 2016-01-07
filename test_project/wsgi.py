"""
WSGI config for www project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import os.path
import sys

from django.conf import settings
from django.core.wsgi import get_wsgi_application
from dj_static import Cling
from urlparse import urlparse

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_project.settings")

class CustomCling(Cling):
    def __init__(self, app):
        super(CustomCling, self).__init__(app, base_dir=self.base_dir, ignore_debug=True)

    def get_base_url(self):
        base_url = urlparse(self._base_url).path

        if not base_url.endswith('/'):
            base_url += '/'

        return base_url


class MirrorCling(CustomCling):
    base_dir = settings.MIRRORSVC_BASE_PATH
    _base_url = settings.MIRRORSVC_BASE_URL


class AptCling(CustomCling):
    base_dir = settings.BUILDSVC_REPOS_BASE_PUBLIC_DIR
    _base_url = settings.BUILDSVC_REPOS_BASE_URL


application = MirrorCling(AptCling(Cling(get_wsgi_application())))
