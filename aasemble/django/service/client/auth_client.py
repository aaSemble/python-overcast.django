from aasemble.django.apps.api import base

class AuthClient(base.APIv1Tests):
    list_url = '/api/v1/auth/user/'
    def get_auth(self):
        response = self.client.get(self.list_url)
        return response
