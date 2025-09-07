#  Find  outputs  (Home  work)
def  change(b):
	b . append(25)
	b[2] = 17
	del  b[1]
# End  of  the  function
a = [10 , 20 , 15 , 18]
print(a)#[10, 20, 15, 18]
change(a)
print(a)#[10, 17, 18, 25]

# Find  outputs  (Home  work)
def  change(b):
	b  = [50 , 60 , 70 , 80]
	print(b)
# End  of  the  function
a = [10 , 20 , 30 , 40]
print(a)#[10 , 20 , 30 , 40]
change(a)# [50 , 60 , 70 , 80]
print(a)#[10 , 20 , 30 , 40]

Find  outputs  (Home  work)
def   f1(x):
	x = 20
	print(x)
# End  of   the   function
x = 10
print(x)#10
f1(x)#20
print(x)#10

def  f1(b):
	#b[2] = 25#tuple' object does not support item assignment
    pass
#end  of  the  function
a = (10 , 20 , 15 , 18)
print(a)#(10 , 20 , 15 , 18)
f1(a)
print(a)#(10 , 20 , 15 , 18)

#find outputs
square = lambda  x = 10  :   x * x
print(square(5))#25
print(square())#100

# Find  outputs  (Home  work)
print((lambda   x  :   x * x) (7))#49
print( lambda   x  :  x * x(7))#<function <lambda> at 0x000002EF682E1300>
print( lambda   x  :   x * x)#<function <lambda> at 0x000002EF682E1300>
print( (lambda  x = 25 :  x * x) () )#625
square = lambda  x :  x  *  x
print(square(5))#25

# Find  output (Home  work)
#How  to  define  lambda  function   to  return  sum   of  two  arguments
add = lambda x, y: x + y
print(type(add))#<class 'function'>
print(add(10 , 20))#30
print(add(10.6 , 20.8))#31.4
print(add('Hyder' , 'abad'))#Hyderabad
print(add(True , False))#1
print(add(25 , 10.8))#35.8
print(add(3 + 4j , 5 + 6j))#(8+10j)
# print(add(10 , '20'))#error
#print(add())#positional arguments: 'x' and 'y'
print(add)#<function <lambda> at 0x0000013D894E0680>

#find outputs
add = lambda  a = 1 , b = 2 :  a + b
print(add(10 , 20))#30
print(add())#3

#find outputs
print((lambda  x , y : x + y) (10 , 20) )#30
print((lambda  x , y : x + y) (10.8 , 20.6))#31.400000000000002
print((lambda  x , y : x + y) ('Hyder' , 'abad'))#Hyderabad
print(lambda  x , y : x + y  ('Hyder'  ,  'abad'))#<function <lambda> at 0x00000284A21E1300>

#  Find  outputs (Home  work)
#How  to  define  lambda  to  detrmine  largest  of  two  arguments
large = lambda x, y : x if x > y else y
print(large(10  ,  20))#20
print(large(10.7  ,  5.6))#10.7
print(large('g'  ,  's'))#s
print(large('Rama'  ,  'Rajesh'))#Rama
print(large(True  ,  False))#True

#Find  outputs (Home  work)
power = lambda  a = 3.5 , b = 2  :  a ** b
print(power(2 , 3))#8
print(power(4.5 , 4))#410.0625
print(power())#12.25
print(power(9))#81

# Find  outputs
all = lambda  a , b :  (a + b ,  a - b , a * b , a / b)
x = all(10 , 7)
print(type(x))#<class 'tuple'>
print(x)#11
p , q , r , s = all(9 , 2)
print(p)#11
print(q)#7
print(r)#18
print(s)#4.5

#  Find  outputs
a  =  lambda  :  'Hyd'
print(a())#Hyd
print(a)#<function <lambda> at 0x00000213E69E1440>

# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a())
#output
#Sec
#Cyb
#Hyd
#None

#find output
a  =  lambda  : 'Hyd' ;  print('Sec') ;  print('Cyb')
print(a())
#output
#Sec
#Cyb
#Hyd

# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a)) 
print(a) 
for  x  in  a:
	print(x)
# a() #'tuple' object is not callable
print(a[0]())
#output:
#Sec
#Cyb
#(<function <lambda> at 0x0000028796BE1440>, None, None)
#<function <lambda> at 0x0000028796BE1440>
#None
#None
#Hyd
#None

#  Find  outputs  (Home  work)
s = 'Hyd'
print(lambda  s  :  print(s))
print(lambda  x  :  print(x) (s))
print((lambda  x  :  print(x)) (s))
(lambda  x  :  print(x)) (s)
#output:
# <function <lambda> at 0x0000029072AE0680>
# Hyd
# None
# Hyd

