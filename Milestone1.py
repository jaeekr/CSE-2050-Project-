class Product:

    def __init__(self, id:str, name:str, price:float):
        self.id=id 
        self.name=name
        self.price= price

        
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name

    def get_price(self):
        return self.price


from cart import ShoppingCart
class Customer:

    def __init__(self, id:str, name:str):
            self.id= id
            self.name= name
            self.cart = ShoppingCart()

    def get_id(self):
            return self.id
    
    def get_name(self):
            return self.name
    
    def get_cart(self):
            return self.cart

class ShoppingCart:
    
    def __init__(self):
        self.items: list[Product] = []

    def add_product(self, product: 'Product'):
        self.items.append(product)

    def remove_product(self, product_id: str):
        for product in self.items:
            if product.get_id() == product_id:
                self.items.remove(product)
                return True       
        return False       
            
    def get_items(self):
        return self.items

    def calculate_total(self):
        total = 0
        for product in self.items:
            total += product.get_price()

        return total

    def is_empty(self):
        return len(self.items) == 0

class Store:
    
    def __init__(self):
        self.products = []
        self.customers = []

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



