from unittest.mock import *
from unittest import TestCase, main
from src.serviceClients import Client, SpyValidationEmail
from src.dataClients import ClientsData


class testEditClient(TestCase):

    def setUp(self):
        self.temp = Client()
        self.clients = ClientsData().clients

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

    def test_edit_client_good_validation_new_email(self):
        validation = SpyValidationEmail(status=True)
        self.temp.validation = validation

        self.temp.ClientStorage.getAllClients = MagicMock()
        self.temp.ClientStorage.getAllClients.return_value = self.clients

        self.temp.editClient(4, "Piotr", "Nowick", "piotr123@example.com")
        self.assertIn("piotr123@example.com", validation.check_email)

    def test_edit_client_good_validation_new_email_verification_mock(self):
        validation = SpyValidationEmail(status=True)
        self.temp.validation = validation

        self.temp.ClientStorage.getAllClients = MagicMock()
        self.temp.ClientStorage.getAllClients.return_value = self.clients

        self.temp.editClient(4, "Piotr", "Nowick", "piotr123@example.com")
        self.temp.ClientStorage.getAllClients.assert_called_once()

    def test_edit_client_new_email_exists(self):
        self.temp.ClientStorage.getAllClients = Mock()
        self.temp.ClientStorage.getAllClients.return_value = self.clients

        result = self.temp.editClient
        self.assertRaisesRegex(Exception, "This email exists", result, 5, None, None,
                               "beatalewandowska@example.com")

    def test_edit_client_client_not_exist(self):
        self.temp.ClientStorage.getAllClients = Mock()
        self.temp.ClientStorage.getAllClients.return_value = self.clients

        result = self.temp.editClient
        self.assertRaisesRegex(Exception, "This client not exist in data base", result, 21, "Bartek", None,
                               None)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    main()
