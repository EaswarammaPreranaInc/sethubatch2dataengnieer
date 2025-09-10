                             NAME:M.SAICHARAN                    HOMEWORK
                             DATE:05-09-2025

1.#  Find  outputs  (Home  work)
def  change(b):
	b . append(25)
	b[2] = 17
	del  b[1]
# End  of  the  function
a = [10 , 20 , 15 , 18]
print(a)				#[10, 20, 15, 18]
change(a)
print(a)				#[10, 17, 18, 25]

'''
1)  a = [10 , 20 , 15 , 18]
    change(a)
    What  is   passed  to  change()  function ? --->
    List  itself  but  not  elements  of  list

2) Modifying  list  'b' is  as  good  as  modifying  list  'a'  becoz  'a'  and  'b'  point  to  same  list
'''


2.# Find  outputs  (Home  work)
def  change(b):
	b  = [50 , 60 , 70 , 80]
	print(b)				
# End  of  the  function
a = [10 , 20 , 30 , 40]
print(a)				#[10, 20, 30, 40]					
change(a)				#[50, 60, 70, 80]
print(a)				#[10, 20, 30, 40]					



3.#  Find  outputs  (Home  work)
def   f1(x):
	x = 20
	print(x)
# End  of   the   function
x = 10
print(x)
f1(x)
print(x)

#Output:
10
20
10


4.#  Find  outputs  (Home  work)
def  f1(b):
	b[2] = 25			#Error
#end  of  the  function
a = (10 , 20 , 15 , 18)
print(a)				#(10, 20, 15, 18)
f1(a)					#Error
print(a)				#(10, 20, 15, 18)


5.# Find  outputs (Home  work)
square = lambda  x = 10  :   x * x
print(square(5))			#25
print(square())				#100


6.# Find  outputs  (Home  work)
print((lambda   x  :   x * x) (7))	#49
print( lambda   x  :  x * x(7))		#<function <lambda> at 0x000002653219C0E0>
print( lambda   x  :   x * x)		#<function <lambda> at 0x000002653219C0E0>
print( (lambda  x = 25 :  x * x) () )	#625
square = lambda  x :  x  *  x
print(square(5))			#25


7.# Find  output (Home  work)
How  to  define  lambda  function   to  return  sum   of  two  arguments
print(type(add))			#<Class 'function'>
print(add(10 , 20))			#30
print(add(10.6 , 20.8))			#31.4
print(add('Hyder' , 'abad'))		#Hyderabad
print(add(True , False))		#1
print(add(25 , 10.8))			#35.8
print(add(3 + 4j , 5 + 6j))		#(8+10j)
print(add(10 , '20'))			#Error
print(add())				#Error
print(add)				#<function <lambda> at 0x...> (


8.#  Find  outputs (Home  work)
add = lambda  a = 1 , b = 2 :  a + b
print(add(10 , 20))			#30
print(add())				#3



9.#  Find  outputs (Home work)
print((lambda  x , y : x + y) (10 , 20) )			#30
print((lambda  x , y : x + y) (10.8 , 20.6))			#31.400000000000002
print((lambda  x , y : x + y) ('Hyder' , 'abad'))		#Hyderabad
print(lambda  x , y : x + y  ('Hyder'  ,  'abad'))		#<function <lambda> at 0x000001E88D96C040>




10.#  Find  outputs (Home  work)
How  to  define  lambda  to  detrmine  largest  of  two  arguments
print(large(10  ,  20))						#20
print(large(10.7  ,  5.6))					#10.7
print(large('g'  ,  's'))					#s
print(large('Rama'  ,  'Rajesh'))				#Rama
print(large(True  ,  False))					#True



11.#Find  outputs (Home  work)
power = lambda  a = 3.5 , b = 2  :  a ** b
print(power(2 , 3))					#8
print(power(4.5 , 4))					#410.0625
print(power())						#12.25
print(power(9))						#81


12.# Find  outputs
all = lambda  a , b :  (a + b ,  a - b , a * b , a / b)
x = all(10 , 7)
print(type(x))						#<Class 'tuple'>
print(x)						#(17, 3, 70, 1.4285714285714286)
p , q , r , s = all(9 , 2)
print(p)						#11
print(q)						#7
print(r)						#18
print(s)						#4.5


13.#  Find  outputs
a  =  lambda  :  'Hyd'
print(a())						#Hyd
print(a)						#<function <lambda> at 0x0000028F28F4BF60>


14.# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a())

#Output:
Sec
Cyb
Hyd
None


15.# Find  outputs (Home  work)
a  =  lambda  : 'Hyd' ;  print('Sec') ;  print('Cyb')
print(a())

#Output:
Sec
Cyb
Hyd


16.# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a)) 
print(a) 
for  x  in  a:
	print(x)
a()				#Error
print(a[0]())

#Output:
Sec
Cyb
<class 'tuple'>
(<function <lambda> at 0x000002465495C040>, None, None)
<function <lambda> at 0x000002465495C040>
None
None
Hyd
None



17.#  Find  outputs  (Home  work)
s = 'Hyd'
print(lambda  s  :  print(s))
print(lambda  x  :  print(x) (s))
print((lambda  x  :  print(x)) (s))
(lambda  x  :  print(x)) (s)

#Output:
<function <lambda> at 0x0000021D3D5BBF60>
<function <lambda> at 0x0000021D3D5BBF60>
Hyd
None
Hyd


18.# Find outputs  (Home  work)
x = 5
adder1 = lambda  y , x = x  : x + y
x = 10
adder2 = lambda  y , x = x : x + y
x = 20
print(adder1(100))
print(adder2(200))
print(adder1(300 , 400))

