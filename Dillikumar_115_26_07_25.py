#  Find  outputs  (Home  work)
x = 25
y = F'{x}'     : 25
print(y)        :  25
print(type(y)) : <class ‘str’>
x = 10.8
y = F'{x}'
print(y)  : 10.8
print(type(y))   :  <class ‘str’>

x = [10,20,30,40]
y = F'{x}'
print(y)         : [10,20,30,40]
print(type(y))  : <class ‘str’>

#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}')   : 25 <tab> 10.8<tab> ‘Hyd’
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}')  : a=25 b=10.8 c=’Hyd’
print(F'{a=}  \t   {b=}   \t  {c=}')  : a=25 b=10.8 c=’Hyd’
print(F'{a:}  \t   {b:}   \t  {c:}')  : 25   10.8   ‘Hyd’
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}') : a  =  {a}   b  =  {b}   c  =   {c}
print(F'a  =  a  \t  b  =  b  \t  c  =  c')  : a=a   b=b   c=c
print(F'{x =}  \t   {y =}   \t  {z =}')  : o or error 
#  Find  outputs  (Home  work)
x = 25
print(F'{x}')  #  25
print(F'{{x}}')   #  {x}
print(F'{{{x}}}')  #   {25}
print(F'{{{{x}}}}')    :  25
print(F'{{{{{x}}}}}')   : {{25}}
print(F'{{{{{{x}}}}}}')  : 25
print(F'{{{{{{{x}}}}}}}')     :{{{25}}}
print(F'{{{{{{{{x}}}}}}}}')   : 25

Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
          a=12  
b=6
sum=a+b
print("sum of " , a , "and" , b , "is" ,sum)
sub=a-b
print("subraction  of " , a , "and" , b , "is" ,sub)
pro=a*b
print("product of " , a , "and" , b , "is" ,pro)
div=a/b
print("quotient  of " , a , "/" , b , "is" ,div)
rem=a%b
print("remainder of " , a , "and " , b , "is" ,rem)
maxm = max(a, b)
print("Maximum element in",a , "and" ,b,  " is:", maxm)
minm = min(a, b)
print("Minimum element in",a, "and" ,b , "is:", minm)


output : 
	sum of  12 and 6 is 18
	subraction  of  12 and 6 is 6
	product of  12 and 6 is 72
	quotient  of  12 / 6 is 2.0
	remainder of  12 and  6 is 0
	Maximum element in 12 and 6  is: 12
	Minimum element in 12 and 6 is: 6
   
Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input
#
c=math.sqrt(a)
print("squart of ",a,"is ",c)
d = math.sqrt(b)
print("Square root of", b, "is", d)
#power 
e=math.pow(a,b)
print(a,"power ",b,"is :",e)
#gcd 
gc=math.gcd(a,b)
print("gcd of", a,"and" ,b, "is", gc)
#factorial 
f = 1                               
for i in range(1, a + 1): 
    f = f * i
print("Factorial value of", a, "is:", f)
#factorial for b
f = 1
for i in range(1, b + 1): 
    f = f * i
print("Factorial value of", b, "is:", f)
Hint:  Use  F  string  to  print  results
 squart of  12 is  3.4641016151377544
Square root of 6 is 2.449489742783178
12 power  6 is : 2985984.0
gcd of 12 and 6 is 6
Factorial value of 12 is: 479001600
Factorial value of 6 is: 720
///////////////////////////
import math

a = 5
b = 3

# Square roots
c = math.sqrt(a)
print(f"Square root of {a} is {c}")

d = math.sqrt(b)
print(f"Square root of {b} is {d}")

# Power
e = math.pow(a, b)
print(f"{a} power {b} is: {e}")

# GCD
gc = math.gcd(a, b)
print(f"GCD of {a} and {b} is {gc}")

# Factorial of a
f = 1
for i in range(1, a + 1):
    f *= i
print(f"Factorial value of {a} is: {f}")

# Factorial of b
f = 1
for i in range(1, b + 1):
    f *= i
