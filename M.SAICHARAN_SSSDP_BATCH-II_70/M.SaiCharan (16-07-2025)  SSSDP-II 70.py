1.#  Find  outputs  (Home  work)
a = "Rama Rao"			# Reference 'a' points to string "Rama Rao'
print(a)			# Rama Rao
print(type(a))			# Type of object 'a' i.e. <class 'str'>
print(id(a))			# Address of object (may be 1000)
b = 'Hyd'
print(b)			# Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c)			# Hyd is green city.
				# Hyd is hitec city.
				# Hyd is beautiful city.


2.# Index   demo  program  (Home  work)
a = 'Hyd'
print(How  to  print  'H'  of  object  'a')	# print(a[0]) ----> a[0]
print(How  to  print  'y'  of  object  'a')	# print(a[1]) ----> a[1]
print(How  to  print  'd'  of  object  'a')	# print(a[2]) ----> a[2]
print(a[3])					# Error 
print(How  to  print  'd'  of  object  'a')	# print(a[-1]) ----> a[-1]
print(How  to  print  'y'  of  object  'a')	# print(a[-2]) ----> a[-2]
print(How  to  print  'H'  of  object  'a')	# print(a[-3]) ----> a[-3]
print(a[-4])					# Error
print(a[0] ==  a[-3])				# True because both are indexes of 'H', a[0] is positive index and a[-3] is negative index
a[2] = 'c'					# Error because string is Immutable, we cannot change the string 
print(25[0])					# Error
print('25'[0])					# 2 ----> here 25 is string, so 2 has index [0] and 5 has index [1]
print(True[1])					# Error
print('True'[1])				# r ----> here True is a string, so [0]=T, [1]=r, [2]=u, [3]=e


3.#  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3)			# HydHydHyd
print(a * 2)			# HydHyd
print(a * 1)			# Hyd
print(a * 0)			# emptystring
print(a * -1)			# emptystring
print(25 * 3)			# 75
print('25' * 3)			# 252525
print('25' * 4.0)		# Error
print(3 * 'Hyd')		# HydHydHyd
print('25' * True)		# 25


4.#  Find  outputs  (Home work)
a = 'Hyd'
print(a , id(a))		# Hyd, address of a may be 2000
a = a * 3
print(a , id(a))		# HydHydHyd, address of a may be 3000


5.# len()  function  (Home  work)
print(len('Hyd'))		# 3
print(len('Rama Rao'))		# 8
print(len('9247'))		# 4
print(len(''))			# 0
print(len(' '))			# 1
print(len(689))			# Error, because 689 is integer, it has no length


