# float  object  demo  program (Homework)
a = 10.8       # Assigns reference 'a' to float object 10.8
print(a)       # Prints Value of an object 'a' 10.8
print(type(a)) # Prints Type of object 'a' is <class 'float'>
print(id(a))   # Prints Address of object 'a'(may be something 153498)
b = 25.        # Assigns reference 'b' to float object 25
print(b)       # Prints Value of an object 'a' 25
print(type(b)) # Prints Address of object 'b' is <class 'float'>
c = .689       # Assigns reference 'c' to float object 0.689
print(c)       # Prints the value of the object 'c', which is 0.569
d = 3.4E2      # Assigns reference 'd' to the float object 340.0 (3.4 × 10²)
print(d)       # Prints the value of 'd', which is 340.0
print(type(d)) # Prints the type of 'd', which is <class 'float'>
e = 9.62e-2    # Assigns reference 'e' to the float object 0.0962 (Scientific notation: 9.62 × 10⁻²)
print(e)       # Prints the value of 'e', which is 0.0962
#print(9.8.2)   # Invalid Syntax. So, no output(only 9.8 can be valid)

# complex object demo program
a = 3 + 4j      # Assigns reference 'a' to the complex object (3 + 4j)
print(a)        # Prints  value of the complex number: (3+4j)
print(type(a))  # Prints value of the type of 'a', which is <class 'complex'>
print(id(a))    # Prints the memory address (ID) of object 'a'
print(a.real)   # Prints the real part of the complex number: 3.0
print(a.imag)   # Prints the imaginary part of the complex number: 4.0
print(type(a.real))  # Prints the type of the real part: <class 'float'>
print(type(a.imag))  # Prints the type of the imaginary part: <class 'float'>

# Find outputs (Home work)
a = 6j          # Assigns 'a' to a complex number with imaginary part 6 and real part 0
print(a)        # Prints the value of 'a' which is 6j
print(type(a))  # Prints the type of the type  which is <class 'complex'>
print(a.real)   # prints  Output: 0.0 
print(a.imag)   # Prints Output: 6.0 
#print(5 + j6)   # Error: imag is after j6 (instead it should be 6j)
#print(3 + 4i)   # Error: Python does not use 'i' (only j is used in python)
#print(4+j)      # prints Error: 'j' (There is no number)
print(4 + 1j)   # prints Output: (4+1j) – it is a valid complex number
print(4 + 0j)   # prints Output: (4+0j) – it is a valid complex number

# bool object demo program  (Home  work)
a = True        # Assigns reference 'a' to the boolean object True
print(a)        # Prints the value referenced by 'a'; Output: True
print(type(a))  # Prints the type of 'a' which is<class 'bool'>
print(id(a))    # Prints the memory address (ID) of 'a'
b = False       # Assigns reference 'b' to the boolean value 
print(b)        # Prints the value referenced by 'b'; Output: False
print(type(b))            # Prints the type of 'b' which is <class 'bool'>
print(True + True)        # Prints the Output: 2  (1 + 1)
print(True + False)       # Prints the Output: 1  (1 + 0)
print(False + True)       # Prints the Output: 1  (0 + 1)
print(False + False)      # Prints the Output: 0  (0 + 0)
print(True + True + True) # Prints the Output: 3  (1 + 1 + 1)
print(25 + 10.8 + True)   # Prints the Output: 36.8  (25 + 10.8 + 1)
print(True > False)       # Prints the Output: True  (1 > 0)
print(True)   # Prints the Output: True
print(False)  # Prints the Output: False
#print(true)   # Prints Error: 'true' is not defined
#print(false)  # Prints Error: 'false' is not defined

# Find  outputs (Home  work)
a = 0O6247      # Assigns the variable 'a' to a valid octal
print(a)        # Prints the  Output: 3247 (octal 6247 = decimal 3247)
print(type(a))  # Prints the type of the object <class 'int'>
print(id(a))    # Prints the memory address (ID) of the variable 'a'
b = 0o6247      # Assigns reference 'b' to a valid octal
print(id(b))    # Prints the memory address of 'b' Likely same ID as 'a', since value is same
print(b)        # Prints the decimal equivalent of the octal value; Output: 3239
c = 3239        # Assigns the integer value 3239 to 'c'
print(c)        # Prints the value of 'c'; Output: 3239
print(id(c))    # Prints the memory address (ID) of 'c'
#print(0o9248)   # Error as '9' is invalid in Octal (0-7)

# Find  outputs  (Home  work)
a = 0XA7B9      # Assigns the reference 'a' to a valid hexadecimal (A7B9 in base 16 = 42937 in decimal)
print(a)        # prints the value of the object referenced by 'a' Output: 42937
print(type(a))  # prints the type of the object Output: <class 'int'>
b = 0xBEEF      # Assigns the variable 'b' to a valid hexadecimal
print(b)        # prints the value of the object referenced by 'b'. Output: 48879
#print(A7B9)     # The A7B9 is not defined, so no output
print('A7B9')   # prints  Outputs string 'A7B9'
# print(0XBEER)   # Error: 'R' is not a valid hexadecimal (only 0-9, A-F)
# print(0XHYD)    # Error: 'H', 'Y', 'D' are invalid hexadecimal (only 0-9, A-F)
# print(0xA7G9B)  # Error: 'G' is not a valid hexadecimal (only 0-9, A-F)

# Find outputs (Home  work)
a = 9248  	# Assigns reference 'a' to integer object 9248
print(a)  	# Prints the value of the object referenced by 'a'; Output: 9248
print(type(a))  # prints the type of the object  Output: <class 'int'>