# Find outputs  (Home  work)
x = 5
adder1 = lambda  y , x = x  : x + y
x = 10
adder2 = lambda  y , x = x : x + y
x = 20
print(adder1(100))#105
print(adder2(200))#210
print(adder1(300 , 400))#700

#Find  outputs  (Home  work)
a = [lambda   x  :  x ** 2 , lambda   x  :  x ** 3 ,  lambda   x  :  x ** 4]
for   fun   in   a:
        print(fun(5))
#output:
25
125
625

#find outputs
def   f1():
	print('Hyd')
def   f2():
	print('Sec')
a = [f1 , f2]
for  x  in  a:
	     x()
a = [def   f1():  print('Hyd') ,  def   f2():  print('Sec')]cannot write def inside a list literal.
print(a)


# Find output  (Home  work)
a = {'power_2'  :  lambda   x  :  x ** 2 ,
       'power_3'  :  lambda   x  :  x ** 3 ,
  	   'power_4'  :  lambda   x  :  x ** 4}
key = 'power_3'
print(a[key])#<function <lambda> at 0x00000219C52E0680>
print(a[key](5))#125

# Find  outputs   (Home  work)
def   eval(a , b , c):
        return   lambda    x  :    a *   x **  2  +   b * x  +  c
lam  = eval(3 , 4 , 5)
print(lam(2))#25
print(lam(2.5))#33.75
print(lam(4))#69

#Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()
print(a(20))#30
print(add(30)(40))#70

# Find  outputs
a= ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0) , (15 ,'Rajesh' , 500.0) ,  (18 , 'Kiran' , 2800.0) , (5 , 'Amar' , 1300.0))
b = sorted(a)
print(b)#(())
print()
c = sorted(a , reverse = True)
print(c)
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
print(sorted(a , key = x[1]))#name 'x' is not defined
#output:
[(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]

[(20, 'Sita', 2000.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0)]

[(5, 'Amar', 1300.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (20, 'Sita', 2000.0)]

[(15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0), (20, 'Sita', 2000.0), (18, 'Kiran', 2800.0)]

[(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]

[(20, 'Sita', 2000.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (5, 'Amar', 1300.0)]

# Find outputs  (Home  work)
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year'])
print(b)#[{'Make': 'Tesla', 'Model': 'X', 'Year': 1999}, {'Make': 'Mercedes', 'Model': 'C350E', 'Year': 2008}, {'Make': 'Ford', 'Model': 'Focus', 'Year': 2013}]
print(sorted(a))#'<' not supported between instances of 'dict' and 'dict'

#There are 21 matchsticks.
#User can pick 1,2,3 or 4 matchsticks.
#computer picks after user and whoever picks the last matchstick,they lost the game.write a program such that computer wins.

n = 21   
while n > 1:
    user = int(input("How many matchsticks would you like to pick (1, 2, 3 or 4)? : "))
    while user < 1 or user > 4:
        user = int(input("Input can not be > 4 nor < 1, Reenter : "))
    n -= user
    print(f"You picked {user} matchstick(s). Remaining = {n}")
    
    comp = 5 - user
    n -= comp
    print(f"Computer picks {comp} matchstick(s). Remaining = {n}")
print("You have lost the game and Computer wins")
output                                                                                                                                                                                                           How many matchsticks would you like to pick (1, 2, 3 or 4)? : 4
You picked 4 matchstick(s). Remaining = 17
Computer picks 1 matchstick(s). Remaining = 16
How many matchsticks would you like to pick (1, 2, 3 or 4)? : 3
You picked 3 matchstick(s). Remaining = 13
Computer picks 2 matchstick(s). Remaining = 11
How many matchsticks would you like to pick (1, 2, 3 or 4)? : 2
You picked 2 matchstick(s). Remaining = 9
Computer picks 3 matchstick(s). Remaining = 6
How many matchsticks would you like to pick (1, 2, 3 or 4)? : 1
You picked 1 matchstick(s). Remaining = 5
Computer picks 4 matchstick(s). Remaining = 1
You have lost the game and Computer wins


#convert a roman number to regular number
def roman_to_arabic(roman):
    values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    roman = roman.upper()
    total = 0
    i = 0
    
    while i < len(roman):
        if i + 1 < len(roman) and values[roman[i]] < values[roman[i+1]]:
            total += values[roman[i+1]] - values[roman[i]]
            i += 2
        else:
            total += values[roman[i]]
            i += 1
    return total
print("III   →", roman_to_arabic("III"))        # 3
print("IV    →", roman_to_arabic("IV"))         # 4
print("IX    →", roman_to_arabic("IX"))         # 9
print("LVIII →", roman_to_arabic("LVIII"))      # 58
print("MCMXCIV →", roman_to_arabic("MCMXCIV"))  # 1994
print("MMMCDXXIV →", roman_to_arabic("MMMCDXXIV"))  # 3424





















