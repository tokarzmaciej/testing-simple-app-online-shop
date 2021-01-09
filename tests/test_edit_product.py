from unittest.mock import *
from unittest import TestCase, main
from src.serviceProducts import Product
from src.dataProducts import ProductsData


class testEditProduct(TestCase):
    def setUp(self):
        self.temp = Product()
        self.products = ProductsData().products

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

    def test_edit_product_not_exist(self):
        self.temp.ProductStorage.getAllProducts = Mock()
        self.temp.ProductStorage.getAllProducts.return_value = self.products

        result = self.temp.editProduct
        self.assertRaisesRegex(Exception, "This product not exist in data base", result, 20, "bike", 1500)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    main()
