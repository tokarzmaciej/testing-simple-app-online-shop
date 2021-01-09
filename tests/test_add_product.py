from unittest.mock import *
from unittest import TestCase, main
from src.serviceProducts import Product


class testAddProduct(TestCase):
    def setUp(self):
        self.temp = Product()

    def test_add_product_bad_name(self):
        result = self.temp.addProduct
        self.assertRaisesRegex(TypeError, "Bad type name", result, False, int)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    main()