6.# Find  outputs  (Home  work)
a = """"Hyd"""
print(a)
print(len(a))
print(a[0])
print("""Hyd"""")
b = """""Hyd"""
print(b)
print(len(b))




7.# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12])		# a[ 7 : 12 : 1] ----> string from indexes 7 to 11 in steps of 1  i.e. Dayal
print(a[7 : ])			# a[ 7 : 18 : 1] ----> string from indexes 7 to 17 in steps of 1  i.e. Dayal<space>Sarma
print(a[ : 6])			# a[ 0 : 6 : 1] ----> string from indexes 0 to 5 in steps of 1  i.e. Sankar
print(a[ : ])			# a[ 0 : 18 : 1] ----> string  from  indexes  0  to  17  in  steps  of   1  i.e.  Sankar<space>Dayal<space>Sarma
print(a[:  : ])			# a[ 0 : 18 : 1]  ---> string from indexes 0 to 17 in steps of 1  i.e. Sankar<space>Dayal<space>Sarma
print(a[1 : 10 : 2])		# a[ 1 : 10 : 2] ----> string from indexes 1 to 9 in steps of 2  i.e. akrDy
print(a[0 : : 2])		# a[ 0 : 18 : 2] ----> string from indexes 0 to 17 in steps of 2  i.e. sna<space>aa<space>am
print(a[1 : : 2])		# a[ 1 : 18 : 2] ----> string from indexes 1 to 17 in steps of 2  i.e. akrDylSra
print(a[-5 : -1])		# a[ -5 : -1 : -1] ----> string from indexes -5 to -2 in steps of -1  i.e. Sarm
print(a[::-1])			# a[ -1 : -19 : -1] ----> string from indexes -1 to -18 in steps of -1  i.e. amraS<space>layaD<spac>raknaS
print(a[-1:-5:-1])		# a[ -1 : -5 : -1] ----> string from indexes -1 to -4 in steps of -1  i.e. amra
print(a[ : : -2])		# a[-1 :  -19 : -2]  --->  string  from  indexes  -1  to  -18  in  steps  of   -2  i.e.  arSlyDrka
print(a[3 : -3])		# a[ 3 : -3 : 1] ----> string from indexes 3 to -4(or 14)  in steps of 1  i.e. kar<space>Dayal<space>Sa
print(a[2 : -5])		# a[ 2 : -5 : 1] ----> string from indexes 2 to -6(or 11) in steps of 1  i.e. nkar<space>Dayal
print(a[-1:-5])			# Empty
print(a[3 : 3])			# Empty



8.#  Find  outputs  (Home  work)
a =  'A'
print(a[1])		# Error, there is only index [0]
print(a[1:])		# empty



9.# int()  function  demo  program
print(int(10.8))	# Converts  float   object  10.8  to  int  object  10
print(int(True))	# Converts  bool   object    True  to  int  object 1
print(int(False))	# converts bool object False to int object 0
print(int('25'))	# converts string object '25' to int object 25
print(int('0075'))	# converts string object '0075' to int object 75
print(int(0B11010))	# converts Decimal equivalent '0B11010' to int 26 ----> 16*1 + 8*1 + 2*1 = 26
print(0B11010)		# 26 ----> 2^4*1 + 2^3*1 + 2^1*1 ----> 16*1 + 8*1 + 2*1 = 26
print(int(0O6247))	# converts Decimal equivalent '0O6247' to int 3239 ----> 512*6 + 64*2 + 8*4 + 7*1 ----> 3072 + 128 + 32 + 7 = 3239
print(0O6247)		# 3239 ----> 8^3*6 + 8^2*2 + 8^1*4 + 8^0*7 ----> 512*6 + 64*2 + 8*4 + 1*7 ----> 3072 + 128 + 32 + 7 = 3239
print(int(0XA7B9))	# converts Decimal equivalent '0XA7B9' to int 42937 ----> 4096*10 + 256*7 + 16*11 + 1*9 ----> 40960 + 1792 + 176 + 9 = 42937
print(0XA7B9)		# 42937 ----> (A=10,B=11) i.e. 16^3*10 + 16^2*7 + 16^1*11 + 16^0*9 ----> 4096*10 + 256*7 + 16*11 + 1*9 ----> 40960 + 1792 + 176 + 9 = 42937
print(int(3 + 4j))	# Error
print(int('25.4'))	# Error
print(int('Ten'))	# Error



10.# float()  function  demo  program
print(float(25))		#  Converts  int  object  25  to  float  object   25.0
print(float(True))		#  Converts  bool  object   True   to  float  object   1.0
print(float(False))		#  Converts  bool  object   False   to  float  object   0.0
print(float('92'))		#  Converts  string  object   '92'   to  float  object   92.0
print(float('36.4'))		#  Converts  string  object   '36.4'   to  float  object 36.4
print(float('0075'))		#  Converts  string  object   '0075'   to  float  object 75.0
print(float(0B1010101))		#  Converts  Decimal equivalent to  float  object 85.0 
print(float(0O6247))		#  Converts  Decimal equivalent to  float  object 3239.0 
print(float(0XA7B9))		#  Converts  Decimal equivalent to  float  object 42937.0 
print(float(3 + 4j))		# Error
print(float('Ten'))		# Error



11.# complex()  function  demo  program
print(complex(3 , 4))		# 3+4j
print(complex(0 , 4))		# 4j
print(complex(3))		# 3+0j
print(complex(3.8 , 4.6))	# 3.8+4.6j
print(complex(3.8))		# 3.8+0j
print(complex(3 , 4.5))		# 3+4.5j
print(complex(True , False))	# 1+0j
print(complex(True))		# 1+0j
print(complex(False))		# 
print(complex(True , 4))	# 1+4j
print(complex('3'))		# 3+0j
print(complex('3.8'))		# 3.8+0j
print(complex(3 , '4'))		# Error
print(complex('3' , 4))		# Error
print(complex('3' , '4'))	# Error
print(complex('Ten'))		# Error



12.#  bool()  function  demo  program
print(bool(0)) 		# False
print(bool(10)) 	# True :  10  is  non-zero
print(bool(-25))	# True : -25 is non-zero
print(bool(0.0))	# False
print(bool(0.1))	# True : 0.1 is non-zero
print(bool(0 + 0j))	# False
print(bool(10 + 20j))	# True : non-zero complex number
print(bool(-15j))	# True : non-zero complex number
print(bool('False'))	# True : non-empty string
print(bool(''))		# False
print(bool('Hyd'))	# True : non-empty string
print(bool(' '))	# True : non-empty string
print(bool('True'))	# True : non-empty string




13.# str()  function  demo  program
print(str(25))		#  Converts   25  to  '25'
print(str(10.8))	#  Converts   10.8  to  '10.8'
print(str(3 + 4j))	#  Converts   3+4j  to  '3+4j'
print(str(True))	#  Converts   True  to  'True'
print(str(False))	#  Converts   False  to  'False'
print(str(None))	#  Converts   None  to  'None'



14.# oct()  function  demo  program
print(oct(195))			# converts decimal to octal i.e. 0o303
print(oct(0B10101110010))	# converts binary to octal i.e. 0o2562
					 ----> 4 2 1    4 2 1    4 2 1     4 2 1 
					       0 1 0    1 0 1    1 1 0     0 1 0
					         2       4+1      4+2        2
					         2	  5	   6	     2
print(oct(0xA7B9))





15.# hex()  function  demo  program
print(hex(25))			# converts decimal to hexa i.e. 0x19
print(hex(0B10101111010111))	# 0x2BD7 ----> 8 4 2 1     8 4 2 1     8 4 2 1    8 4 2 1 
					       0 0 1 0     1 0 1 1     1 1 0 1    0 1 1 1
					          2	    8+2+1	8+4+1	    4+2+1
						  2	      11	  13		7
						  2	      B	          D		7
print(hex(0O6247))