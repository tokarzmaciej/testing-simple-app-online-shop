from unittest.mock import *
from unittest import TestCase, main
from assertpy import assert_that
from src.serviceProducts import Product
from src.dataProducts import ProductsData


class testGetByNameProduct(TestCase):
    def setUp(self):
        self.temp = Product()
        self.products = ProductsData().products

    def test_get_product_bad_name(self):
        result = self.temp.getProductByName
        self.assertRaisesRegex(TypeError, "Bad type name", result, 1)

    @patch('src.serviceProducts.ProductStorage')
    def test_get_product_lack_product(self, products):
        instance_products = Mock()
        instance_products.getAllProducts.return_value = self.products
        products.return_value = instance_products

        result = Product().getProductByName
        self.assertRaisesRegex(Exception, "This product exist", result, "shoe")

    @patch('src.serviceProducts.ProductStorage')
    def test_get_product_by_name_positive(self, products):
        instance_products = Mock()
        instance_products.getAllProducts.return_value = self.products
        products.return_value = instance_products

        result = Product().getProductByName("ball")
        assert_that(result).contains_only({
            "id": 2,
            "name": "ball",
            "value": 50
        })

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    main()
