a = 25
print(++a)        # 25      # +(+a) = +25 = 25
print(a++)        # Error Python does not support post-increment like a++
print(a++1)       # 26      # a + (+1) = 25 + 1 = 26
print(--a)        # 25      # -(-a) = 25
print(a--)        # Error Python does not support post-decrement like a--
print(a--1)       # 26      # a - (-1) = 25 - (-1) = 25 + 1 = 26 (if a was still 25)
print(-a)         # -25     # Unary minus of a = -25
print(+-a)        # -25     # +(−a) = −25
print(-+a)        # -25     # −(+a) = −25

print('One')       # One
print('Two')       # Two
print('Three')     # Three
print('Hyd') ; print('Sec') ; print('Cyb')  # Hyd
 				          #Sec
          #Cyb

import math
print(math.floor(10.8))    # 10
print(math.ceil(10.8))     # 11
print(math.floor(25.0))    # 25
print(math.ceil(25.0))     # 25
print(math.floor(-3.5))    # -4
print(math.ceil(-3.5))     # -3
print(math.floor(-9.0))    # -9
print(math.ceil(-9.0))     # -9
print(math.floor(25.1))    # 25
print(math.ceil(25.1))     # 26
print(floor(3.5))          # Error: name 'floor' is not defined
print(ceil(3.5))           # Error: name 'ceil' is not defined

import math
print(math.gcd(12, 15))     # 3
print(math.gcd(12, 18))     # 6
print(math.gcd(4, 7))       # 1
print(math.gcd(7, 7))       # 7
print(math.gcd(-18, -27))   # 9
print(math.gcd(-4, 6))      # 2
print(math.gcd(0, 7))       # 7
print(math.gcd(3, 0))       # 3
print(math.gcd(0, 0))       # 0
print(gcd(5, 15))           # Error: name 'gcd' is not defined



from builtins import abs
print(abs(-35.8))      # 35.8
print(abs(-27))        # 27
print(abs(29.5))       # 29.5
print(abs(32))         # 32
import builtins
print(builtins.abs(-25))   # 25

from builtins import max, min
print(max(10.8, 20.6))                    # 20.6
print(min(10.8, 20.6, 5.9, 12.3))         # 5.9
print(max(25, 10.8))                      # 25
import builtins
print(builtins.max(10, 20, 30))           # 30
print(builtins.min(10, 20, 15, 5, 12))    # 5

from builtins import pow
print(pow(10, -2))            # 0.01        # 10 ** -2 = 1 / 100
print(pow(4, pow(3, 2)))      # 262144      # 3**2 = 9, then 4**9 = 262144
import builtins
print(builtins.pow(2, 3))     # 8           # 2**3 = 8
print(builtins.pow(-2, -3))   # -0.125      # (-2)**-3 = 1 / (-8) = -0.125

from keyword import kwlist                  # How to import kw list
print(kwlist)          # How to print kwlist
print(len(kwlist))     # How to print number of keywords
print(type(kwlist))    # How to print type of kwlist
['False', 'None', 'True', 'and', 'as', ..., 'yield']         # print(keyword.kwlist)

import keyword                  # How to import keyword module
print(keyword.kwlist)          # How to print kwlist
print(len(keyword.kwlist))     # How to print number of keywords
print(type(keyword.kwlist))    # How to print type of kwlist
Error: name 'kwlist' is not defined   # print(kwlist)
