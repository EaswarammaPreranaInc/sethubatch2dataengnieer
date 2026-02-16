# 1. Tricky Itertools Count and Zip Program

from itertools import count
cnt = count()
lst = [10, 20, 15, 18]

z1 = zip(cnt, lst)
print('while loop')
while True:
    try:
        print(next(z1))
    except:
        break

z2 = zip(lst, cnt)
print('for loop')
for x in z2:
    print(x)

z3 = zip(cnt, lst)
print(next(z3))
print(*z3)

z4 = zip(lst, cnt)
print(next(z4))
'''
Expected Output:

while loop
(0, 10)
(1, 20)
(2, 15)
(3, 18)
for loop
(10, 4)
(20, 5)
(15, 6)
(18, 7)
(4, 10)
15 18
(10, 8)
'''



# 2. Find Outputs: Custom Iterator with __iter__

import time
class c3:
    def __iter__(self):
        print('__iter__ method')
        return reversed([10, 20, 15, 18])

itr = c3()
for x in itr:
    print(x)
    time.sleep(1)
print(next(itr))
'''
Expected Output:

__iter__ method
18
15
20
10
TypeError: 'c3' object is not an iterator
'''





# 3. Identify Error: Iterator Returns Self Only

class c4:
    def __iter__(self):
        print('__iter__ method')
        return self

itr = c4()
for x in itr:
    print(x)
'''
Expected Output:

__iter__ method
TypeError: iter() returned non-iterator of type 'c4'
'''




# 4. Identify Error: __iter__ present, no __next__

class c5:
    def __iter__(self):
        print('__iter__ method')

itr = c5()
for x in itr:
    print(x)
'''
Expected Output:

__iter__ method
TypeError: iter() returned non-iterator of type 'NoneType'
'''




# 5. Identify Error: method naming, no __iter__/__next__

class c6:
    def iter(self):
        return reversed([10, 20, 15, 18])
    def next(self):
        print('next method')

a = c6()
print(dir(c6))
for x in a:
    print(x)
while True:
    print(next(a))
a.next()
'''
Expected Output:
- `c6` does not implement `__iter__` or `__next__`, so `for x in a` will fail.
- Output: `TypeError: 'c6' object is not iterable`.
'''



# 6. Find Outputs: Correct Iterator Example

class c1:
    def __init__(self):
        self.x = 1
    def __iter__(self):
        print('__iter__ method')
        return self
    def __next__(self):
        value = self.x
        self.x += 1
        return value

a = c1()
print('Elements of iterator with for loop')
for element in a:
    print(element)
    if element == 5:
        break
print('Elements of iterator with next() function')
while True:
    element = next(a)
    print(element)
    if element == 10:
        break
print('Elements of iterator with for loop')
for element in a:
    print(element)
    if element == 15:
        break
'''
Expected Output:

Elements of iterator with for loop
__iter__ method
1
2
3
4
5
Elements of iterator with next() function
6
7
8
9
10
Elements of iterator with for loop
11
12
13
14
15






# 7. Find Outputs: Remote Channel Custom Iterator

import time
class Remote:
    def __init__(self):
        self.list = ['Tv 9', 'Espn', 'Zee Tv', 'ETV']
        self.index = -1
    def __iter__(self):
        return self
    def __next__(self):
        self.index += 1
        if self.index == len(self.list):
            raise StopIteration
        return self.list[self.index]
r = Remote()
for x in r:
    print(x)
    time.sleep(1)
'''
Expected Output:

Tv 9
Espn
Zee Tv
ETV
'''




# 8. Iterator that yields 10...20 (inclusive)

class RangeIt:
    def __iter__(self):
        for i in range(10, 21):
            yield i

for x in RangeIt():
    print(x)
'''
Output:

10
11
12
13
14
15
16
17
18
19
20
'''




# 9. Iterator yielding powers of 2 (2^0...2^7)

class Pow2It:
    def __iter__(self):
        for i in range(8):
            yield 2 ** i

for x in Pow2It():
    print(x)

Output:

1
2
4
8
16
32
64
128
'''
