unconfirmed_users = ['jeremy', 'jacob', 'jackson']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f'Verfying {current_user.title()}...')
    confirmed_users.append(current_user)

print("\nHere are the confirmed users: ")
for user in confirmed_users: 
    print(user.title())

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets: 
    pets.remove('cat')
print(pets)