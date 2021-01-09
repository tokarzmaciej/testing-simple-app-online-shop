from src.baseProducts import ProductStorage


class Product:
    def __init__(self):
        self.ProductStorage = ProductStorage()

    def addProduct(self, name, value):
        products = self.ProductStorage.getAllProducts()
        if type(name) != str:
            raise TypeError("Bad type name")
        if type(value) != int and type(value) != float:
            raise TypeError("Bad type value")
        if list(filter(lambda product: product["name"] == name, products)):
            raise Exception("This product exist")
        else:
            return self.ProductStorage.postProduct(name, value)

    def deleteProduct(self, id_product):
        products = self.ProductStorage.getAllProducts()
        if type(id_product) != int:
            raise TypeError("Bad type id product")
        if len(list(filter(lambda product: product["id"] == int(id_product), products))) == 1:
            return self.ProductStorage.delProduct(id_product)
        else:
            raise Exception("This product not exist in data base")

    def editProduct(self, id_product, new_name=None, new_value=None):
        if type(id_product) != int:
            raise TypeError("Bad type id product")
        else:
            raise TypeError("Bad type new name")
