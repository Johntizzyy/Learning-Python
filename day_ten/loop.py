count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)


# Break and Continue - Part 1

while count < 10:
    if count == 7:
        count = count + 1
        continue
    count += 1
    print(count)



numbers = (0,1,2,3,4,5)

for number in numbers:
    print(number)

language = 'Python'
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])

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

for key in person:
    print(key)

for key,value in person.items():
    print(key,value)

for number in numbers:
    print(number)
    if number == 3:
        break

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')

alphabet = ('a','b',"c",'d')

for abc in alphabet:
    # print(abc)
    if abc == 'b':
        continue
    print(abc)


# The range function
lst = list(range(5,11))
print(lst)

st = list(range(0,100,9))
print(st)


for key in person:
    if 'skills' == key:
        for skill in person['skills']:
            print(skill)

for i in range(11):
    print(i)
else:
    print('loop ends at', i)

for i in range(5):
    pass


# Exercise 

count = 0
while count < 10:
    print(count)
    count = count + 1

while count < 10:
    count += 1
    # print(count)
    if count == 7:
        break
    print(count)


for i in range(11):
    print(i)

lst = list(range(11))
lst.sort(reverse=True)

print(lst)

for num in lst:
    print(num)

numbers = list(range(11))
print(numbers)

for num in numbers:
    print('{} * {} = {}'.format(num,num,num * num))

libraries = ['Python', 'Numpy','Pandas','Django', 'Flask']

for library in libraries:
    print(library)
    pass

for i in range(0,100,2):
    print(i,'is an even number')
    pass

for i in range(0,100):
    if i%2 != 0:
        print(i,'is an odd number')
        pass

numbers = tuple(range(101))

print('The sum of all numbers from 0 to 100 are',sum(numbers))

even_num = tuple(range(0,101,2))
print('The sum of all even numbers from 0 to 100 is',sum(even_num))


numbers = list(numbers)
for num in numbers:
    numbers.sort(reverse = True)
    print(num)