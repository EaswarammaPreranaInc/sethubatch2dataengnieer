from prog9a import student
s = student()
print(s.__dict__)  # {}
s.get()            # (User inputs: 25, Rama Rao, male, 52, 48, 55)
print(s.__dict__)  # {'rno': 25, 'name': 'Rama Rao', 'gender': 'male', 'marks': [52, 48, 55]}
s.compute()
print(s.__dict__)  # {'rno': 25, 'name': 'Rama Rao', 'gender': 'male', 'marks': [52, 48, 55], 'total': 155, 'avg': 51.666666666666664, 'grade': 'Second class'}









# Import Student class from prog9a
from prog9a import Student

n = int(input("Enter number of students: "))
a = []

for i in range(n):
    print(f"Student {i+1}")
    s = Student()     # Create object
    s.get()           # Input details
    s.compute()       # Calculate total, avg, grade
    a.append(s)       # Store in list

print("Roll\tName\tGender\tTotal\tAverage\tGrade")
for s in a:
    print(f"{s.rno}\t{s.name}\t{s.gender}\t{s.total:.1f}\t{s.avg:.2f}\t{s.grade}")









# dir() Function Demo with Rat Class

from prog10a import Rat
a = Rat()
a.nr = 22
a.dr = 7
print(dir(Rat))
print()
print()
print(dir(a))
'''
Outputs:

- `dir(Rat)` lists all attributes of the class `Rat`, including inherited default methods like `__init__`, `__module__`, etc.
- `dir(a)` lists attributes of object `a` including `nr` and `dr` along with class attributes.
'''





# hasattr() Function Outputs

class Rat:
    def m1():
        pass
a = Rat()
a.nr = 22
print(hasattr(a, 'nr'))   # True because attribute 'nr' exists in object a
print(hasattr(a, 'dr'))   # False because 'dr' is not assigned
print(hasattr(a, 'm1'))   # True because m1 exists as a method in class Rat accessible from a
print(hasattr(a, 'm2'))   # False, no such method or attribute
print(hasattr(Rat, 'm1')) # True, method exists in class
print(hasattr(Rat, 'm2')) # False
print(hasattr(Rat, 'nr')) # False, attribute 'nr' is on instance, not class







# Polymorphism with Cat, Dog, Goat Classes

class Cat:
    def talk(self):
        print('Meow Meow Meow ....')
class Dog:
    def bark(self):
        print('Bhow Bhow Bhow ....')
class Goat:
    def talk(self):
        print('Mehar Mehar Mehar ....')

a = [Cat(), Dog(), Goat()]
for x in a:
    if hasattr(x, 'talk'):
        x.talk()
    else:
        x.bark()

Output:
Meow Meow Meow ....
Bhow Bhow Bhow ....
Mehar Mehar Mehar ....
'''







# setattr() and getattr() Dynamic Attribute Manipulation

class c1:
    pass

a = c1()
a.x = 10

varname = input('Enter variable name to be added to object : ')  # Assume 'y' input
value = eval(input('Enter value of the variable : '))           # Assume '20' input
setattr(a, varname, value)

print(a.__dict__)  # {'x': 10, 'y': 20}
print(a.x)         # 10

while True:
    try:
        varname = input('Enter variable name whose value is to be retrieved : ')
        print(getattr(a, varname))
    except:
        print(f'Invalid variable name : {varname}')
        break
'''

For inputs 'x', 'y', 'z' sequentially:
10
20
Invalid variable name : z
'''









# Convert Dictionary to Object Using setattr

class Emp:
    pass

dict1 = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 10000.0}
e = Emp()
for k, v in dict1.items():
    setattr(e, k, v)

# To print attributes:
for k in dict1.keys():
    print(getattr(e, k))
'''
Output:

25
Rama Rao
10000.0
'''








# Sample Python Program for 3 Rat Objects with Arithmetic Operations


from prog10a import Rat

# Create 3 Rat objects
a = Rat()
b = Rat()
a.nr, a.dr = 6, 7
b.nr, b.dr = 3, 4

# Perform operations
c = a + b
print("a + b =", c)

c = a - b
print("a - b =", c)

c = a * b
print("a * b =", c)

c = a / b
print("a / b =", c)







# Using a List of 6 Rat Objects

from prog10a import Rat

a = [Rat() for _ in range(6)]

# Example to initialize each Rat object
for i, obj in enumerate(a):
    obj.nr = i + 1
    obj.dr = i + 2

# Object names: a[0], a[1], a[2], a[3], a[4], a[5]
for i in range(6):
    print(f"Rat object a[{i}] has numerator = {a[i].nr} and denominator = {a[i].dr}")
