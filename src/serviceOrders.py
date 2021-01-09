from src.baseClients import ClientStorage
from src.baseProducts import ProductStorage
from src.spyPostOrder import SpyPostOrder
from src.baseOrders import OrderStorage


class Order:
    def __init__(self):
        self.ClientStorage = ClientStorage()
        self.ProductStorage = ProductStorage()
        self.SpyPostOrder = SpyPostOrder()
        self.OrderStorage = OrderStorage()

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
            product_in_base = list(filter(lambda product: product["name"] == element, products))
            if not product_in_base:
                raise Exception("This product not exist")
            else:
                id_product = product_in_base[0]["id"]
                if not self.SpyPostOrder.postOrderProduct(id_product):
                    raise Exception("Problem connection in base")
        return self.OrderStorage.postOrder(id_client)

    def deleteOrder(self, id_order):
        orders = self.OrderStorage.getAllOrders()

        if type(id_order) != int:
            raise TypeError("Bad type id order")

        if len(list(filter(lambda order: order["id"] == int(id_order), orders))) != 1:
            raise Exception("This order not exist in data base")
        else:
            return self.OrderStorage.delOrder(id_order)

    def deleteOrderProduct(self, id_order, id_product):
        ordersProducts = self.OrderStorage.getAllOrdersProducts()

        if type(id_order) != int:
            raise TypeError("Bad type order id")

        if type(id_product) != int:
            raise TypeError("Bad type product id")

        if not list(filter(lambda order: order["order_id"] == int(id_order) and order["product_id"] == int(id_product),
                           ordersProducts)):
            raise Exception("This order not exist in data base")
        else:
            return self.OrderStorage.delOrderProduct(id_order, id_product)

    def getProductsInOrder(self, id_order):
        orders = self.OrderStorage.getAllOrders()
        ordersProducts = self.OrderStorage.getAllOrdersProducts()
        products = self.ProductStorage.getAllProducts()

        if type(id_order) != int:
            raise TypeError("Bad type order id")

        if len(list(filter(lambda order: order["id"] == int(id_order), orders))) == 1:
            look_products_id = list(
                filter(lambda order_product: order_product["order_id"] == int(id_order), ordersProducts))
            list_found_products = []
            for product_id in look_products_id:
                found_product = list(filter(lambda product: product["id"] == product_id["product_id"], products))
                list_found_products.append(found_product[0])
            return list_found_products
        else:
            raise Exception("This order not exist in data base")
