# int object 
a=8  #  ref 'a' points to object 8
print(a)  # 8 : value of object 'a'
print(type(a))  # <class 'int'> : type of object 'a'
print(id(a))  # address of object 'a'

# float object
b=10.8 # ref 'b' points to object 10.8
print(b)  # 10.8 : value of object 'b'
print(type(b))  # <class 'float'> : type of object 'b'
print(id(b))  # address of object 'b'
c=.689 # ref 'c' points to object 0.689
print(c)  # 0.689 : value of object 'c'
d=3.4E2  # ref 'd' points to object 3.4E2
print(d) # 3.4*10^2=340
print(type(d)) #  <class 'float'>
e=9.62e-2  # ref 'e' points to object 9.62e-2
print(e) # 9.62*10^-2=0.0962
#print(9.4.3) # invalid synatax

#complex object 
a=3+4j # ref 'a' points to object 3+4j
print(a) # (3+4j) : value of object 'a'
print(type(a))  # <class 'complex'> : type of object 'a'
print(id(a))  # address of object 'a'
print(a.real)  # 3.0 
print(a.imag)  # 4.0
print(type(a.real)) # <class 'float'> : type of real part of complex number
print(type(a.imag))  # <class 'float'> : type of imaginary part of complex number
a=6j # ref 'a' points to object 6j
print(a)  # 6j : value of object 'a'
print(type(a))  # <class 'complex'> : type of object 'a'
print(a.real) # 0.0 
print(a.imag) # 6.0
#print(5+j6) # error 
#print(3+4i) # error
#print(4+j) # error : it should be written as 4+1j
print(4+1j) # o/p: 4+1j 
print(4+0j) # o/p: 4+0j

#bool object
a=True # ref 'a' points to object True
print(a) # True : value of object 'a'
print(type(a)) # <class 'bool'> : type of object 'a'
print(id(a)) # address of object 'a'
b=False # ref 'b' points to object False
print(b)    # False : value of object 'b'
print(type(b)) # <class 'bool'> : type of object 'b'
print(True+True)  # 2 : True is 1 and True is 1, so 1+1=2
print(True+False) # 1 :  1+0=1
print(False+False) # 0 : 0+0=0
print(True+True+True)   # 3 : 1+1+1=3
print(25+10.8+True) # 36.8 : 25+10.8+1=36.8
print(True>False) # True : 1>0
print(True) # True : value of object 'True'
print(False) # False : value of object 'False'
#print(true)  # error : 'true' is not defined
#print(false)  # error : 'false' is not defined
a=0xA7B9 # ref 'a' points to object 0xA7B9
print(a) # 43033 : value of object 'a' in decimal
print(type(a)) # <class 'int'> : type of object 'a'
b=0xBEEf # ref 'b' points to object 0xBEEf
print(b) # 48879 : value of object 'b' in decimal
print('A7B9') # prints 'A7B9' because it is a string
#print(0xbeer) # error: hexadecimal values are from 0 to 9 and A to F
#print(0xHyd) # error: 'H' is not a valid hexadecimal digit
#print(0xA7G9B) # error: 'G' is not a valid hexadecimal digit
a=0o6427 # ref 'a' points to object 0o6427
print(a)  # 3343 : value of object 'a' in decimal
print(type(a)) # <class 'int'> : type of object 'a'
print(id(a))  # address of object 'a'
b=0o6427  # ref 'b' points to object 0o6427
print(id(a))#id's of a and b are same
c=3229 # ref 'c' points to object 3229
print(c) # 3229 
print(id(c)) # address of object 'c'
#print(0o9248) # error: octal values are from 0 to 7
a=9248 # ref 'a' points to object 9248
print(a) # 9248 : value of object 'a'
print(type(a)) # <class 'int'> : type of object 'a'