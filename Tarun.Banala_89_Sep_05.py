#TARUN BANALA    05-09-2025
#  Find  outputs  (Home  work)
def  change(b):
	b.append(25)
	b[2] = 17
	del  b[1]
# End  of  the  function
a = [10 , 20 , 15 , 18]
print(a)                   # [10, 20, 15, 18]

change(a)
print(a)                   # [10, 17, 25]

# Find  outputs  (Home  work)
def  change(b):
	b  = [50 , 60 , 70 , 80]
	print(b)               # [50, 60, 70, 80]
# End  of  the  function
a = [10 , 20 , 30 , 40]
print(a)                   # [10, 20, 30, 40]
change(a)
print(a)                   # [10, 20, 30, 40]

#  Find  outputs  (Home  work)
def   f1(x):
	x = 20
	print(x)              # 20
# End  of   the   function
x = 10
print(x)                  # 10
f1(x)
print(x)                  # 10

#  Find  outputs  (Home  work)
def  f1(b):
	b[2] = 25
#end  of  the  function
a = (10 , 20 , 15 , 18)
print(a)                  # (10, 20, 15, 18)
try:
    f1(a)
    print(a)
except TypeError as e:
    print(f"TypeError: {e}")  # TypeError: 'tuple' object does not support item assignment

# Find  outputs (Home  work)
square = lambda  x = 10  :   x * x
print(square(5))          # 25
print(square())           # 100

# Find  outputs  (Home  work)
print((lambda   x  :   x * x) (7))        # 49
print(lambda   x  :  x * x(7))           # <function <lambda> at 0x...>
print(lambda   x  :   x * x)             # <function <lambda> at 0x...>
print((lambda  x = 25 :  x * x) ())     # 625
square = lambda  x :  x  *  x
print(square(5))                          # 25

# Find  output (Home  work)
add = lambda x, y: x + y
print(type(add))          # <class 'function'>
print(add(10 , 20))       # 30
print(add(10.6 , 20.8))   # 31.4
print(add('Hyder' , 'abad'))  # 'Hyderabad'
print(add(True , False))  # 1
print(add(25 , 10.8))     # 35.8
print(add(3 + 4j , 5 + 6j))  # (8+10j)
try:
    print(add(10 , '20'))     # TypeError
except TypeError as e:
    print(f"TypeError: {e}")
try:
    print(add())              # TypeError
except TypeError as e:
    print(f"TypeError: {e}")
print(add)                # <function <lambda> at 0x...>

#  Find  outputs (Home  work)
add = lambda  a = 1 , b = 2 :  a + b
print(add(10 , 20))       # 30
print(add())              # 3

#  Find  outputs (Home work)
print((lambda  x , y : x + y) (10 , 20))        # 30
print((lambda  x , y : x + y) (10.8 , 20.6))     # 31.4
print((lambda  x , y : x + y) ('Hyder' , 'abad'))  # 'Hyderabad'
print(lambda  x , y : x + y  ('Hyder'  ,  'abad'))  # <function <lambda> at 0x...>

#  Find  outputs (Home  work)
large = lambda x, y: x if x > y else y
print(large(10 , 20))       # 20
print(large(10.7 , 5.6))    # 10.7
print(large('g' , 's'))     # 's'
print(large('Rama' , 'Rajesh'))  # 'Rama'
print(large(True , False))  # True

#Find  outputs (Home  work)
power = lambda  a = 3.5 , b = 2  :  a ** b
print(power(2 , 3))       # 8
print(power(4.5 , 4))     # 410.0625
print(power())            # 12.25
print(power(9))           # 81

# Find  outputs
all_func = lambda  a , b :  (a + b ,  a - b , a * b , a / b)
x = all_func(10 , 7)
print(type(x))            # <class 'tuple'>
print(x)                  # (17, 3, 70, 1.4285714285714286)
p , q , r , s = all_func(9 , 2)
print(p)                  # 11
print(q)                  # 7
print(r)                  # 18
print(s)                  # 4.5

#  Find  outputs
a_func  =  lambda  :  'Hyd'
print(a_func())                # 'Hyd'
print(a_func)                  # <function <lambda> at 0x...>

# Find  outputs
a_func2  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a_func2())                # Hyd\nSec\nCyb\nNone

# Find  outputs (Home  work)
a_func3  =  lambda  : 'Hyd' ;  print('Sec') ;  print('Cyb')
print(a_func3())                # Sec\nCyb\n'Hyd'

# Find  outputs   (Home  work)
a_func4  =  lambda  :  (print('Hyd'), print('Sec'), print('Cyb'))
print(type(a_func4))            # <class 'function'>
print(a_func4)                  # <function <lambda> at 0x...>
try:
    for  x  in  a_func4:
        print(x)
