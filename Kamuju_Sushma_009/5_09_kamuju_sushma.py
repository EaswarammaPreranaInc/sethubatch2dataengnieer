#HW1
#  Find  outputs  (Home  work)
def  change(b):
	b . append(25)
	b[2] = 17
	del  b[1]
# End  of  the  function
a = [10 , 20 , 15 , 18]
print(a)#[10 , 20 , 15 , 18]
change(a)
print(a)#[20 , 15 , 18,25]

#HW2
# Find  outputs  (Home  work)
def  change(b):
	b  = [50 , 60 , 70 , 80]
	print(b)
# End  of  the  function
a = [10 , 20 , 30 , 40]
print(a) #[10 , 20 , 30 , 40]
change(a) #[50 , 60 , 70 , 80]
print(a) #[50 , 60 , 70 , 80]

#HW3
#  Find  outputs  (Home  work)
def   f1(x):
	x = 20
	print(x) #20
# End  of   the   function
x = 10
print(x) #10
f1(x)
print(x) #10

#HW4
#  Find  outputs  (Home  work)
def  f1(b):
	# b[2] = 25 error, tuple is immutable
	pass
#end  of  the  function
a = (10 , 20 , 15 , 18)
print(a) #(10 , 20 , 15 , 18)
f1(a)
print(a) #(10 , 20 , 15 , 18)

#HW5
# Find  outputs (Home  work)
square = lambda  x = 10  :   x * x
print(square(5)) #25
print(square()) #100

#HW6
# Find  outputs  (Home  work)
print((lambda   x  :   x * x) (7)) #49
print( lambda   x  :  x * x(7)) #error
print( lambda   x  :   x * x) #None
print( (lambda  x = 25 :  x * x) () ) #625
square = lambda  x :  x  *  x
print(square(5)) #25

#HW6
# Find  output (Home  work)
# How  to  define  lambda  function   to  return  sum   of  two  arguments
add=lambda x,y: x+y
print(type(add)) #<class 'function'> 
print(add(10 , 20)) #30
print(add(10.6 , 20.8))#31.4
print(add('Hyder' , 'abad'))#Hyderabad
print(add(True , False)) #1
print(add(25 , 10.8))#35.8
print(add(3 + 4j , 5 + 6j)) #8+10j
# print(add(10 , '20')) #error
# print(add())#error
print(add) #<class 'function'> address

#HW7
#  Find  outputs (Home  work)
add = lambda  a = 1 , b = 2 :  a + b
print(add(10 , 20)) #30
print(add())#3

#HW8
#  Find  outputs (Home work)
print((lambda  x , y : x + y) (10 , 20) ) #30
print((lambda  x , y : x + y) (10.8 , 20.6))#31.4
print((lambda  x , y : x + y) ('Hyder' , 'abad'))#Hyderabad
# print(lambda  x , y : x + y  ('Hyder'  ,  'abad'))#error

#HW9
#  Find  outputs (Home  work)
# How  to  define  lambda  to  detrmine  largest  of  two  arguments
large =lambda x,y:max(x,y)
print(large(10  ,  20)) #20
print(large(10.7  ,  5.6))#10.7
print(large('g'  ,  's'))#s
print(large('Rama'  ,  'Rajesh')) #Rama
print(large(True  ,  False))#True

#HW10
#Find  outputs (Home  work)
power = lambda  a = 3.5 , b = 2  :  a ** b
print(power(2 , 3)) #8
print(power(4.5 , 4)) #4.5 ^4
print(power())# 3.5^2
print(power(9))#81

#HW11
# Find  outputs
all = lambda  a , b :  (a + b ,  a - b , a * b , a / b)
x = all(10 , 7) 
print(type(x))#<class 'function'>
print(x)#<class 'function'> address
p , q , r , s = all(9 , 2) 
print(p)#11
print(q)#7
print(r)#18
print(s)#4.5

#HW12
#  Find  outputs
a  =  lambda  :  'Hyd'
print(a()) #Hyd
print(a) #<class 'function'> address

#HW 13
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a())

# Sec 
# Cyb 
# Hyd

#HW 14
# Find  outputs (Home  work)
a  =  lambda  : 'Hyd' ;  print('Sec') ;  print('Cyb')
print(a())
#Sec
#Cyb
#Hyd

#HW15
# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a))  #<class 'tuple'>
print(a) #<class 'tuple'> address
for  x  in  a:
	print(x) 
