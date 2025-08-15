#Home Work-1
#  Find  outputs  (Home  work)
a = "Rama Rao"
print(a) #the value of the string object, which is Rama Rao
print(type(a)) #type of the string object, which is <class 'string'>
print(id(a)) #address of the string object, say 1000
b = 'Hyd'
print(b) #the value of the string object, which is Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c) #prints the multi line string which is 
Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.

#Home Work-2
# Index   demo  program  (Home  work)
a = 'Hyd'
print(How  to  print  'H'  of  object  'a') #print(a[0])
print(How  to  print  'y'  of  object  'a') #print(a[1])
print(How  to  print  'd'  of  object  'a') #print(a[2])
print(a[3]) #error, reason for error: the index of string ranges from (0 to length of string-1)
print(How  to  print  'd'  of  object  'a') #print(a[-1])
print(How  to  print  'y'  of  object  'a') #print(a[-2])
print(How  to  print  'H'  of  object  'a') #print(a[-3])
print(a[-4]) #error, reason for error: the indexes of string ranges from -1 to -(length of string)
print(a[0] ==  a[-3]) #prints True, because both a[0] and a[-3] accesses the same char of the string
a[2] = 'c' #error, because string objects are immutable
print(25[0]) #error, because integer objects cannot be accessed with index
print('25'[0]) #prints the 1st char of the string, which is 2
print(True[1]) #error, because bool objects cannot be accessed with index
print('True'[1]) #prints the 2nd char of the string, which is 'r'

#Home Work-3
#  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3) #repeats the string object thrice, which is HydHydHyd
print(a * 2) #repeats the string object twice, which is HydHyd
print(a * 1) #repeats the string object only once, which is Hyd
print(a * 0) #repeats the string object zero times, which is empty string
print(a * -1) #empty string
print(25 * 3) #does multiplication and prints 75
print('25' * 3) #repeats the string thrice, which is 252525
print('25' * 4.0) #error, because string cannot be repeating with float values
print(3 * 'Hyd') #repeats the string thrice, which is HydHydHyd
print('25' * True)#does multiplication and prints 25, where True is treated as 1 since operation is going on.

#Home Work-4
#  Find  outputs  (Home work)
a = 'Hyd'
print(a , id(a)) #prints the string Hyd with address of the string object say 4000
a = a * 3 
print(a , id(a)) #prints the updated string which is repeated thrice which is HydHydHyd with address day 4001, the address changes here because since string objects are immutable a new string object will be created when we try to modify the string

#Home Work-5
# len()  function  (Home  work)
print(len('Hyd')) #the length of string object which is 3
print(len('Rama Rao'))# the length of string object which is 8
print(len('9247'))#the string of the string object which is 4
print(len(''))#the length of empty string which is 0
print(len(' '))#the length of string which is 1
print(len(689))#error len function is only for sequence objects

#Home Work-6
# Find  outputs  (Home  work)
a = """"Hyd"""
print(a)#"Hyd, the extra quote is taken as char of the string making the string as "Hyd
print(len(a))#4
print(a[0])#"
print("""Hyd"""")#Hyd", the extra quote is taken as char of the string making the string as Hyd"
b = """""Hyd"""
print(b)#""Hyd, the 2 extra quotes are taken as char of the string making the string as ""Hyd
print(len(b))#5

#Home work-7
# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12])#prints chars of string from index 7 to 11, which is Dayal
print(a[7 : ])#prints chars of string from 7 to 17, which is Dayal Sarma
print(a[ : 6])#prints chars of string from 0 to 5, which is Sankar
print(a[ : ])  #  a[ 0 :  18  : 1]  --->   string  from  indexes  0  to  17  in  steps  of   1  i.e.  Sankar<space>Dayal<space>Sarma
print(a[:  : ]) #prints chars of string from index 0 to 17, which is Sankar Dayal Sarma
print(a[1 : 10 : 2]) #prints the chars of string from 1 to 9 with step as 2, which is akrDy
print(a[0 : : 2])#prints chars of string from 0 to 17 with step 2, which is Sna<space>aa<space>am
print(a[1 : : 2])#prints chars of string from 1 to 17 with step2, which is  akrDylsra
print(a[-5 : -1])#prints from -5 to -2 which is sarm
print(a[::-1])#prints chars of string from -1 to -18 which is amraS layaD raknaS
print(a[-1:-5:-1]) #prints chars of string from -1 to -4 which is amra
print(a[ : : -2]) #   a[-1 :  -19 : -2]  --->  string  from  indexes  -1  to  -18  in  steps  of   -2  i.e.  arSlyDrka
print(a[3 : -3]) #prints chars of string from 3 to -4 which is kar Dayal Sa
print(a[2 : -5]) #prints chars of string from 2 to -6 which is nkar<space>Dayal<space>
print(a[-1:-5]) #prints empty string, as step is not given it is taken as 1 and indices goes from -1,0,1...
print(a[3 : 3]) #prints chars of the string from 3 to 2, which is empty string


#   0      1      2      3      4       5       6           7       8       9     10     11     12           13     14       15      16     17
#   S      a      n      k      a       r                    D       a       y      a       l                     S       a         r       m       a
#  -18   -17   -16   -15    -14   -13    -12        -11     -10    -9     -8    -7      -6          -5      -4       -3      -2      -1

#Home Work8
#  Find  outputs  (Home  work)
a =  'A'
print(a[1])#prints the first char of the string which is A
print(a[1:])#prints chars of string from 1 to 0,which is empty string

#Home Work9
# int()  function  demo  program
print(int(10.8))  #  Converts  float   object  10.8  to  int  object  10
print(int(True))  #  Converts  bool   object    True  to  int  object 1
print(int(False)) #converts bool object False to int object 0
print(int('25')) #converts string object to int object which is 25
print(int('0075')) #converts string object to int object which is 75
print(int(0B11010)) #prints the decimal equivalent of the binary number which is 26
print(0B11010) #error, reason this isn't the way of printing int object because chars are involved here
print(int(0O6247)) #prints the decimal equivalent of the octal number which is 3239
print(0O6247)#error, it is treated as int object and involving chars in int object is not allowed
print(int(0XA7B9)) #prints the decimal equivalent of the hexadecimal number which is 42937
print(0XA7B9) #it is treated as int object and involving chars in int object is not allowed
print(int(3 + 4j))#error, complex object cannot be converted to int object
print(int('25.4'))#converts string object to int object which is 25
print(int('Ten'))#error, strings with chars as alphabets cannot be converted to int object



'''
int()  function
----------------
1) What  does  int(x)  do  ?  --->  Converts  object  'x'  to  integer

#Home Work 10
# float()  function  demo  program
print(float(25))  #  Converts  int  object  25  to  float  object   25.0
print(float(True))   #  Converts  bool  object   True   to  float  object   1.0
print(float(False)) #converts bool object False to float object 0.0
print(float('92')) #converts string object to float object which is 92.0
print(float('36.4')) #converts string object to float object which is 36.4
print(float('0075')) #converts string object to float object which is 75.0
print(float(0B1010101)) #converts int object of decimal equivalent of the binary representation to float object which is 75.0
print(float(0O6247)) #converts the int object (decimal representation of octal number) to float object which is 3239.0
print(float(0XA7B9)) #converts the int object (decimal representation of hexadecimal number ) to float object which is 42937.0
print(float(3 + 4j)) #error, cannot convert complex object to float object
print(float('Ten')) #error, cannot convert string object to float which which involves alphabets





'''
float()   function
--------------------
1) What  does  float(x)  do  ?  --->  Converts  object  'x'  to  float

