empty_set = set()

print(empty_set)

## set of fruits
fruits = {"mango","cashew","pawpaw","mango"}
fruits.add('lemon') # Adding one fruits
fruits.update(['friut1','fruits2'])

print(len(fruits))

print('mango' in fruits)

# fruits.clear()  - To clear all the items in a set
# del fruits - To delete the set gangan

print(fruits)

## Lits to set
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
print(set(lst))


## Joining sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}

st3 = st2.union(st1)
print(st3)  

## Today's date is 24/06/2024

## Intersection
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}

print(st1.intersection(st2))
print(st2.difference(st1))

## Finding symmetric differnce
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
print(st2.symmetric_difference(st1)) # {'item1', 'item4'}


## Joining sets
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # False

print(st1.isdisjoint(st2))



# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

it_companies.update(["Twitter","Oppo"])

print(it_companies)
print(len(it_companies))

age_set = set(age)