#Hyd Sec None Cyb None
# a() #error
print(a[0]())#HYd

#HW16
#  Find  outputs  (Home  work)
s = 'Hyd'
# print(lambda  s  :  print(s)) #error
# print(lambda  x  :  print(x) (s)) #error
print((lambda  x  :  print(x)) (s))#Hyd
# (lambda  x  :  print(x)) (s) #error

#HW 17
# Find outputs  (Home  work)
x = 5
adder1 = lambda  y , x = x  : x + y
x = 10
adder2 = lambda  y , x = x : x + y
x = 20
print(adder1(100)) #105
print(adder2(200)) #110
print(adder1(300 , 400))#500

#HW 18
#Find  outputs  (Home  work)
a = [lambda   x  :  x ** 2 , lambda   x  :  x ** 3 ,  lambda   x  :  x ** 4]
for   fun   in   a:
        print(fun(5)) #25 125 625
		
#HW 19
#  Find  outputs
def   f1():
	print('Hyd')
def   f2():
	print('Sec')
a = [f1 , f2]
for  x  in  a:
	     x() #Hyd Sec
a = [def   f1():  print('Hyd') ,  def   f2():  print('Sec')]
print(a) #[<class 'function'> address, <class 'function'> address]

#HW 20
# Find output  (Home  work)
a = {'power_2'  :  lambda   x  :  x ** 2 ,
       'power_3'  :  lambda   x  :  x ** 3 ,
  	   'power_4'  :  lambda   x  :  x ** 4}
key = 'power_3'
print(a[key]) #<class 'function'> address
print(a[key](5)) #125

#HW 21
# Find  outputs  (Home  work)
def   f1(x):
        return  lambda  n  :  x ** n
lamb = f1(3)
print(type(f1)) #<class 'function'> 
print(type(lamb)) #<class 'function'>
print(lamb(2)) #9
print(lamb(5)) #243
print(lamb) #<class 'function'> address
# print(lamb()) #error

#HW 22
# Find  outputs   (Home  work)
def   eval(a , b , c):
        return   lambda    x  :    a *   x **  2  +   b * x  +  c
lam  = eval(3 , 4 , 5)
print(lam(2))#25
print(lam(2.5))#33.75
print(lam(4))#69

#HW 23
#Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()
# print(a(20)) #error, y value is missing 
print(add(30)(40))#70

#HW 24
# Find  outputs
a= ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0) , (15 ,'Rajesh' , 500.0) ,  (18 , 'Kiran' , 2800.0) , (5 , 'Amar' , 1300.0))
b = sorted(a)
print(b) #[(5),(10),(15),(18),(20)]
print()
c = sorted(a , reverse = True)
print(c) #[(20),(18),(15),(10),(5)]
print()
d = sorted(a ,  key =  lambda   x  :  x[1])
print(d) #[(Amar),(kiran),(Rajesh),(Rama),(sita)]
print()
e = sorted(a , key =  lambda   x  :  x[2])
print(e) #[(500.0),(1000.0),(1300.0),(2000.0),(2800.0)]
print()
f = sorted(a , key = lambda   x  :  x[0])
print(f) #[(5),(10),(15),(18),(20)]
print()
g = sorted(a , key = lambda  x : x[1] , reverse = True)
print(g) #[(Sita),(Rama),(Rajesh),(kiran),(Amar)]
print(sorted(a , key = x[1]))#[(Amar),(kiran),(Rajesh),(Rama),(sita)]

#HW 25
# Find outputs  (Home  work)
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year'])
print(b)# [{'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999}, {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008},
		 # {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013}]
print(sorted(a)) #[{'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,{'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008}
#{'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999}]

#HW 26
# Find outputs  (Home  work)
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))
print(max(a , key = lambda  x  :  x[0] )) #(20 , 'Sita' , 2800.0)
print(max(a , key = lambda  x  :  x[1] )) #(15 , 'Vamsi' , 2000.0)
print(max(a , key = lambda  x  :  x[2] )) #(20 , 'Sita' , 2800.0) 
print(max(a)) #(20 , 'Sita' , 2800.0)

#HW 27
# Find  output  (Home  work)
add = lambda  x  :   x == 25
print(add(10)) #False
add = lambda  x = 25 :   x == 35
print(add()) #False
add = lambda  x  :   x = 25 #error, modification is not allowed
add = lambda  x  :   x := 25 #error, modification is not allowed

#HW 28