#Home Work 11
# complex()  function  demo  program
print(complex(3 , 4)) #3+4j
print(complex(0 , 4))#0+4j
print(complex(3))#3
print(complex(3.8 , 4.6))#3.8+4.6j
print(complex(3.8))#3.8
print(complex(3 , 4.5))#3+4.5j
print(complex(True , False))#1+0j
print(complex(True))#1
print(complex(False))#0
print(complex(True , 4))#1+4j
print(complex('3'))#3
print(complex('3.8'))#3.8
print(complex(3 , '4'))#error, 2nd component cannot be string
print(complex('3' , 4))#error, if 1st component is string then there shouldn't be 2nd component
print(complex('3' , '4'))#error, if 1st component is string then there shouldn't be 2nd component
print(complex('Ten'))#error, string with alphabets cannot be converted to complex object

#Home Work 12
#  bool()  function  demo  program
print(bool(0)) #   False
print(bool(10)) #   True :  10  is  non-zero
print(bool(-25))# True, -25 is non-zero
print(bool(0.0))#Flase
print(bool(0.1))# True, 0.1 is non-zero
print(bool(0 + 0j))#False, both the components are zero
print(bool(10 + 20j))#True, if either of them is non zero here both are non zero
print(bool(-15j))#True, one of the component is non zero
print(bool('False'))#True, string length is greater than 0
print(bool(''))#False, string length is 0
print(bool('Hyd'))#True, string length is greater than 0
print(bool(' '))#True, string length is greater than 0
print(bool('True'))#True, string length is greater than 0


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

#Home Work 13
# str()  function  demo  program
print(str(25))  #  Converts   25  to  '25'
print(str(10.8))# converts 10.8 to '10.8'
print(str(3 + 4j))# converts 3 + 4j to '3 + 4j'
print(str(True))# converts True to 'True'
print(str(False))# converts False to 'False'
print(str(None))# converts None to 'None'


'''
What  does  str(x)  do ?  --->  Converts  object  'x'  to  string
'''

#Home Work 14
# oct()  function  demo  program
print(oct(195))#prints the octal representation of the 195 which is 303
print(oct(0B10101110010))#prints the octal representation of the 10101110010 which is 2562
print(oct(0xA7B9)) #prints the octal representation of A7B9 which is 123671












'''
oct()  function
-----------------
1) What  does  oct(x)  do ?  --->  Converts  object  'x'  to  octal  number  where
								                    'x'  can  be  binary / decimal / hexa-decimal  number

#Home Work 15
# hex()  function  demo  program
print(hex(25))#prints the hexadecimal representation of 25 which is 19
print(hex(0B1010 1111 010111))#prints the hexadecimal representation of 10101111010111 which is 15D7
print(hex(0O6247))#prints the hexadecimal representation of 6247 which is CA7













'''
hex()  function
------------------
1) What  does  hex(x)  do ?  --->  Converts  object  'x'  to  hexa-decimal  number  where
								                     'x'  can  be  binary / decimal / octal  number