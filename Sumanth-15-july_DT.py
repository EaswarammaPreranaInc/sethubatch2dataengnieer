# float  object  demo  program (Home  work)
a = 10.8 # Ref a points to object 10.8
print(a) # value of object a i.e 10.8
print(type(a)) # Type of object < class float>
print(id(a)) # Address of object < may be 1000>
b = 25. # Ref b points to object 25.0
print(b) # value of object b i.e 25.0
print(type(b))  # Type of object < class float>
c = .689 # Ref c points to object 0.689
print(c) # value of object c i.e 0.689
d = 3.4E2 # Ref d points to object 3.4E2
print(d) # value of object d i.e 340.0
print(type(d))  # Type of object < class float>
e = 9.62e-2 # Ref e points to object 9.62e-2
print(e) # value of object e i.e 0.0962 
print(9.8.2) # Error

# complex object demo program
a = 3 + 4j # Ref a points to object 3+4j
print(a)  # value of object a i.e 3+4j
print(type(a)) # Type of object < class complex>
print(id(a)) # Address of object < may be 1000>
print(a . real) # Real value of object a is i.e 3.0
print(a . imag) # Imag value of object a is i.e 4.0
print(type(a . real)) # Type of object < class complex>
print(type(a . imag)) # Type of object < class complex>

# Find outputs (Home work)
a = 6j # Ref a points to object 0+6j
print(a) # value of object a i.e 0+6j
print(type(a)) # Type of object < class complex>
print(a.real) # Real value of object a is i.e not Mentioned
print(a.imag) # Imag value of object a is i.e 6.0
print(5 + j6) # Error
print(3 + 4i) # Error 
print(4+j) # Error
print(4 + 1j) # (4+1j)
print(4 + 0j) # (4+0j)

# bool object demo program  (Home  work)
a = True # Ref a points to object True
print(a) # value of object a i.e True
print(type(a)) # Type of object < class bool>
print(id(a)) # Address of object < may be 1000>
b = False # Ref b points to object False
print(b) # value of object b i.e False
print(type(b)) # Type of object < class bool>
print(True + True) # True=1,False=0---Result=1+1=2
print(True + False) # True=1,False=0---Result=1+0=1
print(False + True) # True=1,False=0---Result=0+1=1
print(False + False) # True=1,False=0---Result=0+0=0
print(True + True + True) # True=1,False=0---Result=1+1+1=3
print(25 + 10.8 + True) # True=1,False=0---Result=25+10.8+1=36.8
print(True > False) # True
print(True)  # True
print(False) # False
print(true) # Error
print(false) #Error

# Find  outputs (Home  work)
a = 0O6247 # Ref a points to object 0O6247
print(a) # 3239
print(type(a)) # Type of object < class int>
print(id(a))  # Address of object < may be 1000>
b = 0o6247 # Ref b points to object 0o6247
print(id(b))  # Address of object < may be 1000>
print(b) # 3239
c = 3239 # Ref c points to object 3239 
print(c) # 3239
print(id(c))  # Address of object < may be 1000>
print(0o9248) # Error
 
# Find  outputs  (Home  work)
a = 0XA7B9 # Ref a points to object 0X7B9
print(a) # 42937
print(type(a)) # Type of object < class int>
b = 0xBEEF # Ref b points to object 0XBEEF
print(b) # 48879
print(A7B9) # Error
print(0XBEER) # Error
print(0XHYD) # Error 
print(0xA7G9B) # Error

# Find outputs (Home  work)
a = 9248 # Ref a points to object 9248
print(a) # 9248
print(type(a)) # Type of object < class int>
