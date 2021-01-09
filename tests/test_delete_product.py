from unittest.mock import *
from unittest import TestCase, main
from src.serviceProducts import Product
from src.dataProducts import ProductsData


class testDeleteProduct(TestCase):
    def setUp(self):
        self.temp = Product()
        self.products = ProductsData().products

    def test_delete_product_bad_id(self):
        result = self.temp.deleteProduct
        self.assertRaisesRegex(TypeError, "Bad type id product", result, False)

    def test_delete_product_lack_product(self):
        self.temp.ProductStorage.getAllProducts = Mock()
        self.temp.ProductStorage.getAllProducts.return_value = self.products

        result = self.temp.deleteProduct
        self.assertRaisesRegex(Exception, "This product not exist in data base", result, 88)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    main()
