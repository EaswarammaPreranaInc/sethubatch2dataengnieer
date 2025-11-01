# Find outputs (Home work)
from threading import *
import time

print("=== Code 1 ===")
try:
    def disp():
        main_thread().join(10)  # This will cause error
        for i in range(10):
            print('new thread')
    new = Thread(target=disp)
    new.start()
    for i in range(10):
        print('main thread')
        time.sleep(2)
except Exception as e:
    print(f"Error in Code 1: {e}")  # Output: Error in Code 1: 'function' object has no attribute 'join'

print("\n=== Code 2 ===")
try:
    def disp():
        main_thread().join()  # This will cause error
        for i in range(10):
            print('child thread')
    child = Thread(target=disp)
    child.start()
    child.join()
    for i in range(10):
        print('main thread')
except Exception as e:
    print(f"Error in Code 2: {e}")  # Output: Error in Code 2: 'function' object has no attribute 'join'

print("\n=== Code 3 ===")
def disp(s):
    print('[', s, end='')
    time.sleep(1)
    print(']', end=' ')
t1 = Thread(target=disp, args=('Hyd',))
t2 = Thread(target=disp, args=('Sec',))
t3 = Thread(target=disp, args=('Cyb',))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print()  # Output: [ Hyd[ Sec[ Cyb] ] ] 

print("\n=== Code 4 ===")
try:
    class Account:
        def _init_(self, acno1, bal1):  # Note: should be __init__
            self.acno = acno1
            self.bal = bal1
        def credit(self, amt):
            s = current_thread().name
            print(f'{s} is depositing Rs. {amt} into account {self.acno}')
            x = self.bal
            time.sleep(1)
            self.bal = x + amt

    ac = Account(25, 1000.0)  # __init__ not called due to typo
    print('Initial Balance : ', ac.bal)  # Error: ac.bal doesn't exist
except Exception as e:
    print(f"Error in Code 4: {e}")  # Output: Error in Code 4: 'Account' object has no attribute 'bal'

print("\n=== Code 5 ===")
try:
    list_data = [25, 10.8, 'Hyd', True]
    e = enumerate(list_data, start=5)
    while True:
        try:
            print(next(e))  # Output: (5, 25), (6, 10.8), (7, 'Hyd'), (8, True)
            time.sleep(0.5)
        except StopIteration:
            break
    print(list_data[5])  # Error: index out of range
except Exception as e:
    print(f"Error in Code 5: {e}")  # Output: Error in Code 5: list index out of range

print("\n=== Code 6 - String Enumeration ===")
a = 'Hyd'  # Simulating input
e = enumerate(a)
while True:
    try:
        print(next(e))  # Output: (0, 'H'), (1, 'y'), (2, 'd')
        time.sleep(0.5)
    except StopIteration:
        break
print("Answer: Yes, strings can be enumerated.")  # Output: Answer: Yes, strings can be enumerated.

print("\n=== Code 7 - Set Enumeration ===")
a = {25, 10.8, 'Hyd', True}
print("Set:", a)  # Output: Set: {True, 10.8, 'Hyd', 25} (order may vary)
b = enumerate(a)
while True:
    try:
        print(next(b))  # Output: (0, True), (1, 10.8), (2, 'Hyd'), (3, 25) (order may vary)
        time.sleep(0.5)
    except StopIteration:
        break
print("Answer: Yes, sets can be enumerated.")  # Output: Answer: Yes, sets can be enumerated.

print("\n=== Code 8 - Dictionary Enumeration ===")
def disp(e):
    while True:
        try:
            print(next(e))
            time.sleep(0.5)
        except:
            break
    print()

a = {'Empno': 25, 'Emp Name': 'Rama Rao', 'Sal': 10000.0}
e1 = enumerate(a.keys())
print("Keys:")  # Output: Keys:
disp(e1)  # Output: (0, 'Empno'), (1, 'Emp Name'), (2, 'Sal')
e2 = enumerate(a.values())
print("Values:")  # Output: Values:
disp(e2)  # Output: (0, 25), (1, 'Rama Rao'), (2, 10000.0)
e3 = enumerate(a.items())
print("Items:")  # Output: Items:
disp(e3)  # Output: (0, ('Empno', 25)), (1, ('Emp Name', 'Rama Rao')), (2, ('Sal', 10000.0))
e4 = enumerate(a, start=5)
print("With start=5:")  # Output: With start=5:
disp(e4)  # Output: (5, 'Empno'), (6, 'Emp Name'), (7, 'Sal')

print("\n=== Code 9 - State-Capital Printing ===")
a = ['Telangana', 'Andhra Pradesh', 'Karnataka', 'TamilNadu', 'Maharastra']
b = ['Hyderabad', 'Amaravathi', 'Bangalore', 'Chennai', 'Mumbai']
for state, capital in zip(a, b):
    print(f"{state:15} ... {capital}")  
# Output: 
# Telangana       ... Hyderabad
# Andhra Pradesh  ... Amaravathi
# Karnataka       ... Bangalore
# TamilNadu       ... Chennai
# Maharastra      ... Mumbai

