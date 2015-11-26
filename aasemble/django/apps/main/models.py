from django.contrib.auth.models import User
from django.db import models


class UserActionLogger(models.Model):
    ACTION_TYPE_CHOICES = (
        ('API', 'API'),
        ('WEBUI', 'Web UI')
    )
    action_type = models.CharField(choices=ACTION_TYPE_CHOICES, max_length=10)
    time_action_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True)
    HTTP_METHOD_CHOICES = (
        ('GET', 'GET'),
        ('POST', 'POST'),
        ('PUT', 'PUT'),
        ('PATCH', 'PATCH'),
        ('DELETE', 'DELETE')
    )
    http_method_used = models.CharField(choices=HTTP_METHOD_CHOICES, null=True, max_length=15)
    method_url = models.URLField(null=True)
    remote_addr = models.IPAddressField(null=True)
    view_function = models.CharField(blank=True, max_length=200)

    def log_action(self, request):
        try:
            action = UserActionLogger(action_type='API', http_method_used=request.method, method_url=request.path,
                                      remote_addr=request.META.get('REMOTE_ADDR'))
            if isinstance(request.user, User):
                action.user = request.user
            action.save()
        except Exception as e:
            print('Exception raised in UserActionLogger.log_action', e)
            pass
