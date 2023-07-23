from dice import Dice

my_dice = Dice()
count = 6
while count > 0:
    my_dice.roll_die()
    count -= 1

print()

my_dice_10 = Dice(10)
count = 10
while count > 0: 
    my_dice_10.roll_die()
    count -= 1