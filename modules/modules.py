import mymodules
from mymodules import generate_full_name
print(generate_full_name('Adepoju','John'))

print(mymodules.toUpper('Johntizzy'))

from mymodules import toUpper as capitalize
print(capitalize('Omo ologo'))

import sys
# print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
# print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))

# sys.version

# # to exit sys
# sys.exit()
# # To know the largest integer variable it takes
# sys.maxsize
# # To know environment path
# sys.path
# # To know the version of python you are using
# sys.version



# Statistics Module
from statistics import *
# from statistics import *
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
ages.sort()
print(ages)
print(mean(ages))
print(median((ages)))
print(mode((ages)))
print(stdev(ages))      # ~2.3


# Math Modules
import math
print(math.pi)
print(math.floor(math.pi))

print(help(math))

from math import *
print(pi)                  # 3.141592653589793, pi constant
print(sqrt(2))             # 1.4142135623730951, square root
print(pow(2, 3))           # 8.0, exponential
print(floor(9.81))         # 9, rounding to the lowest
print(ceil(9.81))          # 10, rounding to the highest
print(math.log10(100))     # 2

# STRING MODULES
import string
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

# print(help(string))


# RANDOM MODULES
from random import random,randint,randrange
# print(random())
print(random())
print(randint(2,7))
print(randrange(7))


# def generate_random_user_id(length = 6):
#     characters = string.ascii_letters + string.digits
#     return ''.join(random.choice(characters)for _ in range(length))

# print(generate_random_user_id)
import random
import string

def generate_random_user_id(length=6):
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Example usage:
random_id = generate_random_user_id()
print(random_id)


for _ in range(5):
    print(generate_random_user_id())


dig = string.digits
print(dig)


from random import random,randint
from math import floor

print()

def randRgb ():
    rand1 = math.floor(randint(0,255))   
    rand2 = math.floor(randint(0,255))    
    rand3 = math.floor(randint(0,255))
    return ('rgb({},{},{})'.format(rand1,rand2,rand3))

print(randRgb())

def generate_colors (n):

    for _ in range(n):
        print(randRgb())

    # print(randRgb())
 

generate_colors(7)

from random import random
def  generate_hexa_num (length = 6):
    character = string.ascii_letters + string.digits
    return ''.join(random.choice(character) for _ in range(length))

print(generate_hexa_num())

