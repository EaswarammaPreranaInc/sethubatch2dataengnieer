# 1. Producer-Consumer Problem

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
p = Thread(target=f1, name='producer', args=(buf,))
c = Thread(target=f2, name='consumer', args=(buf,))
p.start()
c.start()

print('Press ctrl + break or Fn+B to stop')
'''
Output (sample):
producer stores 1
consumer retrieves 1
producer stores 2
consumer retrieves 2
'''




# 2. Iterating list_iterator in Different Ways

list_data = [10, 20, 15, 18]

print('Iterate list with for loop')
for i in list_data:
    print(i)

list_itr1 = iter(list_data)
print(type(list_itr1))
print(list_itr1)

print('Iterate thru list_iterator with next() function')
try:
    while True:
        print(next(list_itr1))
except StopIteration:
    pass

print('Iterate thru list_iterator with _next_() method')
list_itr2 = iter(list_data)
try:
    while True:
        print(list_itr2.__next__())
except StopIteration:
    pass

print('Iterate thru list_iterator with for loop')
for x in list_data:
    print(x)

print('Unpacks List_iterator :', [*iter(list_data)])
'''

Output:

Iterate list with for loop
10
20
15
18
<class 'list_iterator'>
<list_iterator object at 0x...>
Iterate thru list_iterator with next() function
10
20
15
18
Iterate thru list_iterator with _next_() method
10
20
15
18
Iterate thru list_iterator with for loop
10
20
15
18
Unpacks List_iterator : [10, 20, 15, 18]
'''




# 3. Iterating over an integer (error demonstration)

a = 25
print(a)
for x in a:
    print(x)
'''

Output:

25
TypeError: 'int' object is not iterable
'''




# 4. Filter even numbers using regular function and for loop

import time

def is_even(x):
    return x % 2 == 0

lst = [25, 9, 10, 15, 17, 24, 35, 47, 0, 19, 53, 18, 65, 83]
f = filter(is_even, lst)

for val in f:
    print(val)
    time.sleep(1)
'''
Output:

10
24
0
18
'''




# 5. Filter with always True condition

import time

lst = [25, 10.8, 3 + 4j, 'Hyd', False]
f = filter(lambda x: True, lst)
try:
    while True:
        print(next(f))
        time.sleep(1)
except StopIteration:
    pass
'''
Output:

25
10.8
(3+4j)
Hyd
False
'''




# 6. Filter with always False condition

import time

lst = [25, 10.8, 3 + 4j, 'Hyd', True]
f = filter(lambda x: False, lst)
try:
    while True:
        print(next(f))
        time.sleep(1)
except StopIteration:
    pass

#Output:(none printed)






# 7. Filter with truthy values (filtering falsy out)

import time

lst = [25, 10.8, False, 3 + 4j, 0, 'Hyd', '', (25,), ()]
f = filter(lambda x: x, lst)
try:
    while True:
        print(next(f))
        time.sleep(1)
except StopIteration:
    pass
'''
Output:

25
10.8
(3+4j)
Hyd
(25,)
'''




# 8. Filter with `lambda x: None` and `filter(None, list)`

import time

lst = [10, 0, -25, (), (25,), 'Hyd', '', [], 10.8, 0.0, [10, 20], True, False]

f1 = filter(lambda x: None, lst)
print('Filter f1')
try:
    while True:
        print(next(f1))
        time.sleep(1)
except StopIteration:
    pass

f2 = filter(None, lst)
print('Filter f2')
try:
    while True:
        print(next(f2))
        time.sleep(1)
except StopIteration:
    pass
'''
Output:

Filter f1
Filter f2
10
-25
(25,)
Hyd
10.8
[10, 20]
True
'''




# 9. Filter strings with length >= 5

import time

lst = ['Rama Rao', 'Sita', 'Rajesh', 'Kiran', 'Amar', 'Manohar', 'Vamsi']
f = filter(lambda x: len(x) >= 5, lst)
try:
    while True:
        print(next(f))
        time.sleep(1)
except StopIteration:
    pass
'''
Output:

Rama Rao
Rajesh
Kiran
Manohar
Vamsi
'''




# 10. Filter list of tuples with second element >= 12

import time

lst = [('A', 10), ('B', 20), ('C', 15), ('D', 5), ('E', 18)]
f = filter(lambda x: x[1] >= 12, lst)
try:
    while True:
        print(next(f))
        time.sleep(1)
