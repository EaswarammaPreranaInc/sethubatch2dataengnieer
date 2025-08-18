# Find outputs (Home work)

x = 25
y = F'{x}'                    # Converts integer 25 into string using f-string
print(y)                      # '25'
print(type(y))                # <class 'str'>
x = 10.8
y = F'{x}'                    # Converts float 10.8 into string
print(y)                      # '10.8'
print(type(y))                # <class 'str'>
x = [10, 20, 30, 40]
y = F'{x}'                    # Converts list [10, 20, 30, 40] into string
print(y)                      # '[10, 20, 30, 40]'
print(type(y))                # <class 'str'>


# Find outputs (Home work)

a, b, c = 25, 10.8, 'Hyd'
print(F'{a}  \t   {b}   \t  {c}')                    # 25<2 spaces><tab><3 spaces>10.8<3 spaces><tab><2 spaces>Hyd
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}')      # a = 25<2 spaces><tab><2 spaces>b = 10.8<2 spaces><tab><2 spaces>c = Hyd
print(F'{a=}  \t   {b=}   \t  {c=}')                 # a=25<2 spaces><tab><3 spaces>b=10.8<3 spaces><tab><2 spaces>c='Hyd'
print(F'{a:}  \t   {b:}   \t  {c:}')                 # 25<2 spaces><tab><3 spaces>10.8<3 spaces><tab><2 spaces>Hyd
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}')    # a  =  {a}<2 spaces><tab><2 spaces>b  =  {b}<2 spaces><tab><3 spaces>c  =   {c}
print(F'a  =  a  \t  b  =  b  \t  c  =  c')          # Literal output (hardcoded): a = a<2 spaces><tab><2 spaces>b = b<2 spaces><tab><2 spaces>c = c
print(F'{x =}  \t   {y =}\t  {z=}')              # x,y,z not defined


# Find outputs (Home work)

x = 25
print(F'{x}')                  # Inserts the value of x
print(F'{{x}}')                # Prints {x}
print(F'{{{x}}}')              # Prints {25}
print(F'{{{{x}}}}')            # Prints {{x}}
print(F'{{{{{x}}}}}')          # Prints {{25}}
print(F'{{{{{{x}}}}}}')        # Prints {{{x}}}
print(F'{{{{{{{x}}}}}}}')      # Prints {{{25}}}
print(F'{{{{{{{{x}}}}}}}}')    # Prints {{{{x}}}}


# Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers. Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input.

import math
a = int(input("Enter 1st integer number : "))
b = int(input("Enter 2nd integer number : "))

sum_result = a + b
diff = a - b
prod = a * b
quotient = a / b
remainder = a % b
maximum = max(a, b)
minimum = min(a, b)
sqrt_a = math.sqrt(a)
power = a ** b
gcd_val = math.gcd(a, b)
fact = math.factorial(a)

print(F"{a} + {b} = {sum_result}")
print(F"{a} - {b} = {diff}")
print(F"{a} * {b} = {prod}")
print(F"{a} / {b} = {quotient:.2f}")
print(F"{a} % {b} = {remainder}")
print(F"max({a} , {b}) = {maximum}")
print(F"min({a} , {b}) = {minimum}")
print(F"{a} ^ {b} = {power:.2f}")
print(F"sqrt({a}) = {sqrt_a:.2f}")
print(F"gcd({a} , {b}) = {gcd_val}")
print(F"fact({a}) = {fact}")


# Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

x = input("Enter 1st input: ")
y = input("Enter 2nd input: ")
print(F"Before swap: x = '{x}', y = '{y}'")
x, y = y, x
print(F"After swap:  x = '{x}', y = '{y}'")


# Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

x = eval(input("Enter 1st input: "))
y = eval(input("Enter 2nd input: "))
z = eval(input("Enter 3rd input: "))
largest = x if x > y and x > z else (y if y > z else z)
print(f"Largest Input: {largest}")


# Write  a  program  to  print   '>'  if  1st  input  >  2nd  input, '<'  if  1st  input  <  2nd  input  and '='  if  inputs  are  same

x = eval(input("Enter 1st input: "))
y = eval(input("Enter 2nd input: "))
result = ">" if x > y else "<" if x < y else "="
print("Result:", result)


# Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

x = eval(input("Enter any number: "))
result = 1 if x > 0 else -1 if x < 0 else 0
print("Result:", result)


# Write  a  program  to  test  input  is  even  number  or  odd  number

x = int(input("Enter any +ve integer: "))
result = "Even number" if x % 2 == 0 else "Odd number"
print(result)


# Write  a  program  to  determine  area  and  perimeter  of  rectangle

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area = length * breadth
perimeter = 2 * (length + breadth)
print(f"Area = {area:.2f}")
print(f"Perimeter = {perimeter:.2f}")


# Write  a  program  to  determine  volume  of  a  sphere

import math
radius = float(input("Enter radius: "))
volume = (4 / 3) * math.pi * radius ** 3
print(f"Volume of sphere = {volume:.2f}")


# Write  a  program  to  determine  simple  interest  and  compound  interest

p = float(input("Enter principal: "))
t = float(input("Enter time (in years): "))
r = float(input("Enter rate of interest: "))
si = (p * t * r) / 100
ci = p * (1 + r / 100) ** t - p
print(f"Simple Interest = {si:.2f}")
print(f"Compound Interest = {ci:.2f}")


# Write  a  program  to  swap  values  of  two  objects  using  3rd   object

x = eval(input("Enter first element:"))
y = eval(input("Enter Second element:"))
temp = x
x = y
y = temp
print(f"x = {x}, y = {y}")


# Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

x = eval(input("Enter first element:"))
y = eval(input("Enter Second element:"))
x = x + y
y = x - y
x = x - y
print(f"x = {x}, y = {y}")


# Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

x = eval(input("Enter first element:"))
y = eval(input("Enter Second element:"))
x = x * y
y = x // y
x = x // y
print(f"x = {x}, y = {y}")