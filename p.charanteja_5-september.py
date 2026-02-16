List/Function Output Tracing

1) change modifies a list in-place


def change(b):
    b.append(25)
    b[2] = 17
    del b[1]
# End of function
a = [10, 20, 15, 18]
print(a)
change(a)
print(a)

Output:

[10, 20, 15, 18]
[10, 15, 17, 18, 25]







2) change reassigns the parameter (local scope)

def change(b):
    b = [50, 60, 70, 80]
    print(b)
a = [10, 20, 30, 40]
print(a)
change(a)
print(a)

Output:

[10, 20, 30, 40]
[50, 60, 70, 80]
[10, 20, 30, 40]



3) Integer as immutable parameter

def f1(x):
    x = 20
    print(x)
x = 10
print(x)
f1(x)
print(x)

Output:

10
20
10




4) Tuple element assignment (causes error)

def f1(b):
    b[2] = 25
a = (10, 20, 15, 18)
print(a)
f1(a)
print(a)

Output:

(10, 20, 15, 18)
TypeError: 'tuple' object does not support item assignment





5) Lambda function with default

square = lambda x=10: x * x
print(square(5))      # 25
print(square())       # 100





6) Lambda expressions evaluation

print((lambda x: x*x)(7))                     # 49
# Next line causes error. Interpreted as: x * x(7) so x*... but x(7) is error. 
# print(lambda x: x * x(7))  # TypeError
print(lambda x: x * x)                        # <function ...>
print((lambda x=25: x*x)())                   # 625
square = lambda x: x*x
print(square(5))                              # 25






7) Lambda adding different argument types

add = lambda a, b: a + b
print(type(add))                   # <class 'function'>
print(add(10, 20))                 # 30
print(add(10.6, 20.8))             # 31.400000000000002
print(add('Hyder', 'abad'))        # Hyderabad
print(add(True, False))            # 1
print(add(25, 10.8))               # 35.8
print(add(3+4j, 5+6j))             # (8+10j)
# print(add(10, '20'))             # TypeError: unsupported operand type(s)
# print(add())                     # TypeError: missing 2
print(add)                         # <function ...>






8) Lambda with default arguments

add = lambda a=1, b=2: a+b
print(add(10, 20))     # 30
print(add())           # 3





9) Lambdas with two arguments

print((lambda x, y: x + y)(10, 20))          # 30
print((lambda x, y: x + y)(10.8, 20.6))      # 31.4
print((lambda x, y: x + y)('Hyder', 'abad')) # Hyderabad
# Last one syntax error, must use parenthesis
# print(lambda x, y: x + y ('Hyder', 'abad')) # TypeError





10) Largest of two arguments (lambda)

large = lambda a, b: a if a > b else b
print(large(10, 20))              # 20
print(large(10.7, 5.6))           # 10.7
print(large('g', 's'))            # 's'
print(large('Rama', 'Rajesh'))    # 'Rajesh'
print(large(True, False))         # True (1)





11) Power lambda

power = lambda a=3.5, b=2: a ** b
print(power(2, 3))      # 8
print(power(4.5, 4))    # 410.0625
print(power())          # 12.25
print(power(9))         # 81






12) Lambda returning tuple

all = lambda a, b: (a+b, a-b, a*b, a/b)
x = all(10, 7)
print(type(x))         # <class 'tuple'>
print(x)               # (17, 3, 70, 1.428571...)
p, q, r, s = all(9, 2)
print(p)               # 11
print(q)               # 7
print(r)               # 18
print(s)               # 4.5






13) Lambda function reference

a = lambda: 'Hyd'
print(a())         # Hyd
print(a)           # <function ...>








14) Lambda with print statements on the same line

a = lambda: 
print('Hyd') ; 
print('Sec'); 
print('Cyb')
print(a())

Output:

Sec
Cyb
Hyd
None
Explanation:The lambda is created but not called until print(a()).






15) Lambda returning a string, prints outside the lambda

a = lambda: 'Hyd'
print('Sec')
print('Cyb')
print(a())
Output:

Sec
Cyb
Hyd






16) Tuple of lambdas and prints, then various calls

a = lambda: print('Hyd'), print('Sec'), print('Cyb')
print(type(a))
print(a)
for x in a:
    print(x)
a[0]()
print(a[0]())

Output:

<class 'tuple'>
(<function <lambda> at 0x...>, None, None)
<function <lambda> at 0x...>
None
None
Hyd
None







17) Lambdas involving print/arguments/outputs

s = 'Hyd'
print(lambda s: print(s))
# print(lambda x: print(x) (s))   # Syntax Error, as print(x) returns None and None is not callable
print((lambda x: print(x))(s))
(lambda x: print(x))(s)


Output:

<function <lambda> at 0x...>
# Error if uncommented
Hyd
Hyd







18) Printing with lambdas

s = 'Hyd'
print(lambda s: print(s))             # <function ...>
# print(lambda x: print(x)(s))        # Syntax error
print((lambda x: print(x))(s))        # Hyd\nNone
(lambda x: print(x))(s)               # Hyd




