# float object demo program (Home work)
a = 10.8 # a is assigned to float object class
print(a) #10.8
print(type(a)) #<class 'float'>
print(id(a)) # address of a
b = 25. # b is assigned to int object class
print(b) #25.0
print(type(b)) #<class 'int'
c = .689 #c is assigned to float object class
print(c) #0.689
d = 3.4E2 # dis assigned to float object class
print(d) #340.0
#e is assigned to float object class
print(type(d)) #<class 'float'>
e = 9.62e-2
print(e)
print(9.8.2)
#0.0962
# invalid because 9.8 or 9.2 ( invalid syntax )


#complex object demo program
a = 3 + 4j
print(a)
# a is assigned to complex object class
#3 +4j
print(type(a)) #<class 'complex'>
print(id(a)) #address of a
print(a. real) #3.0
print(a. imag) #4.0
print(type(a. real)) #<class 'float'>
print(type(a. imag)) #<class 'float'>


# Find outputs (Home work)
a = 6j # a is assigned to complex object class
print(a) #6]
print(type(a))#<class 'complex'>
print(a.real) #0.0
print(a.imag) #6.0
print(5 + j6) #invalid j should be last or after number
print(3 + 4i) #invalid i is not used in python for imaginary numbers
print(4+j) #invalid single j should notbe declare, need to declare with 1j
print(4 + 1j) #4 +1j
print(4 + 0j) #4 +0j



# bool object demo program (Home work)
a = True
print(a)
print(type(a))
print(id(a))
b = False
print(b)
print(type(b))
# a is assigned to bool object class
#True
#class 'bool'>
#address of a
# b is assigned to bool object class
#False
#<class 'bool'>
print(True + True) #2
print(True + False) #1
print(False + True) #1
print(False + False) #0
print(True + True + True) #3
print(25 + 10.8 + True) #36.8
print(True > False) #True
print(True) #True
print(False) #False
print(true) #invaid because it is not keyward
print(false) #invaid because it is not keyward


# Find outputs (Home work)
a = 006247 # a is assigned to int object class
print(a) #3239
print(type(a)) #<class 'int'>
print(id(a)) #address of а
b = 006247 # b is assigned to int object class
print(id(b)) #address of a
print(b) #3239
c = 3239 # a is assigned to int object class
print(c) #3239
print(id(c)) # same address of a
print(009248) #invaild because 9 is not octal number


# Find outputs (Home work)
a = 0XA7B9 # a is assigned to int object class
print(a) #42937
print(type(a)) #<class 'int'>
b = 0xBEEF # a is assigned to int object class
print(b) #48879
print(A7B9) #invalid because it is not defined
print('A7B9') #A7B9
print(0XBEER) #invalid because hexadecimial has 0 to 9 and a to f
print(0XHYD) #invalid because hexadecimial has 0 to 9 and a to f
print (0xA7G9B) #invalid because hexadecimial has 0 to 9 and a to f


# Find outputs (Home work)
a = 9248 #a is assigned to int object class
print(a) #9248
print(type(a)) #<class 'int'>
