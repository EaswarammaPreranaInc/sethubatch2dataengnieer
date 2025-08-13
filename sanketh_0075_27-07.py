#Program 1: Arithmetic operations and math functions on two numbers

import math
x = int(input("Enter 1st integer number: "))
y = int(input("Enter 2nd integer number: "))

print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} / {y} = {x / y}")
print(f"{x} % {y} = {x % y}")
print(f"max({x} , {y}) = {max(x, y)}")
print(f"min({x} , {y}) = {min(x, y)}")
print(f"{x} ^ {y} = {x ** y}")
print(f"sqrt({x}) = {math.sqrt(x)}")
print(f"gcd({x} , {y}) = {math.gcd(x, y)}")
print(f"fact({x}) = {math.factorial(x)}")

#Program 2: Swap values without 3rd object

x = input("Enter 1st input: ")
y = input("Enter 2nd input: ")
print(f"Before swap: x='{x}' y='{y}'")
x, y = y, x
print(f"After swap: x='{x}' y='{y}'")

#Program 3: Largest of 3 inputs using nested ternary operator

a = eval(input("Enter 1st input: "))
b = eval(input("Enter 2nd input: "))
c = eval(input("Enter 3rd input: "))
max_val = a if a > b and a > c else (b if b > c else c)
print("Largest Input:", max_val)

#Program 4: Compare two inputs

x = eval(input("Enter 1st input: "))
y = eval(input("Enter 2nd input: "))
print("Result:", ">" if x > y else ("<" if x < y else "="))

#Program 5: Sign check

n = int(input("Enter any number: "))
print("Result:", 1 if n > 0 else (-1 if n < 0 else 0))

#Program 6: Even or Odd

num = int(input("Enter any +ve integer: "))
print("Even number" if num % 2 == 0 else "Odd number")

#Program 7: Area and Perimeter of Rectangle

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area = length * breadth
perimeter = 2 * (length + breadth)
print(f"Area = {area}, Perimeter = {perimeter}")

#Program 8: Volume of Sphere
import math
r = float(input("Enter radius: "))
volume = (4/3) * math.pi * r ** 3
print(f"Volume of sphere = {volume}")

#Program 9: Simple and Compound Interest

p = float(input("Enter principle: "))
t = float(input("Enter time: "))
r = float(input("Enter rate of interest: "))
si = (p * t * r) / 100
ci = p * ((1 + r/100) ** t) - p
print(f"Simple Interest = {si}, Compound Interest = {ci}")

#Program 10: Swap using 3rd variable

x = int(input("Enter x: "))
y = int(input("Enter y: "))
temp = x
x = y
y = temp
print(f"After swap: x = {x}, y = {y}")

#Program 11: Swap without 3rd variable (add-sub)

x = int(input("Enter x: "))
y = int(input("Enter y: "))
x = x + y
y = x - y
x = x - y
print(f"After swap: x = {x}, y = {y}")

#Program 12: Swap without 3rd variable (mul-div)

x = int(input("Enter x: "))
y = int(input("Enter y: "))
x = x * y
y = x // y
x = x // y
print(f"After swap: x = {x}, y = {y}")
