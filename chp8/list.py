def print_models(unprinted_models, completed_models): 
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_models: 
        current_model = unprinted_models.pop()
        print(f"Printing model {current_model}")
        completed_models.append(current_model)

def show_completed(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed!")
    for model in completed_models:
        print(f"{model}")

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
# print_models(unprinted_designs, completed_models)
print_models(unprinted_designs[:], completed_models) # Uses a copy of unprinted_designs for the first argument
show_completed(completed_models)

print(unprinted_designs)