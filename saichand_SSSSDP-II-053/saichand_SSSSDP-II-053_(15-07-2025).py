# float  object  demo  program (Home  work)
a = 10.8		# Reference 'a' points to object 10.8
print(a)		# Value of object 'a' i.e. 10.8
print(type(a))		# Type of object 'a'  i.e. <class 'float'>
print(id(a))		# Address of object 'a' (may be 2000)
b = 25.			# Reference 'b' points to object 25.0
print(b)		# Value of object 'b' i.e. 25.0
print(type(b))		# Type of object 'b'  i.e. <class 'float'>
c = .689		# Reference 'c' points to object 0.689
print(c)		# Value of object 'c' i.e. 0.689
d = 3.4E2		# Reference 'd' points to object 3.4E2
print(d)		# Value of object 'd' i.e. 3.4E2
print(type(d))		# Type of object 'd'  i.e. <class 'float'>
e = 9.62e-2		# Reference 'e' points to object 9.62e-2
print(e)		# Value of object 'e' i.e. 9.62e-2
print(9.8.2)		# Error due to invalid syntax i.e. '9.8.2'



# complex object demo program
a = 3 + 4j		# Assigns reference 'a' to complex object 3+4j
print(a)		# Value of object 'a' i.e. 3+4j
print(type(a))		# Type of object 'a'  i.e. <class 'complex'>
print(id(a))		# Address of object 'a' (may be 3000)
print(a . real)		# 3.0
print(a . imag)		# 4.0
print(type(a . real))	# Type of real object 3.0 i.e. <class 'float'>
print(type(a . imag))	# Type of imag object 4.0 i.e. <class 'float'>


# Find outputs (Home work)
a = 6j			# Assigns reference 'a' to complex object 6j
print(a)		# Value of object 'a' i.e. 6j
print(type(a))		# Type of object 'a'  i.e. <class 'complex'>
print(a.real)		# 0.0
print(a.imag)		# 6.0
print(5 + j6)		# Error because imag is after 'j'
print(3 + 4i)		# Error due to 'i'
print(4+j)		# Error because imag is missing
print(4 + 1j)		# 4+1j
print(4 + 0j)		# 4+0j


# bool object demo program  (Home  work)
a = True			# Assigns reference 'a' to bool object True
print(a)			# Value of object 'a' i.e. True
print(type(a))			# Type of object 'a'  i.e. <class 'bool'>
print(id(a))			# Address of object 'a' (may be 4000)
b = False			# Assigns reference 'b' to bool object False
print(b)			# Value of object 'b' i.e. False
print(type(b))			# Type of object 'b'  i.e. <class 'bool'>
print(True + True)		# 2 ----> 1 + 1 = 2
print(True + False)		# 1 ----> 1 + 0 = 1
print(False + True)		# 1 ----> 0 + 1 = 1
print(False + False)		# 0 ----> 0 + 0 = 0
print(True + True + True)	# 3 ----> 1 + 1 + 1 = 3
print(25 + 10.8 + True)		# 36.8 ----> 25 + 10.8 + 1 = 36.8
print(True > False)		# True ----> 1 > 0
print(True)			# True
print(False)			# False
print(true)			# Error due to 't'
print(false)			# Error due to 'f'


# Find  outputs (Home  work)
a = 0O6247		# Object contains decimal equivalent i.e. 8^3*6 + 8^2*2 + 8^1*4 + 8^0*7 ----> 512*6 + 64*2 + 8*4 + 1*7 ----> 3072 + 128 + 32 + 7 = 3239
print(a)		# 3239
print(type(a))		# Type of object 'a'(3239)  i.e. <class 'int'>
print(id(a))		# Address of object 'a' (may be 5000)
b = 0o6247		# Reference 'b' points to same object 3239
print(id(b))		# same address
print(b)		# 3239
c = 3239		# Reference 'c' points to same object 3239
print(c)		# 3239
print(id(c))		# same address
print(0o9248)		# Error due to '9'


# Find  outputs  (Home  work)
a = 0XA7B9		# Object contains decimal equivalent (A=10,B=11) i.e. 16^3*10 + 16^2*7 + 16^1*11 + 16^0*9 ----> 4096*10 + 256*7 + 16*11 + 1*9 ----> 40960 + 1792 + 176 + 9 = 42937
print(a)		# 42937
print(type(a))		# Type of object 'a'(42937)  i.e. <class 'int'>
b = 0xBEEF		# Object contains decimal equivalent (B=11,E=14,F=15) i.e. 16^3*11+16^2*14+16^1*14+16^0*15 ----> 4096*11+256*14+16*14+1*15 ----> 45056+3584+224+15 ----> 48879
print(b)		# 48879
print(A7B9)		# Error
print('A7B9')		# A7B9
print(0XBEER)		# Error due to 'R'
print(0XHYD)		# Error due to 'H & Y'
print(0xA7G9B)		# Error due to 'G'


# Find outputs (Home  work)
a = 9248		# Reference 'a' points to object 9248
print(a)		# 9248
print(type(a))		# Type of object 'a' i.e. <class 'int'>