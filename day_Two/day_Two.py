## This is day two of my pyhton programme

##  VARIABLES

print(str(10))
print(float(10))
print(int('10'))

print(min(20,30,40))
print(max(20,30,40))

## List
# print(min[20,30,40])
# print(max[20,30,40])
# print(sum[20,30,40])
# print(sum([20,30]))

first_name = "Johntizzy"
skills = ["HTML","CSS","JavaScript","Python"]
age = 1010

myBio = {
    "firstname":"Adepoju",
    "lastname":"John",
    "age":1010,
    "skills":["HTML","CSS","JavaScript","Python"]
}
print("firstname:",first_name)
print("namelength:",len(first_name))
print("Skills:",skills)

print("My name is",first_name,"I am",age,"My skills lists are",skills)
print(myBio)


## Declaring multiple variables
# firstName= input("What's your firstName")
# lastName = input("what is your last name")

# print(firstName,lastName)

print(type({"firstname":"John","lastname":"Tizzy"}))
print(type(myBio))


## Casting
str_list = "Dave"
str_list = "John"
print((str_list))


num_one = 5
num_two = 10

print(num_one + num_two)
print(sum([num_one,num_two]))
print(num_one // num_two)

PI = 3.142
area_of_circle = 2 * PI * 30
print(area_of_circle)

# first = input("f")

student_Id = {
    "firstname":"Adepoju",
    "lastname":"John",
    "cgpa":"5.0"
}

print(student_Id)
