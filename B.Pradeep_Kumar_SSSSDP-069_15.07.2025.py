a = 10.8
print(a) # 10.8
print(type(a)) # <class 'float'>
print(id(a)) # address of object a

b = 25.
print(b) # 25.0
print(type(b)) # <class 'float'>

c = .689
print(c) # 0.689

d = 3.4E2
print(d) # 340.0
print(type(d)) # <class 'float'>

e = 9.62e-2
print(e) # 0.0962

print(9.8.2) # SyntaxError: invalid syntax

a = 3 + 4j
print(a) # (3+4j)
print(type(a)) # <class 'complex'>
print(id(a)) # address of object a
print(a.real) # 3.0
print(a.imag) # 4.0
print(type(a.real)) # <class 'float'>
print(type(a.imag)) # <class 'float'>

a = 6j
print(a) # 6j
print(type(a)) # <class 'complex'>
print(a.real) # 0.0
print(a.imag) # 6.0

print(5 + j6) # SyntaxError: invalid syntax
print(3 + 4i) # SyntaxError: invalid syntax
print(4+j) # SyntaxError: invalid syntax
print(4 + 1j) # (4+1j)
print(4 + 0j) # (4+0j)

a = True
print(a) # True
print(type(a)) # <class 'bool'>
print(id(a)) # address of object a

b = False
print(b) # False
print(type(b)) # <class 'bool'>

print(True + True) # 2
print(True + False) # 1
print(False + True) # 1
print(False + False) # 0
print(True + True + True) # 3
print(25 + 10.8 + True) # 36.8
print(True > False) # True
print(True) # True
print(False) # False
print(true) # NameError: name 'true' is not defined

a = 0O6247
print(a) # 3239
print(type(a)) # <class 'int'>
print(id(a)) # address of object a

b = 0o6247
print(id(b)) # address of object b
print(b) # 3239

c = 3239
print(c) # 3239
print(id(c)) # address of object c

print(0o9248) # SyntaxError: invalid digit '9' in octal literal

a = 0XA7B9
print(a) # 42937
print(type(a)) # <class 'int'>

b = 0xBEEF
print(b) # 48879

print(A7B9) # NameError: name 'A7B9' is not defined
print('A7B9') # A7B9
print(0XBEER) # SyntaxError: invalid syntax
print(0XHYD) # SyntaxError: invalid syntax
print(0xA7G9B) # SyntaxError: invalid syntax

a = 9248
print(a) # 9248
print(type(a)) # <class 'int'>
