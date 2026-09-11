class Product:

    def __init__(self, product_id:str, name:str, price:float):
        self.product_id=product_id, 
        self.name=name
        self.price= price

        
    def get_id(self):
        return f'{self.product_id}'
    
    def get_named(self):
        return f'{self.name}'

    def get_price(self):
        return f'{self.price}'

class Customer:

    def __init__(self, customer_id:str, name:str):
            self.customer_id= customer_id
            self.name= name
            self.cart=[]

    def get_id(self):
            return f'{self.customer_id}'
    
    def get_name(self):
            return f'{self.get_name}'
    
    def get_cart(self):
            return f'{self.cart}'

class ShoppingCart:
    
    def __init__(self):
            pass

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