print(f"Factorial value of {b} is: {f}")

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
Enter 1st  integer  number :  10
Enter 2nd  integer  number :  7
X=10 
Y=7
10 + 7 = 17  : print(f”{x}+{y}={x+y}”)
10 - 7 = 3      : print(f”{x}-{y}={x-y}”)
10 * 7 = 70    : print(f”{x}*{y}={x*y}”)
10 / 7 = 1.4285714285714286: print(f”{x}/{y}={x/y}”)
10 % 7 = 3    : print(f”{x}%{y}={x%y}”)
print(f"{x}+{y}={x+y}")
maxm = max(x, y)
print("Maximum element in",x , "and" ,y, " is:", maxm)
minm = min(x, y)
print("Minimum element in",x, "and" ,y , "is:", minm)
10 ^ 7 = 10000000  :  print("power value for ",a,"is:", math.pow(x,y))	
sqrt(10) = 3.1622776601683795   print("root value for ",a,"is:", math.sqrt(x))
gcd(10 , 7) = 1   : print("gcde for ",a,"is:", math.gcd(x,y))


fact(10) = 3628800   : print("factorial value  for ",a,"is:", math. factorial(x))
'''
Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object
Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  ---> Hyd  and  25
#approach1 
x = 25
y = 'hyd'
print("Before swap: x =", x, "y =", y)
x, y = y, x
print("After swap: x =", x, "y =", y)
Hint:  Swap  references  but  not  objects
‘’’
Approach2:
  x = 25
y = 'hyd'
print("Before swap: x ={x}, y ={y})
x, y = y, x
print("After swap: x ={x}, y ={y})
'''
Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function
1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20
          a=[10,20,15]
         mx=a[0]
          for i in a:
               if i>mx:
                 mx=i
        print(f"maximum element in {a}is :",mx)


2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   --->  42.8
 [b=eval(input("enter values "))
mx=b[0]
for i in b:
if i>mx:
mx=i
print(f"maximum element in {a}is :",mx)


3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'
name = ['RAMA', 'RAKESH', 'RAJESH']
mx = name[0]
for i in name:
if i > mx:
mx = i
print("Maximum string is", mx)

4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] 
?  ---> [10 , 20 , 32 , 19] 
                     #  max_list = l1 if m1 >= m2 and m1 >= m3 else l2 if m2 >= m1 and m2 >= m3 else l3 
(Or )
l1=[10 , 20 , 15 , 18] 
l2=[10 , 20 , 32, 19]
l3=[10 , 20 , 25, 17] 

max1=l1[1]
for i in l1:
    if i>max1:
        max1=i
max2=l2[2]
for i in l2:
    if i>max2:
        max2=i
max3=l3[3]
for i in l3:
    if i>max3:
        max3=i

if max1 > max2 and max1 > max3 :
    print(“maximum list among 3 list is :”,l1)
elif max2>max1 and max2 > max3:
    print(“maximum list among 3 list is :”,l2)
else:
    print( “maximum list among 3 list is :”,l3)


5) Inputs  can  be  integers , floats , strings  and  so  on
l1 = [10.5, 20.2, 15.6]
l2 = [11.1, 18.8, 16.7]
l3 = [12.0, 17.5, 19.9]

m1 = l1[0]
for i in l1:
    if i > m1:
        m1 = i

m2 = l2[0]
for i in l2:
    if i > m2:
        m2 = i

m3 = l3[0]
for i in l3:
    if i > m3:
        m3 = i

if m1 >= m2 and m1 >= m3:
    print("Max float list:", l1)
elif m2 >= m1 and m2 >= m3:
    print("Max float list:", l2)
else:
    print("Max float list:", l3)


# using strings 
# String Lists
l1 = ["jakkala", "dilli", "kumar"]
l2 = ["deva", "kumar", "jakkala"]
l3 = ["devendra", "kumar", "jakkala"]

# Manual max of l1
m1 = l1[0]
for i in l1:
    if i > m1:
        m1 = i

# Manual max of l2
m2 = l2[0]
for i in l2:
    if i > m2:
        m2 = i

# Manual max of l3
m3 = l3[0]
for i in l3:
    if i > m3:
        m3 = i

# Compare max values
if m1 >= m2 and m1 >= m3:
    print("Max string list is:", l1)
elif m2 >= m1 and m2 >= m3:
    print("Max string list is:", l2)
else:
    print("Max string list is:", l3)
6) Use  nested  ternary  operator
'''
Output maximum element in [10, 20, 15]is : 20
enter values [35.8, 42.8, 27.9]
maximum element in [10, 20, 15]is : 42.8
Maximum string is RAMA
[10, 20, 32, 19]
Max float list: [10.5, 20.2, 15.6]
Max string list is: ['jakkala', 'dilli', 'kumar']
'''

Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
                                               '<'  if  1st  input  <  2nd  input  and
                                               '='  if  inputs  are  same

