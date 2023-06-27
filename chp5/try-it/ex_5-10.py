current_users = ['Admin', 'chucks', 'James', 'CHARITY', 'PEter']
new_users = ['ada', 'chucks', 'janne', 'charlce', 'peter']
current_users_copy = current_users[:]

for i, user in enumerate(current_users_copy):    
    current_users_copy[i] = user.lower()
    print(i, current_users_copy[i])

for user in new_users: 
    if user in current_users_copy: 
        print(f"{user} is unavailable. Please enter a new username.")
    else:
        print(f"{user} is available!")
        