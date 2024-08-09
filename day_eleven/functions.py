# Functions without parameters

def generate_full_name():
    first_name = 'Adepoju'
    last_name = 'John'
    full_name = first_name + ' ' + last_name
    print(full_name)

generate_full_name()

def generate_full_name():
    first_name = 'Adepoju'
    last_name = 'John'
    full_name = first_name + ' ' + last_name
    return(full_name)

print(generate_full_name())


# Functions with parameters

def greetings (name):
    message = name + ',you\'re welcome'
    print(message)
    pass
greetings('John')

def square_number(x):square = x * x; return square
print(square_number(2))    

def weight_of_object (mass, gravity):
    weight = str(mass * gravity) + 'N'
    print(weight)
weight_of_object(100,9.8)


# Passing Arguments with Key and Value
def sum_of_two_numbers(num1,num2):
    total = num1 + num2
    return ('The sum of {} and {} is {}'.format(num1,num2,total))

print(sum_of_two_numbers(num1=2,num2=3))

def is_even(num):
    # talk
    if num % 2 == 0:
        # print('Even')
        return True
    return False
    
print(is_even(10))
print(is_even(7))


def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))

def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Johntizzy'))

def sum_all_nums(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

print(sum_all_nums(2,3,4,5))

def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
print(generate_groups('Team-1','Asabeneh','Brook','David','Eyob'))

# Functiona as parameter of another funtion
#You can pass functions around as parameters
def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27





# EXERCISES

def area_of_circle(r):
    area = 3.142 * r ** 2
    print('{:.4f}'.format(area))

area_of_circle(20.5)

num = 5.0
print(type(num) is float)

def add_all_num(*numbers):
    total = 0
    for number in numbers:
        if type(number) == int:
            total += number
            print (total)
        else:
            return ('Invalid input')
    return total


(add_all_num)(2,3,4,5)

def convert_celsius_to_fahrenheit(c):
    conversion = str((c * 9/5) + 32)
    return conversion + 'F'

print(convert_celsius_to_fahrenheit(23))


def reverse_list(listt):
    listt.sort(reverse= True)
    return listt

def reverse_list1(listt):
    final = []
    for word in listt:
        final.append(word)
    return final

print(reverse_list([1,2,3,4,5]))

alp = ['a','b','c']
alp.sort(reverse=True)
print(alp)
# alp.swapcase()
# print(alp)

def capitalize_list (word_list):
    capitalize = []
    for word in word_list:
        wo_rd = word.upper()
        capitalize.append(wo_rd)
    print(capitalize)

capitalize_list(alp)

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
food_staff.append("item")
print(food_staff)


def add_item(listtt,item):
    result = listtt.append(item)
    print(result)

(add_item(food_staff, 'Meat'))


def sum_all_numbers(n):
    numbers = list(range(n + 1))
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all_numbers(100))

d = ()
print( d is ())

def is_empty (*args):
    if args == ():
        print('Your input is Empty')
    else:
        print('your is input {}'.format(args))
is_empty(3)