# list comprehension
import random

dices = []
for i in range(5):
    dices.append(random.randint(1,6))
print(dices)

dices =[random.randint(1,6) for i in range(5)]
print(dices)
