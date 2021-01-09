from src.baseClients import ClientStorage
from src.baseProducts import ProductStorage


class Order:
    def __init__(self):
        self.ClientStorage = ClientStorage()
        self.ProductStorage = ProductStorage()

    def addOrder(self, id_client, cart):
        if type(id_client) != int:
            raise TypeError("Bad type id")
        if len(list(filter(lambda client: client["id"] == id_client, self.ClientStorage.getAllClients()))) != 1:
            raise Exception("This client not exist in data base")
        if type(cart) != list:
            raise TypeError("Bad type cart")
        for element in cart:
            product_in_base = list(filter(lambda product: product["name"] == element, self.ProductStorage.getAllProducts()))
            if not product_in_base:
                raise Exception("This product not exist")
