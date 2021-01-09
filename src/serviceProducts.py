from src.baseProducts import ProductStorage


class Product:
    def __init__(self):
        self.ProductStorage = ProductStorage()

    def addProduct(self, name, value):
        if type(name) != str:
            raise TypeError("Bad type name")
        if type(value) != int and type(value) != float:
            raise TypeError("Bad type value")
        if list(filter(lambda product: product["name"] == name, self.ProductStorage.getAllProducts())):
            raise Exception("This product exist")
