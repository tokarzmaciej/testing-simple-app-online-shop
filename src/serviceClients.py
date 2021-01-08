from src.baseClients import ClientStorage
from src.spyValidation import SpyValidationEmail


class Client:
    def __init__(self):
        self.ClientStorage = ClientStorage()
        self.validation = SpyValidationEmail()

    def addClient(self, name, surname, email):
        clients = self.ClientStorage.getAllClients()
        if type(name) != str:
            raise TypeError("Bad type name")
        if type(surname) != str:
            raise TypeError("Bad type surname")
        if type(email) != str:
            raise TypeError("Bad type email")
        if not self.validation.validEmail(email):
            raise ValueError("Bad value email")
        if list(filter(lambda client:
                       client["name"] == name and client["surname"] == surname
                       and client["email"] == email, clients)):
            raise Exception("This client exist")
        else:
            return self.ClientStorage.postClient(name, surname, email)

    def deleteClient(self, id_client):
        clients = self.ClientStorage.getAllClients()
        if type(id_client) != int:
            raise TypeError("Bad type id client")
        if len(list(filter(lambda client: client["id"] == id_client, clients))) != 1:
            raise Exception("This client not exist in data base")
        else:
            return self.ClientStorage.delClient(id_client)

    def editClient(self, id_client, new_name=None, new_surname=None, new_email=None):
        if type(id_client) != int:
            raise TypeError("Bad type id client")
        if type(new_name) != str and new_name is not None:
            raise TypeError("Bad type new name")
        if type(new_surname) != str and new_surname is not None:
            raise TypeError("Bad type new surname")
        if type(new_email) != str and new_email is not None:
            raise TypeError("Bad type new email")
        if not self.validation.validEmail(new_email):
            raise ValueError("Bad value email")
        return self.ClientStorage.getAllClients()
