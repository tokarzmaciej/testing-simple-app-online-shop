from unittest.mock import *
from unittest import TestCase, main
from assertpy import assert_that
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

    def test_delete_product_positive(self):
        self.temp.ProductStorage.getAllProducts = MagicMock()
        self.temp.ProductStorage.getAllProducts.return_value = self.products

        self.temp.ProductStorage.delProduct = MagicMock()
        self.temp.ProductStorage.delProduct.return_value = [{
            "id": 6,
            "name": "racket",
            "value": 75
        }]

        result = self.temp.deleteProduct(6)
        assert_that(result).contains_only({
            "id": 6,
            "name": "racket",
            "value": 75
        })

    def test_delete_product_positive_verification_mock(self):
        self.temp.ProductStorage.getAllProducts = MagicMock()
        self.temp.ProductStorage.getAllProducts.return_value = self.products

        self.temp.ProductStorage.delProduct = MagicMock()
        self.temp.ProductStorage.delProduct.return_value = [{
            "id": 6,
            "name": "racket",
            "value": 75
        }]

        self.temp.deleteProduct(6)
        self.temp.ProductStorage.delProduct.assert_called_once_with(6)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    main()
