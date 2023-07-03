def describe_pet(animal_name, pet_name): 
    """Describes a pet"""
    print(f"{pet_name.title()} is a {animal_name.title()}")

describe_pet("dog", "jefa")
describe_pet("cat", "lucy")
# using keyword arguments 
describe_pet(animal_name="dog", pet_name="Jimi")
describe_pet(pet_name="piona", animal_name="cat")

def describe_cell(device_model, device_brand="Samsung"):
   print(f"I use a {device_brand} {device_model} device")

describe_cell("A23")
describe_cell("7-Plus", "IPhone")

# Variable number of parameters
def make_pizza(*toppings): 
    """Print the list of toppings that have been requested"""
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza2(size, *toppings):
    print(f"\nMaking {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f" - {topping}")

make_pizza2(16, 'pepperoni')
make_pizza2(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using Arbitrary Keyword Arguments
def make_profile(firstname, lastname, **profile):
    profile['firstname'] = firstname
    profile['lastname'] = lastname
    return profile

def show_profile_info(profile):
    for key, value in profile.items():
        print(f"{key} = {value}")
profile = make_profile('Chucks', 'Nwachukwu', position='Cloud Architect', salary='R120,000', city='Cape Town')
show_profile_info(profile)
