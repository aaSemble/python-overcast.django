from aasemble.django.apps.api import base

class RepositoryClient(base.APIv1Tests):
    list_url = '/api/v1/repositories/'
    def create_repository(self, **kwargs):
        params = {}
        for option in kwargs:
            value = kwargs.get(option)
            if isinstance(value, dict) or isinstance(value, tuple):
                params.update(value)
            else:
                params[option] = value
        response = self.client.post(self.list_url, params, format='json')
        return response
    def show_repository(self, repo_id):
        response = self.client.get(repo_id)
        return response
    def get_repository(self):
        response = self.client.get(self.list_url)
        return response
    def delete_repository(self, repo_id):
        response = self.client.delete(repo_id)
        return response
    def update_repository(self,repo_id, **kwargs):
        params = {}
        for option in kwargs:
            value = kwargs.get(option)
            if isinstance(value, dict) or isinstance(value, tuple):
                params.update(value)
            else:
                params[option] = value
        response = self.client.patch(repo_id, params, format='json')
        return response

