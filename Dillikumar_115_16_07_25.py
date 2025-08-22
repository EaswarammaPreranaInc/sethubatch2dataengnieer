(16-07-2025)

# Find outputs (Home work)
a = "Rama Rao"  # Ref 'a' points to a string object "Rama Rao"
print(a)  # Output: Rama Rao
print(type(a))  # Type of object 'a': <class 'str'>
print(id(a))    # Address of object 'a' 
b = 'Hyd'   # Ref 'b' points to string object 'Hyd'
print(b)   # Output: Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''  # Ref 'c' points to Multi-line string using triple quotes
print(c) # Output: Hyd is green city.
		Hyd is hitec city.
		Hyd is beautiful city.


# Index   demo  program  (Home  work)
a = 'Hyd'# Ref 'a' points to string object "Hyd"
print(How  to  print  'H'  of  object  'a')# Output: H
print(How  to  print  'y'  of  object  'a')# Output: y
print(How  to  print  'd'  of  object  'a')# Output: d
print(a[3])	# Error as string index is out of range
print(How  to  print  'd'  of  object  'a')# Output: d
print(How  to  print  'y'  of  object  'a')# Output: y
print(How  to  print  'H'  of  object  'a')# Output: H
print(a[-4])    # Error as string index is out of range
print(a[0] ==  a[-3]) # Output: True
a[2] = 'c'# Error because string is immutable can not used to assign values
print(25[0])# Error because int is a single element cannot performs indexing
print('25'[0])	 # Output: 2
print(True[1])   # Error because bool is a single element cannot performs indexing
print('True'[1]) # Output: r



#  Find  outputs  (Home work)
a = 'Hyd'   # Ref 'a' points to string object "Hyd"
print(a * 3) # Output: 'HydHydHyd'
print(a * 2) # Output: 'HydHyd'
print(a * 1)# Output: 'Hyd'
print(a * 0)# Output: '' (empty string)
print(a * -1)# Output: '' (empty string)
print(25 * 3)	# Output: 75
print('25' * 3) # Output: '252525'
print('25' * 4.0)  # error we can't multiply string with float number 
print(3 * 'Hyd')    # Output: 'HydHydHyd'
print('25' * True)  # Output: '25'



#  Find  outputs  (Home work)

a = 'Hyd'  # Ref 'a' points to string object "Hyd"
print(a , id(a))  # Output: 'Hyd', address of the object 'a'
a = a * 3   # 'a' now refers to a new string object a*3 i.e., 'HydHydHyd'
print(a , id(a))  # Output: 'HydHydHyd', address of the object 'a'



# len()  function  (Home  work) 
print(len('Hyd'))# Output: 3
print(len('Rama Rao'))  # Output: 8
print(len('9247'))# Output: 4
print(len(''))	# Output: 0
print(len(' '))# Output: 1
print(len(689))	# error because can't perform len() on int type



# Find  outputs  (Home  work)

