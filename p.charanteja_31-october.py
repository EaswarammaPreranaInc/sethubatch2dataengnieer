#1. Thread join with timeout

from threading import *
import time

def disp():
    main_thread().join(10)
    for i in range(10):
        print('new thread')

new = Thread(target=disp)
new.start()

for i in range(10):
    print('main thread')
    time.sleep(2)

'''
Output:

main thread
main thread
main thread
main thread
main thread
new thread
new thread
new thread
new thread
new thread
new thread
new thread
new thread
new thread
new thread
main thread
main thread
main thread
main thread
main thread
'''






#2. Deadlock with join()

from threading import *
import time

def disp():
    main_thread().join()
    for i in range(10):
        print('child thread')

child = Thread(target=disp)
child.start()
child.join()

for i in range(10):
    print('main thread')

'''
Output:
(no output; program hangs due to deadlock - child waits for main thread which waits for child)
'''






#3. Multiple threads printing with delay

from threading import *
import time

def disp(s):
    print('[', s, end='')
    time.sleep(3)
    print(']')

t1 = Thread(target=disp, args=('Hyd',))
t2 = Thread(target=disp, args=('Sec',))
t3 = Thread(target=disp, args=('Cyb',))

t1.start()
t2.start()
t3.start()
'''
Output:
Order may vary
[ Hyd[ Sec[ Cyb
] ] ]
(Each ] appears approx 3 seconds after each opening bracket)

'''




#4. Account credit with race condition (corrected __init__)

from threading import *
import time

class Account:
    def __init__(self, acno1, bal1):
        self.acno = acno1
        self.bal = bal1

    def credit(self, amt):
        s = current_thread().name
        print(f'{s} is depositing Rs. {amt} into account {self.acno}')
        x = self.bal
        time.sleep(1)
        self.bal = x + amt

ac = Account(25, 1000.0)
print('Initial Balance:', ac.bal)
t1 = Thread(target=ac.credit, args=[100], name='Rama')
t2 = Thread(target=ac.credit, args=(200,), name='Sita')
t1.start()
t2.start()
t1.join()
t2.join()
print('Final Balance:', ac.bal)
'''
Output:

Initial Balance: 1000.0
Rama is depositing Rs. 100 into account 25
Sita is depositing Rs. 200 into account 25
Final Balance: 1200.0
(Note: The expected final balance is 1300.0, but due to race condition, it shows 1200 or 1100)
'''






#5. Enumerate list with start index and error

import time

list = [25, 10.8, 'Hyd', True]
e = enumerate(list, start=5)
while True:
    try:
        print(next(e))
        time.sleep(1)
    except StopIteration:
        break
print(list[5])
'''
Output:

(5, 25)
(6, 10.8)
(7, 'Hyd')
(8, True)
Traceback (most recent call last):
  ...
IndexError: list index out of range
'''




#6. Enumerate a string

import time
a = 'Hyd'
e = enumerate(a)
while True:
    try:
        print(next(e))
        time.sleep(1)
    except StopIteration:
        break
'''
Output:

(0, 'H')
(1, 'y')
(2, 'd')
'''




#7. Enumerate a set

import time
a = {25, 10.8, 'Hyd', True}
print(a)
b = enumerate(a)
while True:
    try:
        print(next(b))
        time.sleep(1)
    except StopIteration:
        break
'''
Output:

{True, 10.8, 25, 'Hyd'}
(0, True)
(1, 10.8)
(2, 25)
(3, 'Hyd')
(Order of set elements may vary)
'''






#8. Enumerate dictionary keys, values, items

import time

def disp(e):
    while True:
        try:
            print(next(e))
            time.sleep(1)
        except:
            break
    print()

a = {'Empno': 25, 'Emp Name': 'Rama Rao', 'Sal': 10000.0}
disp(enumerate(a.keys()))
disp(enumerate(a.values()))
disp(enumerate(a.items()))
disp(enumerate(a, start=5))
'''
Output:

(0, 'Empno')
(1, 'Emp Name')
(2, 'Sal')

(0, 25)
(1, 'Rama Rao')
(2, 10000.0)

(0, ('Empno', 25))
(1, ('Emp Name', 'Rama Rao'))
(2, ('Sal', 10000.0))

(5, 'Empno')
(6, 'Emp Name')
(7, 'Sal')
'''






#9. Print states and capitals using enumerate

a = ['Telangana', 'Andhra Pradesh', 'Karnataka', 'TamilNadu', 'Maharastra']
b = ['Hyderabad', 'Amaravathi', 'Bangalore', 'Chennai', 'Mumbai']

