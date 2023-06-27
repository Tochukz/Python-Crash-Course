usernames = ['admin', 'chucks', 'james', 'charity', 'peter']
# usernames = []
if usernames:
    for name in usernames:
        if name == 'admin':
            print(f"Hello {name}, do you want to see some reports?")
        else:
            print(f"Hello {name}, thank you for logging in again.")
else:
    print("We need some users")