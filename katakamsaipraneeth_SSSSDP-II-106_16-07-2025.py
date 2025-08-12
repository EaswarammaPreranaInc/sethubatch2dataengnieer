#  Find  outputs  (Home  work)
a = "Rama Rao" # reference 'a' is assigned to string class object "Rama Rao"
print(a)#Rama Rao
print(type(a)) # <class 'string'>
print(id(a)) # prints the address of string class object
b = 'Hyd' # reference 'b' is assigned to string class object 'Hyd'
print(b) # Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.''' # Multi-line string class object ,where only triple quotes are used
print(c) #Hyd is green city.
               Hyd is hitec city.
               Hyd is beautiful city.

# Index   demo  program  (Home  work)
a = 'Hyd' # single-line string # Single quotes are used
print(How  to  print  'H'  of  object  'a') # print(a[0]) ---> H
print(How  to  print  'y'  of  object  'a') # print(a[1]) ---->y
print(How  to  print  'd'  of  object  'a') # print(a[2]) ---->d
print(a[3]) # error, because index out of range
print(How  to  print  'd'  of  object  'a') # print(a[-1]) ---> d
print(How  to  print  'y'  of  object  'a') # print(a[-2]) --->y
print(How  to  print  'H'  of  object  'a') # print(a[-3]) --->H
print(a[-4]) # error, index out of range
print(a[0] ==  a[-3]) # True
a[2] = 'c' # error
print(25[0])# error
print('25'[0]) # 2
print(True[1]) # error
print('True'[1]) # r

#  Find  outputs  (Home work)
a = 'Hyd' # ref 'a' is pointed to string class object
print(a * 3) #Repeates Hyd thrice ; HydHydHyd
print(a * 2) # Repeates Hyd twice ; HydHyd
print(a * 1) # Repeates Hyd once
print(a * 0) # print no Hyd but prints ' '
print(a * -1) # same prints ' '
print(25 * 3) # 75
print('25' * 3)#252525 repeates three times
print('25' * 4.0) # error cannot multiply with float 
print(3 * 'Hyd') # HydHydHyd
print('25' * True) # 25--->'25' * 1

#  Find  outputs  (Home work)
a = 'Hyd' # ref 'a' is pointed towards string object
print(a , id(a)) # prints Hyd and address of the object
a = a * 3 # Hyd is repeated thrice and ref 'a' is pointed to object
print(a , id(a)) # HydHydHyd and address will change because now 'a' is pointing to object which is changed

# len()  function  (Home  work)
print(len('Hyd')) # length --> 3
print(len('Rama Rao')) # 8
print(len('9247'))# 4
print(len('')) #0
print(len(' ')) #1
print(len(689)) # no length for type int

# Find  outputs  (Home  work)
a = """"Hyd""" ref 'a' is pointed to string class obj
print(a) # prints "Hyd  
print(len(a)) # 4
print(a[0]) # "
print("""Hyd"""") # error
b = """""Hyd""" # ref 'b' is pointed to string object
print(b) # ""Hyd
print(len(b)) # 5

# Find  outputs
a = 'Sankar Dayal Sarma' # ref 'a' is assigned to string class object
print(a[7 : 12]) # Dayal
print(a[7 : ])# Dayal<sapce>Sarma
print(a[ : 6])# 'Sankar'
print(a[ : ])  #  a[ 0 :  18  : 1]  --->   string  from  indexes  0  to  17  in  steps  of   1  i.e.  Sankar<space>Dayal<space>Sarma
print(a[:  : ]) # 'Sankar Dayal Sarma' 
print(a[1 : 10 : 2]) # with step 2 we get output as -->akrDy
print(a[0 : : 2]) # Sna<space>aa<space>am
print(a[1 : : 2]) # akrDylSra
print(a[-5 : -1]) # Sarm --> + step index so , len-1 --->-2
print(a[::-1])# amaS layaD raknaS --->prints reverse string
print(a[-1:-5:-1]) #amra
print(a[ : : -2]) #   a[-1 :  -19 : -2]  --->  string  from  indexes  -1  to  -18  in  steps  of   -2  i.e.  arSlyDrka
print(a[3 : -3]) # kar Dayal Sa -->it goes to 3 to -3 index
print(a[2 : -5]) #nkar Dayal
print(a[-1:-5]) # amraS
print(a[3 : 3]) # no output


#   0      1      2      3      4       5       6           7       8       9     10     11     12           13     14       15      16     17
#   S      a      n      k      a       r                    D       a       y      a       l                     S       a         r       m       a
#  -18   -17   -16   -15    -14   -13    -12        -11     -10    -9     -8    -7      -6          -5      -4       -3      -2      -1

#  Find  outputs  (Home  work)
a =  'A' # ref 'a' is assigned to string obj A
print(a[1]) # error
print(a[1:]) # no output

# int()  function  demo  program
print(int(10.8))  #  Converts  float   object  10.8  to  int  object  10
print(int(True))  #  Converts  bool   object    True  to  int  object 1
print(int(False)) # converts bool object False to int object 0
print(int('25')) # Converts string object '25' into int obj 25
print(int('0075')) # converts string obj into int obj 75
print(int(0B11010)) #converts binary obj into int onj 26
print(0B11010) # 26 --> 16+8+2
print(int(0O6247)) # 6*8^3 + 2*8^2 + 4*8^1+7*1--->3239 converted into int obj
print(0O6247) # 3239
print(int(0XA7B9)) # 42937---> 10*16^3 + 7*16^2 + 11*16^1 + 9*1 decimal equivalent converts into int obj
print(0XA7B9) # 42937
print(int(3 + 4j)) # complex obj cannot be converted into int
print(int('25.4')) # float obj connot be converted , error
print(int('Ten')) # error 



'''
int()  function
----------------
1) What  does  int(x)  do  ?  --->  Converts  object  'x'  to  integer

# float()  function  demo  program
print(float(25))  #  Converts  int  object  25  to  float  object   25.0
print(float(True))   #  Converts  bool  object   True   to  float  object   1.0
print(float(False)) #  Converts  bool  object   False   to  float  object   0.0

print(float('92')) #  string obj converts into float obj 92.0
print(float('36.4'))# converts string obj into float obj
print(float('0075')) # converts string obj into float 75.0
print(float(0B1010101)) # converts decimal equivalent obj into float obj 85.0
print(float(0O6247)) # it also same converts to float obj 3239.0
print(float(0XA7B9))# converts to float obj 42937
print(float(3 + 4j)) # error
print(float('Ten')) # error





'''
float()   function
--------------------
1) What  does  float(x)  do  ?  --->  Converts  object  'x'  to  float

