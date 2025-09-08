#HomeWork on 05/09/2025 part 3 

-----------------------------------------  LAMBDA FUNCTIONS QUESTIONS

# Find  outputs (Home  work)
square = lambda  x = 10  :   x * x
print(square(5)) # 25
print(square()) # 100

---

# Find  outputs  (Home  work)
print((lambda   x  :   x * x) (7)) #49
print( lambda   x  :  x * x(7)) # ERROR
print( lambda   x  :   x * x) # ERROR
print( (lambda  x = 25 :  x * x) () ) # 625
square = lambda  x :  x  *  x
print(square(5)) # 25

---

# Find  output (Home  work)
How  to  define  lambda  function   to  return  sum   of  two  arguments # add = lambda a,b : a+b
print(type(add)) # <class 'function'>
print(add(10 , 20)) # 30
print(add(10.6 , 20.8)) #31.4
print(add('Hyder' , 'abad')) # Hyderabad
print(add(True , False)) # 1
print(add(25 , 10.8)) # 35.8
print(add(3 + 4j , 5 + 6j)) # 8+10j
print(add(10 , '20')) # error
print(add()) # error
print(add) # error prints functions object not result

---

#  Find  outputs (Home  work)
add = lambda  a = 1 , b = 2 :  a + b
print(add(10 , 20)) # 30
print(add()) # 3
---

#  Find  outputs (Home work)
print((lambda  x , y : x + y) (10 , 20) ) # 30
print((lambda  x , y : x + y) (10.8 , 20.6)) # 31.4
print((lambda  x , y : x + y) ('Hyder' , 'abad')) # Hyderabad
print(lambda  x , y : x + y  ('Hyder'  ,  'abad')) # error

---------------------------------------------------------

#  Find  outputs (Home  work)
How  to  define  lambda  to  determine  largest  of  two  arguments # large = lambda a,b: a if a>b else b
print(large(10  ,  20)) # 20
print(large(10.7  ,  5.6)) #10.7
print(large('g'  ,  's')) # s
print(large('Rama'  ,  'Rajesh')) # Rama
print(large(True  ,  False)) # True
-----------------------------------------------------------

#Find  outputs (Home  work)
power = lambda  a = 3.5 , b = 2  :  a ** b
print(power(2 , 3)) # 8
print(power(4.5 , 4)) # 410.06
print(power()) # 12.25
print(power(9)) # 81

----------------------------------------------------------------

# Find  outputs
all = lambda  a , b :  (a + b ,  a - b , a * b , a / b)
x = all(10 , 7)
print(type(x)) # <class 'Tuple'>
print(x) # 17, 3 , 70 , 1.42
p , q , r , s = all(9 , 2)
print(p) # 11
print(q) # 7
print(r) #18
print(s) #1.42
-----------------------------------------------------------------

#  Find  outputs
a  =  lambda  :  'Hyd'
print(a()) # Hyd
print(a) # lambda : 'Hyd'
------------------------------------------------

# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a())
# sec 
# cyb
# Hyd
# None
------------------------------------------------------------
# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a))
print(a)
for  x  in  a:
 	print(x)
a()
print(a[0]())


#########
outputs 
# sec
# cyb
#<class 'tuple'>
# lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
# None
# None
---------------------------------------------------------------------------

#  Find  outputs  (Home  work)
s = 'Hyd'
print(lambda  s  :  print(s)) # prints its function and address
print(lambda  x  :  print(x) (s))# print functiona nd its address
print((lambda  x  :  print(x)) (s)) # Hyd # None
(lambda  x  :  print(x)) (s) # Hyd 
			

------------------------------------------

# Find outputs  (Home  work)
x = 5
adder1 = lambda  y , x = x  : x + y
x = 10
adder2 = lambda  y , x = x : x + y
x = 20
print(adder1(100)) # 105
print(adder2(200)) # 210
print(adder1(300 , 400))
#700
--------------------------------------------------

#Find  outputs  (Home  work)
a = [lambda   x  :  x ** 2 , lambda   x  :  x ** 3 ,  lambda   x  :  x ** 4]
for   fun   in   a:
        print(fun(5)) # 
