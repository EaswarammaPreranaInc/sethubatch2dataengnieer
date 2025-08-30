def f1(x=None, y=None, z=None):
    if x is None and y is None and z is None:
        print("No-argument function")
    elif y is None and z is None:
        print("Single argument function :", x)
    elif z is None:
        print("Two argument function :", x, y)
    else:
        print("Three argument function :", x, y, z)

# Test all
f1()
f1(10)
f1(10, 20)
f1(10, 20, 30)

#Prime numbers 
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


n = int(input("Enter a number : "))
count = 0
print("Prime numbers:")
for i in range(2, n+1):
    if prime(i):
        print(i)
        count += 1

print("Number of prime numbers :", count)


def f1(a, b, c):
    print(f'a : {a} \t b : {b} \t c : {c}')

# Function calls
f1(a=10, b=20, c=30)
f1(25, 10.8, 'Hyd')
f1(b=40.7, a=50.2, c=60.5)
f1(c='Hyd', b='Sec', a='Cyb')
f1(c=3+4j, a=True, b=None)
f1(25, c=10.8, b='Hyd')
f1(a=100, 200, 300)    # Error: positional arg after keyword arg
f1(True, None, b='Hyd')
f1(10, 20, x=30)       # Error: unexpected keyword argument 'x'
f1(10, 20)             # Error: missing required argument 'c'


def disp(empno, ename, sal):
    print(f'Emp Number : {empno:4} \t Emp Name : {ename:15} \t Salary : {sal}')

disp(25, 'Rama Rao', 10000.0)  
# Output: Emp Number :   25     Emp Name : Rama Rao        Salary : 10000.0

disp(ename='Sita', sal=20000.0, empno=35)  
# Output: Emp Number :   35     Emp Name : Sita            Salary : 20000.0

x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x, y, z)  
# Output: Emp Number : Rama  Rao    Emp Name : 30000.0         Salary : 20


def f1(a, b, c):
    return a + b * c

print(f1(3, 4, 5))  
# Output: 23

print(f1(*[6, 7, 8]))  
# Output: 62

# print(f1([6, 7, 8])) ERROR (missing 2 arguments)

print(f1(*{1:2, 3:4, 5:6}))  
# Output: 27   (order depends on dict keys but usually {1,3,5})

print(f1({'c':2,'b':4,'a':6}))  
# ERROR (missing 2 arguments)

print(f1({'c':2,'b':4,'a':6}))  
# ERROR again

# print({{'c':2,'b':4,'a':6}}) ERROR (set inside set not allowed)

print(f1({'c':2,'a':4,'x':6}))  
# ERROR (missing 2 arguments)


a = [10, 20, 15, 5, 12]

# print(sorted(reverse=True, a)) ERROR (positional after keyword)
# print(sorted(a, rev=True)) ERROR (invalid keyword 'rev')

# print(25, 10.8, 'Hyd', separator='\t') ERROR (invalid keyword 'separator')

# print(25, 10.8, 'Hyd', endofline='\t') ERROR (invalid keyword 'endofline')

# print(25, sep='\t', 10.8, end='\t', 'Hyd') ERROR (positional after keyword)



# Keyword only arguments demo program
def f1(*, a, b):
    print(F'a  :  {a}  \t  b :  {b}')
# End of the function

f1(a = 10 , b = 20)     # a  :  10 	 b :  20
f1(b = 30 , a = 40)     # a  :  40 	 b :  30
f1(50 , 60)             # Error: takes 0 positional arguments but 2 were given
f1(70 , b = 80)         # Error: a missing
f1(a = 15 , 25)         # Error: positional argument follows keyword argument


# Keyword-only after one positional
def f1(a , * , b , c):
    print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End of function

f1(10 , b = 20 , c = 30)         # a  :  10 	 b :  20 	 c  :  30
f1(a = 40 , b = 50 , c = 60)     # a  :  40 	 b :  50 	 c  :  60
f1(c = 100 , b = 90 , a = 80)    # a  :  80 	 b :  90 	 c  :  100
f1(70 , 80 , c = 90)             # Error: takes 1 positional argument but 2 were given
f1(70 , 80 , 90)                 # Error: too many positional arguments
f1(c = 15 , b = 25 , 35)         # Error: positional argument after keyword argument


# Identify error
def f1(a , b , *):
    pass
# Error: invalid syntax (* must be named like *args or *)


# Positional only arguments demo program
def f1(a , b , /):
    print(F'a  :  {a}  \t  b  :  {b}')
# End of the function

f1(10 , 20)           # a  :  10 	 b :  20
f1(a = 30 ,  b = 40)  # Error: got some positional-only arguments passed as keyword arguments
f1(50 , b = 60)       # Error: got some positional-only arguments passed as keyword arguments
f1(a = 70 , 80)       # Error: positional argument follows keyword argument


# Find outputs (Home work)
def f1(a , b , / , c):
    print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End of function

f1(10 , 20 , 30)              # a: 10   b: 20   c: 30
f1(40 , 50 , c = 60)          # a: 40   b: 50   c: 60
f1(a = 70 , b = 80 , c = 90)  # Error: a and b are positional-only
f1(a = 100 , b = 110 , 120)   # SyntaxError: positional arg follows keyword arg
f1(a = 130 , 140 , c = 150)   # SyntaxError: positional arg follows keyword arg
f1(160 , b = 170 , 180)       # Error: b is positional-only, cannot use keyword
f1(190 , b = 200 , c = 210)   # Error: b is positional-only


