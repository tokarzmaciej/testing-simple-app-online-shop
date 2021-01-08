from unittest.mock import *
from unittest import TestCase, main
from src.serviceClients import Client
from src.dataClients import ClientsData


class testEditClient(TestCase):

    def setUp(self):
        self.temp = Client()

    # dummy
    def test_edit_client_bad_id(self):
        result = self.temp.editClient
        self.assertRaisesRegex(TypeError, "Bad type id client", result, "Two", str, str, str)

    def test_edit_client_bad_new_name(self):
        result = self.temp.editClient
        self.assertRaisesRegex(TypeError, "Bad type new name", result, 4, False, str, str)

    def test_edit_client_bad_new_surname(self):
        result = self.temp.editClient
        self.assertRaisesRegex(TypeError, "Bad type new surname", result, 1, "Adam", 1234, str)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    main()
