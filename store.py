from stack import Stack 
from cart import ShoppingCart
from orderqueue import OrderQueue

class Store:
    
    def __init__(self):
        self.products = []
        self.customers = []
        self.empty_orders =[]
        self.waiting_orders = OrderQueue()
        self.processed_order = Stack()
        self.order_counter = 0


    def add_product(self, product: 'Product') -> bool:
        if self.find_product(product.id) is None:
            self.products.append(product)
            return True
        return False

    def find_product(self, product_id: str) -> 'Product':
        for p in self.products:
            if p.id == product_id:
                return p
        return None

    def add_customer(self, customer: 'Customer') -> bool:
        if self.find_customer(customer.id) is None:
            self.customers.append(customer)
            return True
        return False

    def find_customer(self, customer_id: str) -> 'Customer':
        for c in self.customers:
            if c.id == customer_id:
                return c
        return None

    def find_order(self,order_id:str):
        if order_id in self.waiting_orders or self.processed_order:
            return order_id
        else:
            return None

    def get_order(self):
        wo = list(self.waiting_orders)
        po = list(self.processed_order)
        orders = wo + po
        return orders
    
    def checkout(self,customer_id:str):
        self.empty_orders =ShoppingCart(customer_id) # I dont think this is right, but Im confused on what its asking
        self.waiting_orders.enqueue(self.empty_orders)
        ShoppingCart(customer_id).clear()
        



