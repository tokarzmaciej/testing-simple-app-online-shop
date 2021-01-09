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

    def test_delete_order_positive(self):
        self.temp.OrderStorage = FakeDeleteOrder()
        self.temp.OrderStorage.getAllOrders = MagicMock()
        self.temp.OrderStorage.getAllOrders.return_value = self.orders

        result = self.temp.deleteOrder(8)
        self.assertEqual(result, "Deleted order id:8")

    def test_delete_order_positive_verification_mock(self):
        self.temp.OrderStorage = FakeDeleteOrder()
        self.temp.OrderStorage.getAllOrders = MagicMock()
        self.temp.OrderStorage.getAllOrders.return_value = self.orders

        self.temp.deleteOrder(8)
        self.temp.OrderStorage.getAllOrders.assert_called_once()

    def test_delete_orderProduct_bad_id_order(self):
        self.temp.deleteOrder = MagicMock()
        self.temp.deleteOrder.side_effect = TypeError("Bad type id order")

        result = self.temp.deleteOrderProduct
        self.assertRaisesRegex(TypeError, "Bad type order id", result, "two", int)

    def test_delete_orderProduct_bad_id_product(self):
        result = self.temp.deleteOrderProduct
        self.assertRaisesRegex(TypeError, "Bad type product id", result, 3, "seven")

    def tearDown(self):
        self.temp = None


class FakeDeleteOrder:
    def __init__(self):
        self.deleted = "Deleted order"

    def delOrder(self, id_order):
        return self.deleted + " id:" + str(id_order)


if __name__ == '__main__':
    main()
