person = {
  'firstname': 'Chucks',
  'lastname': 'Nwachukwu',
  'position': 'Cloud Architech',
  'salary': 'R120'
}

for key, value in person.items(): 
    print(f"\nKey: {key}")
    print(f"Value: {value}")

for key in person.keys():
  print(key)

for key in person: 
   print(key)

favorite_languages = {
   'tochi': 'JavaScript',
   'chucks': 'CSharp',
   'tochukwu': 'Java',
   'tKay': 'PHP',
   'chuks': 'JavaScript',
   'clayton': 'PHP',
   'shane': 'CSharp',
}
special_guys = ['tochukwu', 'chucks']
for name in favorite_languages.keys(): 
   print(f"Hi {name.title()}")
   if name in special_guys: 
      language = favorite_languages[name].title()
      print(f"\t{name.title()}, so you love {language}")

if 'tcee' not in favorite_languages.keys(): 
   print("\nHi TCee, please take the our poll!")

for name in sorted(favorite_languages.keys()): 
   print(f"{name.title()}, thank you for taking the pool.")

print("\nLooping the values: ")
for lang in favorite_languages.values(): 
   print(lang)

# A set is a collection in which each item must be unique
print("\nUnique Lamguages: ")
for lang in set(favorite_languages.values()): 
   print(lang)