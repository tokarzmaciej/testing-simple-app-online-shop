from unittest.mock import *
from unittest import TestCase, main
from src.serviceOrders import Order
from src.dataOrders import OrdersData


class testDeleteOrder(TestCase):
    def setUp(self):
        self.temp = Order()
        self.orders = OrdersData().orders

    def test_delete_order_bad_id_order(self):
        self.temp.deleteOrder = MagicMock()
        self.temp.deleteOrder.side_effect = TypeError("Bad type id order")

        result = self.temp.deleteOrder
        self.assertRaisesRegex(TypeError, "Bad type id order", result, "1")

    def test_delete_order_not_exist_order(self):
        self.temp.OrderStorage.getAllOrders = MagicMock()
        self.temp.OrderStorage.getAllOrders.return_value = self.orders

        result = self.temp.deleteOrder
        self.assertRaisesRegex(Exception, "This order not exist in data base", result, 101)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    main()
