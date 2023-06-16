bicycles=['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[1].title())
print(bicycles[-1]) # -1 is index for last element
print(bicycles[-2].title()) # index -2 is second item from the last

bicycles[0]="double-pedal"
print(bicycles)

bicycles.append('ducati')
print(bicycles)

animals=[]
animals.append('dog')
animals.append('goat')
animals.append('sheep')
animals.append('zebra')
animals.append('donkey')
print(animals)

animals.insert(0, 'ram')
print(animals)

del animals[1]
print(animals)

lastAnimal = animals.pop()
print(f"Last animal was {lastAnimal}")
print(animals)

secondAnimal = animals.pop(1)
print(f"The second animal was {secondAnimal}")
print(animals)

# The remove() method deletes only the first occurrence of the value you specify
animals.remove('sheep')
print(animals)

bicycles.sort()
print(bicycles)

bicycles.sort(reverse=True)
print(bicycles)

# unlick the sort() function that sorts a list in place, the sorted() function sorts and return a copy of the list
computers = ['HP', 'Dell', 'MacBook', 'Asus', 'Lenovo']
print(computers)
print(sorted(computers))
print(sorted(computers, reverse=True))
print(computers)

computers.reverse()
print(computers)

print(len(computers))

