from unittest.mock import *
from unittest import TestCase, main
from assertpy import assert_that
from src.serviceOrders import Order
from src.dataClients import ClientsData
from src.dataProducts import ProductsData
from src.spyPostOrder import SpyPostOrder


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

    def test_add_order_data_base_problem_connection(self):
        add_order = SpyPostOrder(status=False)
        self.temp.SpyPostOrder = add_order

        self.temp.ClientStorage.getAllClients = Mock()
        self.temp.ClientStorage.getAllClients.return_value = self.clients

        self.temp.ProductStorage.getAllProducts = MagicMock()
        self.temp.ProductStorage.getAllProducts.return_value = self.products

        result = self.temp.addOrder
        self.assertRaisesRegex(Exception, "Problem connection in base", result, 1, ["skis"])

    def test_add_orderProduct_one_product_positive(self):
        add_order = SpyPostOrder(status=True)
        self.temp.SpyPostOrder = add_order

        self.temp.ClientStorage.getAllClients = Mock()
        self.temp.ClientStorage.getAllClients.return_value = self.clients

        self.temp.ProductStorage.getAllProducts = MagicMock()
        self.temp.ProductStorage.getAllProducts.return_value = self.products

        self.temp.addOrder(1, ["ball"])
        assert_that(add_order.post_order_product).is_length(1)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    main()
