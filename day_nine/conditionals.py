# CONDITIONALS STATEMENT

a = 5

# if else
if a > 0:
    print('A is a positive number')
else:
    print('A is a negative number')


# elif - when there are more conditions
if a > 0:
    print('a is a positive number')
elif a < 0:
    print('a is a negative number')
else:
    print('a is zero')


# Nested conditions
if a > 0:
    if(a % 2 == 0):
        print('A is an even number')
    else:
        print('A is an odd number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')


# If Condition and Logical Operators
a = 5
if a > 0 and a % 2 == 0:
    print('A is a positive number and an even number')
elif a > 0 and a % 2 != 0:
    print('A is a positive number and an odd number')
elif a < 0 and a % 2 == 0:
    print('A is a negative number an even number')
elif a < 0 and a % 2 != 0:
    print('A is a negative number an odd number')
elif a == 0:
    print('A is zero')


# EXERCISE
age = int(input())
print(age)

if age > 18:
    print('You are old enough to drive')
elif age < 18:
    remaining_years = 18 - age
    print('You have {} years left to start driving'.format(remaining_years))
    # python conditionals.py


grade = int(input('Enter your grade '))

if grade > 80:
    print('Your grade is an A')
elif grade > 69 and grade < 80:
    print('Your grade is a B')
elif grade > 59 and grade < 70:
    print('Your grade is a C')
elif grade > 49 and grade < 60:
    print('Your grade is a D')
elif grade > 39 and grade < 50:
    print('Your grade is a E')
elif grade < 49:
    print('Your grade is a F')





person = {
    'first_name':'Adepoju',
    'last_name':'John',
    'age':200,
    'country':'Nigeria',
    'skills':['HTML','CSS','JavaScript','Python'],
    'address':{
        'street':'Money',
        'zipcode':'233236'
    }
}

person['city'] = 'Ilorin'
About = '{} {} is {} years old and He lives in {}'.format(person['first_name'],person['last_name'],person['age'],person['city'])

print(About)


my_age = 20
your_age = int(input('Enter your age '))

if your_age < my_age:
    age_difference = my_age - your_age
    print('I am {} years older than you'.format(age_difference))
elif your_age > my_age:
    age_difference = your_age - my_age
    print('You are {} years older than me'.format(age_difference))
elif your_age == my_age:
    print('We are the same age mate')
else:
    print("Invalid input")

