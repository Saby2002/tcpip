# Objective to create a laptop class with attributes like Brand Name, Model Name, Price. 
# Create how objects/instance of your laptop class. 

#!/usr/bin/venv python

class Laptop: 
    def __init__(self, brand_name, model_name, price):
        # Instance Variable
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price

laptop1 = Laptop('Dell', 'R720', 30000)
laptop2 = Laptop('Apple', 'Pro', 100000)
laptop3 = Laptop('HP', 'Inspiron', 40000)

print(laptop1.brand_name)
