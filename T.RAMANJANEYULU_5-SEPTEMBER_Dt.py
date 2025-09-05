#  Find  outputs  (Home  work)
def  change(b):
	b . append(25)
	b[2] = 17
	del  b[1]
# End  of  the  function
a = [10 , 20 , 15 , 18]
print(a) # [10 , 20 , 15 , 18]
change(a) # object 'b' is modified as well as 'a' is modified
print(a)  # [10 , 17,18, 25]


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
	print(b)
# End  of  the  function
a = [10 , 20 , 30 , 40]
print(a) # [10 , 20 , 30 , 40]
change(a) #[50 , 60 , 70 , 80]
print(a)# [10 , 20 , 30 , 40]


#  Find  outputs  (Home  work)
def   f1(x):
	x = 20
	print(x)
# End  of   the   function
x = 10
print(x) # 10
f1(x) # 20
print(x) # 10


#  Find  outputs  (Home  work)
def  f1(b):
	b[2] = 25
#end  of  the  function
a = (10 , 20 , 15 , 18)
print(a) # (10 , 20 , 15 , 18)
f1(a) # object 'b' is modified as well as 'a' is modified
print(a) # (10 , 20 , 25 , 18) 

# Find  outputs (Home  work)
square = lambda  x = 10  :   x * x
print(square(5)) # 25
print(square()) # 100

