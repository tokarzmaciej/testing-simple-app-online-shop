from src.baseClients import ClientStorage


class Order:
    def __init__(self):
        self.ClientStorage = ClientStorage()

    def addOrder(self, id_client, cart):
        if type(id_client) != int:
            raise TypeError("Bad type id")
        if len(list(filter(lambda client: client["id"] == id_client, self.ClientStorage.getAllClients()))) != 1:
            raise Exception("This client not exist in data base")
        if type(cart) != list:
            raise TypeError("Bad type cart")
