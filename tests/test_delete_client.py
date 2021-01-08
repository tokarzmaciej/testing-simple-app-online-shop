from unittest.mock import *
from unittest import TestCase, main
from src.serviceClients import Client


class testDeleteClient(TestCase):
    def setUp(self):
        self.temp = Client()

    def test_delete_client_bad_id(self):
        result = self.temp.deleteClient
        self.assertRaisesRegex(TypeError, "Bad type id client", result, "2")


if __name__ == '__main__':
    main()
