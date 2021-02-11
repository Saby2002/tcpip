# Apply flat 10% discount on each Laptop Brands.

#/usr/bin/venv python 

class Laptop:
    discount_percent = 10
    def __init__(self, brand, model_name, price):
        # Instance Variable
        self.brand = brand
        self.name = model_name
        self.price = price
        self.laptop_name = brand + ' ' + model_name
    
    def apply_discount(self):
        # Self.Price
        discount_price = (Laptop.discount_percent/100)*self.price
        return self.price - discount_price

laptop1 = Laptop('hp', 'au114tx', 63000)
laptop2 = Laptop('Apple', 'Pro', 100000)


#print(laptop2.apply_discount())
print(laptop1.apply_discount())
        
        
