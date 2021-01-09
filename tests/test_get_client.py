from unittest.mock import *
from unittest import TestCase, main
from src.serviceClients import Client


class testGetClientOrders(TestCase):
    def setUp(self):
        self.temp = Client()

    def test_get_client_orders_bad_id(self):
        result = self.temp.getClientOrders
        self.assertRaisesRegex(TypeError, "Bad type id client", result, True)


if __name__ == '__main__':
    main()
