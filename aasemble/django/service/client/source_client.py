from aasemble.django.apps.api import base

class SourceClient(base.APIv1Tests):
    list_url = '/api/v1/sources/'
    fixtures = ['data.json', 'data2.json', 'repository.json']
    def create_source(self, **kwargs):
        params = {}
        for option in kwargs:
            value = kwargs.get(option)
            if isinstance(value, dict) or isinstance(value, tuple):
                params.update(value)
            else:
                params[option] = value
        response = self.client.post(self.list_url, params, format='json')
        return response
    def show_source(self, repo_id):
        response = self.client.get(repo_id)
        return response
    def get_source(self,uri=list_url):
        response = self.client.get(uri)
        return response
    def delete_source(self, repo_id):
        response = self.client.delete(repo_id)
        return response

