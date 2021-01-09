from src.baseClients import ClientStorage
from src.baseProducts import ProductStorage
from src.spyPostOrder import SpyPostOrder


class Order:
    def __init__(self):
        self.ClientStorage = ClientStorage()
        self.ProductStorage = ProductStorage()
        self.SpyPostOrder = SpyPostOrder()

    def addOrder(self, id_client, cart):
        clients = self.ClientStorage.getAllClients()
        products = self.ProductStorage.getAllProducts()

        if type(id_client) != int:
            raise TypeError("Bad type id")
        if len(list(filter(lambda client: client["id"] == id_client, clients))) != 1:
            raise Exception("This client not exist in data base")
        if type(cart) != list:
            raise TypeError("Bad type cart")
        for element in cart:
            product_in_base = list(
                filter(lambda product: product["name"] == element, products))
            if not product_in_base:
                raise Exception("This product not exist")
            else:
                id_product = product_in_base[0]["id"]
                if not self.SpyPostOrder.postOrderProduct(id_product):
                    raise Exception("Problem connection in base")
