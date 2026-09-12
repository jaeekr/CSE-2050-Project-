class Customer:

    def __init__(self, _id:str, name:str):
            self.id= id
            self.name= name
            self.cart= []

    def get_id(self):
            return self.id
    
    def get_name(self):
            return self.name
    
    def get_cart(self):
            return self.cart