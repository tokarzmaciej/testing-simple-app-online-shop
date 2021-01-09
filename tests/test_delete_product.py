from unittest.mock import *
from unittest import TestCase, main
from src.serviceProducts import Product


class testDeleteProduct(TestCase):
    def setUp(self):
        self.temp = Product()

    def test_delete_product_bad_id(self):
        result = self.temp.deleteProduct
        self.assertRaisesRegex(TypeError, "Bad type id product", result, False)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    main()
