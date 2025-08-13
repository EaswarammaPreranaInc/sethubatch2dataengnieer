



x = 25
y = F'{x}'
print(y)             # '25'
print(type(y))       # <class 'str'>

x = 10.8
y = F'{x}'
print(y)             # '10.8'
print(type(y))       # <class 'str'>

x = [10, 20, 30, 40]
y = F'{x}'
print(y)             # '[10, 20, 30, 40]'
print(type(y))       # <class 'str'>


a, b, c = 25, 10.8, 'Hyd'
print(F'{a}  \t   {b}   \t  {c}')
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}')
print(F'{a=}  \t   {b=}   \t  {c=}')
print(F'{a:}  \t   {b:}   \t  {c:}')
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}')     # Not f-string
print(F'a  =  a  \t  b  =  b  \t  c  =  c')           # Literals
# The below line will raise NameError unless 'z' is defined
#print(F'{x =}  \t   {y =}   \t  {z =}')


x = 25
print(F'{x}')           # 25
print(F'{{x}}')         # {x}
print(F'{{{x}}}')       # {25}
print(F'{{{{x}}}}')     # {{x}}
print(F'{{{{{x}}}}}')   # {{25}}
print(F'{{{{{{x}}}}}}') # {{{x}}}
print(F'{{{{{{{x}}}}}}}')   # {{{25}}}
print(F'{{{{{{{{x}}}}}}}}') # {{{{x}}}}


import math

a, b = 10, 7
print(F"{a} + {b} = {a + b}")
print(F"{a} - {b} = {a - b}")
print(F"{a} * {b} = {a * b}")
print(F"{a} / {b} = {a / b}")
print(F"{a} % {b} = {a % b}")
print(F"max({a} , {b}) = {a if a > b else b}")
print(F"min({a} , {b}) = {a if a < b else b}")
print(F"{a} ^ {b} = {a ** b}")
print(F"sqrt({a}) = {math.sqrt(a)}")
print(F"gcd({a} , {b}) = {math.gcd(a, b)}")
print(F"fact({a}) = {math.factorial(a)}")



x = '25'
y = 'Hyd'
print(F"Before swap : x='{x}'    y='{y}'")
x, y = y, x
print(F"After swap : x='{x}'    y='{y}'")


a, b, c = 10, 20, 15
largest = a if a > b and a > c else (b if b > c else c)
print(f"Largest Input : {largest}")


a, b = 10, 20
print('>' if a > b else '<' if a < b else '=')


x = -25
print(1 if x > 0 else -1 if x < 0 else 0)



x = 45
print("Even number" if x % 2 == 0 else "Odd number")



length = 5
breadth = 3
area = length * breadth
perimeter = 2 * (length + breadth)
print(F"Area = {area}")
print(F"Perimeter = {perimeter}")


import math
r = 5
volume = (4/3) * math.pi * r**3
print(F"Volume of sphere = {volume}")



p = 1000
t = 2
r = 5

si = (p * t * r) / 100
ci = p * ((1 + r/100) ** t) - p
print(F"Simple Interest = {si}")
print(F"Compound Interest = {ci}")



x = 10
y = 25
temp = x
x = y
y = temp
print(f"x = {x}, y = {y}")



x = 25
y = 10
x = x + y
y = x - y
x = x - y
print(f"x = {x}, y = {y}")



x = -200
y = 100
x = x * y
y = x // y
x = x // y
print(f"x = {x}, y = {y}")
