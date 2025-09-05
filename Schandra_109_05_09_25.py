: #  Find  outputs  (Home  work)
def  change(b):
	b . append(25)
	b[2] = 17
	del  b[1]
# End  of  the  function
a = [10 , 20 , 15 , 18]
print(a)
change(a)
print(a)
############
[10, 20, 15, 18]
[10, 17, 18, 25]

'''
1)  a = [10 , 20 , 15 , 18]
    change(a)
    What  is   passed  to  change()  function ? --->


	List  itself  but  not  elements  of  list

2) Modifying  list  'b' is  as  good  as  modifying  list  'a'  becoz  'a'  and  'b'  point  to  same  list
'''


: # Find  outputs  (Home  work)
def  change(b):
	b  = [50 , 60 , 70 , 80]
	print(b)
# End  of  the  function
a = [10 , 20 , 30 , 40]
print(a)
change(a)
print(a)
###########
[10, 20, 30, 40]
[50, 60, 70, 80]
[10, 20, 30, 40]


: #  Find  outputs  (Home  work)
def   f1(x):
	x = 20
	print(x)
# End  of   the   function
x = 10
print(x)
f1(x)
print(x)
#############
10
20
10


: #  Find  outputs  (Home  work)
def  f1(b):
	b[2] = 25
#end  of  the  function
a = (10 , 20 , 15 , 18)
print(a)
f1(a)
print(a)
############
(10, 20, 15, 18)
TypeError: 'tuple' object does not support item assignment


: # Find  outputs (Home  work)
square = lambda  x = 10  :   x * x
print(square(5))
print(square())
###########
25
100


: # Find  outputs  (Home  work)
print((lambda   x  :   x * x) (7))
print( lambda   x  :  x * x(7))
print( lambda   x  :   x * x)
print( (lambda  x = 25 :  x * x) () )
square = lambda  x :  x  *  x
print(square(5))
###########
49
<function <lambda> at 0x...>
<function <lambda> at 0x...>
625
25



: # Find  output (Home  work)
How  to  define  lambda  function   to  return  sum   of  two  arguments
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
###############
<class 'function'>
30
31.4
Hyderabad
1
35.8
(8+10j)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
TypeError: <lambda>() missing 2 required positional arguments
<function <lambda> at 0x...>


: #  Find  outputs (Home  work)
add = lambda  a = 1 , b = 2 :  a + b
print(add(10 , 20))
print(add())
############
30
3


: #  Find  outputs (Home work)
print((lambda  x , y : x + y) (10 , 20) )
print((lambda  x , y : x + y) (10.8 , 20.6))
print((lambda  x , y : x + y) ('Hyder' , 'abad'))
print(lambda  x , y : x + y  ('Hyder'  ,  'abad'))
##########
30
31.4
Hyderabad
<function <lambda> at 0x...>



: #  Find  outputs (Home  work)
How  to  define  lambda  to  detrmine  largest  of  two  arguments
print(large(10  ,  20))
print(large(10.7  ,  5.6))
print(large('g'  ,  's'))
print(large('Rama'  ,  'Rajesh'))
print(large(True  ,  False))
############
20
10.7
s
Rajesh
True


: #Find  outputs (Home  work)
power = lambda  a = 3.5 , b = 2  :  a ** b
print(power(2 , 3))
print(power(4.5 , 4))
print(power())
print(power(9))
###########
8
410.0625
12.25
81


: # Find  outputs
all = lambda  a , b :  (a + b ,  a - b , a * b , a / b)
x = all(10 , 7)
print(type(x))
print(x)
p , q , r , s = all(9 , 2)
print(p)
print(q)
print(r)
print(s)
###########
<class 'tuple'>
(17, 3, 70, 1.4285714285714286)
11
7
18
4.5


: #  Find  outputs
a  =  lambda  :  'Hyd'
print(a())
print(a)
#########
Hyd
<function <lambda> at 0x...>

: # Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a())
############
Sec
Cyb
Hyd
None

: # Find  outputs (Home  work)
a  =  lambda  : 'Hyd' ;  print('Sec') ;  print('Cyb')
print(a())
############
Sec
Cyb
Hyd


: # Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a)) 
print(a) 
for  x  in  a:
	print(x)
