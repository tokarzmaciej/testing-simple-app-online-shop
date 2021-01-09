from unittest.mock import *
from unittest import TestCase, main
from src.serviceOrders import Order


class testGetProductsInOrder(TestCase):
    def setUp(self):
        self.temp = Order()

    def test_get_products_in_order_bad_id(self):
        result = self.temp.getProductsInOrder
        self.assertRaisesRegex(TypeError, "Bad type order id", result, "one")

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    main()
