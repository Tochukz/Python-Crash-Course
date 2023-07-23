# Exercise 9-3

class User: 
    def __init__(self, firstname, lastname):
        self.firstname = firstname 
        self.lastname  = lastname 

    def describe_user(self):
        print(f"Firstname: {self.firstname}")
        print(f"Lastname: {self.lastname}")

    def greet_user(self):
        print(f"Hi {self.firstname}!")
