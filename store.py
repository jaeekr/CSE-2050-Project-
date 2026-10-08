from stack import Stack 
from cart import ShoppingCart
from order_queue import OrderQueue
from order import Order

class Store:
    
    def __init__(self):
        self.products = []
        self.customers = []
        self.orders = []
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

    def find_order(self, order_id:str):
        for order in self.orders:
            if order.get_id() == order_id:
                return order
        return None

    def get_orders(self):
        return self.orders
    
    def checkout(self,customer_id:str):
        self.orders = ShoppingCart(customer_id) 
        self.waiting_orders.enqueue(self.orders)
        self.orders.clear()
        if customer_id not in self.customers or self.orders.is_empty() is True:
            return None 

    def process_next_order(self):
        z=OrderQueue().dequeue() 
        y=Order(z).set_status("PROCESSING")
        self.processed_order().push(y)
        if self.waiting_orders.is_empty():
            return None 


    def get_order_history(self):
        while self.processed_order.is_empty is False:
            return self.processed_order.peek()




        