except StopIteration:
    pass
'''
Output:

('B', 20)
('C', 15)
('E', 18)
'''





# 11. Filter list of dictionaries with marks >= 60

import time

lst = [
    {'Roll Num': 10, 'Stud Name': 'Rama Rao', 'Marks': 75},
    {'Roll Num': 20, 'Stud Name': 'Sita', 'Marks': 52},
    {'Roll Num': 15, 'Stud Name': 'Kiran', 'Marks': 65},
    {'Roll Num': 18, 'Stud Name': 'Amar', 'Marks': 48},
    {'Roll Num': 5, 'Stud Name': 'Rajesh', 'Marks': 82}
]

f = filter(lambda x: x['Marks'] >= 60, lst)
try:
    while True:
        print(next(f))
        time.sleep(1)
except StopIteration:
    pass
'''
Output:

{'Roll Num': 10, 'Stud Name': 'Rama Rao', 'Marks': 75}
{'Roll Num': 15, 'Stud Name': 'Kiran', 'Marks': 65}
{'Roll Num': 5, 'Stud Name': 'Rajesh', 'Marks': 82}
'''




# 12. Filter dictionaries by country and sale

import time

lst = [
    {'country': 'India', 'sale': 150.5},
    {'country': 'china', 'sale': 200.2},
    {'country': 'USA', 'sale': 300.3},
    {'country': 'UK', 'sale': 210.4}
]

f1 = filter(lambda x: x['country'].startswith('U'), lst)
print('Filter f1')
try:
    while True:
        print(next(f1))
        time.sleep(1)
except StopIteration:
    pass

f2 = filter(lambda x: x['sale'] >= 200, lst)
print('Filter f2')
try:
    while True:
        print(next(f2))
        time.sleep(1)
except StopIteration:
    pass
'''
Output:

Filter f1
{'country': 'USA', 'sale': 300.3}
{'country': 'UK', 'sale': 210.4}
Filter f2
{'country': 'china', 'sale': 200.2}
{'country': 'USA', 'sale': 300.3}
{'country': 'UK', 'sale': 210.4}
'''





# 13. Iterate filter object with next(), for loop, unpacking, and list conversion

import time

a = [10, 15, 20, 17, 18, 19, 26]
f1 = filter(lambda x: x % 2 == 0, a)

print('Iterate thru filter object with next() function')
try:
    while True:
        print(next(f1))
        time.sleep(1)
except StopIteration:
    pass

f1 = filter(lambda x: x % 2 == 0, a)
print('Iterate thru filter object with for loop')
for val in f1:
    print(val)

print('Unpack filter object : ', [*filter(lambda x: x % 2 == 0, a)])
print('filter object converted to list : ', list(filter(lambda x: x % 2 == 0, a)))
'''
Output:

Iterate thru filter object with next() function
10
20
18
26
Iterate thru filter object with for loop
10
20
18
26
Unpack filter object :  [10, 20, 18, 26]
filter object converted to list :  [10, 20, 18, 26]
'''





# 14. Nested filter on filter

import time

lst = [
    (10, 'Rama', 10000.0),
    (20, 'Sita', 7000.0),
    (15, 'Rajesh', 15000.0),
    (5, 'Amar', 12000.0),
    (18, 'Ramesh', 8000.0)
]

f = filter(lambda x: x[1].startswith('R'), filter(lambda x: x[2] >= 10000, lst))
try:
    while True:
        print(next(f))
        time.sleep(1)
except StopIteration:
    pass
'''
Output:

(10, 'Rama', 10000.0)
(15, 'Rajesh', 15000.0)
'''




# 15. Print odd numbers between 1 and 20 using filter iterator

# Print odd numbers between 1 and 20 using filter
nums = range(1, 21)
odd_filter = filter(lambda x: x % 2 != 0, nums)
print('Odd numbers between 1 and 20')
for n in odd_filter:
    print(n)


#Output:
'''
Odd numbers between 1 and 20
1
3
5
7
9
11
13
15
17
19
'''




# 16. Print distinct vowels of the string using filter

# Print distinct vowels in a string using filter
s = input("Enter mixed case string: ")
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
filtered = filter(lambda x: x in vowels, s)
result = set(filtered)
print(result)
'''
Sample Output:

Enter mixed case string : RamA raO
{'O', 'A'}

'''
