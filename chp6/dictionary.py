alien = { 'color': 'green', 'points': 5}
print(alien)
print(alien['color'])
print(alien['points'])

alien['x_position'] = 0
alien['y_position'] = 25
print(alien)

person = {}
person['name'] = 'Chukwuka'
person['city'] = 'Cape Town'
print(person)
person['city'] = 'Joburg'
print(person)

del person['city']
print(person)
# Throws an error because city does not exist
# print(person['city']) 
# get key and provide default value if key not found
print(person.get('city', 'no city defined'))
# Will return None since the key does not exist. None is a special value
print(person.get('problem'))