# Find outputs(Home work)
def f1(a , b , / , c , d , * , e , f):
    print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function

f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60)  # a:10 b:20 c:30 d:40 e:50 f:60
f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6) # Error: b is positional-only
f1(1 , 2 , 3 , 4 , 5 , f = 6)                 # Error: e missing
f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60)  # SyntaxError: positional after keyword
f1(10 , 20 , 30 , 40 , e = 50 , f = 60)      # a:10 b:20 c:30 d:40 e:50 f:60


def f1(/ , a , b ,  c):
    pass
# SyntaxError: "/" must appear before arguments

def f2(a , b , c , *):
    pass
# SyntaxError: "*" must be followed by argument name or used alone

def f4(* , a , b , c , /):
    pass
# SyntaxError: cannot have * before / (order invalid)

# Find outputs (Home work)
def f1(x):
    print('1st  function : ' , x)

def f1(y):
    print('2nd  function : ' , y)

def f1(z):
    print('3rd  function : ' , z)

f1(z = 10)  # 3rd function : 10
f1(y = 20)  # 3rd function : 20
f1(x = 30)  # 3rd function : 30


# Default arguments demo program
def add(a, b=20, c=30):
    return a + b + c

print(add(100))                  # 150
print(add(100, 200))             # 330
print(add(100, 200, 300))        # 600
print(add(100, c=200))           # 320
print(add(c=100, b=200, a=300))  # 600
print(add(c=100, a=200))         # 320
# print(add())  Error: missing required argument 'a'
# print(add(a=100 , 200))  Error: positional argument after keyword
# print(add(100 , , 300))  Syntax Error
# print(add(100 ,  b , 300)) 'b' not defined


# default arguments must come AFTER non-defaults
# def f1(a=10, b, c=20, d):   # Error
# Correct version:
def f2(b, d, a=10, c=20):
    pass

#Find outputs
def f1(a=10):
    print(a)

f1(20)        # 20
f1()          # 10
f1(a=30)      # 30


# Find outputs
def add(a, b, c=10, d=20):
    return a + b + c + d

print(add(100, 200))                    # 330
print(add(100, 200, 300))               # 620
print(add(100, 200, 300, 400))          # 1000
print(add(b=100, a=200))                # 330
print(add(100, 200, d=300))             # 600
print(add(d=100, a=200, b=300))         # 610
# print(add(c=100, d=200, 300, 400)) Error: positional after keyword
# print(add(100, 200, c=300, x=400)) Error: unexpected keyword x
# print(add()) Error: missing arguments


# Find outputs
def f1(x=25):
    return x

def f2(x):
    return x

print(f1(10))    # 10
print(f1())      # 25
print(f2(20))    # 20
# print(f2()) Error: missing required argument 'x'


# 6. Find outputs
def disp(ch='*', n=4):
    print(ch * n)

disp('-', 6)               # ------
disp('$')                  # $$$$
disp()                     # ****
disp(n=5)                  # *****
# disp(5) prints 5555 (since ch=5, repeated 4 times)
disp(n=7, ch='%')          # %%%%%%%
# disp(7, '@') '@' not valid here (wrong order)
# disp(7, n=6) multiple values for 'n'
# disp(ch='!', 5) Syntax Error


# Find outputs
def power(a, b=2):
    return a ** b

print(power(2, 6))            # 64
print(power(5))               # 25
print(power(b=3, a=4.5))      # 91.125
print(power(3 + 4j))          # (3+4j)^2 = (-7+24j)
print(power(True))            # 1
# def power(b=2, a): Syntax Error (default before non-default)


# Function overriding (only last one works)
def add(a, b):
    print('2-argument function')
    return a + b

def add(a, b, c):
    print('3-argument function')
    return a + b + c

def add(a=1, b=2, c=3, d=4):
    print('4-argument function')
    return a + b + c + d

print(add(10, 20, 30, 40))   # "4-argument function", 100
print(add(50, 60, 70))       # "4-argument function", 186
print(add(80, 90))           # "4-argument function", 179
print(add(100))              # "4-argument function", 107
print(add())                 # "4-argument function", 10


# disp overriding
def disp(a, b):
    print('2-argument function :', a, b)

def disp(a, b, c, d):
    print('4-argument function :', a, b, c, d)

def disp(a, b, c=25):
    print('3-argument function :', a, b, c)

disp(10, 20, 30)       # "3-argument function : 10 20 30"
disp(40, 50, 60, 70)   # "3-argument function : 40 50 60" (last def wins, ignores d)
disp(80, 90)           # "3-argument function : 80 90 25"

# Keyword-only arguments
def add(*, a=10, b=20):
    return a + b

print(add(a=30, b=40))   # 70
print(add())             # 30
print(add(a=50))         # 70
print(add(b=60, a=70))   # 130
# print(add(80, 90)) Error: must use keywords

# Keyword-only arguments again
# def add(a=10, b, c): Error: non-default follows default
def add(*, a=10, b, c):
    return a + b + c

print(add(a=30, b=40, c=50))     # 120
print(add(b=60, c=70))           # 140
print(add(c=80, b=90, a=100))    # 270
# print(add(c=25, a=43)) Error: missing 'b'
# print(add(1, 2, 3)) Error: positional args not allowed
