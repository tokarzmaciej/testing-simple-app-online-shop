from unittest.mock import *
from unittest import TestCase, main
from src.serviceClients import Client, SpyValidationEmail
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

    def test_edit_client_bad_new_email(self):
        self.temp.editClient = Mock()
        self.temp.editClient.side_effect = TypeError("Bad type new email")

        result = self.temp.editClient
        self.assertRaisesRegex(TypeError, "Bad type new email", result, 4, "Robert", "Kot", 1.2345)

    def test_edit_client_no_validation_new_email(self):
        validation = SpyValidationEmail(status=False)
        self.temp.validation = validation

        result = self.temp.editClient
        self.assertRaisesRegex(ValueError, "Bad value email", result, 4, "Piotr", "Nowick",
                               "piotr123example.com")

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    main()
