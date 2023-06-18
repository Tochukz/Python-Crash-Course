magicians  = ['alice', 'david', 'caroline']
for magician in magicians: 
    print(f"{magician.title()}, that was a great trick.")
    print(f"I can't wait to see your next trick, {magician.title()}\n")
print("Thank you everyone, that was a great magic show!")

# the range() function
for value in range(1, 5): 
    print(value) 

# range with single argument
for value in range(6):
    print(value)

# Create a list from a range
ten_numbers = list(range(1, 11))
print(ten_numbers)

# list with step argument
odd_numbers = list(range(1, 11, 2))
even_numbers = list(range(2, 11, 2))
print(f"Odd numbers: {odd_numbers}")
print(f"Even numbers: {even_numbers}")

# List of square numbers
square_numbers1 = []
for value in range(1, 11): 
    square_numbers1.append(value ** 2)
print(f"Square numbers 1: {square_numbers1}")

# List Comprehension: List of suare number using list comprehension
square_numbers2 = [value ** 2 for value in range(1, 11)]
print(f"Sqaure numbers 2: {square_numbers2}")

# Statistics functions
scores = [78, 91, 82, 67, 95, 54, 71]
max_score = max(scores)
min_score = min(scores)
total_score = sum(scores)
print(f"Max score: {max_score}")
print(f"Min score: {min_score}")
print(f"Total score: {total_score}")