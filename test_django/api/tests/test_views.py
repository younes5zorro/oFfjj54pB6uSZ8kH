from django.shortcuts import reverse

from rest_framework.test import APITestCase

from api.models import Connection


class TestNoteApi(APITestCase):
    def setUp(self):
        # create connection
        self.connection = Connection(name="MS sql", type="rdbms")
        self.connection.save()

    def test_connection_creation(self):
        response = self.client.post(reverse('connections'), {
            'name': 'Mongo',
            'type': "nosql"
        })

        # assert new connection was added
        self.assertEqual(Connection.objects.count(), 2)

        # assert a created status code was returned
        self.assertEqual(201, response.status_code)

    def test_getting_connections(self):
        response = self.client.get(reverse('connections'), format="json")
        self.assertEqual(len(response.data), 1)

    def test_updating_connection(self):
        response = self.client.put(reverse('detail', kwargs={'pk': 1}), {
            'name': 'redis',
            'type': "nosql"
        }, format="json")

        # check info returned has the update
        self.assertEqual('redis', response.data['name'])

    def test_deleting_connection(self):
        response = self.client.delete(reverse('detail', kwargs={'pk': 1}))

        self.assertEqual(204, response.status_code)