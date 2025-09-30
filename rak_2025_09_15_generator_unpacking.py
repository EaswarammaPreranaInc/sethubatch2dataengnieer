'''
Write a generator to divide a string into words

Hint1: Use generator function and for loop

Hint2: Use split() method of str class

Enter any string : Hyd is green city
Words of the string
Hyd
is
green
city
'''
import time
def gen(string):
    lst = string.split()
    for x in lst:
        yield x
string = input('Enter the string:  ')
for x in gen(string):
    print(x)
    time.sleep(1)
        


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
'''
[10, 20]
<class 'list'>
{30, 40, 50}
<class 'set'>
(60, 70, 80, 90)
<class 'tuple'>
100
<class 'int'>
'''



# Find outputs
def f1():
    x = 1
    while x <= 100000000000000000000:
        yield x
        x += 1
# End of generator
g = f1()
print('Begin')           #Begin
print(*g)                #creates memeory error
print('End')




# Find outputs
g = (x * x for x in range(500000000000000000))
print(*g)                                        #creates memeory error




# Find outputs (Home work)
def f1(begin, end):
    while begin <= end:
        print('Hello')
        yield begin
        begin += 1
    print('End of generator')
#end of the genrator function
g = f1(10, 20)
print('Before')                    #Before
print(list(g))                     #Hello <sp> Hello <sp> 11 times
print('After')                     #After
# print(next(g))                   #StopIteration Error
'''
Before
Hello
Hello
.
.
11 times
End of generator
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
After
'''

# '''
# 1) What are the four events for list(g) ? ---> 
#     a) generator function is fully executed without stopping in the middle even though there is yield statement
#     b) All those elements which are yielded are stored in generator object (Non-empty object)
#     c) generator object is converted to list
#     d) generator object becomes empty

# 2) What are the two drawbacks of list(g) ? ---> 
#     a) Waiting time when there are too many yield statements
#     b) Possibility of MemoryError

# 3) Hence list(g) is not recommended for generator as we are losing the power of generator
# '''


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
x, y, z = f1()  
print(x)
print(y)
print(z)
'''
One
1
Two
2
Three
3
End
One
Two
Three
End
1
2
3
'''


# Identify error (Home work)
def f1():
    yield 10
    yield 20
    yield 30
    yield 40
# a, b, c = f1()             #4 values are being yeilded, but only 3 on left
# p, q, r, s, m = f1()       #4 values are being yeilded, but 5 on left


# Find outputs (Home work)
def f1():
    yield 1
    yield 2
    yield 3
# End of generator
g = f1()
# print(len(g))              #error, g is generator not sequenec
# print(g * 3)               #error, generator is empty so it can't be repeated
# print(g[0])                #error, generator do not have indices
# print(g[1:3])              #error, generator do not have indices
print(*g)                    #1 <sp> 2 <sp> 3
