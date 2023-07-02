topping=input("\nType 'quit' to end the program. \nWhat do you want ontop your pizza: ")

while topping != 'quit':
   message = f"\nOkay, we will add {topping}, what else? "
   if topping == 'quit':
       break
   topping=input(message)