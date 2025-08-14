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
print(F'{{{{x}}}}') #  {x}}
print(F'{{{{{x}}}}}') #  {{25}}
print(F'{{{{{{x}}}}}}') #     {{{x}}}
print(F'{{{{{{{x}}}}}}}') #    {{{25}}}
print(F'{{{{{{{{x}}}}}}}}') #   {{{{x}}}}

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
Program:
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

'''Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object
Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  ---> Hyd  and  25
Hint:  Swap  references  but  not  objects'''
Program:
try:
    n=eval(input("Enter 1st  input : "))
    m=eval(input("Enter 2nd  input : "))
    print("Before swapping:")
    print("x =",n)
    print("y =",m)
    n,m=m,n
    print("After swapping:")
    print("x =",n)
    print("y =",m)
except:
    print("Enter String input in Quotes")

Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0
1) What  is  the  result  if  input  is  -25 ?  --->  -1
2) What  is  the  result  if  input  is  75 ?  --->  1
3) What  is  the  result  if  input  is  0 ?  --->  0
4) Use  nested  ternary operator
Program:
x=int(input("enter a number:"))
result=1 if x>0 else 0 if x==0 else -1
print(result)
Write  a  program  to  test  input  is  even  number  or  odd  number
1) What  is  an  even  number  ?  --->  Divisible  by  2
2) What  is  an  odd  number  ?  --->  Not  divisible  by  2
3) Use  ternary  operator
Program:
x=int(input("enter a number:"))
y="even" if x%2==0 else "odd"
print(y)
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle
1) What  are  the  inputs ?  ---> length  and   breadth
2) What  are  the  outputs  ?  --->  area  and  perimeter
3) What  is  the  area  of  rectangle  ?  --->  length * breadth
4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
Program:
l=int(input("enter length:"))
b=int(input("enter breadth:"))
area=l*b
perimeter=2*(l+b)
print("area of rectangle =",area)
print("perimeter of rectangle =",perimeter)

(Home  work)
Write  a  program  to  determine  volume  of  a  sphere
1) What  is  the  input ?  --->  radius
2) What  is  the  output ?  --->  volume
3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
Program:
import math
r=int(input("enter radius:"))
print(f"volume of a sphere={4/3*math.pi*r**3}")
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest
1) What  are  the  inputs  ?  --->  principle , time  and   rate  of  interest
2) What  are  the  outputs ? --->  Simple  interest   and   compound  interest
3) What  is  simple  interest  formula ?  ---> ptr / 100
4) What  is  compound  interest  formula ?  --->  p * (1  +  r  /  100)^t-p
Program:
p=int(input("enter a principle="))
t=int(input("enter time="))
r=int(input("enter rate of interest="))
si=(p*t*r)/100
ci=p*(1+r/100)**t-p
print(f"simple interest={si} and compound interest={ci}")
(Home  work)
Write  a  program  to  swap  values  of  two  objects  using  3rd   object
Let  x = 10  and  y = 25
What  are  the  values  of  x  and  y  after  swap ?  --->  x = 25  and   y = 10
Program:
x=int(input("enter a numper:"))
y=int(input("enter a number:"))
c=x+y
y=c-y
x=c-x
print("x =",x ,"and",end=" ")
print("y =",y)
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object
Hint: One  addition  and  two  subtractions
x = 25
y =  10:
Program:
x=int(input("enter a numper:"))
y=int(input("enter a number:"))
x=x+y
y=x-y
x=x-y
print("x =",x,"and",end=" ")
print("y =",y)
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object
Hint: One  multiplication  and  two  divisions
x =  -200
y =  100
Program:
x=int(input("enter a numper:"))
y=int(input("enter a number:"))
x=x*y
y=x//y
x=x//y
print("x =",x, "and",end=" ")
print("y =",y)
