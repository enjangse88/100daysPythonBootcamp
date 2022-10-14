#!/usr/bin/python3 

import random

random_integer = random.randint(1, 10)
print(random_integer)

#random_float = random.random()
random_float =  random.uniform(0, 5)
round_random = round(random.uniform(0, 5), 2)

print(random_float)
print(round_random)
