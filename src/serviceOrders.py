class Order:

    def addOrder(self, id_client, cart):
        if type(id_client) != int:
            raise TypeError("Bad type id")
