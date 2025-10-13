  Find  outputs  (Home  work)
def  change(b):
	b . append(25)
	b[2] = 17
	del  b[1]
# End  of  the  function
a = [10 , 20 , 15 , 18]
print(a)# [10 , 20 , 15 , 18]
change(a) 
print(a) #[10,17,18,25]

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
	print(b) #[50 , 60 , 70 , 80] 
# End  of  the  function
a = [10 , 20 , 30 , 40]
print(a) #[10 , 20 , 30 , 40]
change(a)
print(a) #[10 , 20 , 30 , 40]


#  Find  outputs  (Home  work)
def   f1(x):
	x = 20
	print(x)
# End  of   the   function
x = 10
print(x) #10
f1(x) #20
print(x) #10


 #  Find  outputs  (Home  work)
def  f1(b):
	#b[2] = 25
	pass
#end  of  the  function
a = (10 , 20 , 15 , 18)
print(a) #(10 , 20 , 15 , 18)
f1(a)  #error tuple object is immutable  
print(a) #(10 , 20 , 15 , 18)

 # Find  outputs (Home  work)
square = lambda  x = 10  :   x * x
print(square(5)) #25
#print(square()) error atleast have 1 argument


 # Find  outputs  (Home  work)
print((lambda   x  :   x * x) (7)) #49
print( lambda   x  :  x * x(7)) #givves address and function becoz inside the function
print( lambda   x  :   x * x) #no value is given so same function and address
print( (lambda  x = 25 :  x * x) () ) #625
square = lambda  x :  x  *  x 
print(square(5)) #error square is not defined inside the braces


 # Find  output (Home  work)
#How  to  define  lambda  function   to  return  sum   of  two  arguments
add = (lambda x,y : x + y)
print(type(add))
print(add(10 , 20))
print(add(10.6 , 20.8))
print(add('Hyder' , 'abad'))
print(add(True , False))
print(add(25 , 10.8))
print(add(3 + 4j , 5 + 6j))
#print(add(10 , '20')) error int and str cannot be added
#print(add()) error no arguments given 
#print(add) error add is not defined

#  Find  outputs (Home  work)
add = lambda  a = 1 , b = 2 :  a + b
print(add(10 , 20)) #30
print(add()) #3 default value is printed


#  Find  outputs (Home work)
print((lambda  x , y : x + y) (10 , 20) ) #30
print((lambda  x , y : x + y) (10.8 , 20.6)) #21.4
print((lambda  x , y : x + y) ('Hyder' , 'abad')) #Hyderabad
print(lambda  x , y : x + y  ('Hyder'  ,  'abad')) #prints function and address


#  Find  outputs (Home  work)
#How  to  define  lambda  to  detrmine  largest  of  two  arguments
large = (lambda x , y : max(x,y))
print(large(10  ,  20)) #20
print(large(10.7  ,  5.6)) #10.7
print(large('g'  ,  's')) #s
print(large('Rama'  ,  'Rajesh')) #Rama
print(large(True  ,  False)) #True


#Find  outputs (Home  work)
power = lambda  a = 3.5 , b = 2  :  a ** b
print(power(2 , 3)) #8
print(power(4.5 , 4)) #410.0625
print(power()) #12.25
print(power(9)) #81


 # Find  outputs
all = lambda  a , b :  (a + b ,  a - b , a * b , a / b)
x = all(10 , 7) #3 , 70 , 1
print(type(x)) #<class 'tuple'>
print(x) #(17, 3, 70, 1.4285714285714286)
p , q , r , s = all(9 , 2)
print(p)
print(q)
print(r)
print(s)
#Takes only 1 argument given 2

#  Find  outputs
a  =  lambda  :  'Hyd'
print(a()) #Hyd
print(a) #function and address


 # Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a())
#Sec
#Cyb
#Hyd
#None

 # Find  outputs (Home  work)
a  =  lambda  : 'Hyd' ;  print('Sec') ;  print('Cyb')
print(a())
#Sec
#Cyb
#Hyd

 # Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a)) #<class 'Tuple'>
print(a)  #Sec #Cyb
for  x  in  a:
	print(x) #func and address , None, None
a() 
#print(a[0]()) #Error tuple object is not callable


