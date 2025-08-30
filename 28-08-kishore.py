''' 
q) Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)
Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}
Hint:  Same  as  prog23a  with  minor  changes

'''

s = input('enter the list = ')
s = s.upper()
x = set(s)
y = 'AEIOU'
m = x.intersection(y)
a = {}
for ch in sorted(m):
    if ch.isalpha():
        a[ch] = a.get(ch, 0) + 1
print(a)


a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a)
print(b)                     # {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue', 'Y' : 'Yellow'}
a . update(b)                # Error : list doesn’t have update method

a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
b.update(a)  
print(b)                     # Error: each tuple has 3 elements, dictionary update needs 2 (key, value)
c = [(10,) , (20,) , (30,)]
b.update(c)  
print(b)                     # Error: each tuple has 1 element, dictionary update needs 2 (key, value)

d = {x : x ** 3   for    x   in  range(5)}
print(d)                      # {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
print(type(d))                # <class 'dict'>

d = { x :  2 * x    for    x   in   range(5) }
print(d)  {0: 0, 1: 2, 2: 4, 3:6 , 4: 8}

a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b)                          # {15: 'Sita', 17: 'Kiran'}
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c)                           # {10: 'Rama', 18: 'Rajesh', 12: 'Rama Rao'}


def f1():
	print('Hyd')                    # Hyd
	print('Sec')                    # Sec
	print('Cyb')                    # Cyb
# End of the function
print('Begin')                    # Begin
x = f1()   
print(x)                          # None
print(type(x))                    # <class 'NoneType'>
print('End')                      # End

def f1():
    return 10, 20, 30              # returning multiple values as a tuple
# End of the function
x = f1()
print(x)               # (10, 20, 30)
print(type(x))         # <class 'tuple'>
a, b, c = f1()         # unpacking the tuple
print(a)               # 10
print(b)               # 20
print(c)               # 30
print('for loop')
for k in f1():         # iterating over tuple elements
    print(k)           # 10 \n 20 \n 30

f1()                     # Error: function is called before it is defined
def f1():
    print('Hello')      # Hello
print(f1())             # None
print(f1)               # <function f1 at  some address>

print('Hello')          # Hello
def f1():
    print('f1  function')             # f1  function
#End  of   function
print('Hi')                           # Hi
print(f1())                           # None
print(f1)                             # <function f1 at 0x...>
print('Bye')                          # Bye

def f1():
    print('Hyd')                      # nothing printed yet, function not called
    print('Sec')                      # nothing printed yet, function not called
    print('Cyb')                      # nothing printed yet, function not called
# End of the function
print('Begin')                        # Begin
print(type(f1))                       # <class 'function'>
print(id(f1))                         # Some unique memory id (e.g. 140239187943744)
print('End')                          # End

def f1():
        print('Hyd')                  # nothing printed yet, function not called
        print('Sec')                  # nothing printed yet, function not called
        print('Cyb')                  # nothing printed yet, function not called
#End of the function
print('Begin')                        # Begin
print(type(f1))                       # <class 'function'>
print(id(f1))                         # some unique memory address (e.g., 140724377338768)
print('End')                          # End

def add(a , b):
        return  a + b
#End  of  the  function
print(add(10 , 20))                     # 30
print(add('Hyder' , 'abad'))            # Hyderabad
print(add(10.8 , 20.6))                 # 31.4
print(add(True , False))                # 1
print(add(3 + 4j , 5 + 6j))             # (8+10j)
print(add(25 , 10.8))                   # 35.8
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec']))   # [25, 10.8, 'Hyd', True, None, (3+4j), 'Sec']
print(add(10 , '20'))                   # Error: cannot add int and str

def  f1():
    print('No-argument  function')
def  f1(x):
    print('Single  argument  function  : ' , x)
def  f1(x , y):
    print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
    print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30)                        # Works → Three  argument  function :  10 20 30
f1(40 , 50)                             # Error: missing 1 required positional argument 'z'
f1(60)                                  # Error: missing 2 required positional arguments 'y' and 'z'
f1()                                    # Error: missing 3 required positional arguments 'x', 'y', and 'z'

q)Write   a  function  to  test  a  number  is  prime  (or)  not.
1) What  is  a  prime  number ?  ---> A  number  without  divisors  except  1  and  itself
2) Let  input  be  25
What  is  the  range  of  divisors ? ---> i =   2 , 3 , 4 , 5 , 6 , .....  12
3) Let  input   be  11
    What  is   the  range  of  divisors ? ---> i =  2 , 3 , 4 , 5
4) What  action  to  be  made  if  'i'  is  not  a  divisor  of  input  number ?  ---> Move  to  the  next  element  of  range  object
5) What  action  to  be  made  if  'i'  is  a  divisor  of  input  number ?  --->  return   False
6) What  action  to  be  made  if  there  are  no  divisiors  to  input  number  ? ---> return  True  outside  the  loop
Ans) def f1():
    if a<=1:
        return False
    for x in range(2,a//2,1):
        if a%x == 0:
            return False
    return True    
#end of the function
try:
a = int(input('Enter the number : '))
if f1():
    print('prime number')
else:
    print('composite number')
except:
    print('Invalid Input')

def disp(empno , ename , sal):
    print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End of the function
disp(25 , 'Rama Rao' , 10000.0)  
# Emp  Number  :  25 	 Emp Name  :  Rama Rao 	 Salary  :  10000.0
disp('Sita' , 20000.0 , 35)  
# Emp  Number  :  Sita 	 Emp Name  :  20000.0 	 Salary  :  35
