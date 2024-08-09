# Creating a Dictionary
# syntax
empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

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

print(person)
print(len(person))


# Accessing Dictionary Items
print(person['first_name'])
print(person['address'])
print(person['address']['street'])
print(person['skills'][2])


# Adding Items to a Dictionary
person['city'] = 'Ilorin'

person['skills'].append('React')
print(person)


# Modifying items in dictinaries
person['last_name']='Johntizzy'
print(person)


print('first_name' in person)

# Removing Key and Value Pairs from a Dictionary
# pop(key): removes the item with the specified key name:
# popitem(): removes the last item
# del: removes an item with specified key name

del person['first_name']
print(person)


# Changing Dictionary to a List of Items
print(list(person))
print(person.items())


# Getting Dictionary Keys as a List
personk = person.values()
print(personk)
# person.clear()
print(person)