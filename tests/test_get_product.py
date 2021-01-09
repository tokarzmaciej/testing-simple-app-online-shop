from unittest.mock import *
from unittest import TestCase, main
from src.serviceProducts import Product


class testGetByNameProduct(TestCase):
    def setUp(self):
        self.temp = Product()

    def test_get_product_bad_name(self):
        result = self.temp.getProductByName
        self.assertRaisesRegex(TypeError, "Bad type name", result, 1)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    main()
