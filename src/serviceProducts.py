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
