from src.baseClients import ClientStorage

class Order:
    def __init__(self):
        self.ClientStorage = ClientStorage()

    def addOrder(self, id_client, cart):
        if type(id_client) != int:
            raise TypeError("Bad type id")
        else:
            raise Exception("This client not exist in data base")
