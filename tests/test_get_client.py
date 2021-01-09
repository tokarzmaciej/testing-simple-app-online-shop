from unittest.mock import *
from unittest import TestCase, main
from src.serviceClients import Client
from src.dataClients import ClientsData


class testGetClientOrders(TestCase):
    def setUp(self):
        self.temp = Client()
        self.clients = ClientsData().clients

    def test_get_client_orders_bad_id(self):
        result = self.temp.getClientOrders
        self.assertRaisesRegex(TypeError, "Bad type id client", result, True)

    @patch('src.serviceClients.ClientStorage')
    def test_get_client_orders_lack_client(self, clients):
        instance_clients = Mock()
        instance_clients.getAllClients.return_value = self.clients
        clients.return_value = instance_clients

        result = self.temp.getClientOrders
        self.assertRaises(Exception, result, 31)


if __name__ == '__main__':
    main()
