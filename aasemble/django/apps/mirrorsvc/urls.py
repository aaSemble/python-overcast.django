from django.conf.urls import url

import aasemble.django.apps.mirrorsvc.views as views

urlpatterns = [
    url(r'^mirrors/(?P<mirror_uuid>[^/]+|new)/$', views.mirror_definition, name='mirror_definition'),  # Added before mirrors/ to override next line
    url(r'^mirrors/(?P<mirror_uuid>[^/]+)/refresh/', views.refresh_mirror_with_uuid, name='mirror_refresh'),  # Added before mirrors/ to override next line
    url(r'^mirrors/', views.mirrors, name='mirrors'),
    url(r'^snapshots/(?P<snapshot_uuid>[^/]+)/tags/(?P<tag_id>[^/]+|new)', views.snapshot_add_tag, name='snapshot_add_tag'),
    url(r'^snapshots/(?P<uuid>[^/]+)/(?P<path>.*)$', views.snapshotfile, name='snapshotfile'),
    url(r'^snapshots/', views.snapshots, name='snapshots'),
    url(r'^mirrorsets/(?P<uuid>[^/]+|new)/$', views.mirrorset_definition, name='mirrorset_definition'),
    url(r'^mirrorsets/(?P<uuid>[^/]+)/snapshots/$', views.mirrorset_snapshots, name='mirrorset_snapshots'),
    url(r'^mirrorsets/(?P<uuid>[^/]+)/snapshots/new', views.create_new_snapshot, name='new_snapshot'),
    url(r'^mirrorsets/', views.mirrorsets, name='mirrorsets'),
]
