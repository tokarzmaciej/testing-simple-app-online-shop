from src.baseClients import ClientStorage
from src.spyValidation import SpyValidationEmail


class Client:
    def __init__(self):
        self.ClientStorage = ClientStorage()
        self.validation = SpyValidationEmail()

    def addClient(self, name, surname, email):
        if type(name) != str:
            raise TypeError("Bad type name")
        if type(surname) != str:
            raise TypeError("Bad type surname")
        if type(email) != str:
            raise TypeError("Bad type email")
        if not self.validation.validEmail(email):
            raise ValueError("Bad value email")
        if list(filter(lambda client:
                       client["name"] == name and client["surname"] == surname and client["email"] == email,
                       self.ClientStorage.getAllClients())):
            raise Exception("This client exist")