for i, state in enumerate(a):
    print(f'{state:<18}... {b[i]}')
'''
Output:

Telangana          ... Hyderabad
Andhra Pradesh     ... Amaravathi
Karnataka          ... Bangalore
TamilNadu          ... Chennai
Maharastra         ... Mumbai
'''






#10. Iterate zip object in different ways

import time
a = ['Telangana', 'Andhra Pradesh', 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad', 'Amaravathi', 'Bangalore', 'Chennai']
z1 = zip(a, b)

print(type(z1))
print(z1)

print('Iterate through zip object with next() function')
z_iter = iter(zip(a, b))
print(next(z_iter))
print(next(z_iter))

print('Iterate through zip object with for loop')
for item in zip(a, b):
    print(item)

print('Unpacks zip object with * operator:', list(zip(*zip(a, b))))

print('zip object in the form of list:', list(zip(a, b)))

print('zip object in the form of dictionary:', dict(zip(a, b)))
'''
Output:

<class 'zip'>
<zip object at 0x...>
Iterate through zip object with next() function
('Telangana', 'Hyderabad')
('Andhra Pradesh', 'Amaravathi')
Iterate through zip object with for loop
('Telangana', 'Hyderabad')
('Andhra Pradesh', 'Amaravathi')
('Karnataka ', 'Bangalore')
('Tamilnadu', 'Chennai')
Unpacks zip object with * operator: [('Telangana', 'Andhra Pradesh', 'Karnataka ', 'Tamilnadu'), ('Hyderabad', 'Amaravathi', 'Bangalore', 'Chennai')]
zip object in the form of list: [('Telangana', 'Hyderabad'), ('Andhra Pradesh', 'Amaravathi'), ('Karnataka ', 'Bangalore'), ('Tamilnadu', 'Chennai')]
zip object in the form of dictionary: {'Telangana': 'Hyderabad', 'Andhra Pradesh': 'Amaravathi', 'Karnataka ': 'Bangalore', 'Tamilnadu': 'Chennai'}
'''





#11. Zip with unequal lengths, printing pairs

import time
a = ['Empno', 'Emp Name', 'Salary']
b = [25, 'Rama Rao', 10000.0, 'Male', True]
c = zip(a, b)
while True:
    try:
        print(next(c))
        time.sleep(1)
    except StopIteration:
        break
'''
Output:

('Empno', 25)
('Emp Name', 'Rama Rao')
('Salary', 10000.0)
'''






#12. Zip with 3 lists

import time
a = ['Telangana', 'Andhra Pradesh', 'Karnataka', 'TamilNadu', 'Maharastra']
b = ['Hyderabad', 'Amaravathi', 'Banglore', 'Chennai', 'Mumbai']
c = [50000000, 40000000, 70000000, 60000000, 30000000]
for x in zip(a, b, c):
    print(x)
    time.sleep(1)
'''
Output:

('Telangana', 'Hyderabad', 50000000)
('Andhra Pradesh', 'Amaravathi', 40000000)
('Karnataka', 'Banglore', 70000000)
('TamilNadu', 'Chennai', 60000000)
('Maharastra', 'Mumbai', 30000000)
'''





#13. Zip sum of two lists

import time
a = [1, 2, 3]
b = [4, 5, 6, 7, 8]
for x, y in zip(a, b):
    print(x + y)
    time.sleep(1)
'''
Output:

5
7
9
'''





#14. Zip with dictionary keys, values, items

import time

def disp(z):
    while True:
        try:
            print(next(z))
            time.sleep(1)
        except:
            break
    print()

a = [10, 20, 30]
b = {1: 2, 3: 4, 5: 6}
disp(zip(a, b.keys()))
disp(zip(a, b.values()))
disp(zip(a, b.items()))
disp(zip(a, b))
disp(zip(a))
disp(zip(b))
disp(zip())
'''
Output:

(10, 1)
(20, 3)
(30, 5)

(10, 2)
(20, 4)
(30, 6)

(10, (1, 2))
(20, (3, 4))
(30, (5, 6))

(10, 1)
(20, 3)
(30, 5)

(10,)
(20,)
(30,)

(1,)
(3,)
(5,)

(no output)
'''




#15. Zip with list comprehension

z = zip(range(5), range(20, 25))
a = [[x, y] for x, y in z]
print(a)
'''
Output:

[[0, 20], [1, 21], [2, 22], [3, 23], [4, 24]]
'''

