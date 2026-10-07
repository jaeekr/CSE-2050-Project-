from product import Product
from customer import Customer

class Order:

    def __init__(self, order_id: str, customer: Customer, items: list[Product]):
        '''initialized an Order object with object_id, customer and a list of products as well as a order status'''
        self.order_id = order_id
        self.customer = customer
        self.purchased_items = items
        self.status = 'PENDING'

    def get_id(self):
        '''returns order id'''
        return self.order_id

    def get_customer(self):
        '''returns order customer'''
        return self.customer

    def get_status(self):
        '''return status of order'''
        return self.status

    def get_items(self):
        ''' return list of items'''
        return self.purchased_items

    def set_status(self, new_status: str):
        '''takes a new status for the order and makes sure it is one of three valid order status and then updates the order status to the valid input'''
        valid = ['PENDING', 'PROCESSING', 'COMPLETED']
        if new_status not in valid:
            raise ValueError('Not a valid status')
        
        self.status = new_status

    def calculate_total(self):
        '''calculates total amount of money in the items list of a Customer by iterating through it and returning a float'''
        total = 0.0

        for i in self.purchased_items:
            total += i.get_price()

        return total

        return total