19) Lambda closure/default in lambdas

x = 5
adder1 = lambda y, x=x: x + y
x = 10
adder2 = lambda y, x=x: x + y
x = 20
print(adder1(100))         # 105 (x=5 captured at creation)
print(adder2(200))         # 210 (x=10 captured at creation)
# print(adder1(300, 400))  # TypeError: got multiple values for argument 'x'





20) List of lambdas

a = [lambda x: x**2, lambda x: x**3, lambda x: x**4]
for fun in a:
    print(fun(5))          # 25, 125, 625





21) List of function references

def f1():
    print('Hyd')
def f2():
    print('Sec')
a = [f1, f2]
for x in a:
    x()                    # Hyd then Sec
# Can't have def inside a list directly: SyntaxError






22) Dictionary of lambdas

a = {'power_2': lambda x: x**2, 'power_3': lambda x: x**3, 'power_4': lambda x: x**4}
key = 'power_3'
print(a[key])     # <function ...>
print(a[key](5))  # 125






23) Lambda returned by function (closure)

def f1(x):
    return lambda n: x ** n
lamb = f1(3)
print(type(f1))      # <class 'function'>
print(type(lamb))    # <class 'function'>
print(lamb(2))       # 9
print(lamb(5))       # 243
print(lamb)          # <function ...>
# print(lamb())      # TypeError: missing 1 required argument





24) Quadratic expression (lambda factory)

def eval(a, b, c):
    return lambda x: a*x**2 + b*x + c
lam = eval(3, 4, 5)
print(lam(2))     # 25
print(lam(2.5))   # 33.25
print(lam(4))     # 69






25) Nested lambda

add = lambda x=10: lambda y: x + y
a = add()
print(a(20))          # 30
print(add(30)(40))    # 70






26) Sorting tuples/lists using lambda

a = ((10, 'Rama', 1000.0), (20, 'Sita', 2000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (5, 'Amar', 1300.0))
b = sorted(a)
print(b)   # Sorted by first element (default)
c = sorted(a, reverse=True)
print(c)   # Reverse sort by first element
d = sorted(a, key=lambda x: x[1])
print(d)   # Sort by second field (names)
e = sorted(a, key=lambda x: x[2])
print(e)   # Sort by third field (amount)
f = sorted(a, key=lambda x: x[0])
print(f)   # Sort by first field (default)
g = sorted(a, key=lambda x: x[1], reverse=True)
print(g)   # Reverse sort by name
# print(sorted(a, key=x[1]))  # Error






27) Sorting list of dictionaries with lambdas

a = [{'Make': 'Ford', 'Model': 'Focus', 'Year': 2013},
     {'Make': 'Tesla', 'Model': 'X', 'Year': 1999},
     {'Make': 'Mercedes', 'Model': 'C350E', 'Year': 2008}]
b = sorted(a, key=lambda x: x['Year'])
print(b)     # Sorted by Year ascending
print(sorted(a))  # May do default sorting, usually by key order in string






28) max() with tuple and lambdas

a = ((10, 'Rama', 1000.0), (20, 'Sita', 2800.0), (15, 'Vamsi', 2000.0), (25, 'Kiran', 1500.0), (5, 'Amar', 1300.0))
print(max(a, key=lambda x: x[0]))   # (25, 'Kiran', 1500.0)
print(max(a, key=lambda x: x[1]))   # ('Vamsi', sorts by name)
print(max(a, key=lambda x: x[2]))   # (20, 'Sita', 2800.0)
print(max(a))                       # (25, ...) by first tuple element





29) Lambda comparison/assignment errors

add = lambda x: x == 25
print(add(10))              # False
add = lambda x=25: x == 35
print(add())                # False
# add = lambda x: x = 25    # SyntaxError
# add = lambda x: x := 25   # SyntaxError (expression expected)








Matchstick Game (User vs Computer)

n = 21
while n > 1:
    user = int(input("How many matchsticks would you like to pick (1, 2, 3 or 4)? : "))
    while user < 1 or user > 4:
        user = int(input("Input can not be > 4 nor < 1, Re-enter: "))
    n -= user
    if n <= 1:
        print("You have lost the game and Computer wins")
        break
    comp = 5 - user
    print(f"Computer picks {comp} matchstick{'s' if comp > 1 else ''}")
    n -= comp
    if n <= 1:
        print("You have lost the game and Computer wins")
        break
    print(f"Matchsticks remaining: {n}")






Roman Number to Arabic Number Converter

def roman_to_arabic(roman):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    prev = 0
    for ch in reversed(roman):
        val = roman_dict[ch]
        if val >= prev:
            sum += val
        else:
            sum -= val
        prev = val
    return sum
'''
 Example outputs:
print(roman_to_arabic('III'))         # 3
print(roman_to_arabic('IV'))          # 4
print(roman_to_arabic('IX'))          # 9
print(roman_to_arabic('LVIII'))       # 58
print(roman_to_arabic('MCMXCIV'))     # 1994
print(roman_to_arabic('MMMCDXXIV'))   # 3424
'''



