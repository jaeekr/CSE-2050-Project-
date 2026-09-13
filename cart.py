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
        if len(self.items) == 0:
            return True
        else:
            return False
