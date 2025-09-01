# float object demo program (Home work)
a = 10.8
print(a)           # 10.8
print(type(a))     # <class 'float'>
print(id(a))       # returns the address of object 10.8
b = 25. 
print(b)	         # 25.0
print(type(b)) 	   # <class 'float'>
c = .689 
print(c) 	         # 0.689
d = 3.4E2 
print(d)	         # 340.0
print(type(d))     # <class 'float'>
e = 9.62e-2 
print(e)           # 0.0962
print(9.8.2)       # returns errors as it contains two decimal points




# complex object demo program
a = 3 + 4j
print(a) 	       # 3+4j
print(type(a))         # <class 'complex'>
print(id(a))           # Returns the address of the object 3+4j
print(a.real)          # 3.0 
print(a.imag)          # 4.0 
print(type(a.real))    # <class 'float'> 
print(type(a.imag))    # <class 'float'>




# Find outputs (Home work)
a = 6j
print(a)           # 6j
print(type(a))     # <class 'complex'>
print(a.real)      # 0.0
print(a.imag)      # 6.0
print(5 + j6)      # returns error as it must be 6j not j6.
print(3 + 4i)      # returns error as i is not valid in python. Only j is valid in case of complex numbers
print(4 + j)       # returns error as there is no prefix for j. It must be 1j not j.
print(4 + 1j)      # 4+1j
print(4 + 0j)      # 4+0j




# bool object demo program (Home work)
a = True 
print(a)                   # True 
print(type(a))             # <class 'bool'>
print(id(a))      	       # returns the address at which object True is stored.
b = False 
print(b) 	  	             # False 
print(type(b)) 	  	       # <class 'bool'>
print(True + True)	       # 2 
print(True + False)	       # 1 
print(False + True)	       # 1 
print(False + False)	     # 0 
print(True + True + True)  # 3
print(25 + 10.8 + True)    # 36.8 
print(True > False)        # True
print(True)                # True
print(False)               # False
print(true)                # returns error as it must be True not true.
print(false)               # returns error as it must be False not false.




#Find outputs (Home work)
a = 0O6247
print(a)                  # 3239 (Octal 0O6247 = Decimal 3239) 
print(type(a))            # <class 'int'> 
print(id(a))              # returns the address at which the object 0O6247 is stored.
b = 0o6247 
print(id(b))              # returns the same numbers which was returned earlier at line 4.
print(b)                  # 3239
c = 3239 
print(c)                  # 3239 
print(id(c))              # returns the same numbers which was returned earlier at line 4.
print(0o9248)             # returns error as an octal number can only have digits between 0-7 after prefix 0o.



#Find outputs (Home work)
a = 0XA7B9 
print(a)                  # 42937  
print(type(a))            # <class 'int'> 
b = 0xBEEF 
print(b)                  # 48879 
print(A7B9)               # returns error as it is neither a string nor a hexadecimal number. For it to be hexadecimal number, it must have 0X as prefix.
print('A7B9')             # A7B9 (as it is a string).
print(0XBEER)             # returns error as a hexadecimal number has only digits 0-9 and alphabets A-F. But this number has R in it.
print(0XHYD)              # returns error as a hexadecimal number has only digits 0-9 and alphabets A-F. But this number has H,Y and D. Also, the error is shown at H as python won’t be moving forward once it spots H which is the first error in this number.
print(0xA7G9B)            # returns error as a hexadecimal number has only digits 0-9 and alphabets A-F. But this number has G in it.



# Find outputs (Home work)
a = 9248 
print(a)             # 9248 
print(type(a))       # <class 'int'>

