message = input("Tell me something and I will repeat it back to you: ")
print(message)

prompt = "If you tell us who you are, we can personalize the meessage you see "
prompt += "\nWhat is your firstname? "
name  = input(prompt)
print(f"\nHello {name}")

prompt = "How many years of experince do you have? "
years = input(prompt)
years = int(years)
if years >= 6:
    print("You are a senior developer!")
else:
    print("You are a junior or mid-level developer")
