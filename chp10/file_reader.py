# Python will automatically close the file when the with block finish executing 
with  open('pi_digits.txt') as file_object:
    content = file_object.read()
print(content)