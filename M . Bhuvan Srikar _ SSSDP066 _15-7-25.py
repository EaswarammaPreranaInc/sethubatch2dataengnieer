# float  object  demo  program (Home  work)
a = 10.8 # reference 'a' points to  float  object 10.8 
print(a) # 10.8
print(type(a)) # <class 'float'>
print(id(a)) # address of object 10.8
b = 25. # reference b points to float object 25.0
print(b) # 25.0
print(type(b)) # <class 'float'>
c = .689 # reference 'c' points to float object 0.689
print(c) # 0.689
d = 3.4E2 # reference 'd' points to float object 3.4 * 10 ^ 2
print(d) # 3.4 * 10 ^ 2
print(type(d)) # <class 'float'>
e = 9.62e-2 # reference 'e' points to float object 9.62 * 10 ^ -2
print(e) # 9.62 * 10 ^ -2
print(9.8.2) # error as there are two decimal points  

# complex object demo program
a = 3 + 4j # reference 'a' points to complex object 3 + 4j 
print(a) # 3 + 4j
print(type(a)) # <class 'complex'>
print(id(a)) # address of the object 3 + 4j
print(a . real) # 3.0
print(a . imag) # 4.0
print(type(a . real)) # <class 'float'>
print(type(a . imag)) # <class 'float'>


# Find outputs (Home work)
a = 6j # reference 'a' points to complex number 6j
print(a) # 6j
print(type(a)) # <class 'complex'>
print(a.real) # 0.0
print(a.imag) # 6.0
print(5 + j6) # error becoz j is before 6
print(3 + 4i) # error due to i 
print(4+j) # error becoz before j there is no float number
print(4 + 1j) # 4 + 1j
print(4 + 0j) # 4 + 0j


# bool object demo program  (Home  work)
a = True # reference 'a' points to True
print(a) # True
print(type(a)) # <class 'bool'>
print(id(a)) # address of object True
b = False # reference 'b' points to False 
print(b) # False
print(type(b))  # <class 'bool'>
print(True + True) # 1 + 1 = 2
print(True + False) # 1 + 0 = 1
print(False + True) # 0 + 1 = 1
print(False + False) # 0 + 0 = 0
print(True + True + True) # 1 + 1 + 1 = 3
print(25 + 10.8 + True) # 25 + 10.8 + 1 = 36.8
print(True > False) # True
print(True) # True
print(False) # False
print(true) # error due to t becoz True is a keyword
print(false) # error due to f becoz False is a keyword


# Find  outputs (Home  work)
a = 0O6247 # reference 'a' points to octal number 0O6247
print(a) # decimal equivalent of the corresponding octal number is 6 * 8 ^ 3 + 2 * 8 ^ 2 + 4 * 8 ^ 1 + 7 * 8 ^ 0 = 3239
print(type(a)) # <class 'int'>
print(id(a)) # address of the octal number 0O6247
b = 0o6247 # reference 'b' also points to same octal number 0O6247
print(id(b))
print(b)
c = 3239  # reference 'c' points to decimal number 3239
print(c) # 3239
print(id(c)) # address of the object 3239
print(0o9248) # error as the octal number contains 0 to 7 digits only


# Find  outputs  (Home  work)
a = 0XA7B9 # reference 'a' points to hexa-decimal number 0XA7B9
print(a) # decimal equivalent of the corresponding hexa-decimal number is 10 * 16 ^ 3 + 7 * 16 ^ 2 + 11 * 16 ^ 1 + 9 * 16 ^ 0 = 42937
print(type(a)) # <class 'int'>
b = 0xBEEF # reference 'b' points to hexa-decimal number 0XBEEF
print(b)  # decimal equivalent of the corresponding hexa-decimal is 11 * 16 ^ 3 + 14 * 16 ^ 2 + 14 * 16 ^ 1 +  15 * 16 ^ 0 = 48879
print(A7B9) # error as there is no 0X or 0x 
print('A7B9') # string A7B9
print(0XBEER) # error as in hexa-decimal there is no R
print(0XHYD)  # error as in hexa-decimal there is no H and Y
print(0xA7G9B) # error as in hexa-decimal there is no G

# Find outputs (Home  work)
a = 9248 # reference 'a' points to the int object 9248
print(a) # 9248
print(type(a)) # <class 'int'>
