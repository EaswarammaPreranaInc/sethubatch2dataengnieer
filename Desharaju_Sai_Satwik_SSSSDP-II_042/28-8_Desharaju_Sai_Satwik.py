a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b.update(a)
print(b)   # {'Y': 'Yellow', 'G': 'Green', 'R': 'Red', 'B': 'Blue'}
a.update(b)   # error


a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
b.update(a)
print(b)   # {10: 20, 40: 50, 70: 80}
c = [(10,) , (20,) , (30,)]
b.update(c)   # error
print(b)

d = {x : x ** 3   for    x   in  range(5)}
print(d)        # {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
print(type(d))  # <class 'dict'>

d = { x :  2 * x    for    x   in   range(5) }
print(d)   # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b)   # {15: 'Sita', 17: 'Kiran'}
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c)   # {10: 'Rama', 18: 'Rajesh', 12: 'Rama Rao'}

def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Begin')
x = f1()
print(x)         # None
print(type(x))   # <class 'NoneType'>
print('End')
# Begin
# Hyd
# Sec
# Cyb
# None
# <class 'NoneType'>
# End

def  f1():
	return  10 , 20 , 30
x = f1()
print(x)         # (10, 20, 30)
print(type(x))   # <class 'tuple'>
a , b , c =  f1()
print(a)         # 10
print(b)         # 20
print(c)         # 30
print('for  loop')
for  k   in   f1():
	print(k)     # 10 \n 20 \n 30

def    f1():
        return  10
        return  20
        return  30
print('Begin')
x = f1()
print(x)   # 10
print('End')
return   100   # error

f1()   # error
def   f1():
        print('Hello')
print(f1())   # Hello \n None
print(f1)     # <function f1 at 0x...>

print('Hello')   # Hello
def  f1():
        print('f1  function')
print('Hi')      # Hi
print(f1())      # f1  function \n None
print(f1)        # <function f1 at 0x...>
print('Bye')     # Bye

def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Begin')       # Begin
print(type(f1))      # <class 'function'>
print(id(f1))        # (some id)
print('End')         # End

def   add(a , b):
        return  a + b
print(add(10 , 20))                          # 30
print(add('Hyder' , 'abad'))                 # Hyderabad
print(add(10.8 , 20.6))                      # 31.4
print(add(True , False))                     # 1
print(add(3 + 4j , 5 + 6j))                  # (8+10j)
print(add(25 , 10.8))                        # 35.8
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec']))  
# [25, 10.8, 'Hyd', True, None, (3+4j), 'Sec']
print(add(10 , '20'))                        # error

def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30)   # Three  argument  function :  10 20 30
f1(40 , 50)        # error
f1(60)             # error
f1()               # error

def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
disp(25 , 'Rama  Rao' , 10000.0)  
# Emp  Number  :  25 	  Emp Name  :  Rama  Rao 	  Salary  :  10000.0
disp('Sita' , 20000.0 , 35)  
# Emp  Number  :  Sita 	  Emp Name  :  20000.0 	  Salary  :  35

# Prime Number Program
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

try:
    n = int(input("Enter number: "))
    if prime(n):
        print("Prime number")
    else:
        print("Composite number")
except:
    print("Invalid input")
