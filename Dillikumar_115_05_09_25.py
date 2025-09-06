
#  Find  outputs  (Home  work)
def  change(b):
	b . append(25)
	b[2] = 17
	del  b[1]
# End  of  the  function
a = [10 , 20 , 15 , 18]
print(a) # [10 , 20 , 15 , 18]
change(a)
print(a)# # [10 , 17 , 15 , 25]



'''
1)  a = [10 , 20 , 15 , 18]
    change(a)
    What  is   passed  to  change()  function ? --->

List  itself  but  not  elements  of  list

2) Modifying  list  'b' is  as  good  as  modifying  list  'a'  becoz  'a'  and  'b'  point  to  same  list
'''


 # Find  outputs  (Home  work)
def  change(b):
	b  = [50 , 60 , 70 , 80]
	print(b) # [10 , 20 , 30 , 40]
# End  of  the  function
a = [10 , 20 , 30 , 40]
print(a) # [50 , 60 , 70 , 80]
change(a)
print(a) # [10 , 20 , 30 , 40]


#  Find  outputs  (Home  work)
def   f1(x):
	x = 20
	print(x)# 10
# End  of   the   function
x = 10
print(x) #20
f1(x)
print(x) # 10


#  Find  outputs  (Home  work)
def  f1(b):
	b[2] = 25
#end  of  the  function
a = (10 , 20 , 15 , 18)
print(a) # (10 , 20 , 15 , 18)
f1(a)
print(a) # error



# Find  outputs (Home  work)
square = lambda  x = 10  :   x * x
print(square(5)) # 5*5 = 25
print(square())   # 100


# Find  outputs  (Home  work)
print((lambda   x  :   x * x) (7))  # 49
print( lambda   x  :  x * x(7)) # errir 
print( lambda   x  :   x * x)  # only x will print no value is assigned 
print( (lambda  x = 25 :  x * x) () ) # 625
square = lambda  x :  x  *  x    
print(square(5))  # 25


# Find  output (Home  work)
How  to  define  lambda  function   to  return  sum   of  two  arguments
print(type(add))       # <class 'function'>
print(add(10 , 20))    # 30 
print(add(10.6 , 20.8)) # 40.0
print(add('Hyder' , 'abad')) #'Hyderabad'
print(add(True , False)) # True or 1
print(add(25 , 10.8)) # 35.8
print(add(3 + 4j , 5 + 6j)) # (8+10j)
print(add(10 , '20'))  # error
print(add()) #() error
print(add) # add # nothings will be added



#  Find  outputs (Home  work)
add = lambda  a = 1 , b = 2 :  a + b
print(add(10 , 20)) # 30
print(add())  # 3


#  Find  outputs (Home work)
print((lambda  x , y : x + y) (10 , 20) )   # 30
print((lambda  x , y : x + y) (10.8 , 20.6)) # 31.4
print((lambda  x , y : x + y) ('Hyder' , 'abad')) # 'Hyderabad'
print(lambda  x , y : x + y  ('Hyder','abad')) # <function <lambda> at 0x...>


#  Find  outputs (Home  work)
How  to  define  lambda  to  detrmine  largest  of  two  arguments
print(large(10  ,  20)) #  20
print(large(10.7  ,  5.6)) # 10.7
print(large('g'  ,  's')) # 's'
print(large('Rama'  ,  'Rajesh')) # 'Rama'
print(large(True  ,  False)) # 1

 #Find  outputs (Home  work)
power = lambda  a = 3.5 , b = 2  :  a ** b
print(power(2 , 3))  # 2**3=8
print(power(4.5 , 4)) # 410.0625 # 81/4*81/4
print(power()) # 12.25
print(power(9)) # 81


 # Find  outputs
all = lambda  a , b :  (a + b ,  a - b , a * b , a / b)
x = all(10 , 7)
print(type(x)) # <class 'tuple'>
print(x)     # (17, 3, 70, 1.4285714285714286)
p , q , r , s = all(9 , 2)
print(p) # 11
print(q) # 7
print(r) # 18
print(s) # 4.5

 #  Find  outputs
a  =  lambda  :  'Hyd'
print(a()) # 'Hyd'
print(a) #<function <lambda> at 0x...>

 # Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a())# Sec

 # Find  outputs (Home  work)
a  =  lambda  : 'Hyd' ;  print('Sec') ;  print('Cyb')
print(a()) # Cyb

 # Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a)) # <class 'tuple'>
print(a)   # # (<function <lambda> at 0x...>, None, None)

for  x  in  a:
	print(x)  #<function <lambda> at 0x...>
a() 
print(a[0]())  #  None 

#  Find  outputs  (Home  work)
s = 'Hyd'
print(lambda  s  :  print(s)) # <function <lambda> at 0x...>
print(lambda  x  :  print(x) (s)) # error
print((lambda  x  :  print(x)) (s))  # Hyd
(lambda  x  :  print(x)) (s) # None

