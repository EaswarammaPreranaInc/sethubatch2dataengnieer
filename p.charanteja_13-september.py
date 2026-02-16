# 1. Iterating a generator with for loop

import time
def f1():
    print('One')
    yield 25
    print('Two')
    yield 10.8
    print('Three')
    yield 'Hyd'
    print('Four')
# End of generator
g = f1()
for x in g:
    print(x)
    time.sleep(1)
    print('Hello')
# End of for loop
print('End')
print(g)
print(next(g))
g = f1()
print(next(g))

'''
Output:

One
25
Hello
Two
10.8
Hello
Three
Hyd
Hello
Four
End
<generator object f1 at 0x...>
StopIteration
One
25
'''







# 2. Most tricky generator program

import time
def f1():
    yield 25
    yield 10.8
    yield 'Hyd'
# End of generator
g = f1()
print(next(g))
for x in g:
    print(x)
print()
for x in f1():
    print(x)
print()
gen = f1()
print(next(gen))
for x in f1():
    print(x)
print(next(gen))

'''

Output:

25
10.8
Hyd

25
10.8
Hyd

25
25
10.8
Hyd
10.8
'''





# 3. Iterating generator expression once

g = (x * x for x in range(5))
for y in g:
    print(y)
    time.sleep(2)
    print('Hello')
for y in g:
    print(y)

'''
Output:

0
Hello
1
Hello
4
Hello
9
Hello
16
Hello
'''





# 4. Fresh generator expressions in two for loops

```python
for y in (x * x for x in range(5)):
    print(y)
    time.sleep(2)
for y in (x * x for x in range(5)):
    print(y)
    time.sleep(2)

'''
Output:

0
1
4
9
16
0
1
4
9
16
'''






# 5. Same generator object, two for loops

g1 = (x * x for x in range(5))
g2 = g1
for y in g1:
    print(y)
    time.sleep(2)
for y in g2:
    print(y)
print(g1 is g2)

'''
Output:

0
1
4
9
16
True
'''






# 6. Comprehension type demonstration

l = [x * x for x in range(5)]
print(l)
print(type(l))
s = {x * x for x in range(5)}
print(s)
print(type(s))
d = {x: x * x for x in range(5)}
print(d)
print(type(d))
g = (x * x for x in range(5))
print(g)
print(type(g))

'''
Output:

[0, 1, 4, 9, 16]
<class 'list'>
{0, 1, 4, 9, 16}
<class 'set'>
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
<class 'dict'>
<generator object <genexpr> at 0x...>
<class 'generator'>
'''





# 7. return vs yield in functions

def f1():
    return 10
    return 20
    return 30
def f2():
    yield 10
    yield 20
    yield 30
# End of the function
print(f1())
print(f1())
print(f1())
print()
g = f2()
print(next(g))
print(next(g))
print(next(g))
print(next(g))

'''
Output:

10
10
10

10
20
30
StopIteration
'''
