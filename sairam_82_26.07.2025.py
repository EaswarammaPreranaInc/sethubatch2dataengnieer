#1)  Find  outputs  (Home  work) 
x = 25 
y = F'{x}' 
print(y) #25 
print(type(y)) #<class 'str'> 
x = 10.8 
y = F'{x}' 
print(y) #10.8 
print(type(y)) #<class 'str'> 
x = [10,20,30,40] 
y = F'{x}' 
print(y) #[10, 20, 30, 40] 
print(type(y)) #<class 'str'> 

#2) Find  outputs  (Home  work) 
a ,  b , c = 25 , 10.8 , 'Hyd' 
print(F'{a}  \t   {b}   \t  {c}')#25 10.8 Hyd 
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}') # a=25 b=10.8 c=Hyd 
print(F'{a=}  \t   {b=}   \t  {c=}') #a=25 b=10.8 c='Hyd' 
print(F'{a:}  \t   {b:}   \t  {c:}') #25 10.8 Hyd 
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}') #a={a} b={b} c={c} 
print(F'a  =  a  \t  b  =  b  \t  c  =  c')#a=a b=b c=c 
print(F'{x =}  \t   {y =}   \t  {z =}') #Error 

#3)  Find  outputs  (Home  work) 
x = 25 
print(F'{x}')  #  25 
print(F'{{x}}')   #  {x} 
print(F'{{{x}}}')  #   {25} 
print(F'{{{{x}}}}') #{{x}} 
print(F'{{{{{x}}}}}') #{{25}} 
print(F'{{{{{{x}}}}}}') #{{{x}}} 
print(F'{{{{{{{x}}}}}}}') #{{{25}}} 
print(F'{{{{{{{{x}}}}}}}}') #{{{{x}}}} 
import math 

#4)  
a = 10 
b = 7 
sum = a + b 
difference = a - b 
product = a * b 
quotient = a / b 
remainder = a % b 
largest = max(a, b) 
smallest = min(a, b) 
sqrt_a = math.sqrt(a) 
power = a ** b 
gcd = math.gcd(a, b) 
factorial_a = math.factorial(a) 
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

#5) x = 25 
y = 'Hyd' 
x, y = y, x 
Output 
print(f"What are 'x' and 'y' after swap ?  ---> {x} and {y}") 

#6) a, b, c = 10, 20, 15 
print(a if a > b and a > c else (b if b > c else c)) 
a, b, c = 35.8, 42.8, 27.9 
print(a if a > b and a > c else (b if b > c else c)) 
a, b, c = 'RAMA', 'RAKESH', 'RAJESH' 
print(a if a > b and a > c else (b if b > c else c)) 
a = [10, 20, 15, 18] 
b = [10, 20, 32, 19] 
c = [10, 20, 25, 17] 
print(a if a > b and a > c else (b if b > c else c)) 

#7) a, b = 10, 20 
print('>' if a > b else ('<' if a < b else '='))  # < 
a, b = 70, 60 
print('>' if a > b else ('<' if a < b else '='))  # > 
a, b = 25, 25 
print('>' if a > b else ('<' if a < b else '='))  # = 
a, b = 'RAKESH', 'RAJESH' 
print('>' if a > b else ('<' if a < b else '=')) 

#8) x = -25 
print(1 if x > 0 else (-1 if x < 0 else 0))  # Output: -1 
x = 75 
print(1 if x > 0 else (-1 if x < 0 else 0))  # Output: 1 
x = 0 
print(1 if x > 0 else (-1 if x < 0 else 0))  # Output: 0 

#9) x = int(input("Enter a number: ")) 
print("Even" if x % 2 == 0 else "Odd") 

#10) length = float(input("Enter length: ")) 
breadth = float(input("Enter breadth: ")) 
area = length * breadth 
perimeter = 2 * (length + breadth) 
print(f"Area of rectangle ---> {area}") 
print(f"Perimeter of rectangle ---> {perimeter}") 

#11) import math 
radius = float(input("Enter radius: ")) 
volume = (4 / 3) * math.pi * (radius ** 3) 
print(f"Volume of sphere ---> {volume}") 

#12)  
p = float(input("Enter principal amount: ")) 
t = float(input("Enter time (years): ")) 
r = float(input("Enter rate of interest: ")) 
Simple interest = (p * t * r) / 100 
Compound interest = p * ((1 + r / 100) ** t) - p 
print(f"Simple interest ---> {simple_interest}") 
print(f"Compound interest ---> {compound_interest}") 

#13)  
x = 10 
y = 25 
temp = x 
x = y 
y = temp 
print(f"x = {x} and y = {y}") 
output: x = 25 and y = 10 

#14) 
x = 25 
y = 10 
x = x + y 
y = x - y 
x = x - y 
print(f"x = {x} and y = {y}") 

#15) 
x = -200 
y = 100 
x = x * y 
y = x // y  
x = x // y 
print(f"x = {x} and y = {y}") 
 