except TypeError as e:
    print(f"TypeError: {e}")    # TypeError: 'function' object is not iterable
result = a_func4()              # Hyd\nSec\nCyb
print(result)                   # (None, None, None)
try:
    print(a_func4[0]())
except TypeError as e:
    print(f"TypeError: {e}")    # TypeError: 'function' object is not subscriptable

#  Find  outputs  (Home  work)
s = 'Hyd'
print(lambda  s  :  print(s))            # <function <lambda> at 0x...>
print(lambda  x  :  print(x) (s))        # <function <lambda> at 0x...>
print((lambda  x  :  print(x)) (s))      # Hyd\nNone
(lambda  x  :  print(x)) (s)             # Hyd

# Find outputs  (Home  work)
x = 5
adder1 = lambda  y , x = x  : x + y
x = 10
adder2 = lambda  y , x = x : x + y
x = 20
print(adder1(100))        # 105
print(adder2(200))        # 210
print(adder1(300 , 400))  # 700

#Find  outputs  (Home  work)
a_list = [lambda   x  :  x ** 2 , lambda   x  :  x ** 3 ,  lambda   x  :  x ** 4]
for   fun   in   a_list:
        print(fun(5))     # 25\n125\n625

#  Find  outputs
def   f1():
	print('Hyd')
def   f2():
	print('Sec')
a_funcs = [f1 , f2]
for  x  in  a_funcs:
	x()              # Hyd\nSec

# Find output  (Home  work)
a_dict = {'power_2'  :  lambda   x  :  x ** 2 ,
       'power_3'  :  lambda   x  :  x ** 3 ,
  	   'power_4'  :  lambda   x  :  x ** 4}
key = 'power_3'
print(a_dict[key])              # <function <lambda> at 0x...>
print(a_dict[key](5))           # 125

# Find  outputs  (Home  work)
def   f1(x):
        return  lambda  n  :  x ** n
lamb = f1(3)
print(type(f1))            # <class 'function'>
print(type(lamb))          # <class 'function'>
print(lamb(2))             # 9
print(lamb(5))             # 243
print(lamb)                # <function f1.<locals>.<lambda> at 0x...>
try:
    print(lamb())              # TypeError
except TypeError as e:
    print(f"TypeError: {e}")

# Find  outputs   (Home  work)
def   eval_func(a , b , c):
        return   lambda    x  :    a *   x **  2  +   b * x  +  c
lam  = eval_func(3 , 4 , 5)
print(lam(2))              # 25
print(lam(2.5))            # 33.75
print(lam(4))              # 69

#Nested  lambda  function  (Home  work)
add_nested  =  lambda    x = 10   :    lambda   y  :  x  +  y
a_func5 = add_nested()
print(a_func5(20))               # 30
print(add_nested(30)(40))         # 70

# Find  outputs
a_tuples = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0) , (15 ,'Rajesh' , 500.0) ,  (18 , 'Kiran' , 2800.0) , (5 , 'Amar' , 1300.0))
b = sorted(a_tuples)
print(b)                   # [(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]

c = sorted(a_tuples , reverse = True)
print(c)                   # Reverse sorted

d = sorted(a_tuples ,  key =  lambda   x  :  x[1])
print(d)                   # Sorted by name

e = sorted(a_tuples , key =  lambda   x  :  x[2])
print(e)                   # Sorted by salary

f = sorted(a_tuples , key = lambda   x  :  x[0])
print(f)                   # Same as b

g = sorted(a_tuples , key = lambda  x : x[1] , reverse = True)
print(g)                   # Reverse sorted by name

# Find outputs  (Home  work)
cars = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b_cars = sorted(cars , key = lambda  x  :  x['Year'])
print(b_cars)                   # Sorted by year
try:
    print(sorted(cars))           # TypeError
except TypeError as e:
    print(f"TypeError: {e}")

# Find outputs  (Home  work)
employees = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))
print(max(employees , key = lambda  x  :  x[0] ))  # (25, 'Kiran', 1500.0)
print(max(employees , key = lambda  x  :  x[1] ))  # (15, 'Vamsi', 2000.0)
print(max(employees , key = lambda  x  :  x[2] ))  # (20, 'Sita', 2800.0)
print(max(employees))               # (25, 'Kiran', 1500.0)

# Find  output  (Home  work)
add1 = lambda  x  :   x == 25
print(add1(10))             # False

add2 = lambda  x = 25 :   x == 35
print(add2())               # False

add3 = lambda  x  :   x := 25
print(add3(10))             # 25
