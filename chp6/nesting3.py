# Dictionaries in Dictionary
users = {
  'chucks': {
    'firstname': 'chucks',
    'lastname': 'nwachukwu',
    'location': 'cape town'
  },
  'shane': {
    'firstname': 'shane',
    'lastname': 'peters',
    'location': 'joburg'
  },
  'clayton': {
    'firstname': 'clayton',
    'lastname': 'james',
    'location': 'east london'
  }
}
for username, user in users.items(): 
    print(f"\nUsername: {username}")
    fullname = f"{user['firstname'].title()} {user['lastname'].title()}"
    location = user['location'].title()

    print(f"\tFullname: {fullname}")
    print(f"\tLocation: {location}")
    
