# ++ and -- operators demo program
a = 25
print(++a)        # +(+a) = +25 => 25
# print(a++)      # Error: Python does not support ++ or -- operators (SyntaxError)
# print(a++1)     # Error: invalid syntax
print(--a)        # -(-a) = +25 => 25
# print(a--)      # Error: Python does not support ++ or -- operators (SyntaxError)
# print(a--1)     # Error: invalid syntax
print(-a)         # -a = -25
print(+-a)        # +(-a) = -25
print(-+a)        # -(+a) = -25

# Semicolon demo program
print('One');                 # One
print('Two');                 # Two
print('Three');               # Three
print('Hyd'); print('Sec'); print('Cyb')  
# Hyd
# Sec
# Cyb

# floor() and ceil() functions demo program
import math
print(math.floor(10.8))        # 10
print(math.ceil(10.8))         # 11
print(math.floor(25.0))        # 25
print(math.ceil(25.0))         # 25
print(math.floor(-3.5))        # -4
print(math.ceil(-3.5))         # -3
print(math.floor(-9.0))        # -9
print(math.ceil(-9.0))         # -9
print(math.floor(25.1))        # 25
print(math.ceil(25.1))         # 26
# print(floor(3.5))            # Error: floor is not defined without math.
# print(ceil(3.5))             # Error: ceil is not defined without math.

'''
1. What does floor(x) do? ---> Returns nearest previous integer of 'x'
2. What does ceil(x) do?  ---> Returns nearest next integer of 'x'
'''

# gcd() function demo program
import math
print(math.gcd(12, 15))        # 3
print(math.gcd(12, 18))        # 6
print(math.gcd(4, 7))          # 1
print(math.gcd(7, 7))          # 7
print(math.gcd(-18, -27))      # 9
print(math.gcd(-4, 6))         # 2
print(math.gcd(0, 7))          # 7
print(math.gcd(3, 0))          # 3
print(math.gcd(0, 0))          # 0
# print(gcd(5, 15))            # Error: gcd is not defined without math.

# abs() function demo program
from builtins import abs
print(abs(-35.8))              # 35.8
print(abs(-27))                # 27
print(abs(29.5))               # 29.5
print(abs(32))                 # 32
import builtins
print(builtins.abs(-25))       # 25

# max() and min() functions demo program
from builtins import max, min
print(max(10.8, 20.6))                        # 20.6
print(min(10.8, 20.6, 5.9, 12.3))              # 5.9
print(max(25, 10.8))                           # 25
import builtins
print(builtins.max(10, 20, 30))                # 30
print(builtins.min(10, 20, 15, 5, 12))         # 5

# pow() function demo program
from builtins import pow
print(pow(10, -2))                             # 0.01
print(pow(4, pow(3, 2)))                        # 4^9 = 262144
import builtins
print(builtins.pow(2, 3))                       # 8
print(builtins.pow(-2, -3))                     # -0.125

# Find outputs
import keyword
print(keyword.kwlist)                          # List of Python keywords
print(len(keyword.kwlist))                      # Number of keywords (e.g., 36 in Python 3.10+)
print(type(keyword.kwlist))                     # <class 'list'>
[26-07-2025 10:06 PM] Sanketh: Sanketh 
# eval() function demo program
print(eval('25'))                             # 25 (int)
print(eval('10.8'))                           # 10.8 (float)
print(eval('False'))                          # False (bool)
print(eval('3+4j'))                           # (3+4j) (complex number)
# print(eval('Hyd'))                          # Error: NameError ('Hyd' is undefined)
print(eval("    'Hyd'   "))                   # 'Hyd' (str)
print(eval('3 + 4 * 5'))                      # 23 (4*5=20 + 3)
print(eval('[10 , 20 , 15 , 18]'))            # [10, 20, 15, 18] (list)
print(eval('{10,20,15,18,20,12,18}'))         # {10, 12, 15, 18, 20} (set, no duplicates)
print(eval('(10 , 20 , 30)'))                 # (10, 20, 30) (tuple)
print(eval("{10 : 'Hyd' , 10 : 'Sec'}"))      # {10: 'Sec'} (duplicate key, latest kept)
# print(eval(4 + 5))                          # Error: eval expects a string

# Tricky program
print(eval("    'hyd'   "))                   # 'hyd'
hyd = 'Sec'
print(eval('hyd'))                            # 'Sec'
sec = '25'
print(eval('sec'))                            # '25'
print(eval(sec))                              # 25 (converted string to int)
cyb = 10.8
print(eval('cyb'))                            # 10.8
print(eval(str(cyb)))                         # 10.8 (converted to string, then eval'd)

# Tricky program
print(eval('print("Hyd")'))                   # Hyd \n None (print returns None)

