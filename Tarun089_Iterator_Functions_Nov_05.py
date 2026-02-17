# Producer-Consumer problem
from threading import *
import time
from random import randint
class buffer:
    def store(self, y):
        s = current_thread().name
        self.x = y
        print(s, 'stores', self.x)
    def ret(self):
        s = current_thread().name
        print(s, 'retrieves', self.x)
def f1(buf):
    i = 1
    while True:
        buf.store(i)
        i += 1
        time.sleep(randint(1, 4))
def f2(buf):
    while True:
        buf.ret()
        time.sleep(randint(1, 4))
buf = buffer()
p = Thread(target = f1, name = 'producer', args = (buf,))
c = Thread(target = f2, name = 'consumer', args = (buf,))
p.start()
c.start()
print('Press ctrl + break or Fn+B to stop')
# Output: Producer stores numbers, consumer retrieves them randomly with delays until stopped

# How to iterate list_iterator in different ways
import time
list = [10, 20, 15, 18]
print('Iterate list with for loop')
for item in list: print(item)  # Output: 10 20 15 18
#print(next(list))  # Error: 'list' object is not an iterator
list_itr1 = iter(list)
print(type(list_itr1))  # Output: <class 'list_iterator'>
print(list_itr1)  # Output: <list_iterator object at ...>
print('Iterate thru list_iterator with next() function')
print(next(list_itr1)); print(next(list_itr1))  # Output: 10 20
print('Iterate thru list_iterator with _next_() method')
print(list_itr1.__next__()); print(list_itr1.__next__())  # Output: 15 18
list_itr1 = iter(list)  # Reset iterator
print('Iterate thru list_iterator with for loop')
for item in list_itr1: print(item)  # Output: 10 20 15 18
list_itr1 = iter(list)  # Reset iterator
print('Unpacks List_iterator : ', *list_itr1)  # Output: 10 20 15 18

# Find outputs
a = 25
print(a)  # Output: 25
#for x in a: print(x)  # Error: 'int' object is not iterable
#print(iter(a))  # Error: 'int' object is not iterable
#print(next(a))  # Error: 'int' object is not an iterator

'''
Modify following program such that
1) Use regular function instead of lambda function
2) Use for loop to iterate filter instead of while loop
'''
import time
list = [25, 9, 10, 15, 17, 24, 35, 47, 0, 19, 53, 18, 65, 83]
def is_even(x): return x % 2 == 0  # Regular function instead of lambda
f = filter(is_even, list)
print(type(f))  # Output: <class 'filter'>
print(f)  # Output: <filter object at ...>
for item in f: print(item)  # Output: 10 24 18 (even numbers using for loop)

# Find outputs (Home work)
import time
list = [25, 10.8, 3 + 4j, 'Hyd', False]
f = filter(lambda x: True, list)
while True:
    try:
        print(next(f))  # Output: All elements: 25, 10.8, (3+4j), 'Hyd', False
        time.sleep(1)
    except: break

# Find outputs (Home work)
import time
list = [25, 10.8, 3 + 4j, 'Hyd', True]
f = filter(lambda x: False, list)
while True:
    try:
        print(next(f))  # Output: Nothing (immediately raises StopIteration)
        time.sleep(1)
    except: break

# Find outputs (Home work)
import time
list = [25, 10.8, False, 3 + 4j, 0, 'Hyd', '', (25,), ()]
f = filter(lambda x: x, list)  # Truthy values filter
while True:
    try:
        print(next(f))  # Output: 25, 10.8, (3+4j), 'Hyd', (25,) (truthy values)
        time.sleep(1)
    except: break

# Find outputs
import time
def disp(f):
    while True:
        try:
            print(next(f))
            time.sleep(1)
        except: break
list = [10, 0, -25, (), (25,), 'Hyd', '', [], 10.8, 0.0, [10, 20], True, False]
f1 = filter(lambda x: None, list)
print('Filter f1')  # Output: Filter f1
disp(f1)  # Output: Nothing (None is falsy)
f2 = filter(None, list)  # Truthy values filter
print('Filter f2')  # Output: Filter f2
disp(f2)  # Output: 10, -25, (25,), 'Hyd', 10.8, [10, 20], True (truthy values)

