#  Find  outputs  (Home  work)
def  change(b):
	b . append(25)
	b[2] = 17
	del  b[1]
# End  of  the  function
a = [10 , 20 , 15 , 18]
print(a)  # [10, 20, 15, 18]
change(a)
print(a)  # [10, 17, 18, 25]


'''
1)  a = [10 , 20 , 15 , 18]
    change(a)
    What  is   passed  to  change()  function ? --->


	List  itself  but  not  elements  of  list

2) Modifying  list  'b' is  as  good  as  modifying  list  'a'  becoz  'a'  and  'b'  point  to  same  list
'''

# Find  outputs  (Home  work)
def  change(b):
	b  = [50 , 60 , 70 , 80]
	print(b)
# End  of  the  function
a = [10 , 20 , 30 , 40]
print(a)  # [10, 20, 30, 40]
change(a) # [50, 60, 70, 80]
print(a)  # [10, 20, 30, 40]

#  Find  outputs  (Home  work)
def   f1(x):
	x = 20
	print(x)
# End  of   the   function
x = 10
print(x) # 10
f1(x)    # 20
print(x) # 10

#  Find  outputs  (Home  work)
def  f1(b):
	b[2] = 25
#end  of  the  function
a = (10 , 20 , 15 , 18)
print(a) # (10, 20, 15, 18)
f1(a)    # Error 
print(a)


# Find  outputs (Home  work)
square = lambda  x = 10  :   x * x
print(square(5)) # 25
print(square())  # 100


# Find  outputs  (Home  work)
print((lambda   x  :   x * x) (7)) # 49
print( lambda   x  :  x * x(7))  # <function <lambda> at 0x...>
print( lambda   x  :   x * x)   # <function <lambda> at 0x...>
print( (lambda  x = 25 :  x * x) () ) # 625
square = lambda  x :  x  *  x
print(square(5)) # 25

# Find  output (Home  work)
How  to  define  lambda  function   to  return  sum   of  two  arguments
print(type(add)) # <class 'function'>
print(add(10 , 20))  # 30
print(add(10.6 , 20.8))  # 31.4
print(add('Hyder' , 'abad')) # Hyderabad 
print(add(True , False)) # 1
print(add(25 , 10.8)) # 35.8
print(add(3 + 4j , 5 + 6j))  # 8+10j
print(add(10 , '20'))  # Error 
print(add()) # Error 
print(add)  # <function <lambda> at 0x...>

#  Find  outputs (Home  work)
add = lambda  a = 1 , b = 2 :  a + b
print(add(10 , 20))  # 30
print(add())   # 3

#  Find  outputs (Home work)
print((lambda  x , y : x + y) (10 , 20) )  # 30
print((lambda  x , y : x + y) (10.8 , 20.6))  # 31.4
print((lambda  x , y : x + y) ('Hyder' , 'abad')) # Hyderabad 
print(lambda  x , y : x + y  ('Hyder'  ,  'abad'))  # <function <lambda> at 0x...>


#  Find  outputs (Home  work)
How  to  define  lambda  to  detrmine  largest  of  two  arguments
print(large(10  ,  20)) # 20
print(large(10.7  ,  5.6)) # 10.7
print(large('g'  ,  's')) # s
print(large('Rama'  ,  'Rajesh')) # Rama
print(large(True  ,  False))  # True


#Find  outputs (Home  work)
power = lambda  a = 3.5 , b = 2  :  a ** b
print(power(2 , 3)) # 8
print(power(4.5 , 4)) # 410.06
print(power())  # 12.25
print(power(9)) # 81


# Find  outputs
all = lambda  a , b :  (a + b ,  a - b , a * b , a / b)
x = all(10 , 7)
print(type(x))  # <class 'tuple'>
print(x)  # (17, 3, 70, 1.428
p , q , r , s = all(9 , 2)
print(p) # 11
print(q) # 7
print(r) # 18
print(s) # 4.5

#  Find  outputs
a  =  lambda  :  'Hyd'
print(a()) # Hyd
print(a)  # <function <lambda> at 0x...>


# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a()) # Sec
             Hyd
             Cyb 
             None


# Find  outputs (Home  work)
a  =  lambda  : 'Hyd' ;  print('Sec') ;  print('Cyb')
print(a()) # Sec
             Cyb
             Hyd

# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a))  # <class 'function'>
print(a)  # <function <lambda> at 0x...>
for  x  in  a:
	print(x)
a() 
print(a[0]()) # Error

#  Find  outputs  (Home  work)
s = 'Hyd'
print(lambda  s  :  print(s))  # <function <lambda> at 0x...>
print(lambda  x  :  print(x) (s))  # Error 
print((lambda  x  :  print(x)) (s)) 
(lambda  x  :  print(x)) (s)


# Find outputs  (Home  work)
x = 5
adder1 = lambda  y , x = x  : x + y
x = 10
adder2 = lambda  y , x = x : x + y
x = 20
print(adder1(100)) # 105
print(adder2(200)) # 210
print(adder1(300 , 400)) # 700


#Find  outputs  (Home  work)
a = [lambda   x  :  x ** 2 , lambda   x  :  x ** 3 ,  lambda   x  :  x ** 4]
for   fun   in   a:
        print(fun(5)) # 25
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
a = [def   f1():  print('Hyd') ,  def   f2():  print('Sec')]
print(a) # Hyd
           Sec

