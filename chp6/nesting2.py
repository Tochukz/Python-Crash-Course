# Lists in a dictionary
pizza = {
  'crust': 'Thicks',
  'toppings': ['mushrooms', 'extra cheese']
}
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings: ")
for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {
  'chucks': ['CSharp', 'TypeScript'],
  'chad': ['C++'],
  'clayton': ['PHP', 'JavaScript'],
  'shane': ['Java', 'CSharp'],
  'gordon': ['Delphi', 'Python']
}
for name, languages in favorite_languages.items(): 
    if len(languages) == 1:
        print(f"{name}'s favorite language is {languages[0]}")
        continue
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages: 
        print("\t" + language)
