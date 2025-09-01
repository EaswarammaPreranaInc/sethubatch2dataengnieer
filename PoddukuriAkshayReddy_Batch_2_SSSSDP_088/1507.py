15/7/25
# float  object  demo  program (Home  work)
a = 10.8
print(a) #10.8
print(type(a)) #<class 'float'>
print(id(a)) #some Number
b = 25.
print(b) #25.0
print(type(b)) #<class 'float'>
c = .689
print(c) # 0.689
d = 3.4E2
print(d) # 340.0
print(type(d)) #<class 'float'>
e = 9.62e-2
print(e)  # 0.0962
print(9.8.2) #error due to 2 points or dots


# complex object demo program
a = 3 + 4j
print(a) # 3+4j
print(type(a)) #<class 'comples'>
print(id(a)) #some Number
print(a . real) # 3.0
print(a . imag) # 4.0
print(type(a . real)) #<class 'float'>
print(type(a . imag)) #<class 'float'>


# Find outputs (Home work)
a = 6j
print(a) #6j
print(type(a)) # <class 'complex'>
print(a.real) # 0.0
print(a.imag) #6.0
print(5 + j6) #error due to j should be after nnumeric
print(3 + 4i) #error due to i is not used in python
print(4+j)    #error due j value is not defined
print(4 + 1j) #4+1j
print(4 + 0j) #4+0j


# bool object demo program  (Home  work)
a = True
print(a) #True
print(type(a)) #<class 'bool'>
print(id(a)) # some Number
b = False
print(b) # False
print(type(b))  #<class 'bool'>
print(True + True) #2
print(True + False) #1
print(False + True) #1
print(False + False) #0
print(True + True + True) #3
print(25 + 10.8 + True) #36.8
print(True > False) # True
print(True)  #True
print(False) #False
print(true) # error Due to its True not true
print(false) # error Due to its false not false


# Find  outputs (Home  work)
a = 0O6247
print(a) #3239
print(type(a)) #<class 'int'>
print(id(a)) # some Number
b = 0o6247
print(id(b)) # some Number
print(b) #3239
c = 3239
print(c) #3239
print(id(c)) #<class 'int'>
print(0o9248) #error due to octal does not have 9 its has 0 to 7


# Find  outputs  (Home  work)
a = 0XA7B9
print(a) #42937
print(type(a)) #<class 'int'>
b = 0xBEEF  #48879
print(b)
print(A7B9) # it is not defined
print('A7B9') # A7B9
print(0XBEER) # error due to R is not hexa decimal
print(0XHYD) #  error due to HY is not hexa decimal
print(0xA7G9B) # error due to G is not hexa decimal


# Find outputs (Home  work)
a = 9248
print(a) # 9248
print(type(a)) # <class 'int'>