#1st
x = 25
y = F'{x}'
print(y)
print(type(y))
x = 10.8
y = F'{x}'
print(y)
print(type(y))
x = [10,20,30,40]
y = F'{x}'
print(y)
print(type(y))

#2nd
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}')
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}')
print(F'{a=}  \t   {b=}   \t  {c=}')
print(F'{a:}  \t   {b:}   \t  {c:}')
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}')
print(F'a  =  a  \t  b  =  b  \t  c  =  c')
#print(F'{x =}  \t   {y =}   \t  {z =}')

#3rd
x = 25
print(F'{x}')  #  25
print(F'{{x}}')   #  {x}
print(F'{{{x}}}')  #   {25}
print(F'{{{{x}}}}')
print(F'{{{{{x}}}}}')
print(F'{{{{{{x}}}}}}')
print(F'{{{{{{{x}}}}}}}')
print(F'{{{{{{{{x}}}}}}}}')


#4th
a= int(input('Enter 1st integer number :'))
b= int(input('Enter 2nd integer number :'))
print(f'{a}+{b}','=', a+b)
print(f'{a}-{b}','=', a-b)
print(f'{a}*{b}','=', a*b)
print(f'{a}/{b}','=', a/b)
print(f'{a}%{b}','=', a%b)
print(f'max{(a ,b)}',"=", max(a,b))
print(f'min{(a ,b)}',"=", min(a,b))
import math
print(f'{a}^{b}',"=" ,pow(a,b))
print( f'sqrt({a})' ,"=" ,math.sqrt(a))
print(f'gcd({a,b})' ,"=", math.gcd(a,b))
print(f'fact({a})' ,"=", math.factorial(a))

#5th
x=eval(input('Enter 1st input:'))
y=eval(input('Enter 2nd input:'))
print(f'Before swap:{x=} {y= }')
x,y=y,x
print(f'After swap:{x=} {y= }')

#6th
a=eval(input('Enter 1st input : '))
b=eval(input('Enter 2nd input : '))
c=eval(input('Enter 3rd input : '))
res=a if a>b and a>c else b if b>a and b>c else c
print("largest input:" , res)

#7th
a=eval(input('Enter 1st input : '))
b=eval(input('Enter 2nd input : '))
res= ">" if a>b else "<" if a<b  else "="
print("Result:" , res)

#8th
a=eval(input('Enter any number: '))
res= "1" if a>0 else "-1" if a<0  else "0"
print("Result:" , res)

#9th
a=eval(input('Enter any +ve integer: '))
res= "even number" if a%2==0 else "odd number"
print( res)

#10th
l=eval(input("Enter the length :"))
b=eval(input("Enter the breadth :"))
perimeter=2*(l+b)
area=l*b
print("The perimeter is :",perimeter)
print("The area is :",area)

#11th
r=eval(input("Enter the radius :"))
import math
vol=4/3*math.pi*r**3
print("The volume is :",vol)

#12th
p=eval(input("Enter the principal amount :"))
t=eval(input("Enter the time :"))
r=eval(input("Enter the rate of interest :"))
SI=(p*t*r)/100
CI=p*(1+r/100)(t-p)
print ("The simple Interest is:" , SI)
print ("The compound Interest is:",CI)

#13th
x=10
y=25
print("before swap x and y are" ,x,y)
temp=x
x=y
y=temp
print("after swap x and y are" ,x,y)

#14th
x=10
y=25
print("before swap x and y are" ,x,y)
x=x+y
y=x-y
x=x-y
print("after swap x and y are" ,x,y)

#15th
x=-200
y=100
print("before swap x and y are" ,x,y)
x=x*y
y=x//y
x=x//y
print("after swap x and y are" ,x,y)