# Find  outputs  (Home  work)
print((lambda   x  :   x * x) (7)) # 49
print( lambda   x  :  x * x(7)) #<function <lambda> at 0x00000234F7AD1760>
print( lambda   x  :   x * x # <function <lambda> at 0x00000234F7AD1760>
print( (lambda  x = 25 :  x * x) () ) # 625
square = lambda  x :  x  *  x
print(square(5)) # 25


# Find  output (Home  work)
How  to  define  lambda  function   to  return  sum   of  two  arguments
add=lambda a,b:a+b
print(type(add))
print(add(10 , 20))
print(add(10.6 , 20.8))
print(add('Hyder' , 'abad'))
print(add(True , False))
print(add(25 , 10.8))
print(add(3 + 4j , 5 + 6j))
print(add(10 , '20')) # Error
print(add()) # Error
print(add)

# Output :
<class 'function'>
30
31.4
Hyderabad
1
35.8
(8+10j)
<function <lambda> at 0x000001C46F8E8900>

#  Find  outputs (Home  work)
add = lambda  a = 1 , b = 2 :  a + b
print(add(10 , 20)) # 30
print(add()) # 3

#  Find  outputs (Home work)
print((lambda  x , y : x + y) (10 , 20) ) # 30
print((lambda  x , y : x + y) (10.8 , 20.6)) # 31.4
print((lambda  x , y : x + y) ('Hyder' , 'abad')) # Hyderabad
print(lambda  x , y : x + y  ('Hyder'  ,  'abad')) # <function <lambda> at 0x00000293DCEE8E00>


#  Find  outputs (Home  work)
How  to  define  lambda  to  detrmine  largest  of  two  arguments
large=lambda a,b: 'a' if a>b else b:
print(large(10  ,  20)) 
print(large(10.7  ,  5.6))
print(large('g'  ,  's'))
print(large('Rama'  ,  'Rajesh'))
print(large(True  ,  False))

# Output:
20
10.7
's'
Rama
True


#Find  outputs (Home  work)
power = lambda  a = 3.5 , b = 2  :  a ** b
print(power(2 , 3)) # 8
print(power(4.5 , 4)) # 410.06
print(power()) # 12.25
print(power(9)) # 81

# Find  outputs
all = lambda  a , b :  (a + b ,  a - b , a * b , a / b)
x = all(10 , 7) 
print(type(x))
print(x)
p , q , r , s = all(9 , 2)
print(p)
print(q)
print(r)
print(s)

# Output:
<class 'tuple'>
(17, 3, 70, 1.4285714285714286)
11
7
18
4.5

#  Find  outputs
a  =  lambda  :  'Hyd'
print(a()) # 'Hyd'
print(a) # <function <lambda> at 0x00000293DCEE8E00>

# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a())

# Output:
Sec
Cyb
Hyd
None

# Find  outputs (Home  work)
a  =  lambda  : 'Hyd' ;  print('Sec') ;  print('Cyb')
print(a())

# Output:
Sec
Cyb
Hyd

# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a)) 
print(a) 
for  x  in  a:
	print(x)
a() 
print(a[0]())

# Output :
Sec
Cyb
<class 'tuple'>
(<function <lambda> at 0x000001F945CD1760>, None, None)
<function <lambda> at 0x000001F945CD1760>
None
None
Hyd
None

#  Find  outputs  (Home  work)
s = 'Hyd'
print(lambda  s  :  prin(s))
print(lambda  x  :  print(x) (s))
print((lambda  x  :  print(x)) (s))
(lambda  x  :  print(x)) (s)

# Output :
<function <lambda> at 0x000001C007921760>
<function <lambda> at 0x000001C007921760>
Hyd
None
Hyd


# Find outputs  (Home  work)
x = 5
adder1 = lambda  y , x = x  : x + y
x = 10
adder2 = lambda  y , x = x : x + y
x = 20
print(adder1(100))
print(adder2(200))
print(adder1(300 , 400))

# Output :
120
220
700

#Find  outputs  (Home  work)
a = [lambda   x  :  x ** 2 , lambda   x  :  x ** 3 ,  lambda   x  :  x ** 4]
for   fun   in   a:
        print(fun(5))

# Output :
25
125
625

#  Find  outputs
def   f1():
	print('Hyd')
def   f2():
	print('Sec')
a = [f1 , f2]
for  x  in  a:
	     x()
#a = [def   f1():  print('Hyd') ,  def   f2():  print('Sec')] # Error
print(a ) 

# Output :
Hyd
Sec
[<function f1 at 0x000002890A4D1760>, <function f2 at 0x000002890A6E8860>]

# Find output  (Home  work)
a = {'power_2'  :  lambda   x  :  x ** 2 ,
       'power_3'  :  lambda   x  :  x ** 3 ,
  	   'power_4'  :  lambda   x  :  x ** 4}
key = 'power_3'
print(a[key])
print(a[key](5))

# Output :
<function f1 at 0x000002890A4D1760>
125

# Find  outputs  (Home  work)
def   f1(x):
        return  lambda  n  :  x ** n
lamb = f1(3)
print(type(f1))
print(type(lamb))
print(lamb(2))
print(lamb(5))
print(lamb)
print(lamb()) # Er

# Output :
<class 'function'>
<class 'function'>
9
243
<function f1.<locals>.<lambda> at 0x000001E8BADE8900>

# Find  outputs   (Home  work)
def   eval(a , b , c):
        return   lambda    x  :    a *   x **  2  +   b * x  +  c
lam  = eval(3 , 4 , 5)
print(lam(2))
print(lam(2.5))
print(lam(4))
# Output :
25
33.75
69

#Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()
print(a(20))
print(add(30)(40))
# Output :
30
70

# Find  outputs
a= ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0) , (15 ,'Rajesh' , 500.0) ,  (18 , 'Kiran' , 2800.0) , (5 , 'Amar' , 1300.0))
b = sorted(a)
print(b) # [(5 , 'Amar' , 1300.0),(10 , 'Rama' , 1000.0),(15 ,'Rajesh' , 500.0),(18 , 'Kiran' , 2800.0),(20 , 'Sita' , 2000.0)]
print() 
c = sorted(a , reverse = True) 
print(c) # [(20 , 'Sita' , 2000.0),(18 , 'Kiran' , 2800.0),(15 ,'Rajesh' , 500.0),(10 , 'Rama' , 1000.0),(5 , 'Amar' , 1300.0)]
print()
d = sorted(a ,  key =  lambda   x  :  x[1])
print(d)
print()
e = sorted(a , key =  lambda   x  :  x[2])
print(e)
print()
f = sorted(a , key = lambda   x  :  x[0])
print(f)
print()
g = sorted(a , key = lambda  x : x[1] , reverse = True)
print(g)
print(sorted(a , key = x[1]))

# Output :
[(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20,'Sita', 2000.0)]

[(20, 'Sita', 2000.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5,'Amar', 1300.0)]

[(5, 'Amar', 1300.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (20,'Sita', 2000.0)]

[(15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0), (20, 'Sita', 2000.0), (18, 'Kiran', 2800.0)]

[(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20,'Sita', 2000.0)]

[(20, 'Sita', 2000.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (5,'Amar', 1300.0)]

# Find outputs  (Home  work)
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year'])
print(b) # [{'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999},{'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008},{'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013}]
print(sorted(a)) # Error

# Find outputs  (Home  work)
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))
print(max(a , key = lambda  x  :  x[0] )) # [(25 , 'Kiran' , 1500.0)]
print(max(a , key = lambda  x  :  x[1] )) # [(15 , 'Vamsi' , 2000.0)]
print(max(a , key = lambda  x  :  x[2] )) # [(20 , 'Sita' , 2800.0)]
print(max(a)) # (25 , 'Kiran' , 1500.0)

# Find  output  (Home  work)
add = lambda  x  :   x == 25
print(add(10)) # False
add = lambda  x = 25 :   x == 35
print(add()) # False
add = lambda  x  :   x = 25 # Error
add = lambda  x  :   x := 25 # Error

# Output :
False
False
