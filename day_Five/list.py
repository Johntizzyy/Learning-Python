# Creating a lists
lst = list()
print(lst)

fruits = ["banana","mango","cashew","carrot"]
print(fruits)
print(len(fruits))

listt = ['Adepoju',20,{"name":"John"},True]
print(listt)

first_fruit = fruits[0]
last_fruit = fruits[len(fruits)-1]

print(first_fruit)
print(last_fruit)

first_fruit,second_fruit,third_fruit,*rest = fruits
print(rest)

countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(scandic)


fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # it returns all the fruits
# this will also give the same result as the one above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the first index
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']


fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # it returns all the fruits
orange_and_mango = fruits[-3:-1] # it does not include the last index,['orange', 'mango']
orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']

print(fruits)

# Modifyin lists in python
fruits[0] = "Cashew"
print(fruits)


# Adding an items to the end of a list

fruits.append("Carrot")
print(fruits)

# Inserting item ito a list
# list.insert(index,item)

fruits.insert(4,"lime")
print(fruits)

# Reoving a item from a list
fruits.remove("lime")
print(fruits)

# removing item using pop
fruits.pop()
print(fruits)

# removing item using del
del fruits[2]
print(fruits)

# Clearng an item list
# fruits.clear()
# print(fruits)

# Copying a list
fruits_copy = fruits.copy()
print(fruits_copy)

# Joining s list
positive_int = [1,2,3,4,5]
zero = [0]
negative_int = [-1,-2,-3,-4,-5]

print(negative_int + zero + positive_int)

# Joining using extend
positive_int.extend(negative_int)
print(positive_int)

num = [8,2,3,3,4,4,4]
print(num.count(4))


# Finding index of an item
print(num.index(4))
print(num[4])

# Reversing a list
num.reverse()
print(num)

# sorting a list
num.sort()
print(num)

num.sort(reverse = True) #Ascending
print(num) # Descending


## ## Challenge
companies = []
print(companies)

companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
# companies + company

# companies = (companies + (company))
print(companies)

print(companies[2].upper())
companies.insert(3,"Johntizzy")
# print(companies.join(','))

print("Facebook" in companies)
print(companies.sort())
print(companies.sort(reverse=True))
print(companies[0:3])
print(companies)
print(companies[-3:])
companies.remove("IBM")
companies.pop()
companies.clear()
print(companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

fullstack = front_end + back_end
print(fullstack)
fullstack_copy = fullstack.copy()
others = ["python","SQL","Redux"]
fullstack_copy = fullstack_copy + others
print(fullstack_copy)



#Exercise level two

# Find the min and max
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)

min_age = ages[0]
max_age = ages[len(ages) -1]
print(min_age)
print(max_age)

reverse_ages = ages.copy()
reverse_ages.sort(reverse= True)
print(reverse_ages)
# print(len(ages)/2)

median = (ages[int(len(ages)/2)] + reverse_ages[int(len(ages)/2)]) / 2
print(median)

average_age = sum(ages)/len(ages)
print(average_age)

range = max_age - min_age
print(range)

print(abs(min_age - average_age) is abs(max_age - average_age))
print(max_age - average_age)

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
ch,Ru,US,*scandic = countries

print(scandic)

## Completed thi\s on the 9th of June 2024