# Find outputs (Home work)
import time
list = ['Rama Rao', 'Sita', 'Rajesh', 'Kiran', 'Amar', 'Manohar', 'Vamsi']
f = filter(lambda x: len(x) >= 5, list)  # Names with length >= 5
while True:
    try:
        print(next(f))  # Output: 'Rama Rao', 'Rajesh', 'Kiran', 'Manohar', 'Vamsi'
        time.sleep(1)
    except: break

# Find outputs (Home work)
import time
list = [('A', 10), ('B', 20), ('C', 15), ('D', 5), ('E', 18)]
f = filter(lambda x: x[1] >= 12, list)  # Tuples with second element >= 12
while True:
    try:
        print(next(f))  # Output: ('B', 20), ('C', 15), ('E', 18)
        time.sleep(1)
    except: break

# Find outputs (Home work)
import time
list = [
    {'Roll Num': 10, 'Stud Name': 'Rama Rao', 'Marks': 75},
    {'Roll Num': 20, 'Stud Name': 'Sita', 'Marks': 52},
    {'Roll Num': 15, 'Stud Name': 'Kiran', 'Marks': 65},
    {'Roll Num': 18, 'Stud Name': 'Amar', 'Marks': 48},
    {'Roll Num': 5, 'Stud Name': 'Rajesh', 'Marks': 82}
]
f = filter(lambda x: x['Marks'] >= 60, list)  # Students with marks >= 60
while True:
    try:
        print(next(f))  # Output: First, third, and fifth dictionaries
        time.sleep(1)
    except: break

# Find outputs (Home work)
import time
def disp(f):
    while True:
        try:
            print(next(f))
            time.sleep(1)
        except: break
list = [
    {'country': 'India', 'sale': 150.5},
    {'country': 'china', 'sale': 200.2},
    {'country': 'USA', 'sale': 300.3},
    {'country': 'UK', 'sale': 210.4}
]
f1 = filter(lambda x: x['country'].startswith('U'), list)  # Countries starting with 'U'
print('Filter f1')  # Output: Filter f1
disp(f1)  # Output: USA and UK dictionaries
f2 = filter(lambda x: x['sale'] >= 200, list)  # Sales >= 200
print('Filter f2')  # Output: Filter f2
disp(f2)  # Output: china, USA, UK dictionaries

# How to print filter object in different ways?
import time
a = [10, 15, 20, 17, 18, 19, 26]
f1 = filter(lambda x: x % 2 == 0, a)  # Even numbers filter
print('Iterate thru filter object with next function')
print(next(f1), next(f1))  # Output: 10 20 (first two even numbers)
f1 = filter(lambda x: x % 2 == 0, a)  # Reset filter
print('Iterate thru filter object with for loop')
for item in f1: print(item)  # Output: 10 20 18 26 (all even numbers)
f1 = filter(lambda x: x % 2 == 0, a)  # Reset filter
print('Unpack filter object: ', *f1)  # Output: 10 20 18 26
f1 = filter(lambda x: x % 2 == 0, a)  # Reset filter
print('filter object converted to list: ', list(f1))  # Output: [10, 20, 18, 26]

# Write a program to print odd numbers between 1 and 20 with filter iterator
numbers = list(range(1, 21))
odd_filter = filter(lambda x: x % 2 != 0, numbers)
print(list(odd_filter))  # Output: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Write a program to print distinct vowels of the string using filter. Input is string and output is set
def is_vowel(char): return char.lower() in 'aeiou'
input_string = "Hello World Programming"
vowels_set = set(filter(is_vowel, input_string))
print(vowels_set)  # Output: {'e', 'o', 'i', 'a'}

# Nested filter i.e. filter on filter
import time
list = [
    (10, 'Rama', 10000.0),
    (20, 'Sita', 7000.0),
    (15, 'Rajesh', 15000.0),
    (5, 'Amar', 12000.0),
    (18, 'Ramesh', 8000.0)
]
f = filter(lambda x: x[1].startswith('R'), filter(lambda x: x[2] >= 10000, list))
while True:
    try:
        print(next(f))  # Output: (10, 'Rama', 10000.0), (15, 'Rajesh', 15000.0)
        time.sleep(1)
    except: break
