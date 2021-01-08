from unittest.mock import *
from unittest import TestCase, main
from assertpy import assert_that
from src.serviceClients import Client, SpyValidationEmail
from src.dataClients import ClientsData


class testEditClient(TestCase):
    def patchClient(self, id_customer, new_name, new_surname, new_email):
        update_customer = list(filter(lambda customer: customer["id"] == id_customer, self.clients))
        if new_name is not None:
            update_customer[0]["name"] = new_name
        if new_surname is not None:
            update_customer[0]["surname"] = new_surname
        if new_email is not None:
            update_customer[0]["email"] = new_email
        return update_customer

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

    def test_edit_name_client_positive(self):
        self.temp.ClientStorage.getAllClients = MagicMock()
        self.temp.ClientStorage.getAllClients.return_value = self.clients

        self.temp.ClientStorage.patchClient = MagicMock()
        self.temp.ClientStorage.patchClient.side_effect = self.patchClient

        result = self.temp.editClient(5, "Agnieszka")

        assert_that(result) \
            .contains(
            {
                "id": 5,
                "name": 'Agnieszka',
                "surname": 'Jankowska',
                "email": 'monikajankowska@example.com'
            })

    def test_edit_name_client_positive_verification_mock(self):
        self.temp.ClientStorage.getAllClients = MagicMock()
        self.temp.ClientStorage.getAllClients.return_value = self.clients

        self.temp.ClientStorage.patchClient = MagicMock()
        self.temp.ClientStorage.patchClient.side_effect = self.patchClient

        self.temp.editClient(5, "Agnieszka")
        self.temp.ClientStorage.patchClient.assert_called_with(5, "Agnieszka", None, None)

    def test_edit_surname_client_positive(self):
        self.temp.ClientStorage.getAllClients = MagicMock()
        self.temp.ClientStorage.getAllClients.return_value = self.clients

        self.temp.ClientStorage.patchClient = MagicMock()
        self.temp.ClientStorage.patchClient.side_effect = self.patchClient

        result = self.temp.editClient(5, None, "Kowalczyk")
        self.assertDictEqual(result[0], {
            "id": 5, "name": 'Monika',
            "surname": 'Kowalczyk',
            "email": 'monikajankowska@example.com'})

    def test_edit_surname_client_positive_verification_mock(self):
        self.temp.ClientStorage.getAllClients = MagicMock()
        self.temp.ClientStorage.getAllClients.return_value = self.clients

        self.temp.ClientStorage.patchClient = MagicMock()
        self.temp.ClientStorage.patchClient.side_effect = self.patchClient

        self.temp.editClient(5, None, "Kowalczyk")
        self.temp.ClientStorage.patchClient.assert_called_with(5, None, "Kowalczyk", None)

    def test_edit_email_client_positive(self):
        self.temp.ClientStorage.getAllClients = MagicMock()
        self.temp.ClientStorage.getAllClients.return_value = self.clients

        self.temp.ClientStorage.patchClient = MagicMock()
        self.temp.ClientStorage.patchClient.side_effect = self.patchClient

        result = self.temp.editClient(1, None, None, "kowalskijan@example.com")
        self.assertListEqual(result, [{
            "id": 1,
            "name": "Jan",
            "surname": "Kowalski",
            "email": "kowalskijan@example.com"
        }])

    def test_edit_email_client_positive_verification_mock(self):
        self.temp.ClientStorage.getAllClients = MagicMock()
        self.temp.ClientStorage.getAllClients.return_value = self.clients

        self.temp.ClientStorage.patchClient = MagicMock()
        self.temp.ClientStorage.patchClient.side_effect = self.patchClient

        self.temp.editClient(1, None, None, "kowalskijan@example.com")
        self.temp.ClientStorage.patchClient.assert_called_once_with(1, None, None, "kowalskijan@example.com")

    def test_edit_surname_and_email_client_positive(self):
        self.temp.ClientStorage.getAllClients = MagicMock()
        self.temp.ClientStorage.getAllClients.return_value = self.clients

        self.temp.ClientStorage.patchClient = MagicMock()
        self.temp.ClientStorage.patchClient.side_effect = self.patchClient

        result = self.temp.editClient(3, None, "Kot", "beatakot@example.com")

        assert_that(result) \
            .contains(
            {
                "id": 3,
                "name": 'Beata',
                "surname": 'Kot',
                "email": 'beatakot@example.com'
            })

    def test_edit_surname_and_email_client_positive_verification_mock(self):
        self.temp.ClientStorage.getAllClients = MagicMock()
        self.temp.ClientStorage.getAllClients.return_value = self.clients

        self.temp.ClientStorage.patchClient = MagicMock()
        self.temp.ClientStorage.patchClient.side_effect = self.patchClient

        self.temp.editClient(3, None, "Kot", "beatakot@example.com")
        self.temp.ClientStorage.patchClient.assert_called_with(3, None, "Kot", "beatakot@example.com")

    def test_edit_all_element_client_positive(self):
        self.temp.ClientStorage.getAllClients = MagicMock()
        self.temp.ClientStorage.getAllClients.return_value = self.clients

        self.temp.ClientStorage.patchClient = MagicMock()
        self.temp.ClientStorage.patchClient.side_effect = self.patchClient

        result = self.temp.editClient(2, "Tomasz", "Kubacki", "tomaszkubacki@example.com")

        assert_that(result) \
            .is_length(1)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    main()
