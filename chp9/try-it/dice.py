from random import randint 

class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        rand_num = randint(1, self.sides)
        print(rand_num)
