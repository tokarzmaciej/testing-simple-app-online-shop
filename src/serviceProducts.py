class Product:

    def addProduct(self, name, value):
        if type(name) != str:
            raise TypeError("Bad type name")
