# Find outputs (Home work)
from threading import *
import time
def disp(s):
    print('[' , s , end = '')
    time.sleep(3)
    print(']')
t1 = Thread(target = disp , args = ('Hyd',))
t2 = Thread(target = disp , args = ('Sec',))
t3 = Thread(target = disp , args = ('Cyb',))
t1.start()
t2.start()
t3.start()
# Output: [ Hyd [ Sec [ Cyb ] ] ] (All three print start almost simultaneously, then after 3 seconds all close brackets print)

# Find outputs (Home work)
from threading import *
import time
class Account:
    def _init_(self , acno1 , bal1):  # Note: Should be __init__ with double underscores
        self.acno = acno1
        self.bal = bal1
    def credit(self , amt):
        s = current_thread().name
        print(F'{s} is depositing Rs. {amt} into account {self.acno}')
        x = self.bal
        time.sleep(1)
        self.bal = x + amt
# End of the class
ac = Account(25 , 1000.0)  # This will fail due to incorrect __init__ method name
print('Initial Balance : ' , ac.bal)
t1 = Thread(target = ac.credit , args = [100] , name = 'Rama')
t2 = Thread(target = ac.credit , args = (200,) , name = 'Sita')
t1.start()
t2.start()
t1.join()
t2.join()
print('Final Balance : ' , ac.bal)
# Output: AttributeError (due to missing __init__ method) or unexpected behavior

# Can set be enumerated? (Home work)
import time
a = {25 , 10.8 , 'Hyd' , True}
print(a)
b = enumerate(a)
while True:
    try:
        print(next(b))
        time.sleep(1)
    except StopIteration:
        break
# Output: Prints set elements with their indices (order may vary as sets are unordered)
# Example: (0, 'Hyd'), (1, 25), (2, 10.8), (3, True) - order may differ

# Can dictionary be enumerated? (Home work)
import time
def disp(e):
    while True:
        try:
            print(next(e))
            time.sleep(1)
        except:
            break
    print()
a = {'Empno' : 25 , 'Emp Name' : 'Rama Rao' , 'Sal' : 10000.0}
e1 = enumerate(a.keys())
disp(e1)
e2 = enumerate(a.values())
disp(e2)
e3 = enumerate(a.items())
disp(e3)
e4 = enumerate(a , start = 5)
disp(e4)
# Output: Enumerates keys, values, items with indices starting from 0 (or 5 for e4)

# Find outputs (Home work)
import time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore' , 'Chennai' , 'Mumbai']
# Write code to print the following outputs using enumerate iterator
for i, state in enumerate(a):
    capital = b[i]
    print(f"{state:<18} ... {capital}")
    time.sleep(1)
# Output: States and capitals aligned in columns

# How to iterate zip object in different ways (Home work)
import time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
z1 = zip(a , b)
print(type(z1))
print(z1)
print('Iterate thru zip object with next() function')
# How to iterate thru zip object with next() function
try:
    while True:
        print(next(z1))
        time.sleep(1)
except StopIteration:
    pass

z1 = zip(a , b)  # Reset zip object
print('Iterate thru zip object with _next_ method')
# How to iterate thru zip object with _next_() method
try:
    while True:
        print(z1.__next__())
        time.sleep(1)
except StopIteration:
    pass

z1 = zip(a , b)  # Reset zip object
print('Iterate thru zip object with for loop')
# How to iterate thru zip object with for loop
for item in z1:
    print(item)
    time.sleep(1)

z1 = zip(a , b)  # Reset zip object
print('Iterate thru elements of each tuple in zip object')
# How to iterate thru elements of each tuple of zip object with for loop
for state, capital in z1:
    print(f"State: {state}, Capital: {capital}")
    time.sleep(1)

z1 = zip(a , b)  # Reset zip object
print('Unpacks zip object with * operator : ' , *z1)
print()
print('zip object in the form of list : ' , list(zip(a , b)))
print()
print('zip object in the form of dictionary : ' , dict(zip(a , b)))

# Find outputs (Home work)
import time
a = [ 'Empno' , 'Emp Name' , 'Salary']
b = [ 25 , 'Rama Rao' , 10000.0 , 'Male' , True]
c = zip(a , b)
while True:
    try:
        print(next(c))
        time.sleep(1)
    except StopIteration:
        break
# Output: ('Empno', 25), ('Emp Name', 'Rama Rao'), ('Salary', 10000.0)

# Find outputs (Home work)
import time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Banglore' , 'Chennai' , 'Mumbai']
c = [50000000 , 40000000 , 70000000 , 60000000 , 30000000]
for x in zip(a , b , c):
    print(x)
    time.sleep(1)
# Output: Tuples containing (state, capital, population) for each state

# Find outputs (Home work)
import time
a = [1 , 2 , 3]
b = [4 , 5 , 6 , 7 , 8]
for x , y in zip(a , b):
    print(x + y)
    time.sleep(1)
# Output: 5, 7, 9 (stops when shortest iterable is exhausted)

# Find outputs (Home work)
import time
def disp(z):
    while True:
        try:
            print(next(z))
            time.sleep(1)
        except:
            break
    print()
a = [10 , 20 , 30]
b = {1 : 2 , 3 : 4 , 5 : 6}
z1 = zip(a , b.keys())
disp(z1)  # (10, 1), (20, 3), (30, 5)
z2 = zip(a , b.values())
disp(z2)  # (10, 2), (20, 4), (30, 6)
z3 = zip(a , b.items())
disp(z3)  # (10, (1, 2)), (20, (3, 4)), (30, (5, 6))
z4 = zip(a , b)
disp(z4)  # (10, 1), (20, 3), (30, 5)
z5 = zip(a)
disp(z5)  # (10,), (20,), (30,)
z6 = zip(b)
disp(z6)  # (1,), (3,), (5,)
z7 = zip()
disp(z7)  # (nothing - empty zip)
