from src.dataOrders import OrdersData
from src.dataProductsOrders import OrdersProductsData


class SpyPostOrder(object):
    def __init__(self, status=True):
        self.connect = status
        self.orders = OrdersData().orders
        self.ordersProducts = OrdersProductsData().productsOrders
        self.post_order_product = []

    def postOrderProduct(self, id_product):
        self.post_order_product.append({"product_id": id_product, "order_id": len(self.orders) + 1})
        return self.connect
