def make_pizza2(size, *toppings):
    print(f"\nMaking {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f" - {topping}")