# 25
#125
#625

-------------------------------------------------------------

#  Find  outputs
def   f1():
 	print('Hyd') 
def   f2():
 	print('Sec')
a = [f1 , f2]
for  x  in  a:
 	     x() 
a = [def   f1():  print('Hyd') ,  def   f2():  print('Sec')]
print(a) 
#outputs
Hyd
Sec
error
--------------------------------------------------------------



# Find output  (Home  work)
a = {'power_2'  :  lambda   x  :  x ** 2 ,
       'power_3'  :  lambda   x  :  x ** 3 ,
  	   'power_4'  :  lambda   x  :  x ** 4}
key = 'power_3'
print(a[key]) # function lambda
print(a[key](5)) # 125 
-------------------------------------------------------------------
\
# Find  outputs  (Home  work)
def   f1(x):
        return  lambda  n  :  x ** n
lamb = f1(3)
print(type(f1))       # <class 'function'>
print(type(lamb))     # <class 'function'>
print(lamb(2))        # 9
print(lamb(5))        # 243
print(lamb)           # <function f1.<locals>.<lambda> at 0x...>
print(lamb())         # TypeError: <lambda>() missing 1 required positional argument: 'n'
#there is no return in lambda function 
-----------------------------------------------------------------------------------------
# Find  outputs   (Home  work)
def   eval(a , b , c):
        return   lambda    x  :    a * x ** 2  +   b * x  +  c
lam  = eval(3 , 4 , 5)
print(lam(2))      # 25
print(lam(2.5))    # 33.75
print(lam(4))      # 69
----------------------------------------------------------------------------------------

#Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()
print(a(20)) # 30
print(add(30)(40)) # 70

---
-----------------------------------------------------------------------------



# Find  outpua= ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0) , (15 ,'Rajesh' , 500.0) ,  (18 , 'Kiran' , 2800.0) , (5 , 'Amar' , 1300.0))
b = sorted(a)
print(b)      # [(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]

print()       # (prints a blank line)

c = sorted(a , reverse = True)
print(c)      # [(20, 'Sita', 2000.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0)]

print()       # (prints a blank line)

d = sorted(a ,  key =  lambda   x  :  x[1])
print(d)      # [(5, 'Amar', 1300.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (20, 'Sita', 2000.0)]

print()       # (prints a blank line)

e = sorted(a , key =  lambda   x  :  x[2])
print(e)      # [(15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0), (20, 'Sita', 2000.0), (18, 'Kiran', 2800.0)]

print()       # (prints a blank line)

f = sorted(a , key = lambda   x  :  x[0])
print(f)      # [(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]

print()       # (prints a blank line)

g = sorted(a , key = lambda  x : x[1] , reverse = True)
print(g)      # [(20, 'Sita', 2000.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (5, 'Amar', 1300.0)]

print(sorted(a , key = x[1])) # NameError: name 'x' is not defined





-# Find outputs  (Home  work)
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
      {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
      {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year'])
print(b)          # [{'Make': 'Tesla', 'Model': 'X', 'Year': 1999}, {'Make': 'Mercedes', 'Model': 'C350E', 'Year': 2008}, {'Make': 'Ford', 'Model': 'Focus', 'Year': 2013}]
print(sorted(a))  # TypeError: '<' not supported between instances of 'dict'
---
# Find outputs  (Home  work)
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))
print(max(a , key = lambda  x  :  x[0] )) # (25, 'Kiran', 1500.0)
print(max(a , key = lambda  x  :  x[1] )) # (15, 'Vamsi', 2000.0)
print(max(a , key = lambda  x  :  x[2] )) # (20, 'Sita', 2800.0)
print(max(a))                               # (25, 'Kiran', 1500.0)
---
# Find  output  (Home  work)
add = lambda  x  :   x == 25
print(add(10))                              # False
add = lambda  x = 25 :   x == 35
print(add())                                # False
add = lambda  x  :   x = 25                 # SyntaxError: invalid syntax
add = lambda  x  :   x := 25                # SyntaxError: invalid syntax