# Find outputs  (Home  work)
x = 5
adder1 = lambda  y , x = x  : x + y
x = 10
adder2 = lambda  y , x = x : x + y
x = 20
print(adder1(100))  # 105
print(adder2(200))   # 210
print(adder1(300 , 400))  # error


#Find  outputs  (Home  work)
a = [lambda   x  :  x ** 2 , lambda   x  :  x ** 3 ,  lambda   x  :  x ** 4]
for   fun   in   a:
        print(fun(5))  # 25 

#  Find  outputs
def   f1():
	print('Hyd')  # Hyd
def   f2():
	print('Sec') # Sec
a = [f1 , f2]
for  x  in  a:
	     x()
a = [def   f1():  print('Hyd') ,  def   f2():  print('Sec')]
print(a)  # Error 

# Find output  (Home  work)
a = {'power_2'  :  lambda   x  :  x ** 2 ,
       'power_3'  :  lambda   x  :  x ** 3 ,
  	   'power_4'  :  lambda   x  :  x ** 4}
key = 'power_3'
print(a[key])   # <function <lambda> at 0x...>
print(a[key](5)) # 125

# Find  outputs  (Home  work)
def   f1(x):
        return  lambda  n  :  x ** n
lamb = f1(3)
print(type(f1)) # <class 'function'>
print(type(lamb)) # <class 'function'>
print(lamb(2))  # 9
print(lamb(5)) # 243
print(lamb)    # function object

print(lamb()) # erro 


# Find  outputs   (Home  work)
def   eval(a , b , c):
        return   lambda    x  :    a *   x **  2  +   b * x  +  c
lam  = eval(3 , 4 , 5)
print(lam(2)) # 25
print(lam(2.5)) # 33.75
print(lam(4))  # 69

#Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()
print(a(20)) # 30
print(add(30)(40)) # 70

 # Find  outputs
a= ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0) , (15 ,'Rajesh' , 500.0) ,  (18 , 'Kiran' , 2800.0) , (5 , 'Amar' , 1300.0))
b = sorted(a)
print(b) 
# a = [(5, 'Amar', 1300.0),
 (10, 'Rama', 1000.0),
 (15, 'Rajesh', 500.0),
 (18, 'Kiran', 2800.0),
 (20, 'Sita', 2000.0)]


c = sorted(a , reverse = True)
print(c) 
# [(20, 'Sita', 2000.0),
 (18, 'Kiran', 2800.0),
 (15, 'Rajesh', 500.0),
 (10, 'Rama', 1000.0),
 (5, 'Amar', 1300.0)]

print()
d = sorted(a ,  key =  lambda   x  :  x[1])
print(d)
# [(5, 'Amar', 1300.0),
 (18, 'Kiran', 2800.0),
 (15, 'Rajesh', 500.0),
 (10, 'Rama', 1000.0),
 (20, 'Sita', 2000.0)]

print()
e = sorted(a , key =  lambda   x  :  x[2])
print(e)
# [(15, 'Rajesh', 500.0),
 (10, 'Rama', 1000.0),
 (5, 'Amar', 1300.0),
 (20, 'Sita', 2000.0),
 (18, 'Kiran', 2800.0)]

print()
f = sorted(a , key = lambda   x  :  x[0])
print(f)
print()
# [(5, 'Amar', 1300.0),
 (10, 'Rama', 1000.0),
 (15, 'Rajesh', 500.0),
 (18, 'Kiran', 2800.0),
 (20, 'Sita', 2000.0)]

g = sorted(a , key = lambda  x : x[1] , reverse = True)
print(g)
print(sorted(a , key = x[1]))
# [(20, 'Sita', 2000.0),
 (10, 'Rama', 1000.0),
 (15, 'Rajesh', 500.0),
 (18, 'Kiran', 2800.0),
 (5, 'Amar', 1300.0)]


 # Find outputs  (Home  work)
a = [(20, 'Sita', 2000.0),
 (10, 'Rama', 1000.0),
 (15, 'Rajesh', 500.0),
 (18, 'Kiran', 2800.0),
 (5, 'Amar', 1300.0)]

print(b)
# [(20, 'Sita', 2000.0),
 (10, 'Rama', 1000.0),
 (15, 'Rajesh', 500.0),
 (18, 'Kiran', 2800.0),
 (5, 'Amar', 1300.0)]

print(sorted(a)) # error

 # Find outputs  (Home  work)
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))
print(max(a , key = lambda  x  :  x[0] ))# (25, 'Kiran', 1500.0)
print(max(a , key = lambda  x  :  x[1] ))# (15, 'Vamsi', 2000.0)
print(max(a , key = lambda  x  :  x[2] )) # (20, 'Sita', 2800.0)
print(max(a))


(25, 'Kiran', 1500.0)

 # Find  output  (Home  work)
add = lambda  x  :   x == 25
print(add(10))  # False
add = lambda  x = 25 :   x == 35
print(add()) # Error
add = lambda  x  :   x = 25
add = lambda  x  :   x := 25