a = """"Hyd""" # Ref 'a' points to string object """"Hyd"""
print(a)# Output: "Hyd
print(len(a))# Output: 4
print(a[0]) # Output: "
print("""Hyd"""") # syntax error as it does not take the last quote gives error
b = """""Hyd"""   # Ref 'b' points to string object """""Hyd"""
print(b)# Output: ""Hyd
print(len(b))  # Output: 5


# Find  outputs
a = 'Sankar Dayal Sarma'  # Ref 'a' points to string object 'Sankar Dayal Sarma'
print(a[7 : 12])  # string  from  indexes  7  to  11  in  steps  of   1  i.e.  'Dayal'
print(a[7 : ])    # string  from  indexes  7  to  end  in  steps  of   1  i.e.  'Dayal Sarma'
print(a[ : 6])    # string  from  indexes  0  to  5  in  steps  of   1  i.e.  'Sankar'
print(a[ : ])     #  a[ 0 :  18  : 1]  --->   string  from  indexes  0  to  17  in  steps  of   1  i.e.  'Sankar Dayal Sarma'
print(a[:  : ])   # string  from  indexes  0  to  17  in  steps  of   1  i.e.  'Sankar Dayal Sarma'
print(a[1 : 10 : 2])  # string  from  indexes  1  to  9  in  steps  of   2  i.e.  'akrDa'
print(a[0 : : 2])  # string  from  indexes  0  to  17  in  steps  of   2  i.e.  'SnkrDylSra'
print(a[1 : : 2])  # string  from  indexes  1  to  17  in  steps  of   2  i.e.  'aa a aama'
print(a[-5 : -1])  # string  from  indexes  -5  to  -2  in  steps  of   1  i.e.  'Sarm'
print(a[::-1])     # string  from  indexes  -1  to  -18  in  steps  of   -1  i.e.  'amraS layaD raknaS'
print(a[-1:-5:-1]) # string  from  indexes  -1  to  -4  in  steps  of   -1  i.e.  'amra'
print(a[ : : -2]) #   a[-1 :  -19 : -2]  --->  string  from  indexes  -1  to  -18  in  steps  of   -2  i.e.  'arSlyDrka'
print(a[3 : -3])  # string  from  indexes  3  to  -4  in  steps  of   1  i.e.  'kar Dayal Sa'
print(a[2 : -5])  # string  from  indexes  2 to  -6  in  steps  of   -1  i.e.  'nkar Dayal '
print(a[-1:-5])   # string  from  indexes  -1  to  -4 but default step is 1 hence no string    will be printed i.e.  '' 
print(a[3 : 3])   # string  from  indexes  3  to  3  is empty string i.e.  '' 


#   0      1      2      3      4       5         6        7       8       9     10     11      12          13     14       15      16     17
#   S      a      n      k      a       r                  D       a       y      a      l                 S       a         r       m       a
#  -18   -17     -16   -15    -14     -13        -12      -11      -10    -9     -8    -7      -6          -5      -4       -3      -2      -1


#  Find  outputs  (Home  work)

a =  'A' # Ref 'a' points to string object 'A'
print(a[1])  # error as string index is out of range
print(a[1:]) # Output: '' 



# int()  function  demo  program

print(int(10.8))  #  Converts  float   object  10.8  to  int  object  : 10
print(int(True))  #  Converts  bool   object    True  to  int  object :	1
print(int(False)) #  Converts  bool   object    False  to  int  object : 0
print(int('25'))#  Converts string object  '25' to  int  object : 25
print(int('0075')) #  Converts  string object  '0075'  to  int  object : 75
print(int(0B11010)) #  Converts binary object 0B11010  to  int  object : 26
print(0B11010)  # decimal equivalent of  0B11010 output: 26
print(int(0O6247)) #  Converts octal object  0O6247  to  int  object : 3239
print(0O6247) #  decimal equivalent of 0O6247 output: 3239 
print(int(0XA7B9)) #  Converts hexa-decimal object  0XA7B9 to  int  object : 42937 
print(0XA7B9)  # decimal equivalent of 0XA7B9 output: 3239 
print(int(3 + 4j)) # error as it can't convert complex to int object
print(int('25.4')) # invalid as it can't convert this object to int object
print(int('Ten'))  # invalid as it can't convert this object to int object





# float()  function  demo  program

print(float(25))  #  Converts  int  object    to  float  object:  25.0
print(float(True)) #  Converts  bool  object      to  float  object   1.0
print(float(False)) #  Converts  bool  object   to  float  object   0.0
print(float('92'))  #  Converts  string object  to  float  object:  92.0
print(float('36.4')) #  Converts  string object  to  float  object:  36.4
print(float('0075'))  #  Converts string object  to  float  object:  75.0
print(float(0B1010101))  #  Converts  binary object   to  float  object:  85.0
print(float(0O6247))  #  Converts octal object  to  float  object:  3239.0
print(float(0XA7B9))  #  Converts hexadecimal object  to  float  object:  42937.0
print(float(3 + 4j))  # error can't convert complex to float
print(float('Ten'))   # error can't convert this string to float: 'Ten'




# complex()  function  demo  program
print(complex(3 , 4)) #  Converts  int objects   to  complex  object:  (3=4j)
print(complex(0 , 4))#  Converts  int objects   to  complex  object:  4j
print(complex(3))    #  Converts int  object  to  complex  object:  (3=0j)
print(complex(3.8 , 4.6))#  Converts float  objects   to  complex  object:  (3.8=4.6j)
print(complex(3.8))   #  Converts  float object   to  complex  object:  (3.8=0j)
print(complex(3 , 4.5))  #  Converts   int, float objects   to  complex  object: (3=4.5j)
print(complex(True , False))  #  Converts  bool objects   to  complex  object:  (1=0j)
print(complex(True))  #  Converts  bool object   to  complex  object:  (1=0j)
print(complex(False)) #  Converts  bool object   to  complex  object:  0j
print(complex(True , 4)) #  Converts  bool,int objects   to  complex  object:  (1=4j)
print(complex('3')) #  Converts string  object  to  complex  object:  (3=0j)
print(complex('3.8'))  #  Converts string float  object  to  complex  object:  (3.8=0j)
print(complex(3 , '4'))  # invalid as second argument can not be a  'str'
print(complex('3' , 4))  # invalid as second argument is not permitted when fisrt argument is a 'str'
print(complex('3' , '4')) # invalid as both arguments can't be two strings
print(complex('Ten'))    # invalid this string is can not be converted to conmplex




#  bool()  function  demo  program
print(bool(0))   # False : 0 is treated as False
print(bool(10)) # True : non-zero number 10 is True
print(bool(-25))   # True : non-zero negative number 25 is True
print(bool(0.0))    # False : 0.0 is treated as False
print(bool(0.1))  # True : non-zero float 0.1 is True
print(bool(0 + 0j)) # False : complex(0,0) is False
print(bool(10 + 20j)) # True : non-zero complex 10 + 20j is True
print(bool(-15j)) # True : non-zero complex -15j is True
print(bool('False')) # True : non-empty strings is True
print(bool('')) # False : empty string is False
print(bool('Hyd'))   # True : non-empty string is True
print(bool(' '))    # True : single space counts as a non-empty string so it True
print(bool('True')) # True : non-empty string is True



# str()  function  demo  program
print(str(25)) #  Converts int object  to string object : '25'
print(str(10.8)) #  Converts float object  to string object : '10.8'
print(str(3 + 4j))  #  Converts complex object  to string object : '(3+4j)'
print(str(True))#  Converts bool object  to string object : 'True'
print(str(False))#  Converts bool object  to string object : 'False'
print(str(None))   #  Converts None object to string object : 'None'




# oct()  function  demo  program
print(oct(195)) #  Converts decimal object  to Octal object : '0o303'
print(oct(0B10101110010)) #  Converts Binary object  to Octal object  : '0o2572'
print(oct(0xA7B9)) # Converts Hexdecimal object  to Octal object : '0o123571'




# hex()  function  demo  program
print(hex(25))   #  Converts decimal object  to Hexdecimal object : '0x19'
print(hex(0B10101111010111)) #  Converts Binary object  to Hexdecimal object  : '0x2c57' 
print(hex(0O6247))  #  Converts Octal object  to Hexdecimal object  : '0xca7'

