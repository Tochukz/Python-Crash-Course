sandwich_orders= ['tuna', 'pickle', 'potato', 'beef']
finished_sandwiches = []
while sandwich_orders: 
    current_sandwich = sandwich_orders.pop()
    print(f"Making {current_sandwich.title()} sandwich")
    finished_sandwiches.append(current_sandwich)

print("----Sandwiches made----")
for sandwich in finished_sandwiches: 
    print(f"{sandwich.title()} sandwich")