#OutPut:
105
210
700


19.#Find  outputs  (Home  work)
a = [lambda   x  :  x ** 2 , lambda   x  :  x ** 3 ,  lambda   x  :  x ** 4]
for   fun   in   a:
        print(fun(5))
#Output:
25
125
625



20.#  Find  outputs
def   f1():
	print('Hyd')
def   f2():
	print('Sec')
a = [f1 , f2]
for  x  in  a:
	     x()
a = [def   f1():  print('Hyd') ,  def   f2():  print('Sec')]
print(a)

#Output:
Hyd
Sec
[<function f1 at 0x0000023B5B77BF60>, <function f2 at 0x0000023B5B77C040>]



21.# Find output  (Home  work)
a = {'power_2'  :  lambda   x  :  x ** 2 ,
       'power_3'  :  lambda   x  :  x ** 3 ,
  	   'power_4'  :  lambda   x  :  x ** 4}
key = 'power_3'
print(a[key])
print(a[key](5))

#Output:
<function <lambda> at 0x000001675727C040>
125



22.# Find  outputs  (Home  work)
def   f1(x):
        return  lambda  n  :  x ** n
lamb = f1(3)
print(type(f1))
print(type(lamb))
print(lamb(2))
print(lamb(5))
print(lamb)
print(lamb())			#Error

#Output:
<class 'function'>
<class 'function'>
9
243
<function f1.<locals>.<lambda> at 0x000002B2F2C3C040>



23.# Find  outputs   (Home  work)
def   eval(a , b , c):
        return   lambda    x  :    a *   x **  2  +   b * x  +  c
lam  = eval(3 , 4 , 5)
print(lam(2))
print(lam(2.5))
print(lam(4))

#Output:
25
33.75
69


24.#Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()
print(a(20))
print(add(30)(40))

#Output:
30
70


25.# Find  outputs
a= ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0) , (15 ,'Rajesh' , 500.0) ,  (18 , 'Kiran' , 2800.0) , (5 , 'Amar' , 1300.0))
b = sorted(a)
print(b)
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
print(sorted(a , key = x[1]))			#Error

#Output:
[(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]

[(20, 'Sita', 2000.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0)]

[(5, 'Amar', 1300.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (20, 'Sita', 2000.0)]

[(15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0), (20, 'Sita', 2000.0), (18, 'Kiran', 2800.0)]

[(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]

[(20, 'Sita', 2000.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (5, 'Amar', 1300.0)]



26.# Find outputs  (Home  work)
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year'])
print(b)
print(sorted(a))	#Error

#Output:
[{'Make': 'Tesla', 'Model': 'X', 'Year': 1999}, {'Make': 'Mercedes', 'Model': 'C350E', 'Year': 2008}, {'Make': 'Ford', 'Model': 'Focus', 'Year': 2013}]



27.# Find outputs  (Home  work)
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))
print(max(a , key = lambda  x  :  x[0] ))
print(max(a , key = lambda  x  :  x[1] ))
print(max(a , key = lambda  x  :  x[2] ))
print(max(a))

#Output:
(25, 'Kiran', 1500.0)
(15, 'Vamsi', 2000.0)
(20, 'Sita', 2800.0)
(25, 'Kiran', 1500.0)




28.# Find  output  (Home  work)
add = lambda  x  :   x == 25
print(add(10))
add = lambda  x = 25 :   x == 35
print(add())
add = lambda  x  :   x = 25		#Error
add = lambda  x  :   x := 25		#Error


'''
29.There  are  21  matchsticks.
User  can  pick  1 , 2 , 3  or  4  matchsticks.
Computer  picks  after  user  and  whoever  picks  the  last  matchstick, they  lose  the  game.
Write  a  program  such  that  computer  wins

Logic:  Total  should  be  5

Hint: Use while  loop

						n = 21
   Iteration     user         computer             n
-------------------------------------------------------------
         1               2                 3               n = 21 - 5  = 16

	 2               3                 2               n = 16 - 5  = 11

	 3               1                 4               n = 11 - 5  =  6

	 4               4                 1               n = 6 -  5  =  1
---------------------------------------------------------------
'''
How  many  matchsticks  would  you  like  to  pick (1 , 2 ,  3 or  4) ?  :  3
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

#Program:
n = 21
print("Game started with 21 matchsticks.")
print("You can pick 1, 2, 3 or 4 matchsticks at a time.")
print("Whoever picks the last matchstick LOSES!")
while n > 1:  
    user = int(input("Your turn (1-4): "))    
    if user < 1 or user > 4:
        print("Invalid choice! Pick between 1 and 4.")
        continue    
    comp = 5 - user   
    n -= (user + comp)    
    print(f"You picked {user}, Computer picked {comp}, Remaining = {n}")   
    print("Only 1 matchstick left.")
    print("You are forced to pick the last matchstick... You LOSE! 😎")






'''
30.Write  a  program  to  convert  roman number to  arabic  number

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
Enter  any  roman  number :  MMMCDXXIV
3424

#Program:
def roman_to_int(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,'C': 100, 'D': 500, 'M': 1000}              
    total = 0
    prev = 0  
    for ch in reversed(s):
        value = roman[ch]
        if value >= prev:   
            total += value
        else:              
            total -= value
        prev = value
    return total
print(roman_to_int("III"))      
print(roman_to_int("IV"))       
print(roman_to_int("IX"))       
print(roman_to_int("LVIII"))    
print(roman_to_int("MCMXCIV"))  
print(roman_to_int("MMMCDXXIV"))

