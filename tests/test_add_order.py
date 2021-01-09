from unittest import TestCase, main
from src.serviceOrders import Order


class testAddOrder(TestCase):
    def setUp(self):
        self.temp = Order()

    def test_add_order_bad_id_client(self):
        result = self.temp.addOrder
        self.assertRaisesRegex(TypeError, "Bad type id", result, "abc", list)
