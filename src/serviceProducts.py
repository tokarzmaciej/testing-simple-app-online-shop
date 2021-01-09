class Product:

    def addProduct(self, name, value):
        if type(name) != str:
            raise TypeError("Bad type name")
        if type(value) != int and type(value) != float:
            raise TypeError("Bad type value")
        else:
            raise Exception("This product exist")

