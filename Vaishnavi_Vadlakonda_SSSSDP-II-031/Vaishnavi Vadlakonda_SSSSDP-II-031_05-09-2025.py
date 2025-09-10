#  Find  outputs  (Home  work)
def  change(b):
	b . append(25)
	b[2] = 17
	del  b[1]
# End  of  the  function
a = [10 , 20 , 15 , 18]
print(a) # prints [10, 20, 15, 18]
change(a)
print(a) # prints [10, 17, 18, 25]
'''
Outputs

[10, 20, 15, 18]
[10, 17, 18, 25]
'''









# Find  outputs  (Home  work)
def change(b):
	b  = [50 , 60 , 70 , 80]
	print(b) 
# End  of  the  function
a = [10 , 20 , 30 , 40]
print(a) 
change(a) 
print(a) 
'''
Outputs

[10, 20, 30, 40]
[50, 60, 70, 80]
[10, 20, 30, 40]
'''









#  Find  outputs  (Home  work)
def f1(x):
	x = 20
	print(x)
# End  of   the   function
x = 10
print(x)
f1(x)
print(x)
'''
Outputs

10
20
10
'''









#  Find  outputs  (Home  work)
def f1(b):
	b[2] = 25 # Error because tuple is immutable
#end  of  the  function
a = (10 , 20 , 15 , 18)
print(a) 
f1(a) 
print(a)
'''
Outputs

(10, 20, 15, 18)
(10, 20, 15, 18)
'''









# Find  outputs (Home  work)
square = lambda  x = 10  :   x * x
print(square(5)) # prints 25
print(square()) # prints 100









# Find  outputs  (Home  work)
print((lambda   x  :   x * x) (7)) # prints 49
print( lambda   x  :  x * x(7)) # prints type and address of the function
print( lambda   x  :   x * x) # prints  type and address of the function
print( (lambda  x = 25 :  x * x) () ) # prints 625
square = lambda  x :  x  *  x
print(square(5)) # prints 25









# Find  output (Home  work)
add = lambda a, b : a + b #How  to  define  lambda  function   to  return  sum   of  two  arguments
print(type(add)) # prints <class 'function'>
print(add(10 , 20)) # prints 30
print(add(10.6 , 20.8)) # prints 31.4
print(add('Hyder' , 'abad')) # prints Hyderabad
print(add(True , False)) # prints 1
print(add(25 , 10.8)) # prints 35.8
print(add(3 + 4j , 5 + 6j)) # prints (7+10j)
print(add(10 , '20')) # Error because int and string cannot be added 
print(add()) # Error because it requires 2 arguments 
print(add) # prints type and address of the lambda function









#  Find  outputs (Home  work)
add = lambda  a = 1 , b = 2 :  a + b
print(add(10 , 20)) # prints 30
print(add()) # prints 3









#  Find  outputs (Home work)
print((lambda  x , y : x + y) (10 , 20) ) # prints 30
print((lambda  x , y : x + y) (10.8 , 20.6)) # prints 31.4
print((lambda  x , y : x + y) ('Hyder', 'abad')) # prints Hyderabad
print(lambda  x , y : x + y  ('Hyder', 'abad')) # prints type and address of the lambda function
							  








#  Find  outputs (Home  work)
large = lambda a, b : max(a, b) #How  to  define  lambda  to  detrmine  largest  of  two  arguments
print(large(10,  20)) # prints 20
print(large(10.7,  5.6)) # prints 10.7
print(large('g',  's')) # prints s
print(large('Rama',  'Rajesh')) # prints Rama
print(large(True, False)) # prints True
			








#Find  outputs (Home  work)
power = lambda  a = 3.5 , b = 2  :  a ** b
print(power(2 , 3)) # prints 8
print(power(4.5 , 4)) # prints 410.0625
print(power()) # prints 12.25
print(power(9))









# Find  outputs
all = lambda  a , b :  (a + b ,  a - b , a * b , a / b)
x = all(10 , 7)
print(type(x)) # prints type of lambda function
print(x) # prints (17, 3, 70, 1.42)
p , q , r , s = all(9 , 2)
print(p) # prints 11
print(q) # prints 7
print(r) # prints 18
print(s) # prints 4.5









#  Find  outputs
a  =  lambda  :  'Hyd'
print(a()) # prints type of the function
print(a) # prints type and address of the function









# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a()) 
'''
Outputs

Sec
Cyb
Hyd
'''









# Find  outputs (Home  work)
a  =  lambda  : 'Hyd' ;  print('Sec') ;  print('Cyb')
print(a())
'''
Outputs

Sec
Cyb
type and address of the lambda function
'''









# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a)) 
print(a)  
for  x  in  a:
	print(x)
