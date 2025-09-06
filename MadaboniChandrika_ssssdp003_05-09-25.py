#1st program
#  Find  outputs  (Home  work)
def  change(b):
	b . append(25)
	b[2] = 17
	del  b[1]
# End  of  the  function
a = [10 , 20 , 15 , 18]
print(a)#[10 , 20 , 15 , 18]
change(a)
print(a)#[10 , 17 , 18 , 25]


#2nd program
# Find  outputs  (Home  work)
def  change(b):
	b  = [50 , 60 , 70 , 80]
	print(b)
# End  of  the  function
a = [10 , 20 , 30 , 40]
print(a)#[10 , 20 , 30 , 40]
change(a)#[50 , 60 , 70 , 80]
print(a)#[10 , 20 , 30 , 40]


#3rd program
#  Find  outputs  (Home  work)
def   f1(x):
	x = 20
	print(x)
# End  of   the   function
x = 10
print(x)#10
f1(x)#20
print(x)#10


#4th program
#  Find  outputs  (Home  work)
def  f1(b):
	#b[2] = 25# tuple cannot be changed
    pass
#end  of  the  function
a = (10 , 20 , 15 , 18)
print(a)#(10 , 20 , 15 , 18)
f1(a)#error
print(a)#(10 , 20 , 15 , 18)


#5th program
# Find  outputs (Home  work)
square = lambda  x = 10  :   x * x
print(square(5))#25
print(square())#100


#6th program
# Find  outputs  (Home  work)
print((lambda   x  :   x * x) (7))#49
print( lambda   x  :  x * x(7))#function type and address
print( lambda   x  :   x * x)#function type and address
print( (lambda  x = 25 :  x * x) () )#625
square = lambda  x :  x  *  x
print(square(5))#25


#7th program
# Find  output (Home  work)
#How  to  define  lambda  function   to  return  sum   of  two  arguments
add=lambda x,y: x+y
print(type(add))
print(add(10 , 20))
print(add(10.6 , 20.8))
print(add('Hyder' , 'abad'))
print(add(True , False))
print(add(25 , 10.8))
print(add(3 + 4j , 5 + 6j))
#print(add(10 , '20'))#error,int and str cannot be added
#print(add())#error missing 2 arguments
print(add)#function type and address


#8th program
#  Find  outputs (Home  work)
add = lambda  a = 1 , b = 2 :  a + b
print(add(10 , 20))#30
print(add())#3


#9th program
#  Find  outputs (Home work)
print((lambda  x , y : x + y) (10 , 20) )#30
print((lambda  x , y : x + y) (10.8 , 20.6))#31.4
print((lambda  x , y : x + y) ('Hyder' , 'abad'))#Hyderabad
print(lambda  x , y : x + y  ('Hyder'  ,  'abad'))#function type and address


#10th program
#  Find  outputs (Home  work)
#How  to  define  lambda  to  detrmine  largest  of  two  arguments
large=lambda x,y: x if x>y else y
print(large(10  ,  20))
print(large(10.7  ,  5.6))
print(large('g'  ,  's'))
print(large('Rama'  ,  'Rajesh'))
print(large(True  ,  False))


#11th program
#Find  outputs (Home  work)
power = lambda  a = 3.5 , b = 2  :  a ** b
print(power(2 , 3))#8
print(power(4.5 , 4))#410.0625
print(power())#12.25
print(power(9))#81


#12th program
# Find  outputs
all = lambda  a , b :  (a + b ,  a - b , a * b , a / b)
x = all(10 , 7)
print(type(x))#<class 'tuple'>
print(x)#(17 , 3 , 70 , 1.4285714285714286)
p , q , r , s = all(9 , 2)
print(p)#11
print(q)#7
print(r)#18
print(s)#4.5


#13th program
#  Find  outputs
a  =  lambda  :  'Hyd'
print(a())#Hyd
print(a)#function type and address


#14th program
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a())
'''
Sec
Cyb
Hyd
None
'''


#15th program
# Find  outputs (Home  work)
a  =  lambda  : 'Hyd' ;  print('Sec') ;  print('Cyb')
print(a())
'''
Sec
Cyb
Hyd
'''


#16th program
# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a)) #<class'tuple'>
print(a) 
for  x  in  a:
	print(x)
#a() #error 
print(a[0]())
'''
Sec
Cyb
<class 'tuple'>
(<function <lambda> at 0x0000021E57211440>, None, None)
<function <lambda> at 0x0000021E57211440>
None
None
Hyd
None
'''


#17th program
# Find  outputs  (Home  work)
s = 'Hyd'
print(lambda  s  :  print(s))#<function <lambda> at address
print(lambda  x  :  print(x) (s))#<function <lambda> at address
print((lambda  x  :  print(x)) (s))#hyd<nextline>None
(lambda  x  :  print(x)) (s)#hyd


