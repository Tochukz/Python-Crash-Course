# Exercise 9-1, Exercise 9-2

class Resturant:
    def __init__(self, resturant_name, cuisine_type):
        self.resturant_name =resturant_name
        self.cuisine_type = cuisine_type
    
    def describe_resturant(self):
        print(f"Resturant name: {self.resturant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_resturant(self):
        print("Resturant is now open!")
