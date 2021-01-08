from unittest.mock import *
from unittest import TestCase, main
from src.serviceClients import Client


class testAddClient(TestCase):
    def setUp(self):
        self.temp = Client()

    def test_add_client_bad_name(self):
        result = self.temp.addClient
        self.assertRaisesRegex(TypeError, "Bad type name", result, 12345, str, str)

    def test_add_client_bad_surname(self):
        result = self.temp.addClient
        self.assertRaisesRegex(TypeError, "Bad type surname", result, "Ola", False, str)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    main()
