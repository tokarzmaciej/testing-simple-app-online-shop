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

    def test_add_orderProduct_one_product_positive_verification_moc(self):
        add_order = SpyPostOrder(status=True)
        self.temp.SpyPostOrder = add_order

        self.temp.ClientStorage.getAllClients = Mock()
        self.temp.ClientStorage.getAllClients.return_value = self.clients

        self.temp.ProductStorage.getAllProducts = MagicMock()
        self.temp.ProductStorage.getAllProducts.return_value = self.products

        self.temp.addOrder(1, ["ball"])
        self.temp.ProductStorage.getAllProducts.assert_called_once()

    def test_add_orderProduct_few_product_positive(self):
        add_order = SpyPostOrder(status=True)
        self.temp.SpyPostOrder = add_order

        self.temp.ClientStorage.getAllClients = Mock()
        self.temp.ClientStorage.getAllClients.return_value = self.clients

        self.temp.ProductStorage.getAllProducts = MagicMock()
        self.temp.ProductStorage.getAllProducts.return_value = self.products

        self.temp.addOrder(4, ["ball", "bike", "racket"])
        assert_that(add_order.post_order_product) \
            .is_length(3)

    def test_add_orderProduct_few_product_positive_verification_mock(self):
        add_order = SpyPostOrder(status=True)
        self.temp.SpyPostOrder = add_order

        self.temp.ClientStorage.getAllClients = Mock()
        self.temp.ClientStorage.getAllClients.return_value = self.clients

        self.temp.ProductStorage.getAllProducts = MagicMock()
        self.temp.ProductStorage.getAllProducts.return_value = self.products

        self.temp.addOrder(4, ["ball", "bike", "racket"])
        self.temp.ProductStorage.getAllProducts.assert_called_once()

    def test_add_order_positive(self):
        add_order = SpyPostOrder(status=True)
        self.temp.SpyPostOrder = add_order

        self.temp.ClientStorage.getAllClients = Mock()
        self.temp.ClientStorage.getAllClients.return_value = self.clients

        self.temp.ProductStorage.getAllProducts = Mock()
        self.temp.ProductStorage.getAllProducts.return_value = self.products

        self.temp.OrderStorage.postOrder = Mock()
        self.temp.OrderStorage.postOrder.return_value = {
            "id": 9,
            "client_id": 2
        }

        result = self.temp.addOrder(2, ["sled", "skis"])
        self.assertDictEqual(result, {
            "id": 9,
            "client_id": 2
        })

    def test_add_order_positive_verification_mock(self):
        add_order = SpyPostOrder(status=True)
        self.temp.SpyPostOrder = add_order

        self.temp.ClientStorage.getAllClients = Mock()
        self.temp.ClientStorage.getAllClients.return_value = self.clients

        self.temp.ProductStorage.getAllProducts = Mock()
        self.temp.ProductStorage.getAllProducts.return_value = self.products

        self.temp.OrderStorage.postOrder = Mock()
        self.temp.OrderStorage.postOrder.return_value = {
            "id": 9,
            "client_id": 2
        }

        self.temp.addOrder(2, ["sled", "skis"])
        self.temp.OrderStorage.postOrder.assert_called_with(2)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    main()
