cars=['audi','bmw','subaru','toyota']
for car in cars: 
    if (car == 'bmw'):
        print(car.upper())
    else: 
        print(car.title())


hour=13
if hour < 12: 
    print("Good morning")
elif hour > 12:
    print("Good afternoon!")
else:
    print("Good evening")

langs = []
if langs:
    for lang in langs:
        print(lang + "\n")
else: 
    print("Please list your programming languages")


available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings: 
    if requested_topping in available_toppings: 
        print(f"Adding {requested_topping}");
    else: 
        print(f"Sorry, we don't have {requested_topping}")

print("\nFinished making your pizza!")