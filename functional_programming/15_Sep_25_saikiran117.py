# Write a generator to divide a string into words
def word_gen(s):
    for word in s.split():
        yield word

s = "Hyd is green city"
for w in word_gen(s):
    print(w)
# Enter any string : Hyd is green city
# Words of the string
# Hyd
# is
# green
# city

# Find outputs
def f1():
    yield [10, 20]
    yield {30, 40, 50}
    yield 60, 70, 80, 90
    yield 100
# End of generator
g = f1()
for x in g:
    print(x)
    print(type(x))
[10, 20]# <class 'list'>
{40, 50, 30}# <class 'set'>
(60, 70, 80, 90)# <class 'tuple'>
100# <class 'int'>

# Find outputs
def f1():
    x = 1
    while x <= 100000000000000000000:
        yield x
        x += 1
# End of generator
g = f1()
print('Begin')# Begin
print(*g)# prints numbers from 1 to very large number, may hang or run forever
print('End')# never reached

# Find outputs
g = (x * x for x in range(500000000000000000))
print(*g)# prints squares from 0 to very large number, may hang, immense output

# Find outputs (Home work)
def f1(begin, end):
    while begin <= end:
        print('Hello')
        yield begin
        begin += 1
    print('End of generator')
# end of the generator function
g = f1(10, 20)
print('Before')# Before
print(list(g))
Hello (11 times), End of generator, [10,11,12,13,14,15,16,17,18,19,20]
print('After')# After
print(next(g))# error

# Find outputs (Home work)
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
# One \n 1 \n Two \n 2 \n Three \n 3 \n End

x, y, z = f1()
print(x)# 1
print(y)# 2
print(z)# 3

# Identify error (Home work)
def f1():
    yield 10
    yield 20
    yield 30
    yield 40
a, b, c = f1()# error 
p, q, r, s, m = f1()# error 

# Find outputs (Home work)
def f1():
    yield 1
    yield 2
    yield 3
# End of generator
g = f1()
print(len(g))# error
print(g * 3)# error
print(g[0])# error
print(g[1 : 3])# error
print(*g)# 1 2 3
