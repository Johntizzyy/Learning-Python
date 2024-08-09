# This is single line comment 
"""This is a multi line comment
if it's not assigned to a variable"""


# Data types in python
"""
Number - Integar(positive, zero and negative), float(decimal) 

String -
'Johntizzy'
'Nigeria'
'Python'
'I love teaching'

Booleans 

    True  #  Is the light on? If it is on, then the value is True
    False # Is the light on? If it is off, then the value is False

List

[0,1,2,3,4,5,6,7] - List of numbers
['John','Oluwatobi','Peace'] - List of names

Dictionary - A Python dictionary object is an unordered collection of data in a key value pair format.

{
    'first_name':'Adepoju',
    'last_name':'John',
    'age':20,
    'is_married':False,
    'skills':['Javascript,'python']
}
"""
{
    'first_name':'Adepoju',
    'last_name':'John',
    'age':20,
    'is_married':False,
    'skills':['Javascript','python']
}

""" Tuple
A tuple is an ordered collection of different data types like list but tuples
 can not be modified once they are created. They are immutable. 

('Johntizzy', 'Pawel', 'Brook', 'Abraham', 'Lidiya') # Names

Set
A set is a collection of data types similar to list and tuple. Unlike list and tuple,
 set is not an ordered collection of items.
 Like in Mathematics, set in Python stores only unique items. 
 {2, 4, 3, 5}
{3.14, 9.81, 2.7} # order is not important in set """

# Day 1 - 30DaysOfPython Challenge

print(2 + 3)             # addition(+)
print(3 - 1)             # subtraction(-)
print(2 * 3)             # multiplication(*)
print(3 / 2)             # division(/)
print(3 ** 2)            # exponential(**)
print(3 % 2)             # modulus(%)
print(3 // 2)            # Floor division operator(//)

# Checking data types
print(type(10))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Asabeneh'))  # String
print(type([1, 2, 3]))   # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple

print("This is my first python code")
print("This is soo easy")


#Exercises

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(3-4j))
print(type(['John','dave']))
print(type(('John','Dave')))



### Find an Euclidian distance between (2, 3) and (10, 8)

p1 = 2
q1 = 3
p2 = 10
q2 = 8

euclidean_distance = ((p2 - p1) ** 2 + (q2 - q1) ** 2)
print(len(euclidean_distance))

"""
False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield

"""