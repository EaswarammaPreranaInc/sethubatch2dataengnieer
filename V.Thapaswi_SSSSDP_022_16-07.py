#string object
a="Geo politics" # ref 'a' points to object "Geo politics"
print(a)  # Geo politics : value of object 'a'
print(type(a))  # <class 'str'> : type of object 'a'
print(id(a))  # address of object 'a'
b='politics'  # ref 'b' points to object 'politics'
print(b)  # politics : value of object 'b'
print(type(b))  # <class 'str'> : type of object 'b'
c='''Hyd is green city
Hyd is beautiful city
Hyd is hitech city.'''
print(c)    # Hyd is green city
            # Hyd is beautiful city  
            # Hyd is hitech city. : value of object 'c'
a='Hyd' # ref 'a' points to object 'Hyd'


print(a[0])  # 0/p: H : character at index 0 of string 'Hyd'
print(a[1])  # 0/p: y : character at index 1 of string 'Hyd'
print(a[2])  # 0/p: d : character at index 2 of string 'Hyd'
#print(a[3])  #  error : string 'Hyd' has characters only at index 0, 1, 2 .
print(a[-1]) # 0/p: d : character at index -1 of string 'Hyd'
print(a[-2]) # 0/p: y : character at index -2 of string 'Hyd'
print(a[-3]) # 0/p: H : character at index -3 of string 'Hyd'
#print(a[-4]) #  error : string 'Hyd' has characters only at index -1, -2, -3.
print(a[0]==a[-3]) # True : character at index 0 and -3 are same.
#a[2]='c' #  TypeError: 'str' object does not support item assignment
#print(25[0])  #  TypeError: 'int' object is not subscriptable. indexing cannot be used on integer.
print('25'[0])  # 2 : character at index 0 of string '25'
#print(True[1]) # TypeError : indexing cannot be used on boolean.
print('True'[0]) # T : character at index 0 of string 'True'

a='Hyd' # ref 'a' points to object 'Hyd'
print(a*3)  # HydHydHyd : string 'Hyd' is repeated 3 times
print(a*2)  # HydHyd : string 'Hyd' is repeated 2 times
print(a*1)  # Hyd : string 'Hyd' is repeated 1 time
print(a*0)  #  : string 'Hyd' is repeated 0 times, so empty string is printed
print(a*-1)  #  : string 'Hyd' is repeated -1 times, so empty string is printed
print(25*3)  # 75 : integer 25 is multiplied by 3
print('25'*3)  # 252525 : string '25' is repeated 3 times
#print('25'*4.0) # TypeError : cannot multiply a string by a float
print(3*"Hyd")  # HYdHydHyd . The order doen't matter for the string repetition. interger * string is same as string * integer.
print('25'*True)  # o/p: 25 : True is treated as 1

a='Hyd' # ref 'a' points to object 'Hyd'
print(a,id(a)) # prints value and address of object 'a'
a=a*3  #  strings are immutable in python. the original string 'Hyd' cannot be changed. so, a complete new string object HydHydHyd is created and ref 'a' points to this new object.
print(a,id(a)) # prints value and address of object 'a' and the address is different from the previous one.

#len() function
print(len('Hyd'))  # o/p: 3 : The 'Hyd' has 3 characters.
print(len("Rama Rao")) # o/p: 8 : The 'Rama Rao' has 8 characters.
print(len('9245'))  # o/p: 4 : The '9245' has 4 characters. because string is alphanumeric 
print(len(''))  # o/p: 0 : The empty string has 0 characters.
#print(len(678))  # TypeError

a=""""Hyd""" # excess opening quotes are treated as characters
print(a)  # o/p: "Hyd 
print(len(a)) # o/p: 4
print(a[0])  # o/p: " : character at index 0 of string '"Hyd'
#print("""Hyd"""") # excess closing quotes will give error 
b="""""Hyd"""
print(b) # o/p: ""Hyd
print(len(b)) # o/p: 5

# Find  outputs
a = 'Sankar Dayal Sarma' # ref 'a' points to string object 'Sankar Dayal Sarma'
print(a[7 : 12]) #  a[7:12]  :  string from indexes 7 to 11 in steps of 1 i.e. Dayal
print(a[7 : ])  #  a[7:18]  :  string from indexes 7 to 17 in steps of 1 i.e. Dayal Sarma
print(a[ : 6])  #  a[0:6]  :  string from indexes 0 to 5 in steps of 1 i.e. Sankar
print(a[ : ])  #  a[ 0 :  18  : 1]  --->   string  from  indexes  0  to  17  in  steps  of   1  i.e.  Sankar<space>Dayal<space>Sarma
print(a[:  : ])  #  a[0:18:1]  :  string from indexes 0 to 17 in steps of 1 i.e. Sankar Dayal Sarma
print(a[1 : 10 : 2])  #  a[1:10:2]  :  string from indexes 1 to 9 in steps of 2 i.e. akrDy
print(a[0 : : 2])  #  a[0:18:2]  :  string from indexes 0 to 17 in steps of 2 i.e. Snar ayalsra
print(a[1 : : 2])  #  a[1:18:2]  :  string from indexes 1 to 17 in steps of 2 i.e. akr Dya am
print(a[-5 : -1])  #  a[-5:-1]  :  string from indexes -5 to -2 in steps of 1 i.e. sarm
print(a[::-1])  #  a[-1:-19:-1]  :  string from indexes -1 to -18 in steps of -1 i.e. amraS layaD rnkaS
print(a[-1:-5:-1])  #  a[-1:-5:-1]  :  string from indexes -1 to -4 in steps of -1 i.e. amra
print(a[ : : -2]) #   a[-1 :  -19 : -2]  --->  string  from  indexes  -1  to  -18  in  steps  of   -2  i.e.  arSlyaan
print(a[3 : -3])  #  a[3:-3]  :  string from indexes 3 to -4 in steps of 1 i.e. kar Dayal Sa
print(a[2 : -5])  #  a[2:-5]  :  string from indexes 2 to -6 in steps of 1 i.e. nkar Dayal
print(a[-1:-5])  #  a[-1:-5]  :  empty string because -1 to -4 in steps of 1 is not possible
print(a[3 : 3])  #  a[3:3]  :  empty string because 3 to 2 in steps of 1 is not possible

