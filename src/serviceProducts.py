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
        products = self.ProductStorage.getAllProducts()

        if type(id_product) != int:
            raise TypeError("Bad type id product")

        if type(new_name) != str and new_name is not None:
            raise TypeError("Bad type new name")

        if type(new_value) != int and type(new_value) != float and new_value is not None:
            raise TypeError("Bad type new value")

        if len(list(filter(lambda product: product["id"] == id_product, products))) == 1:
            return self.ProductStorage.patchProduct(id_product, new_name, new_value)
        else:
            raise Exception("This product not exist in data base")

    def getProductByName(self, name):
        if type(name) != str:
            raise TypeError("Bad type name")
