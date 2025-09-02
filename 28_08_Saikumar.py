'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor changes
'''

s = input("Enter String: ")
s = s.upper()
vowels = set("AEIOU")
present = set(s).intersection(vowels)
freq = {}
for ch in sorted(present):
    freq[ch] = s.count(ch)
print(freq)


# Find outputs (Home work)

a = [('R', 'Red'), ('G', 'Green'), ('B', 'Blue')]
b = {'Y': 'Yellow', 'G': 'Gray'}
b.update(a)
print(b)       # {'Y': 'Yellow', 'G': 'Green', 'R': 'Red', 'B': 'Blue'}
a.update(b)    # 'list' object doesn't have 'update' method


#  Find outputs (Home work)

a = [(10, 20, 30), (40, 50, 60), (70, 80, 90)]
b = {}
b.update(a)    # Error: a can't be converted to dictionary so update can't be possible
print(b)       # {}
c = [(10,), (20,), (30,)]
b.update(c)    # Error: c can't be converted to dictionary so update can't be possible
print(b)       # {}


#  Find outputs (Home work)

d = {x: x ** 3 for x in range(5)}
print(d)        # {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
print(type(d))  # <class 'dict'>


# Find outputs (Home work)

d = {x: 2 * x for x in range(5)}
print(d)   # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}


# Find outputs (Home work)

a = {10: 'Rama', 15: 'Sita', 18: 'Rajesh', 17: 'Kiran', 12: 'Rama Rao'}
b = {k: v for k, v in a.items() if k % 2 != 0}
print(b)   # {15: 'Sita', 17: 'Kiran'}
c = {k: a[k] for k in a if a[k].startswith('R')}
print(c)   # {10: 'Rama', 18: 'Rajesh', 12: 'Rama Rao'}


# Find outputs  (Home  work)

def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
# End  of  the  function
print('Begin')
x = f1()
print(x)
print(type(x))
print('End')


'''
outputs:

Begin
Hyd
Sec
Cyb
None
<class 'NoneType'>
End
'''


# Find  outputs  (Home  work)
def  f1():
	return  10 , 20 , 30
# End  of  the  function
x = f1()
print(x)
print(type(x))
a , b , c =  f1()
print(a)
print(b)
print(c)
print('for  loop')
for  k   in  f1():
	print(k)

'''
outputs:

(10, 20, 30)
<class 'tuple'>
10
20
30
for  loop
10
20
30
'''


# Find  outputs

def f1():
    return 10     # Function exits here, never reaches 20 or 30
    return 20
    return 30
# End of the function
print('Begin')   # Begin
x = f1()
print(x)         # 10
print('End')     # End
#return 100       # Error: 'return' is outside function

'''
outputs:

Begin
10
End
'''


#  Find  outputs

f1()              # NameError: name 'f1' is not defined
def f1():
        print('Hello')
print(f1())       # Hello and None
print(f1)         # <function f1 at 0x7a4b8bb70180>


# Find  outputs  (Home  work)

print('Hello')      # Hello
def f1():
    print('f1  function')
# End of function
print('Hi')         # Hi
print(f1())         # f1  function
                    # None   (because f1() doesn’t return anything)
print(f1)           # <function f1 at 0x7a4b8bb70180>  
print('Bye')        # Bye


'''
outputs:

Hello
Hi
f1  function
None
<function f1 at 0x000001...>
Bye
'''


#  Find  outputs

def f1():
    print('Hyd')
    print('Sec')
    print('Cyb')
# End of the function
print('Begin')      # Begin
print(type(f1))     # <class 'function'>
print(id(f1))       # Some integer
print('End')        # End


#  Find  outputs (Home work)

def add(a, b):
    return a + b
# End of the function
print(add(10, 20))                          # 30   (int + int)
print(add('Hyder', 'abad'))                 # 'Hyderabad'   
print(add(10.8, 20.6))                      # 31.4   (float + float)
print(add(True, False))                     # 1   (True = 1, False = 0 → 1+0)
print(add(3 + 4j, 5 + 6j))                  # (8+10j)   (complex + complex)
print(add(25, 10.8))                        # 35.8   (int + float → float)
print(add([25, 10.8, 'Hyd'], [True, None, 3+4j, 'Sec'])) # [25, 10.8, 'Hyd', True, None, (3+4j), 'Sec']   (list + list → concatenation)
print(add(10, '20'))                        # Error: operand int and string is not concatenate


# Find  outputs (Home  work)

def f1():
    print('No-argument  function')
def f1(x):
    print('Single  argument  function  : ', x)
def f1(x, y):
    print('Two  argument  function : ', x, y)
def f1(x, y, z):
    print('Three  argument  function : ', x, y, z)
f1(10, 20, 30)   # Three  argument  function :  10 20 30
f1(40, 50)       # Error: f1() missing 1 required positional argument: 'z'
f1(60)           # Error: f1() missing 2 required positional arguments: 'y' and 'z'
f1()             # Error: f1() missing 3 required positional arguments: 'x', 'y', and 'z'


'''
Write   a  function  to  test  a  number  is  prime  (or)  not.
1) What  is  a  prime  number ?  ---> A  number  without  divisors  except  1  and  itself

2) Let  input  be  25
    What  is  the  range  of  divisors ? ---> i =   2 , 3 , 4 , 5 , 6 , .....  12

3) Let  input   be  11
    What  is   the  range  of  divisors ? ---> i =  2 , 3 , 4 , 5

4) What  action  to  be  made  if  'i'  is  not  a  divisor  of  input  number ?  ---> Move  to  the  next  element  of  range  object

5) What  action  to  be  made  if  'i'  is  a  divisor  of  input  number ?  --->  return   False

6) What  action  to  be  made  if  there  are  no  divisiors  to  input  number  ? ---> return  True  outside  the  loop
'''

def prime(n):
    if n <= 1:   
        return False
    for i in range(2, (n // 2) + 1):
        if n % i == 0:   
            return False
    return True
try:
    n = int(input("Enter a number: "))
    if prime(n):
        print("Prime number")
    else:
        print("Composite number")
except ValueError:
    print("Invalid input")


# Find  outputs  (Home  work)

def disp(empno , ename , sal):
    print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0)  # Output: Emp  Number  :  25 	   Emp Name  :  Rama  Rao 	   Salary  :  10000.0
disp('Sita' , 20000.0 , 35)       # Output: Emp  Number  :  Sita 	   Emp Name  :  20000.0 	   Salary  :  35



