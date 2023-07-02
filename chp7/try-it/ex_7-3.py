number_string = input("Enter a number and I will tell you if it is a multiple of 10 or not: ")
number = int(number_string)
if number > 10 and number % 10 == 0: 
    print(f"{number} is a multiple of 10")
else:
    print(f"{number} is NOT a multiple of 10")