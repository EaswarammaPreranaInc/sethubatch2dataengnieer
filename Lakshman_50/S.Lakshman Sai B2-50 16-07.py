#  Find  outputs  (Home  work)
a = "Rama Rao"
print(a)                      #Rama Rao
print(type(a))                #<class 'str'>
print(id(a))                  #address of the object 'a' Ex.5000
b = 'Hyd'
print(b)                      #Hyd                                        
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c)                      #Hyd is green city. Hyd is hitec city. Hyd is beautiful city.




# Index   demo  program  (Home  work)
a = 'Hyd'
print(How  to  print  'H'  of  object  'a')        #print(a[0])  #H
print(How  to  print  'y'  of  object  'a')        #print(a[1])  #y
print(How  to  print  'd'  of  object  'a')        #print(a[2])  #d
print(a[3])                                        #Error string index out of range
print(How  to  print  'd'  of  object  'a')        #print(a[-1])  #d
print(How  to  print  'y'  of  object  'a')        #print(a[-2])  #y
print(How  to  print  'H'  of  object  'a')        #print(a[-3])  #H
print(a[-4])                                       #Error string index out of range
print(a[0] ==  a[-3])                              #True
a[2] = 'c' 
print(25[0])                                       #Error 'int' object does not support 
print('25'[0])                                     #2 because '25' is a string
print(True[1])                                     #Error
print('True'[1])                                   #r because 'True' is a string                               



#  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3)             #HydHydHyd
print(a * 2)             #HydHyd
print(a * 1)             #Hyd  
print(a * 0)             #''
print(a * -1)            #''
print(25 * 3)            #75
print('25' * 3)          #252525 beacuse '25' is a string
print('25' * 4.0)        #Error because '4.0' is a float
print(3 * 'Hyd')         #HydHydHyd
print('25' * True)       #25 because True is treated as 1 in operations


#  Find  outputs  (Home work)
a = 'Hyd'
print(a , id(a))          #Hyd , address of object 'a' ex.1000 
a = a * 3
print(a , id(a))          #HydHydHyd , new address of object 'a' ex.2000 because 'a' is immutable

# len()  function  (Home  work)
print(len('Hyd'))            #3
print(len('Rama Rao'))      #8
print(len('9247'))           #4
print(len(''))              #0
print(len(' '))             #1
print(len(689))              #Error because '689' is an int

