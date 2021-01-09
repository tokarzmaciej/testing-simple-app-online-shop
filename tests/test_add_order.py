from unittest.mock import *
from unittest import TestCase, main
from src.serviceOrders import Order
from src.dataClients import ClientsData


class testAddOrder(TestCase):
    def setUp(self):
        self.temp = Order()
        self.clients = ClientsData().clients

    def test_add_order_bad_id_client(self):
        result = self.temp.addOrder
        self.assertRaisesRegex(TypeError, "Bad type id", result, "abc", list)

    def test_add_order_lack_client(self):
        self.temp.ClientStorage.getAllClients = Mock()
        self.temp.ClientStorage.getAllClients.return_value = self.clients

        result = self.temp.addOrder
        self.assertRaisesRegex(Exception, "This client not exist in data base", result, 45, list)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    main()
