class Bakery:
    # Constructor to initialize Bakery product details
    def __init__(self,id,name,price,quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
    
    # String representation of the object (used when printing the object)
    def __str__(self):
        return str(self.id) + " , " + self.name + " , " + str(self.price) + " , " + str(self.quantity)
    
    