print("\n=== Code 10 - Zip Iteration Methods ===")
a = ['Telangana', 'Andhra Pradesh', 'Karnataka', 'Tamilnadu']
b = ['Hyderabad', 'Amaravathi', 'Bangalore', 'Chennai']
z1 = zip(a, b)
print('Type:', type(z1))  # Output: Type: <class 'zip'>
print('Zip object:', z1)  # Output: Zip object: <zip object at 0x...>

print('\nIterate thru zip object with next() function:')
z_temp = zip(a, b)
try:
    print(next(z_temp))  # Output: ('Telangana', 'Hyderabad')
    print(next(z_temp))  # Output: ('Andhra Pradesh', 'Amaravathi')
    print(next(z_temp))  # Output: ('Karnataka', 'Bangalore')
    print(next(z_temp))  # Output: ('Tamilnadu', 'Chennai')
except StopIteration:
    pass

print('\nIterate thru zip object with for loop:')
for item in zip(a, b):
    print(item)  
# Output: 
# ('Telangana', 'Hyderabad')
# ('Andhra Pradesh', 'Amaravathi')
# ('Karnataka', 'Bangalore')
# ('Tamilnadu', 'Chennai')

print('\nIterate thru elements of each tuple in zip object:')
for state, capital in zip(a, b):
    print(f"State: {state}, Capital: {capital}")  
# Output:
# State: Telangana, Capital: Hyderabad
# State: Andhra Pradesh, Capital: Amaravathi
# State: Karnataka, Capital: Bangalore
# State: Tamilnadu, Capital: Chennai

print('\nUnpacks zip object with * operator:')
print(*zip(a, b))  # Output: ('Telangana', 'Hyderabad') ('Andhra Pradesh', 'Amaravathi') ('Karnataka', 'Bangalore') ('Tamilnadu', 'Chennai')

print('\nzip object in the form of list:', list(zip(a, b)))  
# Output: [('Telangana', 'Hyderabad'), ('Andhra Pradesh', 'Amaravathi'), ('Karnataka', 'Bangalore'), ('Tamilnadu', 'Chennai')]

print('\nzip object in the form of dictionary:', dict(zip(a, b)))  
# Output: {'Telangana': 'Hyderabad', 'Andhra Pradesh': 'Amaravathi', 'Karnataka': 'Bangalore', 'Tamilnadu': 'Chennai'}

print("\n=== Code 11 ===")
a = ['Empno', 'Emp Name', 'Salary']
b = [25, 'Rama Rao', 10000.0, 'Male', True]
c = zip(a, b)
while True:
    try:
        print(next(c))  
        # Output: 
        # ('Empno', 25)
        # ('Emp Name', 'Rama Rao')
        # ('Salary', 10000.0)
        time.sleep(0.5)
    except StopIteration:
        break

print("\n=== Code 12 ===")
a = ['Telangana', 'Andhra Pradesh', 'Karnataka', 'TamilNadu', 'Maharastra']
b = ['Hyderabad', 'Amaravathi', 'Banglore', 'Chennai', 'Mumbai']
c = [50000000, 40000000, 70000000, 60000000, 30000000]
for x in zip(a, b, c):
    print(x)  
    # Output:
    # ('Telangana', 'Hyderabad', 50000000)
    # ('Andhra Pradesh', 'Amaravathi', 40000000)
    # ('Karnataka', 'Banglore', 70000000)
    # ('TamilNadu', 'Chennai', 60000000)
    # ('Maharastra', 'Mumbai', 30000000)
    time.sleep(0.5)

print("\n=== Code 13 ===")
a = [1, 2, 3]
b = [4, 5, 6, 7, 8]
for x, y in zip(a, b):
    print(x + y)  # Output: 5, 7, 9
    time.sleep(0.5)

print("\n=== Code 14 ===")
def disp(z):
    while True:
        try:
            print(next(z))
            time.sleep(0.5)
        except:
            break
    print()

a = [10, 20, 30]
b = {1: 2, 3: 4, 5: 6}

print("z1 = zip(a, b.keys()):")  # Output: z1 = zip(a, b.keys()):
z1 = zip(a, b.keys())
disp(z1)  # Output: (10, 1), (20, 3), (30, 5)

print("z2 = zip(a, b.values()):")  # Output: z2 = zip(a, b.values()):
z2 = zip(a, b.values())
disp(z2)  # Output: (10, 2), (20, 4), (30, 6)

print("z3 = zip(a, b.items()):")  # Output: z3 = zip(a, b.items()):
z3 = zip(a, b.items())
disp(z3)  # Output: (10, (1, 2)), (20, (3, 4)), (30, (5, 6))

print("z4 = zip(a, b):")  # Output: z4 = zip(a, b):
z4 = zip(a, b)
disp(z4)  # Output: (10, 1), (20, 3), (30, 5)

print("z5 = zip(a):")  # Output: z5 = zip(a):
z5 = zip(a)
disp(z5)  # Output: (10,), (20,), (30,)

print("z6 = zip(b):")  # Output: z6 = zip(b):
z6 = zip(b)
disp(z6)  # Output: (1,), (3,), (5,)

print("z7 = zip():")  # Output: z7 = zip():
z7 = zip()
disp(z7)  # Output: (empty)

print("\n=== Code 15 ===")
z = zip(range(5), range(20, 25))
a = [[x, y] for x, y in z]
print(a)  # Output: [[0, 20], [1, 21], [2, 22], [3, 23], [4, 24]]
