# Nesting 1: Dictionaries in a list
person_1 = {'name': 'Uche', 'city': 'Lagos'}
person_2 = {'name': 'Chucks', 'city': 'Cape Town'}
person_3 = {'name': 'Oluchi', 'city': 'Toronto'}
people = [person_1, person_2, person_3]
for person in people: 
    print(person)

animals = []
for item in range(20):
  animal = {'name': 'Sheep', 'habitat': 'Land'}
  animals.append(animal)

for animal in animals[:5]: 
   print(animal)
print(':::')

print(f"Total animals = {len(animals)}")