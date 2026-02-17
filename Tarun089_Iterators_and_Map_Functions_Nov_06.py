#TARUN BANALA HOME WORK ||  ITERATORS AND MAPING FUNCTIONS ||   06-11-2025

import time

def square(x):
    return x * x

nums = [10, 20, 15, 18, 5]
m = map(square, nums)

print(type(m))        # <class 'map'>
print(m)              # <map object at ...>
for n in m:
    print(n)          # 100, 400, 225, 324, 25
    time.sleep(1)


#  Find outputs
import time
a = [('A', 10), ('B', 20), ('C', 15), ('D', 5), ('E', 18)]
m = map(lambda x: x[1], a)
while True:
    try:
        print(next(m))   # 10, 20, 15, 5, 18
        time.sleep(1)
    except StopIteration:
        break


#  Find outputs (countries and sales)
import time
def disp(m):
    while True:
        try:
            print(next(m))
            time.sleep(1)
        except StopIteration:
            break

list1 = [
    {'country': 'India', 'sale': 150.5},
    {'country': 'China', 'sale': 200.2},
    {'country': 'USA', 'sale': 300.3},
    {'country': 'UK', 'sale': 210.4}
]

m1 = map(lambda x: x['country'], list1)
print('Map m1')
disp(m1)  # India, China, USA, UK

m2 = map(lambda x: x['sale'], list1)
print('Map m2')
disp(m2)  # 150.5, 200.2, 300.3, 210.4


#  Celsius to Fahrenheit conversion
celsius = [30, 40, 50, 25]
fahrenheit = list(map(lambda c: 1.8 * c + 32, celsius))
print(fahrenheit)   # [86.0, 104.0, 122.0, 77.0]


#  2 ^ 0 , 2 ^ 1 , ... , 2 ^ 9
powers = list(map(lambda x: 2 ** x, range(10)))
print(powers)       # [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]


#  Area of circle for each radius
radii = [3.5, 2.8, 4.2, 1.9]
areas = list(map(lambda r: 3.14159 * r * r, radii))
print(areas)        # [38.4842025, 24.6307264, 55.417554, 11.341711]


#  Add two tuples of different sizes
t1 = (10, 20, 30, 40)
t2 = (1, 2, 3, 4, 5, 6)
t3 = tuple(map(lambda x, y: x + y, t1, t2))
print(t3)           # (11, 22, 33, 44)


#  Multiply two lists
l1 = [10, 20, 15, 18, 19, 17]
l2 = [1, 5, 3, 2]
l3 = list(map(lambda x, y: x * y, l1, l2))
print(l3)           # [10, 100, 45, 36]


#  map inside filter
import time
a = [10, 20, 15, 12, 18, 5, 14, 25, 17]
f = filter(lambda y: y % 2 == 0, map(lambda x: x ** 2, a))
while True:
    try:
        print(next(f))   # 100, 400, 144, 324, 196
        time.sleep(1)
    except:
        break


#  filter inside map
import time
a = [10, 20, 15, 12, 18, 5, 14, 25, 17]
m = map(lambda y: y + y, filter(lambda x: x >= 15, a))
while True:
    try:
        print(next(m))   # 40, 30, 36, 50, 34
        time.sleep(1)
    except:
        break


#  Largest element using reduce()
from functools import reduce
nums = [10, 20, 15, 30, 25, 40, 35]
largest = reduce(lambda x, y: x if x > y else y, nums)
print(largest)      # 40


#  reduce() + map() + filter() combination
from functools import reduce
a = [10, 20, 15, 5, 12, 18, 25, 14]
ans = reduce(lambda x, y: x + y,
             map(lambda y: y ** 2,
                 filter(lambda x: x >= 15, a)))
print(ans)          # 1574
