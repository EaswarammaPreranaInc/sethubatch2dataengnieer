# float  object  demo  program (Home  work)

a = 10.8 # Ref  'a'  points  to  object i.e., 10.8 
print(a) # Value  of  object  'a'  i.e.,  10.8
print(type(a)) # Type  of  object  'a'  i.e.,  <class  'float'>
print(id(a)) # Address  of   object  'a'  i.e., 1933477468816

b = 25. # Ref  'b'  points  to  object  25.
print(b) # Value  of  object  'b'  i.e.  25.0
print(type(b)) # Type  of  object  'b'  i.e.,  <class  'float'>

c = .689 # Ref  'c'  points  to  object  .689
print(c) # Value  of  object  'c'  i.e.,  0.689

d = 3.4E2 # Ref  'd'  points  to  object  3.4E2
print(d) # Value  of  object  'd'  i.e.,  340.0 (3.4 × 10²)
print(type(d)) # Type  of  object  'd'  i.e.,  <class  'float'>

e = 9.62e-2 # Ref  'd'  points  to  object  3.4E2
print(e)  # Value  of  object  'e'  i.e.,  0.0962 (9.62 × 10⁻²)

print(9.8.2) # invalid syntax because multiple dots in one number are not allowed
# complex object demo program

a = 3 + 4j # Ref  'a'  points  to  object I.e., 3+4j
print(a) # Value  of  object  'a'  i.e.,  3+4j
print(type(a)) # Type  of  object  'a'  i.e.,  <class  'complex'>
print(id(a)) # Address  of   object  'a' i.e., 2406242951792 

print(a . real) # Real part of the object 'a' i.e., 3.0
print(a . imag) # imaginary part of the object  'a'  i.e.,  4.0

print(type(a . real)) # Type  of  object  'a'  i.e.,  <class  'float'>
print(type(a . imag)) # Type  of  object  'a'  i.e.,  <class  'float'>

# Find outputs (Home work)

a = 6j                  # Ref 'a' points to a complex object i.e., 0 + 6j
print(a)                # Value of object 'a' i.e., 6j
print(type(a))          # Type of object 'a' i.e., <class 'complex'>

print(a.real)           # Real part of the object 'a' i.e., 0.0
print(a.imag)           # Imaginary part of the object 'a' i.e., 6.0

print(5 + j6)           # Invalid syntax it should be written as 5 + 6j
print(3 + 4i)           # Invalid syntax it does not allow 'i', only it allows 'j' for imaginary
print(4 + j)            # Invalid syntax 'j' must have a number, e.g., 4 + 1j

print(4 + 1j)           # Output: (4+1j)
print(4 + 0j)           # Output: (4+0j)

# Find  outputs (Home  work)

a = 0O6247 # Ref 'a' points to object contains decimal equivalent i.e., 3239
print(a) # Value  of  object  'a'  i.e.,  3239
print(type(a)) # Type  of  object  'a'  i.e.,  <class  'int'>
print(id(a)) # Address  of   object  'a'  i.e., 1795211371120


b = 0o6247 # Ref 'b' points to object contains decimal equivalent i.e., 3239 
print(id(b)) # Address  of   object  'b' is same as 'a' i.e., 1795211371120
print(b) # Value  of  object  'b'  i.e.,  3239


c = 3239 # Ref 'c' points to object contains decimal equivalent i.e., 3239
print(c) # Value  of  object  'c'  i.e.,  3239
print(id(c)) # Address  of   object  'c' is same as 'a' and 'b' i.e., 1795211371120

print(0o9248) #Invalid as Octal digits allowed is 0 to 7 only

# Find  outputs  (Home  work)

a = 0XA7B9 # Ref 'a' points to object contains decimal equivalent I.e. 42937
print(a) #Value  of  object  'a'  i.e. 42937
print(type(a))  # Type  of  object  'a'  i.e.  <class  'int'>

b = 0xBEEF # Ref 'b' points to object contains decimal equivalent I.e. 48879
print(b) #Value  of  object  'a'  i.e.  48879

print(A7B9) # error because object A7B9 not defined
print('A7B9') # print the output A7B9
print(0XBEER) # error due to invalid hexadecimal values i.e. R
print(0XHYD) # error due to invalid hexadecimal values i.e. HY
print(0xA7G9B) # error due to invalid hexadecimal value i.e. G

# bool object demo program  (Home  work)

a = True # Ref  'a'  points  to  object i.e., True 
print(a) # Value  of  object  'a' i.e.,  true
print(type(a)) # Type  of  object  'a'  i.e.,  <class  'bool'>
print(id(a)) # Address  of   object  'a'  i.e., 140724583711152

b = False # Ref  'b'  points  to  object i.e., False
print(b) # Value  of  object  'b'  i.e.  False
print(type(b)) # Type  of  object  'b'  i.e.,  <class  'bool'>

print(True + True) # output: 1 + 1 = 2
print(True + False) # output: 1 + 0 = 1
print(False + True) # output: 0 + 1 = 1
print(False + False) # output: 0 + 0 = 0
print(True + True + True) # output: 1 + 1 + 1 = 3

print(25 + 10.8 + True) # output: 25 + 10.8 + 1 = 36.8

print(True > False) # output: True (1 > 0)
print(True)   # output: True
print(False)  # output: False

print(true) # invaild as true is keyword is should start with captail letter i.e., True
print(false)  # invaild as false is keyword is should start with captail letter i.e., False

# Find outputs (Home  work)

a = 9248 # ref 'a' points to object 9248
print(a) #Value  of  object  'a'  i.e.  9248
print(type(a)) #Type  of  object  'a'  i.e.  <class  'int'>