a() 
print(a[0]())
'''
Outputs

<class 'tuple'>
(type and address of the lambda function, None, None)
type and address of the lambda function
None
None
Hyd
None
'''









#  Find  outputs  (Home  work)
s = 'Hyd'
print(lambda  s  :  print(s)) # prints type and address of the lambda function
print(lambda  x  :  print(x) (s)) # prints type and address of the lambda function
print((lambda  x  :  print(x)) (s)) # prints Hyd<nextline>None
(lambda  x  :print(x))(s) # prints None









# Find outputs  (Home  work)
x = 5
adder1 = lambda  y , x = x  : x + y
x = 10
adder2 = lambda  y , x = x : x + y
x = 20
print(adder1(100)) # prints 105
print(adder2(200)) # prints 210
print(adder1(300, 400)) # prints 700
			 








#Find  outputs  (Home  work)
a = [lambda   x  :  x ** 2 , lambda   x  :  x ** 3 ,  lambda   x  :  x ** 4]
for fun in a:
    print(fun(5))
'''
Outputs

25
125
625
'''	 









#  Find  outputs
def f1():
	print('Hyd')
def f2():
	print('Sec')
a = [f1 , f2]
for x in a:
	x()
a = [def f1():  print('Hyd') ,  def f2():  print('Sec')]
print(a)
'''
Outputs

Hyd
Sec
type and address of f1() function, type and address of f2() function
'''









# Find output  (Home  work)
a = {'power_2'  :  lambda   x  :  x ** 2 ,
       'power_3'  :  lambda   x  :  x ** 3 ,
  	   'power_4'  :  lambda   x  :  x ** 4}
key = 'power_3'
print(a[key]) # prints type and address of lambda function
print(a[key](5)) # prints 125









# Find  outputs  (Home  work)
def f1(x):
    return  lambda  n  :  x ** n
lamb = f1(3)
print(type(f1)) # prints <class 'function'> 
print(type(lamb)) # prints <class 'function'>
print(lamb(2)) # prints 9
print(lamb(5)) # prints 243
print(lamb) # prints type and address of lambda function
print(lamb()) # Error because it requires 1 argument









# Find  outputs   (Home  work)
def eval(a , b , c):
	return   lambda    x  :    a *   x **  2  +   b * x  +  c
lam  = eval(3 , 4 , 5)
print(lam(2)) # prints 25
print(lam(2.5)) # prints 33.75
print(lam(4)) # prints 69









#Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()
print(a(20)) # prints 30
print(add(30)(40)) # prints 70









# Find  outputs
a= ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0) , (15 ,'Rajesh' , 500.0) ,  (18 , 'Kiran' , 2800.0) , (5 , 'Amar' , 1300.0))
b = sorted(a)
print(b) # [(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]
print() # prints nothing
c = sorted(a , reverse = True)
print(c) # [(20, 'Sita', 2000.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0),  (10, 'Rama', 1000.0), (5, 'Amar', 1300.0)]
print() # prints nothing
d = sorted(a ,  key =  lambda   x  :  x[1])
print(d) # prints [(5, 'Amar', 1300.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (20, 'Sita', 2000.0)]
print() # prints nothing
e = sorted(a , key =  lambda   x  :  x[2])
print(e) # prints [(15, ''Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0), (20, 'Sita', 2000.0), (18, 'Kiran', 2800.0)]
print() # prints nothing
f = sorted(a , key = lambda   x  :  x[0])
print(f) # prints [(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]
print() # prints nothing
g = sorted(a , key = lambda  x : x[1] , reverse = True)
print(g) # [(20, 'Kiran', 2800.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (5, 'Amar', 1300.0)]
print(sorted(a, key = x[1])) # Error because key = lambda not x









# Find outputs  (Home  work)
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year'])
print(b) # [{'Make' : 'Tesla', 'Model' : 'X', 'Year' : 1999}, {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008}, {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013}
print(sorted(a)) # comparisions are not supported for dict and dict









# Find outputs  (Home  work)
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))
print(max(a , key = lambda  x  :  x[0] )) # prints ((25 , 'Kiran' , 1500.0))
print(max(a , key = lambda  x  :  x[1] )) # prints ((15 , 'Vamsi' , 2000.0))
print(max(a , key = lambda  x  :  x[2] )) # prints ((20 , 'Sita' , 2800.0))
print(max(a)) # prints ((25 , 'Kiran' , 1500.0))







# Find  output  (Home  work)
add = lambda  x  :   x == 25
print(add(10)) # prints False
add = lambda  x = 25 :   x == 35
print(add()) # prints  False
add = lambda  x  :   x = 25 # Error because assigning value to lambda is invalid
add = lambda x : x := 25 # Error because assigning value to lambda is invalid