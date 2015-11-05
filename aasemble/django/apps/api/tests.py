from django.core.urlresolvers import reverse
from aasemble.django.service.client.repository_client import RepositoryClient
from aasemble.django.service.client.build_client import BuildClient
from aasemble.django.service.client.source_client import SourceClient
from aasemble.django.service.client.auth_client import AuthClient
from rest_framework.authtoken.models import Token

def authenticate(client, username=None, token=None):
    if token is None:
        token = Token.objects.get(user__username=username).key
    client.credentials(HTTP_AUTHORIZATION='Token ' + token)


class APIv1RepositoryTests(RepositoryClient):

    def test_fetch_sources(self):
        # Use alterego2 to make sure it works with users who are members
        # of multiple groups
        authenticate(self.client, 'alterego2')
        response = self.get_repository()

        for repo in response.data['results']:
            resp = self.show_repository(repo['sources'])
            self.assertEquals(resp.status_code, 200)

    def test_fetch_external_dependencies(self):
        # Use alterego2 to make sure it works with users who are members
        # of multiple groups
        authenticate(self.client, 'alterego2')
        response = self.get_repository()

        for repo in response.data['results']:
            resp = self.show_repository(repo['external_dependencies'])
            self.assertEquals(resp.status_code, 200)

    def test_create_repository_empty_fails_400(self):
        data = {}
        authenticate(self.client, 'testuser')
        response = self.create_repository(**data)
        self.assertEquals(response.status_code, 400)
        self.assertEquals(response.data, {'name': ['This field is required.']})


    def test_create_repository_no_auth_fails_401(self):
        data = {}
        response = self.create_repository(**data)
        self.assertEquals(response.status_code, 401)


    def test_create_repository_incorrect_auth_fails_401(self):
        data = {}
        authenticate(self.client, token='invalidtoken')

        response = self.create_repository(**data)

        self.assertEquals(response.status_code, 401)

    def test_create_repository(self):
        data = {'name': 'testrepo'}
        authenticate(self.client, 'testuser')

        response = self.create_repository(**data)
        self.assertEquals(response.status_code, 201)
        self.assertTrue(response.data['self'].startswith('http://testserver' + self.list_url), response.data['self'])
        expected_result = {'external_dependencies': response.data['self'] + 'external_dependencies/',
                           'name': 'testrepo',
                           'binary_source_list': 'deb http://127.0.0.1:8000/apt/testuser/testrepo aasemble main',
                           'source_source_list': 'deb-src http://127.0.0.1:8000/apt/testuser/testrepo aasemble main',
                           'self': response.data['self'],
                           'sources': response.data['self'] + 'sources/',
                           'user': 'testuser',
                           'key_id': u''}

        self.assertEquals(response.data, expected_result)
        response = self.show_repository(response.data['self'])
        self.assertEquals(response.data, expected_result)
        return response.data


    def test_create_duplicate_repository(self):
        data = {'name': 'testrepo'}
        authenticate(self.client, 'testuser')
        response = self.create_repository(**data)
        self.assertEquals(response.status_code, 201)
        response = self.create_repository(**data)
        self.assertEquals(response.status_code, 409)


    def test_delete_repository(self):
        repo = self.test_create_repository()

        response = self.delete_repository(repo['self'])

        self.assertEquals(response.status_code, 204)

        response = self.show_repository(repo['self'])
        self.assertEquals(response.status_code, 404)


    def test_patch_repository(self):
        repo = self.test_create_repository()
        data = {'name': 'testrepo2'}

        response = self.update_repository(repo['self'], **data)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['self'], repo['self'], '"self" attribute changed')

        expected_result = {'external_dependencies': response.data['self'] + 'external_dependencies/',
                           'name': 'testrepo2',
                           'binary_source_list': 'deb http://127.0.0.1:8000/apt/testuser/testrepo2 aasemble main',
                           'source_source_list': 'deb-src http://127.0.0.1:8000/apt/testuser/testrepo2 aasemble main',
                           'self': response.data['self'],
                           'sources': response.data['self'] + 'sources/',
                           'user': 'testuser',
                           'key_id': u''}

        self.assertEquals(response.data, expected_result)
        response = self.show_repository(response.data['self'])
        self.assertEquals(response.data, expected_result, 'Changes were not persisted')

    def test_patch_repository_read_only_field(self):
        repo = self.test_create_repository()
        data = {'user': 'testuser2'}
        response = self.update_repository(repo['self'], **data)

class APIv2RepositoryTests(APIv1RepositoryTests):
    list_url = '/api/v2/repositories/'


class APIv1BuildTests(BuildClient):
    def test_fetch_builds(self):
        # Use alterego2 to make sure it works with users who are members
        # of multiple groups
        authenticate(self.client, 'alterego2')
        response = self.get_build()
        self.assertEquals(response.status_code, 200)


class APIv2BuildTests(APIv1BuildTests):
    list_url = '/api/v2/builds/'


class APIv1SourceTests(SourceClient):

    def test_create_source_empty_fails_400(self):
        data = {}
        authenticate(self.client, 'testuser')

        response = self.create_source(**data)
        self.assertEquals(response.status_code, 400)
        self.assertEquals(response.data, {'git_repository': ['This field is required.'],
                                          'git_branch': ['This field is required.'],
                                          'repository': ['This field is required.']})


    def test_create_invalied_url_fails_400(self):
        data = {'git_repository': 'not a valid url'}
        authenticate(self.client, 'testuser')

        response = self.create_source(**data)
        self.assertEquals(response.status_code, 400)
        self.assertEquals(response.data, {'git_repository': ['Enter a valid URL.'],
                                          'git_branch': ['This field is required.'],
                                          'repository': ['This field is required.']})


    def test_create_source_no_auth_fails_401(self):
        data = {}
        response = self.create_source(**data)
        self.assertEquals(response.status_code, 401)


    def test_create_source_incorrect_auth_fails_401(self):
        data = {}
        authenticate(self.client, token='invalidtoken')

        response = self.create_source(**data)

        self.assertEquals(response.status_code, 401)

    def test_create_source(self):
        authenticate(self.client, 'testuser')
        response = self.get_source(uri=self.list_url.replace('sources', 'repositories'))

        data = {'git_repository': 'https://github.com/sorenh/buildsvctest',
                'git_branch': 'master',
                'repository': response.data['results'][0]['self']}

        response = self.create_source(**data)

        self.assertEquals(response.status_code, 201)
        self.assertTrue(response.data['self'].startswith('http://testserver' + self.list_url), response.data['self'])
        data['self'] = response.data['self']
        data['builds'] = data['self'] + 'builds/'
        self.assertEquals(response.data, data)

        response = self.show_source(data['self'])
        self.assertEquals(response.data, data)
        return response.data

    def test_delete_source(self):
        source = self.test_create_source()

        response = self.delete_source(source['self'])

        self.assertEquals(response.status_code, 204)

        response = self.show_source(source['self'])
        self.assertEquals(response.status_code, 404)


class APIv2SourceTests(APIv1SourceTests):
    list_url = '/api/v2/sources/'


class APIv1AuthTests(AuthClient):
    def test_get_user_details(self):
        authenticate(self.client, 'testuser')

        response = self.get_auth()
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data,
                          {'username': u'testuser',
                           'company': u'aaSemble',
                           'email': u'test1@example.com',
                           'avatar': u'https://avatars.githubusercontent.com/u/160090?v=3',
                           'real_name': u'Soren Hansen'})
