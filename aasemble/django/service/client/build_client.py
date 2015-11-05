from aasemble.django.apps.api import base

class BuildClient(base.APIv1Tests):
    list_url = '/api/v1/builds/'
    fixtures = ['data.json', 'data2.json', 'repository.json']
    def get_build(self):
        response = self.client.get(self.list_url)
        return response

