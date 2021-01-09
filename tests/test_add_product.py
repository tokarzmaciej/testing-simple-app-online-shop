from unittest.mock import *
from unittest import TestCase, main
from src.serviceProducts import Product
from src.dataProducts import ProductsData


class testAddProduct(TestCase):
    def setUp(self):
        self.temp = Product()
        self.products = ProductsData().products

    def test_add_product_bad_name(self):
        result = self.temp.addProduct
        self.assertRaisesRegex(TypeError, "Bad type name", result, False, int)

    def test_add_product_bad_value(self):
        result = self.temp.addProduct
        self.assertRaisesRegex(TypeError, "Bad type value", result, "kite", "22")

    @patch.object(Product, 'addProduct')
    def test_add_product_already_exist(self, mock_method):
        mock_method.side_effect = Exception("This product exist")

        result = self.temp.addProduct
        self.assertRaisesRegex(Exception, "This product exist", result, "ball", 50)

    def test_add_product_positive(self):
        self.temp.ProductStorage = FakeAddProduct()

        self.temp.ProductStorage.getAllProducts = Mock()
        self.temp.ProductStorage.getAllProducts.return_value = self.products

        result = self.temp.addProduct("net", 35)
        self.assertEqual(result, "Add new product name:net value:35")

    def test_add_product_positive_verification_mock(self):
        self.temp.ProductStorage = FakeAddProduct()

        self.temp.ProductStorage.getAllProducts = Mock()
        self.temp.ProductStorage.getAllProducts.return_value = self.products

        self.temp.addProduct("net", 35)
        self.temp.ProductStorage.getAllProducts.assert_called_once()

    def tearDown(self):
        self.temp = None


class FakeAddProduct:
    def __init__(self):
        self.add = "Add new product"

    def postProduct(self, name, value):
        return self.add + " name:" + name + " value:" + str(value)


if __name__ == '__main__':
    main()
