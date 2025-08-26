# int object
'''
a=25
print(a)          # 25
print(type(a))    # <class 'int'>
print(id(a))      # address of object a
b=999999999999
print(b)          # 999999999999
#c=$25   #error dur to $
'''
#float() object
'''
a=10.8
print(a)              # 10.8
print(type(a))        # <class 'float'>
print(id(a))          # address of object a
b=25.
print(b)              # 25.0
print(type(b))        # <class 'float'>
c=.689
print(c)              # 0.689
d=3.4e2               # 3.4*10^2
print(d)              # 340.0
print(type(d))        # <class 'float'>
e=9.62e-2             # 3.4*10^-2
print(e)              # 0.0962
#print(9.8.2)  # error dur to more than one decimal point
'''
#complex object1
'''
a=3+4j
print(a)                   # 3+4j
print(type(a))             # <class 'complex'>
print(id(a))               # address of object a
print(a.real)              # 3.0
print(a.imag)              # 4.0
print(type(a.real))        # <class 'float'>
print(type(a.imag))        # <class 'float'>
'''
#complex object2
'''
a=6j
print(a)                # 6j
print(type(a))          # <class 'complex'>
print(a.real)           # 0.0
print(a.imag)           # 6.0
#print(5+j6)     # error due to j is before 6
#print(3+4i)     # error due to invalid decimal
#print(4+j)       # error due to j is not defined
print(4+1j)            # 4+1j
print(4+0j)            # 4=0j
'''
#bool( object)
'''
a=True
print(a)                  # True
print(type(a))            # <class 'bool'>
print(id(a))              # address of object a
b=False
print(b)                  # False
print(True+True)          # 2
print(True+False)         # 1
print(False+True)         # 1
print(False+False)        # 0
print(True+True+True)     # 3
print(25+10.8+True)       # 36.8
print(True>False)         # True
#print(true)             # error due to t is not capital in True
#print(false)            # error due to f is not capital in False
print(True)                # True
print(False)               # False
'''
#None type object
'''
a=None
print(type(a))           # <class 'Nonetype'>
print(a)                  # None
print(id(a))             # addresss of object a
#print(none)             # error due to 'n'
'''
#Binary demo
'''
a=0b10101
print(a)                                  # 0b10101 i.e. 16+4+1=21
print(type(a))                            # <class 'int'>
print(id(a))                              # address of object 21
b=0b10101
print(b)                                  # 21
print(id(b))                              # same adress of object 21
c=21
print(c)                                  # 21
print(id(c))                              # same address of object 21
d=10101
print(d)                                  # 10101
#e=0b1234                                 # error due to 2,3,4
'''
#octal demo
'''
a=0O6247
print(a)                 # 6*8^3+2*8^2+4*8^1+7*8^0=3239
print(type(a))           # <class 'int'>
print(id(a))             # addresss of object 3239
b=0o6247
print(id(b))             # same address of object 3239
print(b)                 # 3239
c=3239
print(c)                 # 3239
print(id(c))             # same address of object 3239
#print(0o9248)           #error due to 9 is not in octal
'''
#hexa decimal demo
'''
a=0xA7B9 
print(a)                 # 10*16^3+7*16^2+11*16^1+9*16^0=42937
print(type(a))           # <class 'int'>
b=0xBEEF
print(b)                 # 11*16^3+14*16^2+14*16^1+15*16^0=48879
#print(A7B9)             # error 
print('A7B9')            # A7B9
#print(0XBEER)           # error due to R is not a Hexa decimal
#print(0XHYD)            # error due to H Y are not Hexa decimals
#print(0xA7G9B)          # error due to G is not a Hexa decimal
'''
