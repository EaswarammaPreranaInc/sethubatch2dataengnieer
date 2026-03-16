#  Find  outputs  (Home  work)
x = 25 #Here reference x points to integer object 25
y = F'{x}' #Here we are converting the int obj 25 to string with the help of f-string
print(y) #Returns the string-int obj i.e '25'
print(type(y)) #Returns the type of y which is <class 'str'>
x = 10.8 #Here reference x points to float object 10.8
y = F'{x}' #Here we are converting the float-object to string with the help of f-string
print(y) #Returns the string-float object which is '10.8'
print(type(y)) #Returns the type of object i.e <class 'str'>
x = [10,20,30,40] #Here reference x points to list-object
y = F'{x}' #Here we are converting the list-obj into string-obj
print(y) #Returns the string-list object i.e [10,20,30,40]
print(type(y)) #Returns the type of string-list object i.e <class 'str'>


#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'  #Here references a,b,c points to 25, 10.8, 'Hyd'
print(F'{a}  \t   {b}   \t  {c}') #Returns the objects 25,10.8,'Hyd' with tab spaces in between
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}') #Returns the objects 25,10.8,'Hyd' with corresponding references in between tab spaces
print(F'{a=}  \t   {b=}   \t  {c=}') #Here samething is printed where line number 4 returns 
print(F'{a:}  \t   {b:}   \t  {c:}') #Here only the objects of their references are returned with tab spaces
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}') #Returns whatever we have specified in the quotes i.e '' as we have not mentioned f before quotes
print(F'a  =  a  \t  b  =  b  \t  c  =  c') #Returns whatever we specified in the quotes as we have not mentioned {} 
#print(F'{x =}  \t   {y =}   \t  {z =}')  #Returns the error as x,y,z are not defined 


#  Find  outputs  (Home  work)
x = 25
print(F'{x}')  #  25
print(F'{{x}}')   #  {x}
print(F'{{{x}}}')  #   {25}
print(F'{{{{x}}}}') # {{25}}
print(F'{{{{{x}}}}}') # {{25}}
print(F'{{{{{{x}}}}}}') #{{{25}}}
print(F'{{{{{{{x}}}}}}}') #{{{25}}}
print(F'{{{{{{{{x}}}}}}}}') #{{{{25}}}}



'''
1) What  is  printed  when  'x'  is  in  even  number  of  braces ?  --->  'x'  itself

2) What  is  printed  when  'x'  is  in  odd  number  of  braces ?  --->  Value   of  'x'  in  the  form  of  string

3) How  many  braces  are  printed  in  the  output ?  --->  Number  of  braces  //  2
'''

'''
Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input

Hint:  Use  F  string  to  print  results

Let  inputs  be  10  and  7,
What  is  the  sum ?  --->  17
What  is  the  difference ?  --->  3
What  is  the  product ?  ---> 70
What  is  the  quotient ?  --->  1.42
What  is  the  remainder ?  --->  3
What  is  the  largest  number ?  ---> 10
What  is  the  smallest  number ?  --->  7
What  is  the  sqrt  of  1st  input ?  --->  3.16
What  is  the  result  of  power?  --->  10000000
What  is  the  gcd  of  2  numbers ?  ---> 1
What  is  the  factorial   of  1st  input ?  ---> 10!
'''

#Program
import math
try:
    a = int(input("Enter 1st  integer  number : "))
    b = int(input("Enter 2nd  integer  number : "))
    print(F'{a} + {b} =',a+b)
    print(F'{a} - {b} =',a-b)
    print(F'{a} * {b} =',a*b)
    print(F'{a} / {b} =',a/b)
    print(F'{a} % {b} =',a%b)
    print(F'max({a},{b}) =',max(a,b))
    print(F'min({a},{b}) =',min(a,b))
    print(F'{a} ^ {b} =',a**b)
    print(f'sqrt({a}) = ',math.sqrt(a))
    print(f'gcd({a},{b}) =',math.gcd(a,b))
    print(f'fact({a}) = ',math.factorial(a))
except:
    print("Input must be an integer")

#Output
'''
Enter 1st  integer  number :  10
Enter 2nd  integer  number :  7
10 + 7 = 17
10 - 7 = 3
10 * 7 = 70
10 / 7 = 1.4285714285714286
10 % 7 = 3
max(10 , 7) = 10
min(10 , 7) = 7
10 ^ 7 = 10000000
sqrt(10) = 3.1622776601683795
gcd(10 , 7) = 1
fact(10) = 3628800
'''

'''
Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  ---> Hyd  and  25

Hint:  Swap  references  but  not  objects
'''
#Program
try:
    x = eval(input("Enter 1st input: "))
    y = eval(input("Enter 2nd input: "))
    print("Before swap:",x,y)
    x , y = y ,x
    print("After swap:",x,y)
except:
    print("String must be in quotes example:'your_string'")
    
#Output
'''
Enter 1st input: 25
Enter 2nd input: 'Hyd'
Before swap: 25 Hyd
After swap: Hyd 25
'''

'''
Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20

2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   --->  42.8

3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'

4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  ---> [10 , 20 , 32 , 19]

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use  nested  ternary  operator
'''
#Program
a = eval(input("Enter 1st input: "))
b = eval(input("Enter 2nd input: "))
c = eval(input("Enter 3rd input: "))
d = a if a > b and a > c else b if b > c else c #Here we are checking the a with b and c if it is not greater then taking b and checking with c if b is greater then returning b or else c
print(f'Largest input : {d}')

