from stack import Stack 
from cart import ShoppingCart
from order_queue import OrderQueue
from order import Order
from customer import Customer
from product import Product

class Store:
    
    def __init__(self):
        self.products = []
        self.customers = []
        self.orders = []
        self.order_queue = OrderQueue()
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
        '''Turn the customer's cart into a queued Order and clear the cart.'''
        customer= self.find_customer(customer_id)
        if customer is None:
            return None
        cart= customer.get_cart()
        if cart.is_empty():
            return None 
        self.order_counter +=1
        order = Order(f'O{self.order_counter}', customer, list(cart.get_items()))
        self.orders.append(order)
        self.order_queue.enqueue(order)
        cart.clear()
        return order


    def process_next_order(self):
        """Dequeue the oldest waiting order, mark it PROCESSING, and record it."""

        order = self.order_queue.dequeue() 
        if order is None:
            return None
        order.set_status("PROCESSING")
        self.processed_order.push(order)
        return order
        


    def get_order_history(self):
        """Return processed orders, newest first, leaving the stack unchanged."""

        history=[]
        while not self.processed_order.is_empty():
            history.append(self.processed_order.pop())
        for order in reversed(history):
            self.processed_order.push(order)
        return history 






