
responses = {}
is_active = True
while is_active: 
    name = input("What is your name? ")    
    language = input("What is you favorite programming language? ")
    responses[name] = language
    take_poll = input("Would you like someone else to take the poll? yes or no: ")
    if take_poll == 'no':
        is_active = False

print("\n----Polling results----")
for name, lang in responses.items(): 
    print(f"{name.title()}'s favorite programming language is {lang}")