# Find output  (Home  work)
a = {'power_2'  :  lambda   x  :  x ** 2 ,
       'power_3'  :  lambda   x  :  x ** 3 ,
  	   'power_4'  :  lambda   x  :  x ** 4}
key = 'power_3'
print(a[key]) # <function <lambda> at 0x...>
print(a[key](5)) # 125

# Find  outputs  (Home  work)
def   f1(x):
        return  lambda  n  :  x ** n
lamb = f1(3)
print(type(f1)) # <class 'function'>
print(type(lamb)) # <class 'function'>
print(lamb(2)) # 9
print(lamb(5)) # 243
print(lamb) # <function f1.<locals>.<lambda> at 0x...>
print(lamb()) # Error


# Find  outputs   (Home  work)
def   eval(a , b , c):
        return   lambda    x  :    a *   x **  2  +   b * x  +  c
lam  = eval(3 , 4 , 5)
print(lam(2)) # 25
print(lam(2.5)) # 33.75
print(lam(4)) # 69

#Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()
print(a(20)) # 30
print(add(30)(40)) # 70

# Find  outputs
a= ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0) , (15 ,'Rajesh' , 500.0) ,  (18 , 'Kiran' , 2800.0) , (5 , 'Amar' , 1300.0))
b = sorted(a)
print(b)
print()  # [(5, 'Amar', 1300.0),
 (10, 'Rama', 1000.0),
 (15, 'Rajesh', 500.0),
 (18, 'Kiran', 2800.0),
 (20, 'Sita', 2000.0)]
c = sorted(a , reverse = True)
print(c)
print() # [(20, 'Sita', 2000.0),
 (18, 'Kiran', 2800.0),
 (15, 'Rajesh', 500.0),
 (10, 'Rama', 1000.0),
 (5, 'Amar', 1300.0)]
d = sorted(a ,  key =  lambda   x  :  x[1])
print(d)
print() # [(5, 'Amar', 1300.0),
 (18, 'Kiran', 2800.0),
 (15, 'Rajesh', 500.0),
 (10, 'Rama', 1000.0),
 (20, 'Sita', 2000.0)]
e = sorted(a , key =  lambda   x  :  x[2])
print(e)
print()  #[(15, 'Rajesh', 500.0),
 (10, 'Rama', 1000.0),
 (5, 'Amar', 1300.0),
 (20, 'Sita', 2000.0),
 (18, 'Kiran', 2800.0)]
f = sorted(a , key = lambda   x  :  x[0])
print(f)
print()  # [(5, 'Amar', 1300.0),
 (10, 'Rama', 1000.0),
 (15, 'Rajesh', 500.0),
 (18, 'Kiran', 2800.0),
 (20, 'Sita', 2000.0)]
g = sorted(a , key = lambda  x : x[1] , reverse = True)
print(g)  # [(20, 'Sita', 2000.0),
 (10, 'Rama', 1000.0),
 (15, 'Rajesh', 500.0),
 (18, 'Kiran', 2800.0),
 (5, 'Amar', 1300.0)]
print(sorted(a , key = x[1])) # Error



# Find outputs  (Home  work)
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year'])
print(b) # [
  {'Make': 'Tesla', 'Model': 'X', 'Year': 1999},
  {'Make': 'Mercedes', 'Model': 'C350E', 'Year': 2008},
  {'Make': 'Ford', 'Model': 'Focus', 'Year': 2013}
]
print(sorted(a)) # Error


# Find outputs  (Home  work)
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))
print(max(a , key = lambda  x  :  x[0] )) # (25, 'Kiran', 1500.0)
print(max(a , key = lambda  x  :  x[1] )) # (15, 'Vamsi', 2000.0)
print(max(a , key = lambda  x  :  x[2] )) # (20, 'Sita', 2800.0)
print(max(a)) # (25, 'Kiran', 1500.0)


# Find  output  (Home  work)
add = lambda  x  :   x == 25
print(add(10)) # False 
add = lambda  x = 25 :   x == 35
print(add()) # False 
add = lambda  x  :   x = 25 # Error 
add = lambda  x  :   x := 25 # Error


'''
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


n = 21
print("There are 21 matchsticks.")
print("You can pick 1, 2, 3 or 4 matchsticks.")
print("Whoever picks the last matchstick loses!")

while n > 1:
    user = int(input("\nYour turn (pick 1-4): "))
    if user < 1 or user > 4:
        print("Invalid choice! Pick between 1 and 4.")
        continue

    comp = 5 - user
    print(f"Computer picks: {comp}")

    n -= (user + comp)
    print(f"Matchsticks left: {n}")

print("\nOnly 1 matchstick left!")
print("You are forced to pick it.")
print(" Computer wins!")

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
You  have  lost  the  game  and  Computer  wins


'''
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
																							      and  assign  prev  = correponding  value
'''


def roman_to_int(s):
    roman_map = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    s = s[::-1]   
    total = 0
    prev = 0

    for ch in s:
        val = roman_map[ch]
        if val >= prev:
            total += val
        else:
            total -= val
        prev = val
    return total



print("III     ->", roman_to_int("III"))      
print("IV      ->", roman_to_int("IV"))       
print("IX      ->", roman_to_int("IX"))       
print("LVIII   ->", roman_to_int("LVIII"))    
print("MCMXCIV ->", roman_to_int("MCMXCIV"))  
print("MMMCDXXIV ->", roman_to_int("MMMCDXXIV")) # 3424


Enter  any  roman  number :  MMMCDXXIV
3424
