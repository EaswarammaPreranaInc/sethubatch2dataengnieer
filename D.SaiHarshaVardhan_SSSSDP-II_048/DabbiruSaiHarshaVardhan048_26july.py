x = 25
y = F'{x}'
print(y) # 25
print(type(y)) # <class 'str'>
x = 10.8
y = F'{x}'
print(y) # 10.8
print(type(y)) # <class 'str'>
x = [10,20,30,40]
y = F'{x}'
print(y) # [10, 20, 30, 40]
print(type(y)) # <class 'str'>
a , b , c = 25 , 10.8 , 'Hyd'
print(F'{a} \t {b} \t {c}') # 25 10.8 Hyd
print(F'a = {a} \t b = {b} \t c = {c}') # a = 25 b = 10.8 c = Hyd
print(F'{a=} \t {b=} \t {c=}') # a=25 b=10.8 c='Hyd'
print(F'{a:} \t {b:} \t {c:}') # 25 10.8 Hyd
print('a = {a} \t b = {b} \t c = {c}') # a = {a} b = {b} c = {c} (no formatting)
print(F'a = a \t b = b \t c = c') # a = a b = b c = c
#print(F'{x =} \t {y =} \t {z =}') # NameError: name 'x' is not defined (because x, y, z are not defined)
x = 25
print(F'{x}') # 25
print(F'{{x}}') # {x}
print(F'{{{x}}}') # {25}
print(F'{{{{x}}}}') # {{x}}
print(F'{{{{{x}}}}}') # {25}
print(F'{{{{{{x}}}}}}') # {{x}}
print(F'{{{{{{{x}}}}}}}') # {25}
print(F'{{{{{{{{x}}}}}}}}') # {{x}}
import math
a = int(input("Enter 1st integer number : "))
b = int(input("Enter 2nd integer number : "))
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} % {b} = {a % b}")
print(f"max({a} , {b}) = {max(a, b)}")
print(f"min({a} , {b}) = {min(a, b)}")
print(f"{a} ^ {b} = {a ** b}")
print(f"sqrt({a}) = {math.sqrt(a)}")
print(f"gcd({a} , {b}) = {math.gcd(a, b)}")
print(f"fact({a}) = {math.factorial(a)}")
#Write a program to swap values of any two objects in a single statement without using 3rd object?
x, y = 25, 'Hyd'
x, y = y, x
print(x, y)
#Output: x = 'Hyd' y = 25
#Write a program to determine largest of three inputs without using max() function?
a = eval(input("Enter the number: "))
b = eval(input("Enter the number: "))
c = eval(input("Enter the number: "))
largest = a if a>b and a>c else (b if b>c else c)
print("Largest: ", largest)
#if inputs are 10 , 20 and 15 ? ---> 20
#if inputs are 35.8 , 42.8 and 27.9 ? ---> 42.8
#if inputs are 'RAMA' , 'RAKESH' and 'RAJESH' ? ---> 'RAMA'
#if inputs are [10 , 20 , 15 , 18] , [10 , 20 , 32, 19] and [10 , 20 , 25, 17] ? ---> [10 , 20 , 32 , 19]
#Write a program to print '>' if 1st input > 2nd input, '<' if 1st input < 2nd input and
#'=' if inputs are same?
a = eval(input("Enter the number: "))
b = eval(input("Enter the number: "))
print('>' if a>b else ('<' if a<b else '='))
#if inputs are 10 and 20 ? ---> <
#if inputs are 70 and 60 ? ---> >
#if inputs are 25 and 25 ? ---> =
#Write a program to print 1 if input is +ve , -1 if input is -ve and 0 if input is 0?
a = int(input("Enter the number: "))
print('1' if a>0 else('-1' if a<0 else '0'))
#input: 10 output: 1
#input: -10 output: -1
#input: 0 output: 0
#Write a program to test input is even number or odd number?
a = int(input("Enter the number: "))
print('Even number' if a%2==0 else ('Odd Number' if a%2!=0 else 'Neutral'))
#Input: 45 Output: Odd Number
#Write a program to determine area and perimeter of rectangle?
l = float(input("Enter the length: "))
b = float(input("Enter the breadth: "))
area = l*b
print(area)
perimeter = 2*(l+b)
print(perimeter)
#Input: l = 10 b = 2 Output: area = 20.0 perimeter = 24.0
#Write a program to determine volume of a sphere?
from math import pi
r = float(input("Enter the radius: "))
volume = (4/3)*pi*r**3
print(volume)
#Input: r = 3 output: 113.09733552923254
#Write a program to determine simple interest and compound interest?
p = float(input("Enter the principal: "))
t = float(input("Enter the time(in years): "))
r = float(input("Enter the rate: "))
si = (p*t*r)/100
ci = p * ((1 + r / 100) ** t)- p
print(si)
print(ci)
#input: p = 1000 t = 2 r = 5 si = 100.0 ci = 102.5
#Write a program to swap values of two objects using 3rd object?
x = input("Enter the number: ")
y = input("Enter the number: ")
temp = x
x = y
y = temp
print("x=", x)
print("y=", y)
#Input: x = 27 y = 72 Output: x= 72 y = 27
#Write a program to swap values of two objects without using 3rd object?
x = int(input("Enter the number: "))
y = int(input("Enter the number: "))
x = x+y
y = x-y
x = x-y
print("x:",x)
print("y:",y)
#Input: x = 25 y = 10 Output: x= 10 y = 25
#Write a program to swap values of two objects without using 3rd object?
x = int(input("Enter the number: "))
y = int(input("Enter the number: "))
x = x*y
y = x//y
x = x//y
print("x:",x)
print("y:",y)
#Input: x = -200 y = 100 Output: x= 100 y = -200
 