a() 
print(a[0]())
############
Hyd
Sec
Cyb
<class 'tuple'>
(None, None, None)
None
None
None
TypeError: 'tuple' object is not callable


: #  Find  outputs  (Home  work)
s = 'Hyd'
print(lambda  s  :  print(s))
print(lambda  x  :  print(x) (s))
print((lambda  x  :  print(x)) (s))
(lambda  x  :  print(x)) (s)
##############
<function <lambda> at 0x...>
<function <lambda> at 0x...>
Hyd
Hyd


: # Find outputs  (Home  work)
x = 5
adder1 = lambda  y , x = x  : x + y
x = 10
adder2 = lambda  y , x = x : x + y
x = 20
print(adder1(100))
print(adder2(200))
print(adder1(300 , 400))
#############
105
210
TypeError: <lambda>() takes from 0 to 1 positional arguments but 2 were given


: #Find  outputs  (Home  work)
a = [lambda   x  :  x ** 2 , lambda   x  :  x ** 3 ,  lambda   x  :  x ** 4]
for   fun   in   a:
        print(fun(5))
############
25
125
625


: #  Find  outputs
def   f1():
	print('Hyd')
def   f2():
	print('Sec')
a = [f1 , f2]
for  x  in  a:
	     x()
a = [def   f1():  print('Hyd') ,  def   f2():  print('Sec')]
print(a)
###########
Hyd
Sec
SyntaxError


: # Find output  (Home  work)
a = {'power_2'  :  lambda   x  :  x ** 2 ,
       'power_3'  :  lambda   x  :  x ** 3 ,
  	   'power_4'  :  lambda   x  :  x ** 4}
key = 'power_3'
print(a[key])
print(a[key](5))
############
<function <lambda> at 0x...>
125


: # Find  outputs  (Home  work)
def   f1(x):
        return  lambda  n  :  x ** n
lamb = f1(3)
print(type(f1))
print(type(lamb))
print(lamb(2))
print(lamb(5))
print(lamb)
print(lamb())
###########
<class 'function'>
<class 'function'>
9
243
<function f1.<locals>.<lambda> at 0x...>
TypeError: <lambda>() missing 1 required positional argument: 'n'


: # Find  outputs   (Home  work)
def   eval(a , b , c):
        return   lambda    x  :    a *   x **  2  +   b * x  +  c
lam  = eval(3 , 4 , 5)
print(lam(2))
print(lam(2.5))
print(lam(4))
############
25
33.75
69


: #Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()
print(a(20))
print(add(30)(40))
#####
30
70


: # Find  outputs
a= ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0) , (15 ,'Rajesh' , 500.0) ,  (18 , 'Kiran' , 2800.0) , (5 , 'Amar' , 1300.0))
b = sorted(a)
print(b)
print()
###########
[(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0),
 (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]

c = sorted(a , reverse = True)
print(c)
print()
############
[(20, 'Sita', 2000.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0),
 (10, 'Rama', 1000.0), (5, 'Amar', 1300.0)]

d = sorted(a ,  key =  lambda   x  :  x[1])
print(d)
print()
###########
[(5, 'Amar', 1300.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0),
 (10, 'Rama', 1000.0), (20, 'Sita', 2000.0)]

e = sorted(a , key =  lambda   x  :  x[2])
print(e)
print()
#############
[(15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0),
 (20, 'Sita', 2000.0), (18, 'Kiran', 2800.0)]

f = sorted(a , key = lambda   x  :  x[0])
print(f)
print()
###########
[(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0),
 (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]

g = sorted(a , key = lambda  x : x[1] , reverse = True)
print(g)
print(sorted(a , key = x[1]))## error
############
[(20, 'Sita', 2000.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0),
 (18, 'Kiran', 2800.0), (5, 'Amar', 1300.0)]



: # Find outputs  (Home  work)
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year'])
print(b)
print(sorted(a))## error
############
[{'Make':'Tesla','Model':'X','Year':1999},
 {'Make':'Mercedes','Model':'C350E','Year':2008},
 {'Make':'Ford','Model':'Focus','Year':2013}]


: # Find outputs  (Home  work)
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))
print(max(a , key = lambda  x  :  x[0] ))
print(max(a , key = lambda  x  :  x[1] ))
print(max(a , key = lambda  x  :  x[2] ))
print(max(a))
#############
(25, 'Kiran', 1500.0)
(15, 'Vamsi', 2000.0)
(20, 'Sita', 2800.0)
(25, 'Kiran', 1500.0)



