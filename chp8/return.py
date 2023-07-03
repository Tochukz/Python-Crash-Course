def get_fullname(firstname, lastname, middlename = ''):
    """Put together fullname given first and last name"""
    if middlename:
        fullname = f"{firstname} {middlename} {lastname}"
    else:
        fullname = f"{firstname} {lastname}"
    return fullname.title()

fullname = get_fullname("chucks", "nwachukwu")
print(f"My name is {fullname}.")

supervisor = get_fullname("Gordon", "Cooper", "John")
print(f"My project supervisor is {supervisor}.")

def make_user(firstname, lastname, age=None):
    person = { 'firstname': firstname, 'lastname': lastname}
    if age:
        person['age'] = age
    return person

new_user = make_user("James", "Cordon", 47)
print(new_user)

another_user = make_user("Kelvin", "Hart")
print(another_user)
