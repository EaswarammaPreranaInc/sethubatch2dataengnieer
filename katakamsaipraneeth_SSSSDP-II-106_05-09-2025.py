#  Find  outputs  (Home  work)
def  change(b):
	b . append(25)
	b[2] = 17
	del  b[1]
# End  of  the  function
a = [10 , 20 , 15 , 18] # list obj
print(a) # [10 , 20 , 15 , 18] 
change(a) # [10 , 17 , 18, 25]
print(a) # [10 , 17 , 18, 25]


'''
1)  a = [10 , 20 , 15 , 18]
    change(a)
    What  is   passed  to  change()  function ? ---> List  itself  but  not  elements  of  list

2) Modifying  list  'b' is  as  good  as  modifying  list  'a'  becoz  'a'  and  'b'  point  to  same  list
'''


# Find  outputs  (Home  work)
def  change(b):
	b  = [50 , 60 , 70 , 80]
	print(b)
# End  of  the  function
a = [10 , 20 , 30 , 40]
print(a) # [10 , 20 , 30 , 40]
change(a) # [50 , 60 , 70 , 80]
print(a) # [10 , 20 , 30 , 40]


#  Find  outputs  (Home  work)
def  f1(b):
	b[2] = 25
#end  of  the  function
a = (10 , 20 , 15 , 18)
print(a) # (10 , 20 , 15 , 18)
f1(a) # error
print(a) # (10 , 20 , 15 , 18)


# Find  outputs (Home  work)
square = lambda  x = 10  :   x * x
print(square(5)) # 25
print(square()) # 100


# Find  outputs  (Home  work)
print((lambda   x  :   x * x) (7)) # 49
print( lambda   x  :  x * x(7)) # TypeError
print( lambda   x  :   x * x) # <function <lambda> at 0x000001E2B8C1F700>
print( (lambda  x = 25 :  x * x) () ) # 625
square = lambda  x :  x  *  x # Function  object
print(square(5)) # 25



# Find  output (Home  work)
# How  to  define  lambda  function   to  return  sum   of  two  arguments
print(type(add)) # <class 'function'>
print(add(10 , 20)) # 30
print(add(10.6 , 20.8)) # 31.4
print(add('Hyder' , 'abad')) # Hyderabad
print(add(True , False)) # 1
print(add(25 , 10.8)) # 35.8
print(add(3 + 4j , 5 + 6j)) # (8+10j)
print(add(10 , '20')) # TypeError
print(add()) # TypeError
print(add) # TypeError


#  Find  outputs (Home  work)
add = lambda  a = 1 , b = 2 :  a + b # Function  with  default  arguments
print(add(10 , 20)) # 30
print(add()) # 3


#  Find  outputs (Home work)
print((lambda  x , y : x + y) (10 , 20) ) # 30
print((lambda  x , y : x + y) (10.8 , 20.6)) # 31.4
print((lambda  x , y : x + y) ('Hyder' , 'abad')) # Hyderabad
print(lambda  x , y : x + y  ('Hyder'  ,  'abad'))  # TypeError



#  Find  outputs (Home  work)
# How  to  define  lambda  to  detrmine  largest  of  two  arguments
print(large(10  ,  20)) # 20
print(large(10.7  ,  5.6)) # 10.7
print(large('g'  ,  's')) # s
print(large('Rama'  ,  'Rajesh')) # Rama
print(large(True  ,  False)) # True


#Find  outputs (Home  work)
power = lambda  a = 3.5 , b = 2  :  a ** b #  Default  arguments
print(power(2 , 3)) # 8
print(power(4.5 , 4)) # 410.0625
print(power()) # 12.25
print(power(9)) # 81.0


# Find outputs
all = lambda  a , b :  (a + b ,  a - b , a * b , a / b) # 4 outputs
x = all(10 , 7) # 1 output  of  type  tuple
print(type(x)) # <class 'tuple'>
print(x) # (17 , 3 , 70 , 1.4285714285714286)
p , q , r , s = all(9 , 2) # 4 outputs
print(p) # 11
print(q) # 7 
print(r) # 18
print(s) # 4.5


#  Find  outputs
a  =  lambda  :  'Hyd' # function  object
print(a()) # Hyd
print(a) # <function <lambda> at 0x000001E2B8C1F700>


# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb') # function  object
print(a()) # Hyd  None  Sec  Cyb


# Find  outputs (Home  work)
a  =  lambda  : 'Hyd' ;  print('Sec') ;  print('Cyb') # function  object
print(a()) # Hyd  Sec  Cyb



# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb') # function  object
print(type(a))  # <class 'function'>
print(a) # <function <lambda> at 0x000001E2B8C1F700>
for  x  in  a: 
	print(x) # TypeError: 'function' object is not iterable
a() # Hyd  Sec  Cyb
print(a[0]()) # Hyd


#  Find  outputs  (Home  work)
s = 'Hyd' # global  variable
print(lambda  s  :  print(s)) # <function <lambda> at 0x000001E2B8C1F700>
print(lambda  x  :  print(x) (s)) # TypeError: 'NoneType' object is not callable
print((lambda  x  :  print(x)) (s)) # Hyd  None
(lambda  x  :  print(x)) (s) # Hyd


