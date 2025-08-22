#Format String
x = 25
y = F'{x}'
print(y)#25
print(type(y))#<class 'str'>
x = 10.8
y = F'{x}'
print(y)#10.8
print(type(y))#<class 'str'>
x = [10,20,30,40]
y = F'{x}'
print(y)#[10, 20, 30, 40]
print(type(y))#<class 'str'>

a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}')#25  	   10.8   	  Hyd
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}')#a = 25  	  b  =  10.                                            .8  	  c  =  Hyd
print(F'{a=}  \t   {b=}   \t  {c=}')#a=25  	   b=10.8   	  c='Hyd'
print(F'{a:}  \t   {b:}   \t  {c:}')#25  	   10.8   	  Hyd
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}')#a  =  {a}  	  b  =                                              {b}  	  c  =   {c}
print(F'a  =  a  \t  b  =  b  \t  c  =  c')#a  =  a  	  b  =  b  	  c                                         =  c
print(F'{x =}  \t   {y =}   \t  {z =}')#SyntaxError: invalid non-printable character U+00A0

x = 25
print(F'{x}')  #  25
print(F'{{x}}')   #  {x}
print(F'{{{x}}}')  #   {25}
print(F'{{{{x}}}}')#{{x}}
print(F'{{{{{x}}}}}')#{{25}}
print(F'{{{{{{x}}}}}}')#{{{x}}}
print(F'{{{{{{{x}}}}}}}')#{{{25}}}
print(F'{{{{{{{{x}}}}}}}}')#{{{{x}}}}
#program to demaonstrate operators
import math
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
print("a+b=" ,a+b)#a+b= 18
print("a-b=" ,a-b)#a-b= 6
print("a*b=" ,a*b)#a*b= 72
print("a/b=" ,a/b)#a/b= 2.0
print("a%b=" ,a%b)#a%b= 0
print("max(a,b)=" ,max(a,b))#max(a,b)= 12
print("min(a,b)=" ,min(a,b))#min(a,b)= 6
print("a power b=",a**b)#a power b= 2985984
print("sqrt of a=",math.sqrt(a))#sqrt of a= 3.4641016151377544
print("gcd of a,b=",math.gcd(a,b))#gcd of a,b= 6
print("factorial of a-",math.factorial(a))#factorial of a 479001600
#Swap Program
a=25
b='Hyd'
print(f"Before Swap: a= {a} b= {b}" )#Before Swap: a= 25 b= Hyd
a,b=b,a
print(f"After Swap: a= {a} b={b}")#After Swap: a= Hyd b=25
#Largest pf Three numbers using condition operator
a=eval(input("Enter 1 number: "))
b=eval(input("Enter 2nd number: "))
c=eval(input("Enetr 3rd number: "))
Largest_num = a if (a >= b and a >= c) else (b if b >= c else c)
print( "Largest number is: ",Largest_num)
#output:
#Enter 1 number:
#Enter 2nd number: 20
#Enetr 3rd number: 28
#Largest number is: 28
#Enter 1 number: 10.8
#Enter 2nd number: 12.6
#Enetr 3rd number: 9.0
#Largest number is:  12.6
#Enter 1 number: [10,20,30]
#Enter 2nd number: [10,20,40]
#Enetr 3rd number: [10,30,40]
#Largest number is:  [10, 30, 40]
#Enter 1 number: 'Rama'
#Enter 2nd number: 'Rajesh'
#Enetr 3rd number: 'Ravi'
#Largest number is:  Ravi

#progarm to demonstrate comparison operators
a=eval(input("Enter 1st element:"))
b=eval(input("Enter 2nd element:"))
res= '<' if a<b else ('>'if a>b else '=')
print(res)
#Enter 1st element:10 Enter 2nd element:20
# <
#Enter 1st element:20.8 Enter 2nd element:10.9
# >
#Enter 1st element:'Rani' Enter 2nd element:'Rani'
#=

#Program to write numbers positive and negative
a=int(input("Enter a number:"))
Res= -1 if a<0 else (+1 if a>0 else 0)
print("Result= ",Res)#Enter a number:-10
                     #Result=  -1
                     #Enter a number:9
                     #Result=  1
                     #Enter a number:0
#Even or Odd program
a=int(input("Enter a number:"))
res='Even' if a%2==0 else 'Odd'
print(res)#Enter a number:8
          #Even
          #Enter a number:5
          #Odd
                      #Result=  0

#Rectangele area and perimeter

Len=int(input("Enter a Length:"))
Bre=int(input("Enter Breadth:"))
Area=Len*Bre
print("area of rectangle is:",Area)
Perimeter=2*(Len+Bre)
print("Perimeter of rectangle is:", Perimeter)
output:
Enter a Length:4
Enter Breadth:5
area of rectangle is: 20
Perimeter of rectangle is: 18
#Volume of Sphere
import math
r=int(input("Enter radius:"))
V=4/3*math.pi* r**3
print("Volume of Sphere is:",V)
output:
Enter radius:4
Volume of Sphere is: 268.082573106329

#simple interest and compound intereset
p=int(input("Enter Principle amount:"))
r=int(input("Enter Rate:"))
t=int(input("Enter Time"))
SI=(p*t*r)/100
CI=p * ((1  +  r  /  100) ** t)-p
print("Simple Interest",SI)
print("Compund Interest",CI)
output:
Enter Principle amount:1000
Enter Rate:5
Enter Time:2
Simple Interest 100.0
Compund Interest 102.5
#swapping numbers with additiona and subtraction
a=int(input("Enter a:"))
b=int(input("Enter b:"))
print("Before Swap",a,b)
a=a+b
b=a-b
a=a-b
print("After Swap", a,b)
Enter a:10
Enter b:20
Before Swap 10 20
After Swap 20 10
#Swapping numbers using multiplication and division
a=float(input("Enter a:"))
b=float(input("Enter b:"))
print("Before Swap",a,b)
a=a*b
b=a/b
a=a/b
print("After Swap", a,b)
Enter a:25
Enter b:38
Before Swap 25.0 38.0
After Swap 38.0 25.0
