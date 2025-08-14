
a = 3 + 4j   # Ref 'a' points to Object 3+4j (3 is real, 4 is imaginary)
print(a)     # Value of Object 'a' is (3+4j)
print(type(a))   # Type of Object 'a' is complex
print(id(a))     # Address of the complex object

print(a.real)    # Value of Object 'a.real' is 3.0
print(a.imag)    # Value of Object 'a.imag' is 4.0
# Python automatically promotes integers to floats inside complex numbers

# Find Outputs
a = 6j   # Ref 'a' points to Object 6j (0 is real, 6 is imaginary)
print(a)   # Value of Object 'a' is 6j
print(type(a))   # Type of Object 'a' is complex
print(a.real)    # Value of Object 'a.real' is 0.0
print(a.imag)    # Value of Object 'a.imag' is 6.0

print(5 + j6)    # Error: invalid syntax
print(3 + 4+i)   # Error: Python uses 'j' for imaginary part
print(4 + tj)    # Error: 'j' must be part of number
print(4 + 1j)    # Value is (4+1j)
print(4 + 0j)    # Value is (4+0j)

####################################################################
a = 3 + 4j   # Ref 'a' points to Object 3+4j (3 is real, 4 is imaginary)
print(a)     # Value of Object 'a' is (3+4j)
print(type(a))   # Type of Object 'a' is complex
print(id(a))     # Address of the complex object

print(a.real)    # Value of Object 'a.real' is 3.0
print(a.imag)    # Value of Object 'a.imag' is 4.0
# Python automatically promotes integers to floats inside complex numbers

# Find Outputs
a = 6j   # Ref 'a' points to Object 6j (0 is real, 6 is imaginary)
print(a)   # Value of Object 'a' is 6j
print(type(a))   # Type of Object 'a' is complex
print(a.real)    # Value of Object 'a.real' is 0.0
print(a.imag)    # Value of Object 'a.imag' is 6.0

print(5 + j6)    # Error: invalid syntax
print(3 + 4+i)   # Error: Python uses 'j' for imaginary part
print(4 + tj)    # Error: 'j' must be part of number
print(4 + 1j)    # Value is (4+1j)
print(4 + 0j)    # Value is (4+0j)

################################################################################

a = 10.8   # Ref 'a' points to Object 10.8
print(a)   # Value of Object 'a' is 10.8
print(type(a))   # Type of Object 'a' is class float
print(id(a))     # Address of Object 'a'

b = 25.0   # Ref 'b' points to Object 25.0
print(b)   # Value of Object 'b' is 25.0
print(type(b))   # Type of Object 'b' is class float

c = 0.689   # 'c' points to Object 0.689
print(c)    # Value of Object 'c' is 0.689

d = 3.4E2   # 'd' points to Object 3.4E2
print(d)    # 3.4 × 10² = 340.0
print(type(d))   # Type of Object 'd' is class float

e = 9.62e-2
print(e)    # 9.62 × 0.01 = 0.0962

print(9.8.2)  # Error: in Python, a number can have only one decimal point

