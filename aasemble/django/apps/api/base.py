from rest_framework.test import APITestCase

class APIv1Tests(APITestCase):
    fixtures = ['data.json', 'data2.json']
