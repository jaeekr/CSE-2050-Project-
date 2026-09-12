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