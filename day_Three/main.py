## OPERATORS 

"""
Assignment operation
Arithmentic operators
"""
print("Addition:",5 + 2)
print(len("addition"))

a = 10
b = 5

sum = a + b
sub = a - b
exp = a ** b

print(a, "+" ,b, "=", sum)
print(a, "-" ,b, "=", sub)
print(a, "**" ,b, "=", exp)
print('a + b',sum)


##Area of a circle
r = 10
area_of_triangle = 3.14 * r ** 2
print(area_of_triangle)

##Area of rectangle
length = 10
width = 10
area_of_rect = length * width
print(area_of_rect)

#Weight of an object
mass = 75
gravity = 9.8
weight = mass * gravity
print(int(weight),'N')


##Comparison Operators
print(3 < 2)
print(3 > 2)
print(3 <= 2)
print(3 >= 2)
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False


# is: Returns true if both variables are the same object(x is y)
# is not: Returns true if both variables are not the same object(x is not y)
# in: Returns True if the queried list contains a certain item(x in y)
# not in: Returns True if the queried list doesn't have a certain item(x in y)
print(int(weight),'N')
print(a is 10)
print(a is not 10)
print('J' in 'Johntizzy')
print('J' not in 'Johntizzy')
print(2 ** 2 is 4)

# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))


## CHALLENGE
age = 20
height = 6.7
complex_variable = 2 + 2j


# Area of a triangle
# base = int(input("Enter your base"))
# height = int(input("Enter yor height"))
# area_of_triangle = 1/2 * base * height
# print("The area of the triangle",area_of_triangle)

# Perimeter of a triangle
# a = int(input('Enter side a '))
# b = int(input('Enter side b '))
# c = int(input('Enter side c '))
# perimeter = a + b + c
# print('The perimeter of the triangle is',perimeter)

#Area and perimeter of a rectangle
# length = int(input('Enter length '))
# width = int(input('Enter width '))

# area = length * width
# perimeter_of_rect = 2 * area
# perimeter_of_rectangle = 2 * (length * width)

# print('The area of the rectangle is',area)
# print('The perimeter of the rectangle is',perimeter_of_rect)
# print('The perimeter of the rectangle is',perimeter_of_rectangle)
# (2, 2) and point (6,10)
x1 = 2
y1 = 2
x2 = 6
y2 = 10
slope = (y2 - y1) / (x2 - x1)
print('The slope is',slope)

x = -3
y = x**2 + 6 * x + 9
print('y is',y)

print(not len('python') is len('dragon'))

print('on' not in 'python' and 'dragon')
print('jargon' in 'I hope this course is not full of jargon')
print(not('on' in 'python'))
print(9.8 is 10)

