1.# float  object  demo  program (Home  work)
a = 10.8		
print(a)		# Value of object 'a' i.e. 10.8
print(type(a))		# Type of object 'a'  i.e. <class 'float'>
print(id(a))		# Address of object 'a' is 2112581647696
b = 25.			# It is still treated as float even if the decimal is not followed by any digit
print(b)		# Value of object 'b' i.e. 25.0
print(type(b))		# Type of object 'b'  i.e. <class 'float'>
c = .689		# It is still treated as a Float and it is valid 
print(c)		# Value of object 'c' i.e. 0.689
d = 3.4E2		# [ Mantissa Exponent number]
print(d)		# Value of object 'd' is 3.4*10^2 = 340.0
print(type(d))		# Type of object 'd'  is <class 'float'>
e = 9.62e-2		# [Mantissa exponent number]
print(e)		# Value of object 'e' i.e. 9.62*10^-2=0.0962
print(9.8.2)		# Invalid syntax because python does not allow two decimal points in one number.



2.# complex object demo program
a = 3 + 4j		
print(a)		# Value of object 'a' is 3+4j
print(type(a))		# Type of object 'a'  is <class 'complex'>
print(id(a))		# Address of object 'a' May be 2112584429968
print(a . real)		# 3.0
print(a . imag)		# 4.0
print(type(a . real))	# Type of  object (a.real) is <class 'float'>
print(type(a . imag))	# Type of  object (a.imag) is <class 'float'>


3.# Find outputs (Home work)
a = 6j			
print(a)		# Value of object 'a' is 6j
print(type(a))		# Type of object 'a'  is <class 'complex'>
print(a.real)		# 0
print(a.imag)		# 6j
print(5 + j6)		# Invalid syntax because imag is after 'j'
print(3 + 4i)		# Invalid syntax due to 'i'
print(4+j)		# Invalid because imag is missing
print(4 + 1j)		# Valid
print(4 + 0j)		# Valid


4.# bool object demo program  (Home  work)
a = True			
print(a)			# True
print(type(a))			# Type of object 'a'  is <class 'bool'>
print(id(a))			# Address of object 'a' 14071505725730
b = False			
print(b)			# False
print(type(b))			# Type of object 'b'  is <class 'bool'>
print(True + True)		# 1 + 1 = 2 # True
print(True + False)		# 1 + 0 = 1 #True
print(False + True)		# 0 + 1 = 1  #True
print(False + False)		# 0 + 0 = 0 #False
print(True + True + True)	# 1 + 1 + 1 = 3 #True
print(25 + 10.8 + True)		# 36.8 ----> 25 + 10.8 + 1 = 36.8
print(True > False)		# True 
print(True)			# True
print(False)			# False
print(true)			# Invalid because of starting letter should be captial 
print(false)			# Invalid because of starting letter should be captial


5.# Find  outputs (Home  work)
a = 0O6247		
print(a)		# value of object 'a' i.e. 3239
print(type(a))		# Type of object 'a'(3239)  i.e. <class 'int'>
print(id(a))		# Address of object 'a' 1000
b = 0o6247		# Reference 'b' points to same object 3239
print(id(b))		# same address
print(b)		# value of object 'b' is 3239
c = 3239		# Reference 'c' points to same object 3239
print(c)		# value of object 'c' is 3239
print(id(c))		# same address
print(0o9248)		# Error due to '9'


6.# Find  outputs  (Home  work)
a = 0XA7B9		
print(a)		# value of object 'a' is42937
print(type(a))		# Type of object 'a'is <class 'int'>
b = 0xBEEF		# value of object 'b' is 48879
print(b)		# 48879
print(A7B9)		# Error because of name is not defined
print('A7B9')		# valid because we are in single quotes
print(0XBEER)		# Error due to 'R'
print(0XHYD)		# Error due to 'H & Y'
print(0xA7G9B)		# Error due to 'G'


7.# Find outputs (Home  work)
a = 9248		
print(a)		# value of object 'a' is 9248
print(type(a))		# Type of object 'a' is <class 'int'>