class Product:

    def addProduct(self, name, value):
        if type(name) != str:
            raise TypeError("Bad type name")
        elif type(value) != int:
            raise TypeError("Bad type value")
        elif type(value) != float:
            raise TypeError("Bad type value")