# Find outputs  (Home  work)
x = 5 # global  variable
adder1 = lambda  y , x = x  : x + y # default  argument
x = 10 # global  variable
adder2 = lambda  y , x = x : x + y # default  argument
x = 20 # global  variable
print(adder1(100)) # 105
print(adder2(200)) # 210
print(adder1(300 , 400)) # 700


#Find  outputs  (Home  work)
a = [lambda   x  :  x ** 2 , lambda   x  :  x ** 3 ,  lambda   x  :  x ** 4] # list  of  function  objects
for   fun   in   a: # fun  is  function  object
        print(fun(5)) # 25  125  625



#  Find  outputs
def   f1(): # function  object
	print('Hyd') # function  body
def   f2():
	print('Sec')
a = [f1 , f2] # list  of  function  objects
for  x  in  a:
	     x()
a = [def   f1():  print('Hyd') ,  def   f2():  print('Sec')] # SyntaxError: invalid syntax
print(a) # SyntaxError: invalid syntax


# Find output  (Home  work)
a = {'power_2'  :  lambda   x  :  x ** 2 ,
       'power_3'  :  lambda   x  :  x ** 3 ,
  	   'power_4'  :  lambda   x  :  x ** 4} # dict  of  function  objects
key = 'power_3' # input  from  user
print(a[key]) # <function <lambda> at 0x000001E2B8C1F700>
print(a[key](5)) # 125



# Find  outputs  (Home  work)
def   f1(x): # function  object
        return  lambda  n  :  x ** n # lambda  function  object
lamb = f1(3) # function  object
print(type(f1)) # <class 'function'>
print(type(lamb)) # <class 'function'>
print(lamb(2)) # 9
print(lamb(5)) # 243
print(lamb) # <function f1.<locals>.<lambda> at 0x000001E2B8C1F700>
print(lamb()) # TypeError: <lambda>() missing 1 required positional argument: 'n'


# Find  outputs   (Home  work)
def   eval(a , b , c): # function  object
        return   lambda    x  :    a *   x **  2  +   b * x  +  c # lambda  function  object
lam  = eval(3 , 4 , 5) # function  object
print(lam(2)) # 27
print(lam(2.5)) # 36.75
print(lam(4)) # 69


#Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y # lambda  function  object
a = add() # lambda  function  object
print(a(20)) # 30
print(add(30)(40)) # 70


# Find  outputs
a= ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0) , (15 ,'Rajesh' , 500.0) ,  (18 , 'Kiran' , 2800.0) , (5 , 'Amar' , 1300.0)) # tuple  of  tuples
b = sorted(a) # sorted  function  returns  a  list
print(b) # [(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]
print() # blank  line
c = sorted(a , reverse = True) # sorted  function  returns  a  list
print(c) # [(20, 'Sita', 2000.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0)]
print() # blank  line
d = sorted(a ,  key =  lambda   x  :  x[1]) # sorted  function  returns  a  list
print(d) # [(5, 'Amar', 1300.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (20, 'Sita', 2000.0)]
print() # blank  line
e = sorted(a , key =  lambda   x  :  x[2]) # sorted  function  returns  a  list
print(e) # [(15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0), (20, 'Sita', 2000.0), (18, 'Kiran', 2800.0)]
print() # blank  line
f = sorted(a , key = lambda   x  :  x[0]) # sorted  function  returns  a  list
print(f) # [(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]
print() # blank  line
g = sorted(a , key = lambda  x : x[1] , reverse = True) # sorted  function  returns  a  list
print(g) # [(20, 'Sita', 2000.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (5, 'Amar', 1300.0)]
print(sorted(a , key = x[1])) # NameError: name 'x' is not defined


# Find outputs  (Home  work)
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ] # list  of  dicts
b = sorted(a , key = lambda  x  :  x['Year']) # sorted  function  returns  a  list
print(b) # [{'Make': 'Tesla', 'Model': 'X', 'Year': 1999}, {'Make': 'Mercedes', 'Model': 'C350E', 'Year': 2008}, {'Make': 'Ford', 'Model': 'Focus', 'Year': 2013}]
print(sorted(a)) # TypeError: '<' not supported between instances of 'dict' and 'dict'


# Find outputs  (Home  work)
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0)) # tuple  of  tuples
print(max(a , key = lambda  x  :  x[0] )) # (25 , 'Kiran' , 1500.0)
print(max(a , key = lambda  x  :  x[1] )) # (20 , 'Sita' , 2800.0)
print(max(a , key = lambda  x  :  x[2] )) # (20 , 'Sita' , 2800.0)
print(max(a)) # (25 , 'Kiran' , 1500.0)



# Find  output  (Home  work)
add = lambda  x  :   x == 25 # 25  is  compared  with  x
print(add(10)) # False
add = lambda  x = 25 :   x == 35 # 35  is  compared  with  x
print(add()) # False
add = lambda  x  :   x = 25 # SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
add = lambda  x  :   x := 25 # SyntaxError: invalid syntax