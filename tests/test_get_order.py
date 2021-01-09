from unittest.mock import *
from unittest import TestCase, main
from src.serviceOrders import Order
from src.dataProducts import ProductsData
from src.dataProductsOrders import OrdersProductsData
from src.dataOrders import OrdersData


class testGetProductsInOrder(TestCase):
    def setUp(self):
        self.temp = Order()
        self.products = ProductsData().products
        self.productsOrders = OrdersProductsData().productsOrders
        self.orders = OrdersData().orders

    def test_get_products_in_order_bad_id(self):
        result = self.temp.getProductsInOrder
        self.assertRaisesRegex(TypeError, "Bad type order id", result, "one")

    @patch('src.serviceOrders.ProductStorage')
    def test_get_products_in_order_lack_order(self, products):
        instance_products = Mock()
        instance_products.getAllProducts.return_value = self.products
        products.return_value = instance_products

        self.temp.OrderStorage.getAllOrdersProducts = Mock()
        self.temp.OrderStorage.getAllOrdersProducts.return_value = self.productsOrders

        self.temp.OrderStorage.getAllOrders = Mock()
        self.temp.OrderStorage.getAllOrders.return_value = self.orders

        result = self.temp.getProductsInOrder
        self.assertRaisesRegex(Exception, "This order not exist in data base", result, 150)

    def test_get_products_in_order_positive(self):
        self.temp.ProductStorage.getAllProducts = Mock()
        self.temp.ProductStorage.getAllProducts.return_value = self.products

        self.temp.OrderStorage.getAllOrdersProducts = Mock()
        self.temp.OrderStorage.getAllOrdersProducts.return_value = self.productsOrders

        self.temp.OrderStorage.getAllOrders = Mock()
        self.temp.OrderStorage.getAllOrders.return_value = self.orders

        result = self.temp.getProductsInOrder(7)
        self.assertEqual(result, [{'id': 6, 'name': 'racket', 'value': 75},
                                  {'id': 3, 'name': 'shoes', 'value': 39.99}])

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    main()