#  Find  outputs  (Home  work)
s = 'Hyd'
print(lambda  s  :  print(s)) #Func and address
print(lambda  x  :  print(x) (s)) #Func and address
#print((lambda  x  :  print(x)) (s)) error name s is not defined
#(lambda  x  :  print(x)) (s)#error name s is not defined


 # Find outputs  (Home  work)
x = 5
adder1 = lambda  y , x = x  : x + y
x = 10
adder2 = lambda  y , x = x : x + y
x = 20
print(adder1(100)) #105
print(adder2(200))  #210
print(adder1(300 , 400)) #700


#Find  outputs  (Home  work)
a = [lambda   x  :  x ** 2 , lambda   x  :  x ** 3 ,  lambda   x  :  x ** 4]
for   fun   in   a:
        print(fun(5))
#25
#125
#625


#  Find  outputs
def   f1():
	print('Hyd')
def   f2():
	print('Sec')
a = [f1 , f2]
for  x  in  a:
	     x()    #Hyd <nextline> Sec
a = [def   f1():  print('Hyd') ,  def   f2():  print('Sec')]
print(a) #Syntax error


 # Find output  (Home  work)
a = {'power_2'  :  lambda   x  :  x ** 2 ,
       'power_3'  :  lambda   x  :  x ** 3 ,
  	   'power_4'  :  lambda   x  :  x ** 4}
key = 'power_3'
print(a[key]) #Func and Address
print(a[key](5)) #125


 # Find  outputs  (Home  work)
def   f1(x):
        return  lambda  n  :  x ** n
lamb = f1(3)
print(type(f1)) #<class 'function'>
print(type(lamb)) #<class 'function'>
print(lamb(2)) #9
print(lamb(5)) #243
#print(lamb) error  missing argument
#print(lamb())error  missing argument


 # Find  outputs   (Home  work)
def   eval(a , b , c):
        return   lambda    x  :    a *   x **  2  +   b * x  +  c
lam  = eval(3 , 4 , 5)
print(lam(2)) #25
print(lam(2.5)) #33.75
print(lam(4)) #69


#Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()
print(a(20)) #30
print(add(30)(40)) #70


 # Find  outputs
a= ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0) , (15 ,'Rajesh' , 500.0) ,  (18 , 'Kiran' , 2800.0) , (5 , 'Amar' , 1300.0))
b = sorted(a)
print(b) #[(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]
print()
c = sorted(a , reverse = True)
print(c)#[(20, 'Sita', 2000.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0)]
print()
d = sorted(a ,  key =  lambda   x  :  x[1])
print(d) #[(5, 'Amar', 1300.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (20, 'Sita', 2000.0)]
print()
e = sorted(a , key =  lambda   x  :  x[2])
print(e) #(15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0), (20, 'Sita', 2000.0), (18, 'Kiran', 2800.0)]
print()
f = sorted(a , key = lambda   x  :  x[0])
print(f) #[(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]
print()
g = sorted(a , key = lambda  x : x[1] , reverse = True)
print(g) #[(20, 'Sita', 2000.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (5, 'Amar', 1300.0)]
#print(sorted(a , key = x[1])) error x is not defined


 # Find outputs  (Home  work)
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year'])
print(b) #[{'Make': 'Tesla', 'Model': 'X', 'Year': 1999}, {'Make': 'Mercedes', 'Model': 'C350E', 'Year': 2008}, {'Make': 'Ford', 'Model': 'Focus', 'Year': 2013}]
#print(sorted(a)) error dict cannot be compared


 # Find outputs  (Home  work)
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))
print(max(a , key = lambda  x  :  x[0] )) #(25, 'Kiran', 1500.0)
print(max(a , key = lambda  x  :  x[1] )) #(15, 'Vamsi', 2000.0)
print(max(a , key = lambda  x  :  x[2] )) #(20, 'Sita', 2800.0)
print(max(a)) #(25, 'Kiran', 1500.0)



 # Find  output  (Home  work)
add = lambda  x  :   x == 25
print(add(10)) #False
add = lambda  x = 25 :   x == 35
print(add()) #False
#add = lambda  x  :   x = 25 cannot assign to lambda
#add = lambda  x  :   x := 25 cannot use Walrus operator 
