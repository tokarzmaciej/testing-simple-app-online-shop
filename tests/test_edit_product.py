from unittest.mock import *
from unittest import TestCase, main
from src.serviceProducts import Product


class testEditProduct(TestCase):
    def setUp(self):
        self.temp = Product()

    # dummy
    def test_edit_product_bad_id(self):
        result = self.temp.editProduct
        self.assertRaisesRegex(TypeError, "Bad type id product", result, "7", str, str)
