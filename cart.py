class ShoppingCart:
    
    def __init__(self):
        self.cart = []

    def add_product(self, product: 'Product'):
        self.cart.append(product)

    def remove_product(self, product_id: str):
        for product in self.cart:
            if product.get_id() == product_id:
                self.cart.remove(product)
                return True       
        return False       
            
    def get_items(self):
        return f'{self.cart}'

    def calculate_total(self):
        total = 0
        for product in self.cart:
            total += product.get_price()

        return total

    def is_empty(self):
        if len(self.cart) == 0:
            return True
        else:
            return False
