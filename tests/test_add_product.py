from unittest.mock import *
from unittest import TestCase, main
from src.serviceProducts import Product


class testAddProduct(TestCase):
    def setUp(self):
        self.temp = Product()

    def test_add_product_bad_name(self):
        result = self.temp.addProduct
        self.assertRaisesRegex(TypeError, "Bad type name", result, False, int)

    def test_add_product_bad_value(self):
        result = self.temp.addProduct
        self.assertRaisesRegex(TypeError, "Bad type value", result, "kite", "22")

    @patch.object(Product, 'addProduct')
    def test_add_product_already_exist(self, mock_method):
        mock_method.side_effect = Exception("This prodct exist")

        result = self.temp.addProduct
        self.assertRaisesRegex(Exception, "This product exist", result, "ball", 50)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    main()
