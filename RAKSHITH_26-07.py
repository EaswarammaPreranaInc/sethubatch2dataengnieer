#  Find  outputs  (Home  work)
x = 25			
y = F'{x}'		
print(y)		#25
print(type(y))		#<class 'str'>
x = 10.8
y = F'{x}'
print(y)		#10.8
print(type(y))		#<class 'str'>
x = [10,20,30,40]
y = F'{x}'
print(y)		#[10,20,30,40]
print(type(y))		#<class 'str'>
print()

#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}')			#25<tab>10.8<tab>Hyd
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}') 	#a=25<tab>b=10.8<tab>c=Hyd
print(F'{a=}  \t   {b=}   \t  {c=}')			#a=25<tab>b=10.8<tab>c=Hyd
print(F'{a:}  \t   {b:}   \t  {c:}')			#25<tab>10.8<tab>Hyd
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}')	#a={a}<tab>b={b}<tab>c={c}
print(F'a  =  a  \t  b  =  b  \t  c  =  c')		#a=a<tab>b=b<tab>c=c
#print(F'{x =}  \t   {y =}   \t  {z =}')		#error objects x,y,z are not available
print()

#  Find  outputs  (Home  work)
x = 25
print(F'{x}')  			#25
print(F'{{x}}')   		#{x}
print(F'{{{x}}}')  		#{25}
print(F'{{{{x}}}}')		#{{x}}
print(F'{{{{{x}}}}}')		#{{25}}
print(F'{{{{{{x}}}}}}')		#{{{x}}}
print(F'{{{{{{{x}}}}}}}')	#{{{25}}}
print(F'{{{{{{{{x}}}}}}}}')	#{{{{x}}}}
print()

#write a program to determine sum,difference,product,quotient,largest and smallest of two #numbers.Also find remainder sqrt of first inout,powewr , gcd and factorial of first input.

#Hint: Use F string to public results
from math import *
x=eval(input('Enter 1st integer number: ')) #Enter 1st integer number:10
y=eval(input('Enter 2nd integer number: ')) #Enter 2nd integer number:7
print(f"{x} + {y} = {x+y}")		#10+7=17
print(f"{x} - {y} = {x-y}")		#10-7=3
print(f"{x} * {y} = {x*y}")		#10*7=70
print(f"{x} / {y} = {x/y}")		#10/7=1.4285714285714286
print(f"{x} % {y} = {x%y}")		#10%7=3
print(f"max({x},{y}) = {max(x,y)}")	#max(10,7) = 10
print(f"min({x},{y}) = {min(x,y)}")	#min(10,7) = 7
print(f"{x} ^ {y} = {x**y}")		#10 ^ 7 = 10000000
print(f"sqrt({x})= {sqrt(x)}")		#sqrt(10)=3.1622776601683795
print(f"gcd({x},{y})= {gcd(x,y)}")	#gcd(10,7)=1
print(f"fact({x})= {factorial(x)}")	#fact(10)=3628800
print()

#Write a program to swap values of any two objects in a single statement without using 3rd #object
#Let 'x' be 25 and 'y' be 'Hyd' what are 'x' and 'y' after swap? Hyd and 25
#Hint : Swap references but not objects.

x=eval(input('Enter 1st input: '))		#Enter 1st input: 25
y=eval(input('Enter 2nd input: '))		#Enter 2nd input: Hyd
print(f"Before Swap : x='{x}'  y='{y}'")	#Before Swap: x='25'  y='Hyd'
x,y=y,x
print(f"After Swap : x='{x}'  y='{y}'")		#After Swap: x='Hyd'  y='25'
print()


#Write a program to determine largest of three inputs without using max() function.

x=eval(input('Enter 1st input: '))		#Enter 1st input:10
y=eval(input('Enter 2nd input: '))		#Enter 2nd input:20
z=eval(input('Enter 3rd input: '))		#Enter 3rd input: 15.8
print(f"Largest input: {x if (x>y and x>z) else (y if y>z else z)}")	#Largest input: 20
print()


#write a  program to print '>' if 1st input > 2nd input ,'<' if 1st input < 2nd input and #'=' if inputs are same.

x=eval(input('Enter 1st input: '))			#Enter 1st input: 10
y=eval(input('Enter 2nd input: ')) 			#Enter 2nd input: 20
print(f"Result: {'>' if (x>y) else '<' if (x<y) else '='}") # Result: <
print()

#Write a program to print 1 if input is +ve , -1 if input is -ve and 0 if input is 0

x=eval(input('Enter any number: '))		#Enter any number: 25
print(f"Result: {'1' if ( x>0) else '-1' if (x<0) else '0'}")	#Result: 1 
print()


#Write a program to test input is even number or odd number.

x=int(input('Enter any +ve integer: '))			#Enter any +ve integer: 17
print(f"{'Even number' if (x%2==0) else 'Odd number'}")	#Odd number
print()


#write a program to determine area and perimeter of rectangle.

l=int(input('Enter length: '))			#Enter length:2 
b=int(input('Enter breadth: '))			#Enter breadth:3
print(f"Area of a rectangle : {l*b}")		#Area of a rectangle: 6
print(f"Perimeter of a rectangle: {2*(l+b)}")	#Perimeter of a rectangle: 10
print()


#Write a program to determine volume of a sphere.

import math
r=int(input('Enter radius: '))			#Enter radius: 4
print(f"Volume of sphere: { 4/3 * math.pi * r**3:.2f}") #Volume of sphere: 268.08 
print()
'''

#write a program to determine simple interest and compound interest.

p=int(input('Enter principle: '))		#Enter principle: 1000
t=int(input('Enter time: '))			#Enter time: 2
r=int(input('Enter interest: '))		#Enter interest: 10
print(f"Simple interest: {(p*t*r)/100}")	#Simple interest: 200.0
print(f"Compund interest: {p*(1+r/100)**t-p:.2f}")	#Compound interest: 210.00000000000023
print()
'''
#write a program to swap values of two objects using 3rd object.

x=eval(input("Enter 1st input: "))		#Enter 1st input:10
y=eval(input("Enter 2nd input: "))		#Enter 2nd input:'Hyd'
print(f"Before Swap: x='{x}' and y='{y}'")  	#Before Swap: x=10 and y='Hyd'
z=x
x=y
y=z
print(f"After Swap: x='{x}' and y='{y}'")	#After Swap: x='Hyd' and y=10
print()


#write a program to swap values of two objects using 3rd object.
#Hint: One addition and two subtractions

x=eval(input('Enter 1st input: '))		#Enter 1st input: 10 
y=eval(input('Enter 2nd input: '))		#Enter 2nd input: 25
print(f"Before Swap: x='{x} and y='{y}'")	#Before Swap: x='10' and y='25'
z=x+y
x=z-x
y=z-y
print(f"After Swap: x='{x}' and y='{y}'")	#After swap: x='25' and y='10'
print()

#write a program to swap values of two objects without using 3rd object.
#Hint:One multiplication and two divisions

try:
 x=eval(input('Enter 1st input: '))		#Enter 1st input: -200
 y=eval(input('Enter 2nd input: '))		#Enter 2nd input: 100
 print(f"Before Swap: x='{x}' and y='{y}'")	#Before Swap: x='-200' and y='100'
 z=x*y
 x=z//x
 y=z//y
 print(f"After Swap: x='{x}' and y='{y}'")	#After Swap: x='100' and y='-200'
except:
 print('The inputs must be Non-Zero')'''



