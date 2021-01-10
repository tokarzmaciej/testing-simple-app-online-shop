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

    def test_edit_product_new_name_positive(self):
        self.temp.ProductStorage.getAllProducts = Mock()
        self.temp.ProductStorage.getAllProducts.return_value = self.products

        self.temp.ProductStorage.patchProduct = Mock()
        self.temp.ProductStorage.patchProduct.return_value = {
            "id": 3,
            "name": "sport shoes",
            "value": 39.99
        }

        result = self.temp.editProduct(3, "sport shoes")
        self.assertDictEqual(result, {
            "id": 3,
            "name": "sport shoes",
            "value": 39.99
        })

    def test_edit_product_new_name_positive_verification_mock(self):
        self.temp.ProductStorage.getAllProducts = Mock()
        self.temp.ProductStorage.getAllProducts.return_value = self.products

        self.temp.ProductStorage.patchProduct = Mock()
        self.temp.ProductStorage.patchProduct.return_value = {
            "id": 3,
            "name": "sport shoes",
            "value": 39.99
        }

        self.temp.editProduct(3, "sport shoes")

        self.temp.ProductStorage.patchProduct.assert_called_with(3, "sport shoes", None)

    def test_edit_product_new_value_positive(self):
        self.temp.ProductStorage.getAllProducts = Mock()
        self.temp.ProductStorage.getAllProducts.return_value = self.products

        self.temp.ProductStorage.patchProduct = Mock()
        self.temp.ProductStorage.patchProduct.return_value = \
            {
                "id": 7,
                "name": "skis",
                "value": 859.99
            }

        result = self.temp.editProduct(7, None, 859.99)
        self.assertDictEqual(result, {
            "id": 7,
            "name": "skis",
            "value": 859.99
        })

    def test_edit_product_new_value_positive_verification_mock(self):
        self.temp.ProductStorage.getAllProducts = Mock()
        self.temp.ProductStorage.getAllProducts.return_value = self.products

        self.temp.ProductStorage.patchProduct = Mock()
        self.temp.ProductStorage.patchProduct.return_value = \
            {
                "id": 7,
                "name": "skis",
                "value": 859.99
            }

        self.temp.editProduct(7, None, 859.99)

        self.temp.ProductStorage.patchProduct.assert_called_with(7, None, 859.99)

    def test_edit_product_new_name_and_value_positive(self):
        self.temp.ProductStorage.getAllProducts = Mock()
        self.temp.ProductStorage.getAllProducts.return_value = self.products

        self.temp.ProductStorage.patchProduct = Mock()
        self.temp.ProductStorage.patchProduct.return_value = \
            {
                "id": 4,
                "name": "snowboard",
                "value": 599
            }

        result = self.temp.editProduct(4, "snowboard", 599)
        self.assertDictEqual(result, {
            "id": 4,
            "name": "snowboard",
            "value": 599
        })

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    main()
