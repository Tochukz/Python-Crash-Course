from resturant import Resturant

resturant1 = Resturant("Mega Chiken", "Pepper chiken")
print(f"Resturant 1: {resturant1.resturant_name}")
print(f"Cuisine 1: {resturant1.cuisine_type}")
resturant1.describe_resturant()
resturant1.open_resturant()
print()

resturant2 = Resturant("Sweet Sensation", "Chiken Pie")
print(f"Resturant 2: {resturant2.resturant_name}")
resturant2.describe_resturant()
print() 

resturant3 = Resturant("MacDonal", "Bugger")
resturant3.describe_resturant()