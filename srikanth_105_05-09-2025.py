# Find  outputs  (Home  work)
def  change(b):
	b  = [50 , 60 , 70 , 80]
	print(b)
# End  of  the  function
a = [10, 20, 30, 40]
print(a)              # [10, 20, 30, 40]
change(a)             # [50, 60, 70, 80]
print(a)              # [10, 20, 30, 40]

 
#  Find  outputs  (Home  work)
def   f1(x):
	x = 20
	print(x)
# End  of   the   function
x = 10
print(x)     # 10
f1(x)        # 20
print(x)     # 10


#  Find  outputs  (Home  work)
def  f1(b):
	b[2] = 25
#end  of  the  function
a = (10, 20, 15, 18)
print(a)   # (10, 20, 15, 18)
f1(a)      # Error → tuple does not support item assignment
print(a)   # (10, 20, 15, 18)


# Find  outputs (Home  work)
square = lambda  x = 10  :   x * x
print(square(5))    #25
print(square())     #100


# Find  outputs  (Home  work)
print((lambda x: x * x)(7))         # 49
print(lambda x: x * x(7))           # Error → 'int' object is not callable
print(lambda x: x * x)              # <function <lambda> at 0x...>
print((lambda x=25: x * x)())       # 625
print(square(5))                    # 25



# Find  output (Home  work)
add = lambda a,b:a+b
print(type(add))
print(add(10 , 20))
print(add(10.6 , 20.8))
print(add('Hyder' , 'abad'))
print(add(True , False))
print(add(25 , 10.8))
print(add(3 + 4j , 5 + 6j))
print(add(10 , '20'))
print(add())
print(add)
'''
<class 'function'>
30
31.4
Hyderabad
1
35.8
(8+10j)
error
error
<function <lambda> at 0x000001E1A952FF60>
'''


#  Find  outputs (Home  work)
add = lambda  a = 1 , b = 2 :  a + b
print(add(10 , 20)) # 30
print(add())        #3


#  Find  outputs (Home work)
print((lambda x, y: x + y)(10, 20))         # 30
print((lambda x, y: x + y)(10.8, 20.6))     # 31.4
print((lambda x, y: x + y)('Hyder', 'abad'))# 'Hyderabad'
print(lambda x, y: x + y('Hyder', 'abad'))  #  TypeError


#  Find  outputs (Home  work)
# How  to  define  lambda  to  detrmine  largest  of  two  arguments
large = lambda  a , b  :  a  if  a > b  else  b
print(large(10  ,  20))
print(large(10.7  ,  5.6))
print(large('g'  ,  's'))
print(large('Rama'  ,  'Rajesh'))
print(large(True  ,  False))
'''
20
10.7
s
Rama
True
'''

#Find  outputs (Home  work)
power = lambda  a = 3.5 , b = 2  :  a ** b
print(power(2, 3))     # 8
print(power(4.5, 4))   # 410.0625
print(power())         # 12.25
print(power(9))        # 81.0


# Find  outputs
all = lambda  a , b :  (a + b ,  a - b , a * b , a / b)
x = all(10 , 7)
x = all(10, 7)
print(type(x))      # <class 'tuple'>
print(x)            # (17, 3, 70, 1.4285714285714286)
p,q,r,s = all(9, 2)
print(p)   # 11
print(q)   # 7
print(r)   # 18
print(s)   # 4.5



#  Find  outputs
a  =  lambda  :  'Hyd'
print(a())   # 'Hyd'
print(a)     # <function <lambda> at 0x...>



# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a())
'''
Sec
Cyb
Hyd
None
'''

 # Find  outputs (Home  work)
a  =  lambda  : 'Hyd' ;  print('Sec') ;  print('Cyb')
print(a())
'''
Sec
Cyb
Hyd
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
Sec
Cyb
<class 'tuple'>
(<function <lambda> at 0x000001E1A95E09A0>, None, None)
<function <lambda> at 0x000001E1A95E09A0>
None
None
Hyd
Error  ->  'tuple' object is not callable
None
'''


#  Find  outputs  (Home  work)
s = 'Hyd'
print(lambda  s  :  print(s))
print(lambda  x  :  print(x) (s))
print((lambda  x  :  print(x)) (s))
(lambda  x  :  print(x)) (s)
'''
<function <lambda> at 0x...>
TypeError: 'NoneType' object is not callable
Hyd
None
Hyd
'''


