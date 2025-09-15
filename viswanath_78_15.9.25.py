q)Write  a  generator  to  divide  a  string  into  words
Hint1:  Use  generator  function  and  for   loop
Hint2:  Use  split()  method  of  str  class
Ans) def f1(a):
    b = a.split() 
    for x in b:
        yield x
a = eval(input('enter the string : '))
g = f1(a)
for x in g:
    print(x)

def f1():
    yield [10, 20]
    yield {30, 40, 50}
    yield 60, 70, 80, 90
    yield 100
# End of generator
g = f1()
for x in g:
    print(x)          # [10, 20]
                      # {40, 50, 30}
                      # (60, 70, 80, 90)
                      # 100
    print(type(x))    # <class 'list'>
                      # <class 'set'>
                      # <class 'tuple'>
                      # <class 'int'>

def f1():
    x = 1
    while x <= 100000000000000000000:
        yield x
        x += 1
# End of generator

g = f1()
print('Begin')  # Begin
print(*g)    # Error: Infinite / too large output, Memory Error
print('End')  # End

g = (x * x for x in range(500000000000000000))
print(*g)  # Error: Infinite / too large output, Memory Error

def f1(begin, end):
    while begin <= end:
        print('Hello')          # Hello (printed each time before yielding a value)
        yield begin             # yields 10, 11, 12, ..., 20
        begin += 1
    print('End of generator')   # End of generator (printed when loop ends)
# end of the generator function
g = f1(10, 20)
print('Before')   # Before
print(list(g))    # Hello (11 times total)
                  # End of generator
                  # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print('After')    # After
print(next(g))    # Error: generator is already exhausted (StopIteration)

def f1():
    print('One')
    yield 1
    print('Two')
    yield 2
    print('Three')
    yield 3
    print('End')
# End of generator
g = f1()
for m in g:
    print(m)
x, y, z = f1()
print(x)
print(y)
print(z)
Output:
# One
# 1
# Two
# 2
# Three
# 3
# End
# One
# Two
# Three
# End
# 1
# 2
# 3

def f1():
    yield 10
    yield 20
    yield 30
    yield 40
a, b, c = f1()  # Error: too many values to unpack (expected 3)
p, q, r, s, m = f1()# Error: not enough values to unpack (expected 5, got 4)

def f1():
    yield 1
    yield 2
    yield 3
g = f1()
print(len(g)) # Error: 'generator' object has no len()
print(g * 3)  # Error: unsupported operand type(s) for *: 'generator' and 'int'
print(g[0])   # Error: 'generator' object is not subscriptable
print(g[1:3]) # Error: 'generator' object is not subscriptable
print(*g)  # 1 2 3