#output
'''
Enter 1st input: 20
Enter 2nd input: 35
Enter 3rd input: 15
Largest input : 35

'''

'''
Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
                                               '<'  if  1st  input  <  2nd  input  and
                                               '='  if  inputs  are  same

1) What  is  the  result  if  inputs  are  10  and  20 ?  ---> <

2) What  is  the  result  if  inputs  are  70  and  60 ?  --->  >

3) What  is  the  result  if  inputs  are  25  and  25 ?  ---> =

4) Inputs  can  be  integers , floats , strings  and  so  on

5) Use  ternary  operator
'''
a = eval(input("Enter 1st input: "))
b =  eval(input("Enter 2nd input: "))
result = ">" if a > b else "=" if a==b else "<"
print(f"Result {result}")
#output
'''
Enter 1st input: 10
Enter 2nd input: 20
Result <
Enter 1st input: 70
Enter 2nd input: 60
Result >
Enter 1st input: 25
Enter 2nd input: 25
Result =
'''

'''
Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

1) What  is  the  result  if  input  is  -25 ?  --->  -1

2) What  is  the  result  if  input  is  75 ?  --->  1

3) What  is  the  result  if  input  is  0 ?  --->  0

4) Use  nested  ternary  operator
'''

a = eval(input("Enter the input: "))
result = "-1" if a < 0 else "0" if a == 0 else "1" 
print(f"Result {result}")
#output
''' 
Enter the input: -25
Result -1
Enter the input: 75
Result 1
Enter the input: 0
Result 0
'''
'''
Write  a  program  to  test  input  is  even  number  or  odd  number

1) What  is  an  even  number  ?  --->  Divisible  by  2

2) What  is  an  odd  number  ?  --->  Not  divisible  by  2

3) Use  ternary  operator
'''
#Program
a = int(input("Enter the input: "))
r = "Even" if a%2==0 else "Odd"
print(f"Result {r}")

#output
'''
Enter the input: 5
Result Odd

Enter the input: 4
Result Even
'''

'''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  ---> length  and   breadth

2) What  are  the  outputs  ?  --->  area  and  perimeter

3) What  is  the  area  of  rectangle  ?  --->  length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''

#Program
length = float(input("Enter the length of the Rectangle: "))
breadth = float(input("Enter the Breadth of the Rectangle: "))
area = length*breadth
perimeter =  2*(length+breadth)
print(f"Area of Rectangle = {area}")
print(f"Perimeter of Rectangle = {perimeter}")

#output
'''
Enter the length of the Rectangle: 45
Enter the Breadth of the Rectangle: 30
Area of Rectangle = 1350.0
Perimeter of Rectangle = 150.0
'''

'''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  --->  radius

2) What  is  the  output ?  --->  volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''
import math
r = eval(input("Enter the Radius of the Circle: "))
sphere =  4 / 3  * math.pi *  r ** 3
print(f"Volume of sphere = {sphere}")

#output
'''
Enter the Radius of the Circle: 45
Volume of sphere = 381703.5074111598
'''

'''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  --->  principle , time  and   rate  of  interest

2) What  are  the  outputs ? --->  Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  ---> ptr / 100

4) What  is  compound  interest  formula ?  --->  p * (1  +  r  /  100) ^  t  -  p
'''
#program
p_amount = eval(input("Enter the principle amount: "))
duration = eval(input("Enter the duration: "))
roi = eval(input("Enter the Rate of intrest: "))
simple_intrest = p_amount*duration*roi / 100
compound_intrest = p_amount*(1 + roi / 100)**duration - p_amount
print(f"simple intrest = {simple_intrest} and compound_intrest= {compound_intrest}")

#output
'''
Enter the principle amount: 20000
Enter the duration: 12
Enter the Rate of intrest: 2
simple intrest = 4800.0 and compound_intrest= 5364.83589125091
'''

'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  using  3rd   object

Let  x = 10  and  y = 25
What  are  the  values  of  x  and  y  after  swap ?  --->  x = 25  and   y = 10
'''
#Program
x = eval(input("Enter 1st object: "))
y = eval(input("Enter 2nd object: "))
print(f'Before swaping x= {x} and y = {y}')
z = x
x = y
y = z
print(f'After swaping x= {x} and y = {y}')

#Output
'''
Enter 1st object: 45
Enter 2nd object: 33
Before swaping x= 45 and y = 33
After swaping x= 33 and y = 45
'''

'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10
'''
#program
x = eval(input("Enter the x value: "))
y = eval(input("Enter the y value: "))
print(f'Before swapping: x = {x}, y = {y}')
x = x+y
y = x-y
x = x-y
print(f'After swapping: x = {x}, y = {y}')


#Output
'''
Enter the x value: 25
Enter the y value: 10
Before swapping: x = 25, y = 10
After swapping: x = 10, y = 25
'''

'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  -200
y =  100
'''
x = eval(input("Enter the x value: "))
y = eval(input("Enter the y value: "))
print(f'Before swapping: x = {x}, y = {y}')
x = x*y
y = x/y
x = x/y
print(f'After swapping: x = {x}, y = {y}')
# Note: This method works only if y is not zero.    
#Output
'''
Enter the x value: 100
Enter the y value: -200
Before swapping: x = 100, y = -200
After swapping: x = -200.0, y = 100.0
'''