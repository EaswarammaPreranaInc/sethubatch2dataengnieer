## Program to print distinct vowels of the string using set

s = input("Enter a string: ")

# convert to uppercase (case ignored)
s = s.upper()

# set of vowels
vowels = {'A', 'E', 'I', 'O', 'U'}

# collect distinct vowels from string
result = set()

for ch in s:
    if ch in vowels:
        result.add(ch)

# convert set to string
output = ''.join(sorted(result))   # sorting to maintain order A,E,I,O,U
print(output)

s = "RamA    raO"

## Convert to uppercase to ignore case
s = s.upper()

vowels = "AEIOU"
freq = {}

for v in vowels:
    count = s.count(v)
    if count > 0:
        freq[v] = count

print(freq)

# Find outputs (Home  work)
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a)
print(b)# {'Y': 'Yellow', 'G': 'Gray', 'R': 'Red', 'B': 'Blue'} 
a . update(b)# AttributeError: 'list' object has no attribute 'update'

#  Find  outputs  (Home  work)
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
b.update(a)
print(b)# {10: 20, 30: 40, 50: 60, 70: 80, 90: None}
c = [(10,) , (20,) , (30,)]
b . update(c)
print(b)# {10: None, 20: None, 30: None, 40: 50, 60: 70, 80: 90}

#  Find  outputs (Home  work)
d = {x : x ** 3   for    x   in  range(5)}
print(d)# {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
print(type(d))# <class 'dict'>

# Find outputs   (Home  work)
d = { x :  2 * x    for    x   in   range(5) }
print(d)# {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

# Find outputs  (Home  work)
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b)# {15: 'Sita', 17: 'Kiran'}
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c)# {10: 'Rama', 12: 'Rama Rao', 18: 'Rajesh'}

# Find outputs  (Home  work)
def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
# End  of  the  function
print('Begin')
x = f1()
print(x)# None
print(type(x))# <class 'NoneType'>
print('End')# End

# Find  outputs  (Home  work)
def  f1():
	return  10 , 20 , 30
# End  of  the  function
x = f1()
print(x)# (10, 20, 30)
print(type(x))# <class 'tuple'>
a , b , c =  f1()
print(a)# 10
print(b)# 20
print(c)# 30
print('for  loop')
for  k   in   f1():
	print(k)# 10
#20
#30

# Find  outputs
def    f1():
        return  10
        return  20
        return  30
# End  of  the  function
print('Begin')# Begin
x = f1()# 10
print(x)# 10
print('End')# End
return   100# SyntaxError: 'return' outside function

#  Find  outputs
f1()
def   f1():
        print('Hello')# Hello
print(f1())# Hello
print(f1)# None

# Find  outputs  (Home  work)
print('Hello')# Hello
def  f1():
        print('f1  function')# f1  function
#End  of   function
print('Hi')# Hi
print(f1())# f1  function
print(f1)# <function f1 at 0x000001E2B3C8B700>
print('Bye')# Bye

#  Find  outputs
def    f1():
        print('Hyd')# Hyd
        print('Sec')# Sec
        print('Cyb')# Cyb
#End  of  the  function
print('Begin')# Begin
print(type(f1))# <class 'function'>
print(id(f1))# 140735579828688
print('End')# End

#  Find  outputs (Home  work)
def   add(a , b):
        return  a + b
#End  of  the  function
print(add(10 , 20))# 30
print(add('Hyder' , 'abad'))# Hyderabad
print(add(10.8 , 20.6))# 31.4
print(add(True , False))# 1
print(add(3 + 4j , 5 + 6j))# (8+10j)
print(add(25 , 10.8))# 35.8
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec']))# [25, 10.8, 'Hyd', True, None, (3+4j), 'Sec']
print(add(10 , '20'))# TypeError: unsupported operand type(s) for +: 'int' and 'str'
          
# Find  outputs (Home  work)
def  f1():
	print('No-argument  function')# No-argument  function
def  f1(x):
	print('Single  argument  function  : ' , x)# Single  argument  function  :  x
def  f1(x , y):
	print('Two  argument  function : ' , x , y)# Two  argument  function :  x  y
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)# Three  argument  function :  x  y  z
f1(10 , 20 , 30)# Three  argument  function :  10  20  30
f1(40 , 50)# Two  argument  function :  40  50
f1(60)# Single  argument  function  :  60
f1()# TypeError: f1() missing 3 required positional arguments: 'x', 'y', and 'z'

##11. Write a function to check whether a number is prime or not.
def prime(n):
    if n <= 1:   # 0, 1, and negatives are not prime
        return False
    
    for i in range(2, int(n**0.5) + 1):   # check up to sqrt(n)
        if n % i == 0:   # divisor found
            return False
    return True   # no divisors found
## Input from user and check
try:
    n = int(input("Enter a number: "))
    if prime(n):
        print("Prime number")
    else:
        print("Composite number")
except ValueError:
    print("Invalid input")

# Find  outputs  (Home  work)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')# Emp  Number  :  empno 	  Emp Name  :  ename 	  Salary  :  sal
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0)# Emp  Number  :  25 	  Emp Name  :  Rama  Rao 	  Salary  :  10000.0
disp('Sita' , 20000.0 , 35)# TypeError: disp() missing 1 required positional argument: 'sal'