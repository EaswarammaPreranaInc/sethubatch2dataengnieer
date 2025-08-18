#NANDA KISHORE VEMULA (HOME WORK)



'''Enter 1st Integer number :  10
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
fact(10) = 3628800'''
import math 

n=eval(input("Enter 1st Integer number :"))
m=eval(input("Enter 2nd Integer number :"))

print(n,"+",m,"=",n+m)

print(n,"-",m,"=",n-m)

print(n,"*",m,"=",n*m)

print(n,"/",m,"=",n/m)

print(n,"%",m,"=",n%m)

print("max(",n,",",m,")","=",max(n,m))

print("min(",n,",",m,")","=",min(n,m))

print(n,"^",m,"=",n**m)

print("sqrt(",n,")","=",math.sqrt(n))

print("gcd(",n,",",m,")","=",math.gcd(n,m))

print("fact(",n,")","=",math.factorial(n))



#Even Odd Program

a=eval(input("Enter Integer input : "))
print("Result :", "Even" if a%2==0 else "Odd")


#LARGEST AMONG THREE NUMBERS

try:
    a=eval(input("Enter 1st  input : "))
    b=eval(input("Enter 2nd  input : "))
    c=eval(input("Enter 3rd  input : "))
    
    print("Largest Number :",a if a>b and a>c else b if b>c and  b>a else c)
except:
    print("Enter String input in Quotes")
    
    
 
    '''

Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  ---> length  and   breadth

2) What  are  the  outputs  ?  --->  area  and  perimeter

3) What  is  the  area  of  rectangle  ?  --->  length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''


length=eval(input("Enter 1st Integer input : "))
breadth=eval(input("Enter 2nd Integer input : "))

print("Area :", length * breadth)
print("Perimeter :", 2 * (length + breadth))




'''
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  --->  principle , time  and   rate  of  interest

2) What  are  the  outputs ? --->  Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  ---> ptr / 100

4) What  is  compound  interest  formula ?  --->  p * (1  +  r  /  100) ^  t  -  p
'''

import math
principle = eval(input("Enter principle amount : "))
time = eval(input("Enter time in years : "))
rate = eval(input("Enter rate of interest : "))

simple_interest = (principle * time * rate) / 100
compound_interest = principle * (1 + rate / 100) ** time - principle

print("Simple Interest :", simple_interest)
print("Compound Interest :", compound_interest)




'''Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  ---> Hyd  and  25

Hint:  Swap  references  but  not  objects'''

try:
    n=eval(input("Enter 1st  input : "))
    m=eval(input("Enter 2nd  input : "))
    print("Before swapping:")
    print("x =",n)
    print("y =",m)
    
    n,m=m,n  # Swapping in a single statement

    print("After swapping:")
    print("x =",n)
    print("y =",m)
except:
    print("Enter String input in Quotes")



'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  using  3rd   object

Let  x = 10  and  y = 25
What  are  the  values  of  x  and  y  after  swap ?  --->  x = 25  and   y = 10
'''
try:
    x = eval(input("Enter 1st input : "))
    y = eval(input("Enter 2nd input : "))
    temp= x
    x = y
    y = temp
    print("After swap : x =", x, "and y =", y)
except :
    print("Enter String input in Quotes")
    
    
    

    
#SWAPPING OF 2 NUMBERS USING 3RD VARIABLE

x = eval(input("Enter 1st input : "))
y = eval(input("Enter 2nd input : "))
x = x + y
y = x - y
x = x - y
print("After swap : x =", x, "and y =", y)

x = eval(input("Enter 1st input : "))
y = eval(input("Enter 2nd input : "))
x = x * y
y = x / y
x = x / y
print("After swap : x =", x, "and y =", y)




#  given number  is postive or negative or 0

a=eval(input("Enter   input : "))

print("Result :", "Positive  1 " if a>0 else "Zero 0 " if a==0 else "Negative -1 ")



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



a=eval(input("Enter 1st  input : "))
b=eval(input("Enter 2nd  input : "))

print("Result :",">" if a>b else "<")





'''
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  --->  radius

2) What  is  the  output ?  --->  volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''
import math

radius=eval(input("Enter 1st Integer input : "))
volume=(4/3) * math.pi * (radius ** 3)
print("Volume of sphere with radius", radius, "is", volume)


 #  Find  outputs  (Home  work)
x = 25
y = F'{x}'
print(y) #25
print(type(y)) #<class 'str'>
x = 10.8
y = F'{x}' 
print(y) #10.8
print(type(y))#<class 'str'>
x = [10,20,30,40]
y = F'{x}'
print(y) #[10,20,30,40]
print(type(y)) #<class 'str>


 #Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}') #25   10.8    Hyd
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}')# a = 25    b = 10.8     c = Hyd
print(F'{a=}  \t   {b=}   \t  {c=}') #a=25      b=10.8   	  c='Hyd'
print(F'{a:}  \t   {b:}   \t  {c:}') #25  	   10.8   	  Hyd
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}')#a  =  {a}  	  b  =  {b}  	  c  =   {c}
print(F'a  =  a  \t  b  =  b  \t  c  =  c') #a  =  a  	  b  =  b  	  c  =  c
print(F'{x =}  \t   {y =}   \t  {z =}') #Error x,y,z are not defined


 #  Find  outputs  (Home  work)
x = 25
print(F'{x}')  #  25
print(F'{{x}}')   #  {x}
print(F'{{{x}}}')  # {25}
print(F'{{{{x}}}}')#   {x}}
print(F'{{{{{x}}}}}')#  {{25}}
print(F'{{{{{{x}}}}}}')#     {{{x}}}
print(F'{{{{{{{x}}}}}}}')#    {{{25}}}
print(F'{{{{{{{{x}}}}}}}}')#   {{{{x}}}}