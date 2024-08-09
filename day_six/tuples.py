# Tuples

# Ctreating tuple

empty_tuple = tuple()
empty_tuple = ()

fruits = ('banana','apple','mango')
print(fruits)

first_fruit = fruits[0]
print(first_fruit)

# negative index starts from -1
first_fruit = fruits[-3]
print(first_fruit)


## SLicing a tuple
# Syntax
all_items =  fruits[0:4]        # all items
all_items =   fruits[0:]     # all items
middle_two_items = fruits[1:3] # does not include item at index 2

print(middle_two_items)

#Changing tuple to list
list_fruits = list(fruits)
print(list_fruits)

# Joining tuples together
boy_name = ('John','Dave','Samson')
girl_name = ('Lizzie','Joy','Jemimah')

all_names = boy_name + girl_name
print(boy_name)
print(girl_name)
print('John' in boy_name)
print(all_names)

print(all_names[1:4])

first_three_names = all_names[3:]
last_three_names = all_names[-6:-2]

print(first_three_names)
print(last_three_names)
# Delete tuple
del all_names

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)


