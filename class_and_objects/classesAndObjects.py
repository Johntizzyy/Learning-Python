# Creating a Class
class Person:
    pass
print(Person)

p = Person()
print(p)

class Person:
    def __init__(self,first_name,last_name,age,country):
        self.first_name = first_name        
        self.last_name = last_name
        self.age = age
        self.country = country

person1 = Person('Adepoju','John',20,'Nigeria')
print(person1.first_name)
print(person1.last_name)
print(person1.age)
print(person1.country)

class Person:
    def __init__(self,first_name,last_name,age,country):
        self.first_name = first_name        
        self.last_name = last_name
        self.age = age
        self.country = country
    def person_info(self):
        return (f'{self.first_name} {self.last_name} is a {self.age} years old from {self.country}')
    
person1 = Person('Adepoju','John',20,'Nigeria')
print(person1.person_info())


# Objects defaults methods
class Person:
      def __init__(self, firstname='Adepoju', lastname='John', age=250, country='Nigeria', city='Ilorin'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
          self.skills = []

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}. withe the following skills {tuple(self.skills)}'
      def add_skills (self,skill):
          self.skills.append(skill)

p1 = Person()
print(p1.person_info())
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
(p1.add_skills('HTML'))
(p1.add_skills('CSS'))
(p1.add_skills('JavaScript'))
(p1.add_skills('Python'))

print(p1.person_info())


# Inheritance
class Student(Person):
    pass
s1  = Student('Adepoju','John',30,'Nigeria','Ilorin')
print(s1.person_info())


# Overriding parent method
class Student(Person):
    def __init__(self, firstname='Adepoju', lastname='John', age=250, country='Nigeria', city='Ilorin',gender = 'Male'):
        self.gender = gender
        super().__init__(firstname,lastname,age,country,city)
    def person_info(self):
        gender = 'He' if self.gender == 'Male' else 'She'
        
        # return super().person_info()
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}. withe the following skills {tuple(self.skills)}'
    
s1  = Student('Adepoju','John',30,'Nigeria','Ilorin','Female')
s1.add_skills('Python')
print(s1.person_info())


# EXERCISE
from statistics import *
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
print(mean(ages))

class statistics:
    def __init__(self,data):
        self.data = data
    def count(self):
        return len(self.data)    
    def sum(self):
        return sum(self.data)   
    def min(self):
        return min(self.data)    
    def max(self):
        return max(self.data)    
    def range(self):
        return (self.max() - self.min())    
    def mean(self):
        return mean(self.data)      
    def mean(self):
        return mean(self.data)      
    def median(self):
        return median(self.data)      
    def mode(self):
        return f'{mode(self.data)} , count: {(mode(self.data))}'#mode(self.data)      
    def std(self):
        return '{:.1f}'.format(stdev(self.data))    
    def var(self):
        return '{:.1f}'.format(variance(self.data))
    # def freq_dist(self):
    #     retur



data = statistics(ages)
print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
# print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]

from random import *
from math import floor
print(floor(random()*10))

import math
class Point():
    def __init__(self):
        self.x = 0
        self.y = 0
    def setXY(self,x,y):
        self.x = x
        self.y = y
    def calDis (self,p):
        return '{:.3f}'.format(math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2))
    
point1 = Point()
point2 = Point()
point1.setXY(1,2)
point2.setXY(2,3)

print(point1.calDis(point2))

class Test:
    def __init__(self):
        self.__foobar = "private attr"
        self.foobar = "public attr"
test = Test()
# Accessing public and private att
print(test.foobar) # Public attribute
print(test._Test__foobar) # Privae attribute

# Special Objects attributes
# .__name__  - class name
# .__doc__ - Class description
# .__bases__ - Parent classes
# .__dict__ - atribute
# .__module__ - module were class is defined
print('The name of the class is',Test.__name__)
print('The description of ths class is',Test.__doc__)
print('The attribute of this class is',Test.__dict__)
print('The parent classes',Test.__bases__)


class Feature:
    def __init__(self,name):
        self.name = name
        pass

class Point(Feature):
    def __init__(self,x,y):
        self.x = 0
        self.y = 0
        # super.__init__(name)
    def calDis(self,point):
        return math.sqrt((self.x - point.x) **2 + (self.y - point.y) **2)
    
p1 = Point(1,2)
p2 = Point(2,3)

print(p1.calDis(p2))


# Calculate the distance between two points
class Points:
    def  __init__(self,x,y):
        self.x = x
        self.y = y
    def calculate(self,other_points):
        return (f"The distance between points {self.x,self.y} and {other_points.x,other_points.y} is \
{int(math.sqrt((self.x - other_points.x)**2 + (self.y - other_points.y)**2))}")
    
p1 = Points(3,4)
p2 = Points(7,1)
print(p1.calculate(p2))

class Points:
    def  __init__(self):
        self.x = 0
        self.y = 0
    def setXY(self,x,y):
        self.x = x
        self.y = y
    def calculate(self,other_points):
        return (f"The distance between points {self.x,self.y} and {other_points.x,other_points.y} is \
{int(math.sqrt((self.x - other_points.x)**2 + (self.y - other_points.y)**2))}")
    
p1 = Points()
p1.setXY(3,4)
p2 = Points()
p2.setXY(7,1)
print(p1.calculate(p2))

# class Students:
#     def __init__(self,first_name,last_name,age,stu_ID):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.stu_ID = stu_ID
a = 5
b = 2
print(a>>b)
print(a<<b)

# FLIGHT
# class Flight():
#     def __init__(self,capacity):
#         self.capacity = capacity
#         self.passenger = []

#     def add_passenger (self,name):
#         # If there are no open seats left 
#         if not self.open_seats():
#             return False
        
#         # If there are open seats left
#         else:
#             self.passenger.append(name)
#             return True

#     def open_seats (self):
#         return self.capacity - len(self.passenger)


# flight = Flight(5)
# people = ["John",'Tobi','Delilah','Peace','samson','ggd','Race']

# for person in people:
#     success = flight.add_passenger(person)
#     if success:
#         print(f"Added {person} succesfully to the Flight")
#     else:
#         print(f"There are no more seats left for {person}")

class Flight:
    def __init__(self,capacity):
        self.capacity = capacity
        self.passenger = []

    def add_passenger(self,name):
        if not self.open_seats():
            return False
        else:
            self.passenger.append(name)
            return True

    def open_seats (self):
        return self.capacity - len(self.passenger)
        


people = ['John','Peace','Oluwatobi','Ana','stella','gg']
flight = Flight(3)

for person in people:
    success = flight.add_passenger(person)
    if success == True:
        print(f"{person} has been successfully added to the flight")
    else:
        print(f"No available seat for {person}")