#  Find  outputs  (Home  work)

a = "Rama Rao"
print(a) # Rama Rao
print(type(a)) <class 'string'>
print(id(a)) # Address of object "Rama Rao"

b = 'Hyd'
print(b) # 'Hyd'

c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c) # Hyd is green city.
	   Hyd is hitech city.
	   Hyd is beautiful city.
-----------------------------------------------
# Index   demo  program  (Home  work)

a = 'Hyd'
print(How  to  print  'H'  of  object  'a') # a[0]
print(How  to  print  'y'  of  object  'a') # a[1]
print(How  to  print  'd'  of  object  'a') # a[2]

print(a[3]) # Error 

print(How  to  print  'd'  of  object  'a') # a[-1]
print(How  to  print  'y'  of  object  'a') # a[-2]
print(How  to  print  'H'  of  object  'a') # a[-3]
print(a[-4]) # Error
print(a[0] ==  a[-3]) # True
a[2] = 'c' -->   # False
print(25[0])   # 2
print('25'[0]) # error
print(True[1]) # r
print('True'[1]) # error
-----------------------------------------------
#  Find  outputs  (Home work)

a = 'Hyd'
print(a * 3) # HydHydHyd
print(a * 2) # HydHyd
print(a * 1) # Hyd
print(a * 0) # o/p is empty
print(a * -1) # ''
print(25 * 3) # 75
print('25' * 3) # '252525'
print('25' * 4.0) # error
print(3 * 'Hyd') HydHydHyd
print('25' * True) # 25 (since True is 1)
-----------------------------------------
#  Find  outputs  (Home work)

a = 'Hyd'
print(a , id(a)) # Hyd , Address of object 'a'
a = a * 3
print(a , id(a)) # HydHydHyd , Address of object 'a'
---------------------------------------
# len()  function  (Home  work)

print(len('Hyd')) # 3
print(len('Rama Rao')) # 8
print(len('9247')) # 4
print(len('')) # 0
print(len(' ')) # 1
print(len(689)) # error

-------------------------------------
# Find  outputs  (Home  work)

a = """"Hyd"""
print(a) # error becoz invalid syntax
print(len(a))
print(a[0])
print("""Hyd"""") # Hyd

b = """""Hyd"""
print(b) # error
print(len(b))

---------------------------------------
# Find  outputs

a = 'Sankar Dayal Sarma'
print(a[7 : 12]) # 'Dayal'
print(a[7 : ]) # 'Dayal sarma'
print(a[ : 6]) # 'Sankar'
print(a[ : ])  #  a[ 0 :  18  : 1]  --->   string  from  indexes  0  to  17  in  steps  of   1  i.e.  Sankar<space>Dayal<space>Sarma
print(a[:  : ]) # 'Sankar Dayal Sarma'
print(a[1 : 10 : 2]) # 'aka a'
print(a[0 : : 2]) # 'SnkrDylSra'
print(a[1 : : 2]) # 
print(a[-5 : -1])
print(a[::-1])
print(a[-1:-5:-1])
print(a[ : : -2]) #   a[-1 :  -19 : -2]  --->  string  from  indexes  -1  to  -18  in  steps  of   -2  i.e.  arSlyDrka
print(a[3 : -3])
print(a[2 : -5])
print(a[-1:-5])
print(a[3 : 3])

-----------------------------------------------------------
#  Find  outputs  (Home  work)

a =  'A'
print(a[1]) # error due to index out of range
print(a[1:]) # ''

---------------------------------------
# int()  function  demo  program

print(int(10.8))  #  Converts  float   object  10.8  to  int  			     object  10
print(int(True))  #  Converts  bool   object    True  to  int  			      object 1
print(int(False)) #  Converts  bool   object    True  to  int  			     object 0
print(int('25')) #  Converts  string  object   '25' to  int  			     object 25
print(int('0075')) #  Converts  string  object    '0075'  to int  			     object 0075

print(int(0B11010)) #  26
print(0B11010)      #  26
print(int(0O6247))  # 6*5120 + 2*64 + 4*8 + 7*1 =3239
print(0O6247)      # 3239 
print(int(0XA7B9))  #  11×16+9=40960+1792+176+9=42937
print(0XA7B9) # 42937
print(int(3 + 4j))  # error
print(int('25.4')) # error
print(int('Ten')) # error

----------------------------------------------
# float()  function  demo  program

print(float(25))  #  Converts  int  object  25  to  float       	             object   25.0
print(float(True))   #  Converts  bool  object   True   to  	    	              float  object   1.0
print(float(False)) Converts  bool  object   True   to  	    	              float  object   0.0

print(float('92')) # 92.0
print(float('36.4')) # 36.4
print(float('0075')) # 75.0
print(float(0B1010101)) # 0*32 + 1*16 + 0*8 + 1*4 +0*2 + 1*1 =85 
print(float(0O6247)) # 3239.0
print(float(0XA7B9)) # 42937.0
print(float(3 + 4j)) # error 
print(float('Ten')) # error
---------------------------------------------------

# complex()  function  demo  program

print(complex(3 , 4))    # (3+4j)
print(complex(0 , 4))    # (0+4j)
print(complex(3))         # (3+0j)
print(complex(3.8 , 4.6)) # (3.8 + 4.6j)
print(complex(3.8))        # (3.8+0j)
print(complex(3 , 4.5))     #(3+4.5j)
print(complex(True , False)) #(1+0j)
print(complex(True))         # (1+0j)
print(complex(False))         # 0j
print(complex(True , 4))    # (1+4j)
print(complex('3'))         # (3+0j)
print(complex('3.8')) 	    # (3.8+0j)
print(complex(3 , '4')) # error
print(complex('3' , 4)) # error
print(complex('3' , '4')) # error
print(complex('Ten'))     # error

---------------------------------------------------

#  bool()  function  demo  program

print(bool(0)) #   False
print(bool(10)) #   True :  10  is  not a zero
print(bool(-25)) # True becoz non-zero integer
print(bool(0.0)) # False  
print(bool(0.1)) # True
print(bool(0 + 0j)) # False becoz zero complex number
print(bool(10 + 20j)) # True becoz complex number
print(bool(-15j))   # True becoz imag is not zero
print(bool('False')) # True becoz string is non-empty
print(bool('')) # False becoz empty string
print(bool('Hyd')) # True becoz string is non-empty
print(bool(' '))  # True becoz non-empty string
print(bool('True')) # True becoz string is non-empty

-----------------------------------

# str()  function  demo  program

print(str(25))  #  Converts   25  to  '25'
print(str(10.8)) # converts 10.8 to '10'
print(str(3 + 4j)) # converts 3+4j to '3+4j'
print(str(True))  # 'True'
print(str(False)) # 'False'
print(str(None)) # 'None'

----------------------------------------

# oct()  function  demo  program

print(oct(195)) # 0o303
print(oct(0B10101110010)) # oct(1394) -->0o2622
print(oct(0xA7B9)) # 0o176321

--------------------------------

# hex()  function  demo  program

print(hex(25)) # 0x19
print(hex(0B10101111010111)) # hex(11223) -->0x2BD7
print(hex(0o6247)) # 6*8^3 + 2*8^2 + 4*8^1 + 7*8^0 
		    --> 3072  +  128 +  8 +  7
	            -->	 3239 
		    -->  0xCA7





