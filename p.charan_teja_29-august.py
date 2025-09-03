def f1():
    print('No-argument function')
def f2(x):
    print('Single argument function:', x)
def f3(x, y):
    print('Two argument function:', x, y)
def f4(x, y, z):
    print('Three argument function:', x, y, z)

f1()
f2(1)
f3(1, 2)
f4(1, 2, 3)

Outputs:

text
No-argument function
Single argument function: 1
Two argument function: 1 2
Three argument function: 1 2 3







#Prime Numbers Between 2 and n

n = int(input("Enter n: "))
count = 0
for i in range(2, n+1):
    if prime(i):
        print(i)
        count += 1
print("Number of prime numbers: ", count)
For n=10, 

outputs:

text
2
3
5
7
Number of prime numbers: 4







def f1(a, b, c):
    print(f'a : {a} \t b : {b} \t c : {c}')


Function calls:

f1(a=10, b=20, c=30) Output: a : 10 b : 20 c : 30

f1(25, 10.8, 'Hyd') Output: a : 25 b : 10.8 c : Hyd

f1(b=40.7, a=50.2, c=60.5) Output: a : 50.2 b : 40.7 c : 60.5

f1(c='Hyd', b='Sec', a='Cyb') Output: a : Cyb b : Sec c : Hyd

f1(c=3+4j, a=True, b=None) Output: a : True b : None c : (3+4j)

f1(25, c=10.8, b='Hyd') Output: a : 25 b : Hyd c : 10.8

f1(a=100, 200, 300) SyntaxError: positional argument follows keyword argument

f1(True, None, b='Hyd') TypeError: multiple values for argument 'b'

f1(10, 20, x=30) TypeError: got an unexpected keyword argument 'x'

f1(10, 20) TypeError: missing 1 required positional argument: 'c'





#Keyword-Only Arguments

def f1(*, a, b):
    print(f'a : {a} \t b : {b}')

function calls:
f1(a=10, b=20) Output: a : 10, b : 20

f1(b=30, a=40) Output: a : 40, b : 30  
Invalid:

f1(50, 60) Error, positional arguments not allowed

f1(70, b=80) Error, positional arguments not allowed

f1(a=15, 25) Error, positional argument follows keyword argument








#Positional-Only Arguments

def f1(a, b, /):
    print(f'a : {a} \t b : {b}')

function calls:

f1(10, 20) Output: a : 10 b : 20  
Invalid:  
  
f1(a=30, b=40) Error, cannot use keywords for positional-only  
  
f1(50, b=60) Error, b must be positional-only  











#Functions With Both Positional-Only and Keyword-Only

def f1(a, b, /, c):
    print(f'a : {a} \t b : {b} \t c : {c}')

function calls:

f1(10, 20, 30) Output: a : 10 b : 20 c : 30

f1(40, 50, c=60) Output: a : 40 b : 50 c : 60
Invalid:

f1(a=70, b=80, c=90) Error, a and b are positional-only








#Default Arguments


def add(a, b=20, c=30):
    return a + b + c

function calls:
add(100) →  100 + 20 + 30  = 150  

add(100, 200) → 100 + 200 + 30 = 330   

add(100, 200, 300) → 100 + 200 + 300 = 600  









#Function Definition Errors

def f1(a=10, b, c=20, d):
    pass

# Error: non-default argument follows default argument

print(25, 10.8, 'Hyd', separator='\t')
# Error: 'separator' is wrong, should be 'sep'

print(25, 10.8, 'Hyd', endofline='\t')
# Error: 'endofline' not valid, should be 'end'

print(25, sep='\t', 10.8, end='\t', 'Hyd')
# Error: positional argument after keyword, and invalid syntax

