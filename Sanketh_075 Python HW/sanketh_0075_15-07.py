a = 10.8             # Referance b assigns to object 10.8 (float) 
print(a)             # 10.8         # prints value of a
print(type(a))       # <class 'float'>  # type is float
print(id(a))         # e.g., 400000  # memory location of a (id will vary)

b = 25.               # Referance b assigns to object 25.0 (float)
print(b)              # 25.0    # Python automatically adds .0
print(type(b))        # <class 'float'>  # type is float

c = .689              # Reference c assigns to Object 0.689 (float) to c
print(c)              # 0.689       # prints value

d = 3.4E2             # Referance d assigns to object 3.4 × 10^2 (340.0) 
print(d)              # 340.0       
print(type(d))        # <class 'float'>  # type is float

e = 9.62e-2           # reference e assigns to object  9.62 × 10^-2 (0.0962) 
print(e)              # 0.0962      # prints value

print(9.8.2)          # SyntaxError  # invalid syntax: two dots not allowed
#15/07 Homework 2
a = 6j                # assigns complex number (0 + 6j) to a
print(a)              # 6j          # prints value
print(type(a))        # <class 'complex'>  # type is complex
print(a.real)         # 0.0         # real part of a
print(a.imag)         # 6.0         # imaginary part of a
print(5 + j6)         # NameError   # j6 is invalid syntax
print(3 + 4i)         # SyntaxError # Python uses j not i
print(4+j)            # NameError   # j is not defined
print(4 + 1j)         # (4+1j)      # valid complex number
print(4 + 0j)         # (4+0j)      # complex number with 0 imaginary
#15/07 Homework 3
a = 3 + 4j            # assigns complex number (3+4j) to a
print(a)              # (3+4j)      # prints complex number
print(type(a))        # <class 'complex'>  # type is complex
print(id(a))          # e.g., 4000  # memory location (id varies)
print(a.real)         # 3.0         # real part
print(a.imag)         # 4.0         # imaginary part
print(type(a.real))   # <class 'float'>  # real part is float
print(type(a.imag))   # <class 'float'>  # imaginary part is float
#15/07: Homework 4
a = 0O6247            # assigns octal 6247 (decimal 3255) to a
print(a)              # 3255        # prints decimal equivalent
print(type(a))        # <class 'int'>  # type is int
print(id(a))          # e.g., 4000  # memory location
b = 0o6247            # same as above (lowercase o)
print(id(b))          # same as id(a) # integers with same value share id
print(b)              # 3255        # prints decimal equivalent
c = 3239              # assigns 3239 (decimal) to c
print(c)              # 3239        # prints value
print(id(c))          # different id than a/b
print(0o9248)         # SyntaxError # invalid octal digit: 9 and 8 not allowed
#15/07: Homework 5
a = True              # assigns boolean True to a
print(a)              # True        # prints True
print(type(a))        # <class 'bool'>  # type is bool
print(id(a))          # e.g., 4000  # memory location (id varies)
b = False             # assigns boolean False to b
print(b)              # False       # prints False
print(type(b))        # <class 'bool'>  # type is bool
print(True + True)    # 2           # True is 1, so 1+1=2
print(True + False)   # 1           # 1+0=1
print(False + True)   # 1           # 0+1=1
print(False + False)  # 0           # 0+0=0
print(True + True + True)  # 3      # 1+1+1=3
print(25 + 10.8 + True)    # 36.8   # True is 1, so 25+10.8+1=36.8
print(True > False)        # True   # 1 > 0
print(True)                # True   # prints True
print(False)               # False  # prints False
print(true)                # NameError  # 'true' is not defined (Python is case-sensitive)
print(false)               # NameError  # 'false' is not defined
