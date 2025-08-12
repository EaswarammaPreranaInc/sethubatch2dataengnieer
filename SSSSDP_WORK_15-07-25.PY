# float  object  demo  program (Home  work)
a = 10.8  # ref a points towards the  object 10.8 value
print(a)   # value of the object that  a points  is 10.8 
print(type(a)) #<class float>
print(id(a)) #memory address of object a
b = 25.   # ref b points towards the  object 25.0 value
print(b)  # value of the object that  b points  is 25.0
print(type(b))  #<class float>
c = .689   # ref c points towards the  object 0.689 value
print(c)   # value of the object that  c points  is .689
d = 3.4E2 # ref d points towards the  object 3.4E2 value
print(d)  # value of the object that  d points  is 3.4*10^2
print(type(d)) <class 'float'>
e = 9.62e-2 # ref e points towards the  object 9.62e-2 value
print(e)  # value of the object that  e points  is 9.62*10^-2
print(9.8.2) #error


# complex object demo program
a = 3 + 4j   # assigns ref a points towards the object  3+4j value
print(a)  #value of the object that a points is 3+4j
print(type(a)) #<class complex>
print(id(a)) # memory address of object a 
print(a . real) #it points out the value of object  i.e real  3.0
print(a . imag) #it points out the value of object  i.e imaginary 4.0
print(type(a . real)) #<class float>
print(type(a . imag)) #<class float>



# Find outputs (Home work)
a = 6j  # assigns ref a points towards the object  6j value
print(a)  #value of the object that a points is 6j
print(type(a)) #<class complex>
print(a.real) # 0.0
print(a.imag) #6.0
print(5 + j6) #error
print(3 + 4i)   #error
print(4+j)  #error
print(4 + 1j)   #value of the object that a points is 4+1j
print(4 + 0j) #value of the object that a points is 4+0j


# bool object demo program  (Home  work)
a = True    assigns ref a points towards the object  True value
print(a)  #value of the object that a points is True
print(type(a)) #<class bool>
print(id(a))  # memory address of object a 
b = False   assigns ref b points towards the object  False value
print(b)  #value of the object that b points is False
print(type(b))  #<class bool>
print(True + True) #arithmetic operation True become 1 False becomes 0  1+1=2
print(True + False) #arithmetic operation True become 1 False becomes 0  1+0=1
print(False + True) #arithmetic operation True become 1 False becomes 0  0+1=1
print(False + False) #arithmetic operation True become 1 False becomes 0  0+0=0
print(True + True + True) #arithmetic operation True become 1 False becomes 0  1+1+1=3
print(25 + 10.8 + True) #arithmetic operation True become 1 False becomes 0  25+10.8+1=36.8
print(True > False) #True
print(True)  #True
print(False) #False
print(true) #error at t
print(false) #error at f


# Find  outputs (Home  work)
a = 0O6247  assigns ref a points towards the object  3239  decimal equivalent value
print(a)   #value of the object that a points is 3239
print(type(a)) #<class int>
print(id(a)) #memory address of object a
b = 0o6247 assigns ref b points towards the object  3239  decimal equivalent value
print(id(b))  #memory address of object a
print(b) #value of the object that b points is 3239
c = 3239  assigns ref c points towards the object  3239  (same object 3239)
print(c) #value of the object that c points is 3239
print(id(c))  #memory address of object a
print(0o9248)  #error 9 


# Find  outputs  (Home  work)
a = 0XA7B9 assigns ref a points towards the object  42937 decimal equivalent value
print(a)  #value of the object that b points is 42937 
print(type(a)) #<class int>
b = 0xBEEF assigns ref a points towards the object  48879 decimal equivalent value
print(b)  #value of the object that b points is 48879 
print(A7B9) #error
print('A7B9') #A7B9
print(0XBEER) #error at r
print(0XHYD) #error at h 
print(0xA7G9B) #error at G

# Find outputs (Home  work)
a = 9248 assigns ref a points towards the object  9248
print(a)  #value of the object that a points is 9248
print(type(a))  #<class int>