# complex()  function  demo  program
print(complex(3 , 4)) # prints 3+4j
print(complex(0 , 4)) # prints 4j
print(complex(3)) # 3+0j
print(complex(3.8 , 4.6)) # 3.8 + 4.6j
print(complex(3.8))# 3.8 + 0j
print(complex(3 , 4.5)) # 3+4.5j
print(complex(True , False)) # 1+0j
print(complex(True)) # 1+0j
print(complex(False))# 0j
print(complex(True , 4)) # 1+4j
print(complex('3')) # 3 +0j
print(complex('3.8')) # 3.8 + 0j
print(complex(3 , '4'))# error, second arg cannot be string
print(complex('3' , 4)) # error , first arg cannot be string
print(complex('3' , '4')) # error
print(complex('Ten')) # error because of string


#  bool()  function  demo  program
print(bool(0)) #   False
print(bool(10)) #   True :  10  is  non-zero
print(bool(-25))# True
print(bool(0.0)) # False
print(bool(0.1)) # True
print(bool(0 + 0j)) # False
print(bool(10 + 20j)) # True
print(bool(-15j)) # True
print(bool('False')) # True
print(bool('')) # false
print(bool('Hyd')) # True
print(bool(' ')) # True
print(bool('True')) #True


'''
bool()  function
------------------
1) What  does  bool(x)  do  ?  --->  Converts  object  'x'  to  True / False

2) Is  0  True  (or)  False ? --->  False
    What  about  non-zero ?  --->  True

3) Is  ''(i.e.  Empty  string)  True  (or) False ?  --->  False
    What  about  non-empty  string ?  --->	True

4) When  is  x + yj  treated  as  False ?  --->  When  both  'x'  and  'y'  are  zeroes
     When  is  x + yj  treated  as  True ?  --->  When  either  'x'  is   non-zero  (or)  'y'  is  non-zero
'''

# str()  function  demo  program
print(str(25))  #  Converts   25  to  '25'
print(str(10.8)) # Converts 10.8 to '10.8'
print(str(3 + 4j)) # Converts to 3+4j to '3+4j'
print(str(True)) # True
print(str(False)) # False
print(str(None)) # None


'''
What  does  str(x)  do ?  --->  Converts  object  'x'  to  string
'''

# oct()  function  demo  program
print(oct(195)) # Converts 195 to 0o303
print(oct(0B10101110010)) # bin is converted to 0o2562
print(oct(0xA7B9))# hexa decimal converts to 0o123671




'''
oct()  function
-----------------
1) What  does  oct(x)  do ?  --->  Converts  object  'x'  to  octal  number  where
								                    'x'  can  be  binary / decimal / hexa-decimal  number


# hex()  function  demo  program
print(hex(25)) # converts 25 to 0x19
print(hex(0B10101111010111)) bin to 0x2bd7
print(hex(0O6247)) # oct number to 0xca7






'''
hex()  function
------------------
1) What  does  hex(x)  do ?  --->  Converts  object  'x'  to  hexa-decimal  number  where
								                     'x'  can  be  binary / decimal / octal  number