from unittest.mock import *
from unittest import TestCase, main
from src.serviceClients import Client
from src.dataClients import ClientsData


class testDeleteClient(TestCase):
    def setUp(self):
        self.temp = Client()
        self.clients = ClientsData().clients

    def test_delete_client_bad_id(self):
        result = self.temp.deleteClient
        self.assertRaisesRegex(TypeError, "Bad type id client", result, "2")

    def test_delete_client_lack_client(self):
        self.temp.ClientStorage.getAllClients = MagicMock()
        self.temp.ClientStorage.getAllClients.return_value = self.clients

        self.temp.deleteClient = MagicMock()
        self.temp.deleteClient.side_effect = Exception("This client not exist in data base")

        result = self.temp.deleteClient
        self.assertRaisesRegex(Exception, "This client not exist in data base", result, 20)


if __name__ == '__main__':
    main()