# Find  outputs  (Home  work)
a = """"Hyd"""
print(a)               #Hyd
print(len(a))          #3
print(a[0])            #H
print("""Hyd"""")       
b = """""Hyd""" 
print(b)             #Hyd            
print(len(b))        #3


# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12])     #Dayal
print(a[7 : ])       #Dayal Sarma
print(a[ : 6])       #Sankar
print(a[ : ])        #  a[ 0 :  18  : 1]  --->   string  from  indexes  0  to  17  in  steps  of   1  i.e.  Sankar<space>Dayal<space>Sarma
print(a[:  : ])      #Sankar Dayal Sarma 
print(a[1 : 10 : 2])  #akrDy
print(a[0 : : 2])     #Sna aa am
print(a[1 : : 2])      #akrDylSra
print(a[-5 : -1])      # Sarm
print(a[::-1])         #amraS layaD raknas 
print(a[-1:-5:-1])     #amra
print(a[ : : -2])    #   a[-1 :  -19 : -2]  --->  string  from  indexes  -1  to  -18  in  steps  of   -2  i.e.  arSlyDrka
print(a[3 : -3])     #kar Dayal Sa
print(a[2 : -5])        #nkar Dayal<space>
print(a[-1:-5])         #'' Empty string because default step is 1 So, start index -1 next step -1+1 it become 0 and it is away from end index -5 so it returns empty string
print(a[3 : 3])        #'' Empty string because start index and end index are same


#   0      1      2      3      4       5       6           7       8       9     10     11     12           13     14       15      16     17
#   S      a      n      k      a       r                   D       a       y      a      l                  S       a         r      m      a
#  -18   -17   -16       -15    -14   -13      -12          -11     -10    -9     -8    -7      -6          -5      -4       -3      -2      -1

#  Find  outputs  (Home  work)
a =  'A'
print(a[1])      #Error because string out of range
print(a[1:])     #Error because string contains only 0th index 

# int()  function  demo  program
print(int(10.8))  #  Converts  float   object  10.8  to  int  object  10
print(int(True))  #  Converts  bool   object    True  to  int  object 1
print(int(False))    #  Converts  bool   object    False  to  int  object 0
print(int('25'))   #  Converts  string   object  '25'  to  int  object  25
print(int('0075'))  #  Converts  string   object  '0075'  to  int  object  75
print(int(0B11010))  #  int 26
print(0B11010)        #26
print(int(0O6247))   #(8^3 *6) + (8^2 * 2) + (8^1 * 4) + (8^0 * 7) = 3239
print(0O6247)     #3239 
print(int(0XA7B9))   #(16^3 * 10) + (16^2 * 7) + (16^1 * 11) + (16^0 * 9) = 43033
print(0XA7B9)        #43033
print(int(3 + 4j))   #
print(int('25.4'))  #Error because '25.4' is a string with decimal point
print(int('Ten'))   #Error because 'Ten' is a word not a number

'''
int()  function
----------------
1) What  does  int(x)  do  ?  --->  Converts  object  'x'  to  integer

'''


# float()  function  demo  program
print(float(25))  #  Converts  int  object  25  to  float  object   25.0
print(float(True))   #  Converts  bool  object   True   to  float  object   1.0
print(float(False))   #0.0
print(float('92'))     #92.0
print(float('36.4'))   #36.4
print(float('0075'))   #75.0
print(float(0B1010101)) #85.0
print(float(0O6247))     #(8^3 * 6) + (8^2 * 2) + (8^1 * 4) + (8^0 * 7) = 3239.0
print(float(0XA7B9))    #(16^3 * 10) + (16^2 * 7) + (16^1 * 11) + (16^0 * 9) = 43033.0
print(float(3 + 4j))    #Error because complex numbers cannot be converted to float
print(float('Ten'))     #Error because 'Ten' is a word not a number

'''
float()   function
--------------------
1) What  does  float(x)  do  ?  --->  Converts  object  'x'  to  float

'''

# complex()  function  demo  program
print(complex(3 , 4))            #3 + 4j
print(complex(0 , 4))        #0 + 4j
print(complex(3))                #3 + 0j
print(complex(3.8 , 4.6))       #3.8 + 4.6j
print(complex(3.8))            #3.8 + 0j
print(complex(3 , 4.5))         #3 + 4.5j
print(complex(True , False))    #1 + 0j
print(complex(True))            #1 + 0j    
print(complex(False))            #0 + 0j
print(complex(True , 4))        #1 + 4j
print(complex('3'))             #3 + 0j
print(complex('3.8'))           #3.8 + 0j
print(complex(3 , '4'))         #Error because '4' is a string after a integer
print(complex('3' , 4))         #Error because '3' is a string before a integer
print(complex('3' , '4'))        #Error because both '3' and '4' are strings
print(complex('Ten'))             #Error because 'Ten' is a word not a number





#  bool()  function  demo  program
print(bool(0)) #   False
print(bool(10)) #   True :  10  is  non-zero
print(bool(-25))        #True
print(bool(0.0)) #False    
print(bool(0.1))        #True
print(bool(0 + 0j))     #False
print(bool(10 + 20j))    #True
print(bool(-15j))        #True
print(bool('False'))     #True because 'False' is a non-empty string
print(bool(''))         #False because '' is an empty string
print(bool('Hyd'))        #True
print(bool(' '))          #True because ' ' is a non-empty string like there is a space 
print(bool('True'))        #True


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
print(str(10.8))   #'10.8'
print(str(3 + 4j))   #'3+4j'
print(str(True))       #'True'
print(str(False))       #'False'
print(str(None))     #'None'


'''
What  does  str(x)  do ?  --->  Converts  object  'x'  to  string
'''


# oct()  function  demo  program
print(oct(195))      #0o303
print(oct(0B10101110010))  #convert binary  number  to decimal(1394)  and then to octal #0o2652    
print(oct(0xA7B9))  #convert hexadecimal number to decimal (42937) and then to octal #0o123671


'''
oct()  function
-----------------
1) What  does  oct(x)  do ?  --->  Converts  object  'x'  to  octal  number  where
								                    'x'  can  be  binary / decimal / hexa-decimal  number

                                          '''
                           


# hex()  function  demo  program
print(hex(25))                   #0x19
print(hex(0B10101111010111))      #convert  binary  number  to decimal(2^13*1) +(2^11*1)+........+(2^0*1)=0x2bd7
print(hex(0O6247))                #convert octal number to decimal(8^3*6) + (8^2*2) + (8^1*4) + (8^0*7)=0xca7

'''
hex()  function
------------------
1) What  does  hex(x)  do ?  --->  Converts  object  'x'  to  hexa-decimal  number  where
								                     'x'  can  be  binary / decimal / octal  number