1)	What  is  the  result  if  inputs  are  10  and  20 ?  ---> <
2) What  is  the  result  if  inputs  are  70  and  60 ?  --->  >
3) What  is  the  result  if  inputs  are  25  and  25 ?  ---> =
   
a=10
b=20
mx= '>'  if  (a>b) else '<'
print(mx)
-----------------------------------
a=70
b=60
mx= '>'  if  (a>b) else '<'
print(mx)
-----------------------------------
a = 25
b = 25
comp = '>' if a > b else '<' if a < b else '='
print(comp)
4) Inputs  can  be  integers , floats , strings  and  so  on 
5) Use  ternary  operator
'''
Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0
1)	What  is  the  result  if  input  is  -25 ?  --->  -1
2) What  is  the  result  if  input  is  75 ?  --->  1
3) What  is  the  result  if  input  is  0 ?  --->  0
4) Use  nested  ternary  operator
   a=eval(input("enter any number "))
res= 1 if a>0 else -1 if  a<0  else 0
print(f"its a value on {a} , the result is ",{res})
output : enter any number -2
its a value on -2 , the result is  {-1}

    Write  a  program  to  test  input  is  even  number  or  odd  number
1) What  is  an  even  number  ?  --->  Divisible  by  2
2) What  is  an  odd  number  ?  --->  Not  divisible  by  2
3) Use  ternary  operator
'''
'''
 #program 
n=eval(input("enter any number "))
if n%2==0:
print(n,": is an even number ")
else:
print("its an odd number ")
////////////////////////////////
n = eval(input("Enter any number: "))
print(f"{n} is an even number" if n % 2 == 0 else "It is an odd number")
output: enter any number 11
its an odd number

(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle
1) What  are  the  inputs ?  ---> length  and   breadth
2) What  are  the  outputs  ?  --->  area  and  perimeter
3) What  is  the  area  of  rectangle  ?  --->  length * breadth
4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''
l=eval(input("enter length "))
b=eval(input("neter breadth "))
ar=l*b
print("area of rectangle is ",ar)
print("perimeter  of rectagle is ", 2*(l+b))

'''output:
enter length 14
neter breadth 20
area of rectangle is  280
perimeter  of rectagle is  68
PS F:\>
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere
1) What  is  the  input ?  --->  radius
2) What  is  the  output ?  --->  volume
3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''# program 
r=eval(input("enter radius "))
vol=(4/3)*(22/7)*(r**3)
print(f"volume of sphere with radius {r} is :{vol}")

'''output : enter radius 4.4
volume of sphere with radius 4.4 is :356.96152380952384
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest
1) What  are  the  inputs  ?  --->  principle , time  and   rate  of  interest
2) What  are  the  outputs ? --->  Simple  interest   and   compound  interest
3) What  is  simple  interest  formula ?  ---> ptr / 100
4) What  is  compound  interest  formula ?  --->  p * (1  +  r  /  100) ^  t  -  p
'''# program 
import calendar
amt=eval(input("enter amount:"))
months=int(input("enter duration in months :"))
time=months/12
interst=eval(input("rate of interest is :"))
print("simple interest ")
SI=(amt*time*interst)/100
print("simple interesrt is :",SI)
print("compund interest calculation ")
CI=amt*(1+interst/100)**time-amt
print("compound interest is ",CI)



'''output:  enter amount:10000
enter duration in months :6
rate of interest is :12
simple interest
simple interesrt is : 600.0
compund interest calculation
compound interest is  583.0052442583637
(Home  work)
Write  a  program  to  swap  values  of  two  objects  using  3rd   object
	
Let  x = 10  and  y = 25  
(Home  work)#

a=10
b=25
print(f"before swap :a= {a}, b={b}")
t=a
a=b
b=t
print(f"after swap : a= {a}, b={b}")

output :
 before swap :a= 10, b=25
after swap : a= 25, b=10

Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object
Hint: One  addition  and  two  subtractions
x = 25
y =  10
#progam 
x = 25
y =  10
print(f"before  swap : x= {x}, y={y}")
x=x+y
y=x-y
x=x-y
print(f"after swap : x= {x}, y={y}")

output: 
before  swap : x= 25, y=10
after swap : x= 10, y=25

(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object
Hint: One  multiplication  and  two  divisions
x =  -200
y =  100
'''
x =-200
y =100
print(f"before  swap : x= {x}, y={y}")
x=x*y
y=x/y
x=x/y
print(f"after swap : x= {x}, y={y}")
output : before  swap : x= -200, y=100
after swap : x= 100.0, y=-200.0
