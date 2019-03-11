from django.test import TestCase

from api.models import Connection


class TestConnectionModel(TestCase):
    def setUp(self):
        self.connection = Connection(name="Mysql", type="rdbms")
        self.connection.save()

    def test_connection_creation(self):
        self.assertEqual(Connection.objects.count(), 1)

    def test_connection_representation(self):
        self.assertEqual(self.connection.name, str(self.connection))