from resturant import Resturant

class IceCreamStand(Resturant): 
    def __init__(self):
        self.flavors = ['Pinnapple', 'Milk', 'Plain', 'Strawberry']

    def list_flavors(self): 
        print("Flavors: ")
        for flavor in self.flavors: 
            print(f"\t{flavor}")