#   0      1     2    3      4     5      6          7       8       9     10     11     12           13     14       15      16     17
#   S      a     n    k      a     r                 D       a       y     a       l                  S       a         r       m       a
#  -18   -17   -16   -15    -14   -13    -12        -11     -10     -9     -8     -7      -6          -5      -4       -3      -2      -1

#  Find  outputs  
a =  'A' 
#print(a[1]) # error : string 'A' has only one character at index 0.
print(a[1:]) # error : string 'A' has only one character at index 0, so it cannot be sliced from index 1.

# int()  function  demo  program
print(int(10.8))  #  Converts  float   object  10.8  to  int  object  10
print(int(True))  #  Converts  bool   object    True  to  int  object 1
print(int(False)) #  Converts  bool   object    False  to  int  object 0
print(int('25')) # Converts  string  object  '25'  to  int  object 25
print(int('0075')) # Converts  string  object  '0075'  to  int  object 75
print(int(0B11010)) # Converts  binary  object  0B11010  to  int  object 26
print(0B11010) # 26 : binary 0B11010 is 26 in decimal
print(int(0O6247))  # Converts octal object 0O6247 to int object 3289
print(0O6247)  # 3289 : octal 0O6247 is 3289 in decimal
print(int(0XA7B9)) # Converts hexadecimal object 0XA7B9 to int object 42937
print(0XA7B9)  # 42937 : hexadecimal 0XA7B9 is 42937 in decimal
#print(int(3 + 4j)) # typeerror: int() can't convert complex to int
#print(int('25.4')) # valueError
#print(int('Ten'))  # valueError

# float()  function 
print(float(25))  #  Converts  int  object  25  to  float  object   25.0
print(float(True))   #  Converts  bool  object   True   to  float  object   1.0
print(float(False)) #  Converts  bool  object   False   to  float  object   0.0
print(float('92')) # Converts  string  object  '92'  to  float  object   92.0
print(float('36.4')) # Converts  string  object  '36.4'  to  float  object   36.4
print(float('0075'))  # Converts  string  object  '0075'  to  float  object   75.0
print(float(0B1010101)) # Converts  binary  object  0B1010101  to  float  object   85.0
print(float(0O6247))  # Converts  octal  object  0O6247  to  float  object   3289.0
print(float(0XA7B9)) # Converts  hexadecimal  object  0XA7B9  to  float  object   42937.0
#print(float(3 + 4j)) # typeerror: float() can't convert complex to float
#print(float('Ten')) # ValueError

# complex()  function  
print(complex(3 , 4)) # Converts  int  objects  3  and  4  to  complex object (3+4j)
print(complex(0 , 4)) # Converts  int  objects  0  and  4  to  complex object (0+4j)
print(complex(3)) # Converts  int  object  3  to  complex object (3+0j)
print(complex(3.8 , 4.6)) # Converts  float  objects  3.8  and  4.6  to  complex object (3.8+4.6j)
print(complex(3.8)) # (3.8+0j)
print(complex(3 , 4.5)) # (3+4.5j)
print(complex(True , False)) # (1+0j) : True is 1 and False is 0
print(complex(True)) # (1+0j) : True is 1 and False is 0
print(complex(False)) # (0+0j) : True is 1 and False is 0
print(complex(True , 4)) # (1+4j) : True is 1 and False is 0
print(complex('3')) # 3+0j 
print(complex('3.8')) # 3.8+0j
#print(complex(3 , '4')) # TypeError: complex() second argument must be a number, not str
#print(complex('3' , 4)) # TypeError
#print(complex('3' , '4')) # TypeError
#print(complex('Ten'))  # valueError

#  bool()  function  
print(bool(0)) #   False
print(bool(10)) #   True :  10  is  non-zero
print(bool(-25)) #   True :  -25  is  non-zero
print(bool(0.0)) # False
print(bool(0.1)) # True :  0.1  is  non-zero
print(bool(0 + 0j)) # False :  0 + 0j  is  zero complex number
print(bool(10 + 20j)) # True
print(bool(-15j))  # True
print(bool('False')) #True
print(bool('')) # false
print(bool('Hyd')) # True
print(bool(' ')) # True : space is a non-empty string
print(bool('True')) # True

# str()  function  
print(str(25))  #  Converts   25  to  '25'
print(str(10.8)) # Converts   10.8  to  '10.8'
print(str(3 + 4j)) # '(3+4j)'
print(str(True)) # True
print(str(False)) # False
print(str(None))  #  None

# oct()  function  
print(oct(195)) # Converts  int  object  195  to  octal string '0o303'
print(oct(0B10101110010)) # Converts  binary  object  0B10101110010  to  octal string '0o2562'
print(oct(0xA7B9)) # Converts  hexadecimal  object  0xA7B9  to  octal string '0o123671'

 
# hex()  function  
print(hex(25))  # Converts  int  object  25  to  hexadecimal string '0x19'
print(hex(0B10101111010111)) # Converts  binary  object  0B10101111010111  to  hexadecimal string '0x2bd7'
print(hex(0O6247))  # Converts  octal  object  0O6247  to  hexadecimal string '0xCA7'

 