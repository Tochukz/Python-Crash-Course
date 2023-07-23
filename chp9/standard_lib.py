from random import randint 
from random import choice

rand_num = randint(1, 10)
print(f"Random int: {rand_num}")

players = ['Lu Ken', 'Jade', 'Jax', 'Kintana', 'Noob Cybooy', 'Scorpion']
player = choice(players)
print(f"Random player {player}")