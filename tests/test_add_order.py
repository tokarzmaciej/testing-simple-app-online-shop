from unittest.mock import *
from unittest import TestCase, main
from src.serviceOrders import Order
from src.dataClients import ClientsData
from src.dataProducts import ProductsData


class testAddOrder(TestCase):
    def setUp(self):
        self.temp = Order()
        self.clients = ClientsData().clients
        self.products = ProductsData().products

    def test_add_order_bad_id_client(self):
        result = self.temp.addOrder
        self.assertRaisesRegex(TypeError, "Bad type id", result, "abc", list)

    def test_add_order_lack_client(self):
        self.temp.ClientStorage.getAllClients = Mock()
        self.temp.ClientStorage.getAllClients.return_value = self.clients

        result = self.temp.addOrder
        self.assertRaisesRegex(Exception, "This client not exist in data base", result, 45, list)

    def test_add_client_bad_cart(self):
        self.temp.ClientStorage.getAllClients = Mock()
        self.temp.ClientStorage.getAllClients.return_value = self.clients

        result = self.temp.addOrder
        self.assertRaisesRegex(TypeError, "Bad type cart", result, 5, "ball")

    def test_add_order_product_not_exits(self):
        self.temp.ClientStorage.getAllClients = Mock()
        self.temp.ClientStorage.getAllClients.return_value = self.clients

        self.temp.ProductStorage.getAllProducts = MagicMock()
        self.temp.ProductStorage.getAllProducts.return_value = self.products

        result = self.temp.addOrder
        self.assertRaisesRegex(Exception, "This product not exist", result, 3, ["ball", "trampoline"])

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    main()