: # Find  output  (Home  work)
add = lambda  x  :   x == 25
print(add(10))
add = lambda  x = 25 :   x == 35
print(add())
add = lambda  x  :   x = 25
add = lambda  x  :   x := 25
############
False
False
SyntaxError
SyntaxError


: '''
There  are  21  matchsticks.
User  can  pick  1 , 2 , 3  or  4  matchsticks.
Computer  picks  after  user  and  whoever  picks  the  last  matchstick, they  lose  the  game.
Write  a  program  such  that  computer  wins

Logic:  Total  should  be  5

Hint: Use while  loop

						n = 21
   Iteration     user         computer             n
-------------------------------------------------------------
         1               2                 3               n = 21 - 5 = 16

		 2              3                 2               n = 16 - 5 = 11

		 3              1                 4               n = 11 - 5 = 6

		 4              4                 1               n =6 - 5 = 1
---------------------------------------------------------------
'''
: How  many  matchsticks  would  you  like  to  pick (1 , 2 ,  3 or  4) ?  :  3
Computer  picks  2 matchsticks
How  many  matchsticks  would  you  like  to  pick (1 , 2 ,  3 or  4) ?  :  0
Input  can  not  be >  4  nor  <  1,  Reenter  :  1
Computer  picks  4 matchsticks
How  many  matchsticks  would  you  like  to  pick (1 , 2 ,  3 or  4) ?  :  2
Computer  picks  3 matchsticks
How  many  matchsticks  would  you  like  to  pick (1 , 2 ,  3 or  4) ?  :  5
Input  can  not  be >  4  nor  <  1,  Reenter  :  6
Input  can  not  be >  4  nor  <  1,  Reenter  :  7
Input  can  not  be >  4  nor  <  1,  Reenter  :  8
Input  can  not  be >  4  nor  <  1,  Reenter  :  4
Computer  picks  1 matchsticks
You  have  lost  the  game  and  Computer  wins
############
n = 21

while n > 1:
    # User input
    user = int(input("How many matchsticks would you like to pick (1, 2, 3 or 4)? : "))
    
    # Validate input
    while user < 1 or user > 4:
        user = int(input("Input cannot be > 4 nor < 1, Reenter : "))

    # Computer's move (so that total = 5)
    comp = 5 - user
    print(f"Computer picks {comp} matchsticks")

    # Update remaining matchsticks
    n -= (user + comp)

print("You have lost the game and Computer wins")





: '''
Write  a  program  to  convert  roman number to  arabic  number

1) What is the output  if input is  III ? --->  3

2) What is the output if input is  IV --->  4

3) What is the output if input is  IX --->  9

4) What is the output if input is  LVIII --->  58

5) What is the output if input is MCMXCIV ---> 1994

6) What is the output  if  input  is  MMMCDXXIV --->  3424

7) Reverse  the  string

8) {'I' : 1  , 'V' : 5 , 'X' : 10 , 'L' : 50 , 'C' : 100 ,  'D' : 500 , 'M' : 1000}
    What  action  to   be  made  if  the  char  is  >=  prev ?  --->  Add  the  corresponding  value  to  sum
																							       and  assign  prev  = correponding  value

9) What  action  to   be  made  if  the  char  is  <  prev ?  --->  Subtract  the  corresponding  value  from  sum
																							      and  assign  prev  = correponding  value
'''
: Enter  any  roman  number :  MMMCDXXIV
3424
#############
def roman_to_arabic(s):
    values = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total = 0
    prev = 0
    
    # reverse the string
    for ch in reversed(s):
        val = values[ch]
        if val >= prev:
            total += val
        else:
            total -= val
        prev = val
    
    return total

# Demo
s = input("Enter any roman number : ")
print(roman_to_arabic(s))


III      → 3
IV       → 4
IX       → 9
LVIII    → 58
MCMXCIV  → 1994
MMMCDXXIV → 3424


