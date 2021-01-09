from unittest.mock import *
from unittest import TestCase, main
from src.serviceOrders import Order


class testDeleteOrder(TestCase):
    def setUp(self):
        self.temp = Order()

    def test_delete_order_bad_id_order(self):
        self.temp.deleteOrder = MagicMock()
        self.temp.deleteOrder.side_effect = TypeError("Bad type id order")

        result = self.temp.deleteOrder
        self.assertRaisesRegex(TypeError, "Bad type id order", result, "1")

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    main()
