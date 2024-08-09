# LIST COMPREHENSION
'''List comprehension in Python is a compact way of creating a list from a sequence.
It is a short way to create a new list. List comprehension is considerably faster
than processing a list using the for loop.'''

# Changing a string to a list of characters
# syntax
# [i for i in iterable if expression]# syntax

language = 'Python'
lst = list(language)
print(lst)

lst = [i for i in language]
print(lst)
print([i for i in language])

# Generating numbers
one_to_ten = [i for i in range(11)]
print(one_to_ten)

# Doing mathematical operation
squares = [i * i for i in range(11)]
print(squares)

# Making list of tuples
numbers = [(i,i * i) for i in range(11)]
print(numbers)

# List comprehension can be combined with if expression
even_numbers = [i for i in range(11) if i % 2 == 0]
print(even_numbers)

odd_numbers = [i for i in range(11) if i % 2 != 0]
print(odd_numbers)

# Filter numbers: let's filter out positive even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_num = [i for i in numbers if i > 0]
print(positive_num)

neg_num = [i for i in numbers if i < 0]
print(neg_num)

# Flattening a three dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [i for row in list_of_lists for i in row]
print(flattened_list)


# Lambda function
square = lambda x: x * x
print(square(5))

# Named function
def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 3))     # 5
# Lets change the above function to a lambda function
add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))    # 5

# Self invoking lambda function
(lambda a, b: a + b)(2,3) # 5 - need to encapsulate it in print() to see the result in the console

square = lambda x : x ** 2
print(square(3))    # 9
cube = lambda x : x ** 3
print(cube(3))    # 27

# Multiple variables
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3)) # 22


# Lambda Function Inside Another Function
def power(x):
    return lambda n: x ** n
print(power(2)(5))


# EXERCISES
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
even_num = [i for i in numbers if i%2 == 0 and i > 0]
print(even_num)


list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

l_o_l = [i for row in list_of_lists for i in row]
print(l_o_l)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# output
l_o_l = [i for row in names for i in row]
print(l_o_l)
# ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']