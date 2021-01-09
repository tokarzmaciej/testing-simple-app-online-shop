from unittest.mock import *
from unittest import TestCase, main
from assertpy import assert_that
from src.serviceClients import Client
from src.dataClients import ClientsData
from src.dataOrders import OrdersData


class testGetClientOrders(TestCase):
    def setUp(self):
        self.temp = Client()
        self.clients = ClientsData().clients
        self.orders = OrdersData().orders

    def test_get_client_orders_bad_id(self):
        result = self.temp.getClientOrders
        self.assertRaisesRegex(TypeError, "Bad type id client", result, True)

    @patch('src.serviceClients.ClientStorage')
    def test_get_client_orders_lack_client(self, clients):
        instance_clients = Mock()
        instance_clients.getAllClients.return_value = self.clients
        clients.return_value = instance_clients

        result = Client().getClientOrders
        self.assertRaises(Exception, result, 31)

    def test_get_client_orders_positive(self):
        self.temp.ClientStorage.getAllClients = MagicMock()
        self.temp.ClientStorage.getAllClients.return_value = self.clients

        self.temp.OrderStorage.getAllOrders = Mock()
        self.temp.OrderStorage.getAllOrders.return_value = self.orders

        result = self.temp.getClientOrders(3)
        assert_that(result).is_not_empty()

    def test_get_client_orders_positive_verification_mock(self):
        self.temp.ClientStorage.getAllClients = MagicMock()
        self.temp.ClientStorage.getAllClients.return_value = self.clients

        self.temp.OrderStorage.getAllOrders = Mock()
        self.temp.OrderStorage.getAllOrders.return_value = self.orders

        self.temp.getClientOrders(3)
        self.temp.OrderStorage.getAllOrders.assert_called_once()


if __name__ == '__main__':
    main()
