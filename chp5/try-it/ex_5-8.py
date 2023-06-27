usernames = ['admin', 'chucks', 'james', 'charity', 'peter']
for name in usernames: 
    if name == 'admin':
        print(f"Hello {name.title()}, would you like to see a status report?")
    else: 
        print(f"Hello {name.title()}, thank you for logginh in again.")