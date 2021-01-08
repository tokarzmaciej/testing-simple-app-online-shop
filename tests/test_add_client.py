from unittest.mock import *
from unittest import TestCase, main
from src.serviceClients import Client
from src.dataClients import ClientsData
from src.spyValidation import SpyValidationEmail


class testAddClient(TestCase):
    def setUp(self):
        self.temp = Client()
        self.clients = ClientsData().clients

    def test_add_client_bad_name(self):
        result = self.temp.addClient
        self.assertRaisesRegex(TypeError, "Bad type name", result, 12345, str, str)

    def test_add_client_bad_surname(self):
        result = self.temp.addClient
        self.assertRaisesRegex(TypeError, "Bad type surname", result, "Ola", False, str)

    def test_add_client_bad_email(self):
        self.temp.addClient = Mock()
        self.temp.addClient.side_effect = TypeError("Bad type email")

        result = self.temp.addClient
        self.assertRaisesRegex(TypeError, "Bad type email", result, "Robert", "Kot", None)

    def test_add_client_no_validation_email(self):
        validation = SpyValidationEmail(status=False)
        self.temp.validation = validation

        result = self.temp.addClient
        self.assertRaisesRegex(ValueError, "Bad value email", result, "Adrian", "Kowalski",
                               "adrianKowalski_example.com")

    def test_add_client_good_validation_email(self):
        validation = SpyValidationEmail(status=True)
        self.temp.validation = validation

        self.temp.ClientStorage.getAllClients = MagicMock()
        self.temp.ClientStorage.getAllClients.return_value = self.clients

        self.temp.addClient("Adrian", "Kowalski", "adrianKowalski@example.com")
        self.assertIn("adrianKowalski@example.com", validation.check_email)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    main()
