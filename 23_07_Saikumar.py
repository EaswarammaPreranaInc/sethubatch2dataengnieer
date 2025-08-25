#  ++  and  --  operators  demo  program

a = 25
print(++a)       # Same as +(+a), gives 25
print(a++)       # Error, Python doesn't support post-increment
print(a++1)      # Error, invalid syntax in Python
print(--a)       # Same as -(-a), gives 25
print(a--)       # Error, Python doesn't support post-decrement
print(a--1)      # Error, invalid syntax in Python
print(-a)        # Unary minus, gives -25
print(+-a)       # +(-a), gives -25
print(-+a)       # -(+a), gives -25


# Semicolon demo program

print('One')           # Prints 'One'
print('Two')           # Prints 'Two'
print('Three')         # Prints 'Three'
print('Hyd') ; print('Sec') ; print('Cyb')   # Prints 'Hyd', 'Sec', and 'Cyb' on separate lines


# floor() and ceil() functions demo program

import math

print(math.floor(10.8))     # Returns the largest integer less than or equal to 10.8 → 10
print(math.ceil(10.8))      # Returns the smallest integer greater than or equal to 10.8 → 11
print(math.floor(25.0))     # Floor of 25.0 is 25
print(math.ceil(25.0))      # Ceil of 25.0 is also 25
print(math.floor(-3.5))     # Floor of -3.5 is -4 
print(math.ceil(-3.5))      # Ceil of -3.5 is -3 
print(math.floor(-9.0))     # Floor of -9.0 is -9
print(math.ceil(-9.0))      # Ceil of -9.0 is -9
print(math.floor(25.1))     # Floor of 25.1 is 25
print(math.ceil(25.1))      # Ceil of 25.1 is 26
print(floor(3.5))           # Error math method is not defined
print(ceil(3.5))            # Error math method is not defined 


# gcd() function demo program

import math

print(math.gcd(12, 15))      # GCD of 12 and 15 is 3
print(math.gcd(12, 18))      # GCD of 12 and 18 is 6
print(math.gcd(4, 7))        # GCD of 4 and 7 is 1
print(math.gcd(7, 7))        # GCD of 7 and 7 is 7
print(math.gcd(-18, -27))    # GCD of -18 and -27 is 9
print(math.gcd(-4, 6))       # GCD of -4 and 6 is 2
print(math.gcd(0, 7))        # GCD of 0 and 7 is 7
print(math.gcd(3, 0))        # GCD of 3 and 0 is 3
print(math.gcd(0, 0))        # GCD of 0 and 0 is 0
print(gcd(5, 15))            # Error math method is not defined 


# abs() function demo program

from builtins import abs
print(abs(-35.8))         # Prints 35.8 
print(abs(-27))           # Prints 27 
print(abs(29.5))          # Prints 29.5 
print(abs(32))            # Prints 32 
import builtins
print(builtins.abs(-25))  # Prints 25 using abs() from builtins


# max() and min() functions demo program

from builtins import max, min
print(max(10.8, 20.6))                  # Prints 20.6 
print(min(10.8, 20.6, 5.9, 12.3))       # Prints 5.9 
print(max(25, 10.8))                    # Prints 25 
import builtins
print(builtins.max(10, 20, 30))         # Prints 30 using max() from builtins module
print(builtins.min(10, 20, 15, 5, 12))  # Prints 5 using min() from builtins module


# pow() function demo program

from builtins import pow
print(pow(10, -2))                  # Prints 0.01 
print(pow(4, pow(3, 2)))            # Prints 262144 
import builtins
print(builtins.pow(2, 3))           # Prints 8 
print(builtins.pow(-2, -3))         # Prints -0.125 


# Find  outputs

from keyword import kwlist          # How  to  import   kw  list
print(kwlist)                       # How  to  print  kwlist
print(len(kwlist))                  # How  to  print  number  of  keywords
print(type(kwlist))                 # How  to  print  type  of kwlist
print(kwlist)                       # ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


#  Find  outputs  (Home  work)

import keyword                         # How  to  import   keyword  module
print(keyword.kwlist)                  # How  to  print  kwlist
print(len(keyword.kwlist))             # How  to  print  number  of  keywords
print(type(keyword.kwlist))            # How  to  print  type  of kwlist
print(keyword.kwlist)                  # Error 'kwlist' is not defined directly, must use keyword.kwlist