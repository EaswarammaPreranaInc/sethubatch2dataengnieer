# yaswanth_047_15-Jul-2025.py

# Float object HOMEWORK
a = 10.8
print(a) # Value of object 'a' is 10.8
print(type(a)) # Type of object 'a' is <class 'float'>
print(id(a)) # Address of object 'a'
b = 25.
print(b) # Value of object 'b' is 25.0
print(type(b)) # Type of object 'b' is <class 'float'>
c = .689
print(c) # Value of object 'c' is 0.689
d = 3.4E2 # [Mantissa Exponent Number]
print(d) # Value of object 'd' is 3.4 × 10^2 = 340.0
print(type(d)) # Type of object 'd' is <class 'float'>
e = 9.62e-2 # [Mantissa Exponent Number]
print(e) # Value of object 'e' is 9.62 × 10^-2 = 0.0962
print(9.8.2) # Invalid syntax: multiple decimal points not allowed
# Complex object demo program HOMEWORK
a = 3 + 4j
print(a) # Value of object 'a' is (3+4j)
print(type(a)) # Type of object 'a' is <class 'complex'>
print(id(a)) # Address of object 'a'
print(a.real) # Real part of 'a' is 3.0
print(a.imag) # Imaginary part of 'a' is 4.0
print(type(a.real))# Type of real part is <class 'float'>
print(type(a.imag))# Type of imag part is <class 'float'>
# Find outputs HOMEWORK (Complex)
a = 6j
print(a) # Value is 6j
print(type(a)) # Type is <class 'complex'>
print(a.real) # Real part is 0.0
print(a.imag) # Imaginary part is 6.0
print(5 + j6) # Invalid syntax: 'j6' is not valid
print(3 + 4i) # Invalid syntax: use 'j' not 'i'
print(4 + j) # Invalid syntax: 'j' must follow a number
print(4 + 1j) # Value is (4+1j)
print(4 + 0j) # Value is (4+0j)
# Bool object demo program HOMEWORK
a = True
print(a) # Value is True
print(type(a)) # Type is <class 'bool'>
print(id(a)) # Address of object 'a'
b = False
print(b) # Value is False
print(type(b)) # Type is <class 'bool'>
print(True + True) # Output is 2 (1+1)
print(True + False) # Output is 1 (1+0)
print(False + True) # Output is 1 (0+1)
print(False + False) # Output is 0 (0+0)
print(True + True + True) # Output is 3 (1+1+1)
print(25 + 10.8 + True) # Output is 36.8(35.8+1)
print(True > False) # Output is True(1>0)
print(True) # Output is True because keyword
print(False) # Output is False because keyword
print(true) # NameError: name 'true' is not defined it should be T
print(false) # NameError: name 'false' is not defined it should be F
# Find outputs HOMEWORK (Octal)
a = 0O6247
print(a) # Value is 3255
print(type(a)) # Type is <class 'int'> i.e, Decimal Equivalent
print(id(a)) # Address of object 'a'
b = 0o6247
print(id(b)) # Address of object 'b' (same as 'a')
print(b) # Value is 3255
c = 3239
print(c) # Value is 3239
print(id(c)) # Address of object 'c'
print(0o9248) # Invalid digit '9' in octal (base 8)
# Find outputs HOMEWORK (Hexadecimal)
a = 0xA7B9
print(a) # Value is 42937
print(type(a)) # Type is <class 'int'> i.e, Decimal Equivalent
b = 0xBEEF
print(b) # Value is 48879
print(A7B9) # NameError: A7B9 not defined
print('A7B9') # Output is string 'A7B9'
print(0XBEER) # Invalid hexadecimal: 'R' is not allowed
print(0XHYD) # Invalid hexadecimal: 'H', 'Y', 'D' not allowed
print(0xA7G9B) # Invalid hexadecimal: 'G' is not allowed
# Find outputs HOMEWORK (Decimal)
a = 9248
print(a) # Value is 9248
print(type(a)) # Type is <class 'int'>