#18th program
# Find outputs  (Home  work)
x = 5
adder1 = lambda  y , x = x  : x + y
x = 10
adder2 = lambda  y , x = x : x + y
x = 20
print(adder1(100))#105
print(adder2(200))#210
print(adder1(300 , 400))#700


#19th program
# Find  outputs  (Home  work)
a = [lambda   x  :  x ** 2 , lambda   x  :  x ** 3 ,  lambda   x  :  x ** 4]
for   fun   in   a:
        print(fun(5))#25
		             #125
					 #625
					 

#20th program
# Find  outputs
def   f1():
	print('Hyd')
def   f2():
	print('Sec')
a = [f1 , f2]
for  x  in  a:
	     x()
#a = [def   f1():  print('Hyd') ,  def   f2():  print('Sec')]#error invalid syntax
print(a) #Hyd
         #Sec
         # type and address of lambda function 1 and type and address of lambda function2                  
		 

#21st program
# Find output  (Home  work)
a = {'power_2'  :  lambda   x  :  x ** 2 ,
       'power_3'  :  lambda   x  :  x ** 3 ,
  	   'power_4'  :  lambda   x  :  x ** 4}
key = 'power_3'
print(a[key])#type and address of the lambdafunction
print(a[key](5))#125  


#22nd program
# Find  outputs  (Home  work)
def   f1(x):
        return  lambda  n  :  x ** n
lamb = f1(3)
print(type(f1))#<class 'function>
print(type(lamb))#<class 'function>
print(lamb(2))#9
print(lamb(5))#243
print(lamb)#type and address of lambda function
#print(lamb())#error there is no arguments


#23rd program
# Find  outputs   (Home  work)
def   eval(a , b , c):
        return   lambda    x  :    a *   x **  2  +   b * x  +  c
lam  = eval(3 , 4 , 5)                       
print(lam(2))#25
print(lam(2.5))#33.75
print(lam(4))#69



#24th program
# Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()
print(a(20))#30
print(add(30)(40))#70


#25th program
# Find  outputs
a= ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0) , (15 ,'Rajesh' , 500.0) ,  (18 , 'Kiran' , 2800.0) , (5 , 'Amar' , 1300.0))
b = sorted(a)
print(b)#[(5 , 'Amar' , 1300.0),(10 , 'Rama' , 1000.0),(15 ,'Rajesh' , 500.0),(18 , 'Kiran' , 2800.0),(20 , 'Sita' , 2000.0)]
print()#nothing
c = sorted(a , reverse = True)
print(c)#[(20 , 'Sita' , 2000.0),(18 , 'Kiran' , 2800.0),(15 ,'Rajesh' , 500.0),(10 , 'Rama' , 1000.0),(5 , 'Amar' , 1300.0)]
print()#nothing
d = sorted(a ,  key =  lambda   x  :  x[1])
print(d)#[(5 , 'Amar' , 1300.0),(18 , 'Kiran' , 2800.0),(15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0)]]
print()#nothing
e = sorted(a , key =  lambda   x  :  x[2])
print(e)#[(15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0), (20, 'Sita', 2000.0), (18, 'Kiran', 2800.0)]
print()#nothing
f = sorted(a , key = lambda   x  :  x[0])
print(f)#[(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]
print()#nothing
g = sorted(a , key = lambda  x : x[1] , reverse = True)
print(g)#[(20, 'Sita', 2000.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (5, 'Amar', 1300.0)]
#print(sorted(a , key = x[1]))#error


#26th program
# Find outputs  (Home  work)
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year'])
print(b)#[{'Make': 'Tesla', 'Model': 'X', 'Year': 1999}, {'Make': 'Mercedes', 'Model': 'C350E', 'Year': 2008}, {'Make': 'Ford', 'Model': 'Focus', 'Year': 2013}]      
#print(sorted(a))#errir due to '<' not supported betwee dict and dict


#27th program
# Find outputs  (Home  work)
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))
print(max(a , key = lambda  x  :  x[0] ))#(25 , 'Kiran' , 1500.0)
print(max(a , key = lambda  x  :  x[1] ))#(15 , 'Vamsi' , 2000.0)
print(max(a , key = lambda  x  :  x[2] ))#(20 , 'Sita' , 2800.0)
print(max(a))#(25 , 'Kiran' , 1500.0)
        

#28th program
# Find  output  (Home  work)
add = lambda  x  :   x == 25
print(add(10))#False
add = lambda  x = 25 :   x == 35
print(add())#False
add = lambda  x  :   x = 25#error
#add = lambda  x  :   x := 25