# Find outputs
print(bool('False'))                          # True (non-empty string)
print(eval('False'))                          # False (boolean)
print(bool(''))                               # False (empty string is False)
print(eval('  ""  '))                          # '' (empty string)
# print(eval(''))                             # Error: unexpected EOF (empty input)
print(eval('  " "   '))                        # ' ' (string with one space)
# print(eval(' '))                            # Error: invalid syntax (just a space)

# Advantage of eval(input())
# x = eval(input('Enter any input: '))        # Depends on input: e.g., [1,2] gives list
# print(type(x))                              
# print(x)

# Better approach to read string input
a = input('Enter any string: ')               # e.g., input: Hyd
print(len(a))                                 # 3
print(a)                                      # Hyd
# b = eval(input('Enter any string: '))       # e.g., input: 'Hyd' => b = 'Hyd'
# print(len(b))                               # 3
# print(b)                                    # Hyd

# sep argument demo program
a, b, c = 25, 10.8, 'Hyd'
print(a, b, c, sep=',')                       # 25,10.8,Hyd
print(a, b, c, sep='\t')                      # 25<TAB>10.8<TAB>Hyd
print(a, b, c, sep='---')                     # 25---10.8---Hyd
print(a, b, c, sep='\n')                      # prints each on a new line
print(a, b, c)                                # 25 10.8 Hyd
# print(a, b, c, separator=':')               # Error: invalid keyword argument 'separator'

# Find outputs
print(a, b, c, end='---')                     # 25 10.8 Hyd--- (no newline)
print(a, b, c, sep=',,,')                     # 25,,,10.8,,,Hyd
print(a, b, c, sep=':::', end='\t\t\t')       # 25:::10.8:::Hyd<tab><tab><tab>
print(a, b, c)                                # 25 10.8 Hyd

# Find outputs
print('Hyd')                                  # Hyd
print()                                       # blank line
print('Sec')                                  # Sec
print()                                       # blank line
print('Cyb')                                  # Cyb

# Find outputs
l = [10, 20, 30, 40]
t = (10, 20, 30, 40)
s = {10, 20, 30, 40}
print(l, t, s)                                # [10, 20, 30, 40] (10, 20, 30, 40) {40, 10, 20, 30}

# Find outputs
a = 25
b = '%f' % a
print(b)                                      # 25.000000
print(type(b))                                # <class 'str'>
x = 10.8
y = '%d' % x
print(y)                                      # 10 (float to int)
print(type(y))                                # <class 'str'>
m = [10, 20, 15, 18]
n = '%s' % m
print(n)                                      # [10, 20, 15, 18]
print(type(n))                                # <class 'str'>

# Find Outputs
a = 10.9274
print('%8.2f' % a)                            # '   10.93'
print('%9.1f' % a)                            # '     10.9'
print('%10.3f' % a)                           # '    10.927'
print('%.2f' % a)                             # '10.93'
print('%.6f' % a)                             # '10.927400'
print('%f' % a)                               # '10.927400'

# Find outputs
a = 'Hyd'
print('%7s' % a)                              # '   Hyd'
print('%-7s' % a)                             # 'Hyd   '
print('%2s' % a)                              # 'Hyd' (width too small, ignored)
print('%s' % a)                               # 'Hyd'
print('%s', a)                                # ('%s', 'Hyd')  (tuple)
# print('%s' a)                               # SyntaxError
# print('%s', %a)                             # SyntaxError
print(a)                                      # Hyd

# Find outputs
a = [10, 20, 30, 40]
print('%s' % a)                               # [10, 20, 30, 40]
print('%s', a)                                # ('%s', [10, 20, 30, 40])
# print('%s' a)                               # SyntaxError
# print('%s', %a)                             # SyntaxError
# print('%l' % a)                             # ValueError: unknown format code 'l'
print(a)                                      # [10, 20, 30, 40]

# Find outputs
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s' % (a, b, c))           # 25    10.927400    Hyd
print('%i    %g    %s' % (a, b, c))           # 25    10.9274    Hyd
print('%s    %s    %s' % (a, b, c))           # 25    10.9274    Hyd
print('%d    %g    %s', a, b, c)              # ('%d    %g    %s', 25, 10.9274, 'Hyd')
# print('%d    %g      %s'   a, b, c)         # SyntaxError (missing %)
# print('%d    %g    %s' ,  %(a , b , c))     # SyntaxError
# print('%d    %g    %s' % a % b % c)         # TypeError
print('%d' % a, '%f' % b, '%s' % c)           # 25 10.927400 Hyd


x = 25
print(F'{x}')              # 25
print(F'{{x}}')            # {x}
print(F'{{{x}}}')          # {25}
print(F'{{{{x}}}}')        # {{x}}
print(F'{{{{{x}}}}}')      # {{{25}}}
print(F'{{{{{{x}}}}}}')    # {{{{x}}}}
print(F'{{{{{{{x}}}}}}}')  # {{{{{25}}}}}
print(F'{{{{{{{{x}}}}}}}}')# {{{{{{x}}}}}}