# Find outputs  (Home  work)
x = 5
adder1 = lambda y, x=x: x + y   # captures x=5
x = 10
adder2 = lambda y, x=x: x + y   # captures x=10
x = 20

print(adder1(100))      # 105
print(adder2(200))      # 210
print(adder1(300, 400)) # TypeError: <lambda>() takes from 1 to 2 positional arguments but 3 were given



 #Find  outputs  (Home  work)
a = [lambda   x  :  x * 2 , lambda   x  :  x * 3 ,  lambda   x  :  x ** 4]
for   fun   in   a:
        print(fun(5))
'''
10
15
625
'''


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
'''
Hyd
Sec
SyntaxError: invalid syntax
'''


# Find output  (Home  work)
a = {'power_2'  :  lambda   x  :  x ** 2 ,
       'power_3'  :  lambda   x  :  x ** 3 ,
  	   'power_4'  :  lambda   x  :  x ** 4}
key = 'power_3'
print(a[key])
print(a[key](5))
'''
<function <lambda> at 0x...>
125
'''



# Find outputs (Home work)
def f1(x):
    return lambda n: x ** n

lamb = f1(3)

print(type(f1))                     # <class 'function'>
print(type(lamb))                   # <class 'function'>
print(lamb(2))                      # 9
print(lamb(5))                      # 243
print(lamb)                         
print(lamb())                       # Error


# Find outputs (Home work)
def eval(a, b, c):
    return lambda x: a * x ** 2 + b * x + c
lam = eval(3, 4, 5)
print(lam(2))                      # 21
print(lam(2.5))                    # 29.75
print(lam(4))                      # 69


# Nested lambda function (Home work)
add = lambda x=10: lambda y: x + y
a = add()
print(a(20))                     # 30
print(add(30)(40))               # 70


# Find outputs
a = (
    (10, 'Rama', 1000.0),
    (20, 'Sita', 2000.0),
    (15, 'Rajesh', 500.0),
    (18, 'Kiran', 2800.0),
    (5, 'Amar', 1300.0)
)

b = sorted(a)
print(b)                       # [(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]
print()

c = sorted(a, reverse=True)
print(c)                       # [(20, 'Sita', 2000.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0)]
print()
d = sorted(a, key=lambda x: x[1])
print(d)                       # [(5, 'Amar', 1300.0), (18, 'Kiran', 2800.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (20, 'Sita', 2000.0)]
print()
e = sorted(a, key=lambda x: x[2])
print(e)                      # [(15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0), (20, 'Sita', 2000.0), (18, 'Kiran', 2800.0)]
print()
f = sorted(a, key=lambda x: x[0])
print(f)                      # [(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]
print()
g = sorted(a, key=lambda x: x[1], reverse=True)
print(g)                     # [(20, 'Sita', 2000.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (18, 'Kiran', 2800.0), (5, 'Amar', 1300.0)]
print(sorted(a, key=x[1]))   # Error


# Find outputs (Home work)
a = [
    {'Make': 'Ford', 'Model': 'Focus', 'Year': 2013},
    {'Make': 'Tesla', 'Model': 'X', 'Year': 1999},
    {'Make': 'Mercedes', 'Model': 'C350E', 'Year': 2008}
]

b = sorted(a, key=lambda x: x['Year'])
print(b)
# [{'Make': 'Tesla', 'Model': 'X', 'Year': 1999},
#  {'Make': 'Mercedes', 'Model': 'C350E', 'Year': 2008},
#  {'Make': 'Ford', 'Model': 'Focus', 'Year': 2013}]

print(sorted(a))                   # Error: '<' not supported between instances of 'dict' and 'dict'


a = (
    (10, 'Rama', 1000.0),
    (20, 'Sita', 2800.0),
    (15, 'Vamsi', 2000.0),
    (25, 'Kiran', 1500.0),
    (5, 'Amar', 1300.0)
)

print(max(a, key=lambda x: x[0]))
# (25, 'Kiran', 1500.0)

print(max(a, key=lambda x: x[1]))
# (15, 'Vamsi', 2000.0)

print(max(a, key=lambda x: x[2]))
# (20, 'Sita', 2800.0)

print(max(a))
# (25, 'Kiran', 1500.0)




# Find output (Home work)
add = lambda x: x == 25
print(add(10))                                 # False
add = lambda x=25: x == 35
print(add())                                   # False
add = lambda x: x = 25                         # Error
add = lambda x: x := 25                        # Error
