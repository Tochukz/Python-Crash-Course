names = ['James', 'Steven', 'Maxwell', 'Kelvin', 'Peter']
print(names[0:3]) # First to third name
print(names[2:5]) # Third to fifth name

print(names[:4])  # first to fourth name
print(names[2:])  # third to last name
print(names[-2:]) # last two names

print(names[1:4:2])

for value in names[1:4] : 
    print(value)

my_foods = ['Bread', 'Egg']
friend_foods = my_foods[:] # Make a copy of my_foods
my_foods.append('Milo')
friend_foods.append('Hot Choclate')
print(f"my food: {my_foods}")
print(f"friend_food: {friend_foods}")