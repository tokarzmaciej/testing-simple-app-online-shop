from unittest.mock import *
from unittest import TestCase, main
from assertpy import assert_that
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

    def test_add_client_good_validation_email_verification_mock(self):
        validation = SpyValidationEmail(status=True)
        self.temp.validation = validation

        self.temp.ClientStorage.getAllClients = MagicMock()
        self.temp.ClientStorage.getAllClients.return_value = self.clients

        self.temp.addClient("Adrian", "Kowalski", "adrianKowalski@example.com")
        self.temp.ClientStorage.getAllClients.assert_called_once()

    def test_add_client_already_exists(self):
        self.temp.ClientStorage.getAllClients = MagicMock()
        self.temp.ClientStorage.getAllClients.return_value = self.clients

        result = self.temp.addClient
        self.assertRaisesRegex(Exception, "This client exist", result, "Jan", "Kowalski",
                               "jankowalski@example.com")

    def test_add_client_positive(self):
        self.temp.ClientStorage = FakeAddClient(self.clients)
        self.temp.ClientStorage.postClient = Mock()
        self.temp.ClientStorage.postClient.return_value = [
            {"id": len(self.clients), "name": 'Szymon', "surname": 'Polak', "email": 'szymonpolak@example.com'}]

        result = self.temp.addClient("Szymon", "Polak", "szymonpolak@example.com")
        assert_that(result) \
            .contains(
            {"id": len(self.clients), "name": 'Szymon', "surname": 'Polak', "email": 'szymonpolak@example.com'})

    def tearDown(self):
        self.temp = None


class FakeAddClient(object):
    def __init__(self, customers):
        self.customers = customers

    def getAllClients(self):
        return self.customers


if __name__ == '__main__':
    main()
