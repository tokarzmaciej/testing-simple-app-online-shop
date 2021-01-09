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

    def test_edit_product_bad_new_name(self):
        result = self.temp.editProduct
        self.assertRaisesRegex(TypeError, "Bad type new name", result, 7, True, str)

    def test_edit_product_bad_new_value(self):
        self.temp.editProduct = MagicMock()
        self.temp.editProduct.side_effect = TypeError("Bad type new value")
        result = self.temp.editProduct
        self.assertRaisesRegex(TypeError, "Bad type new value", result, 7, "kite", "22")
