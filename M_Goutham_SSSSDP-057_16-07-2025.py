#Day-2 #Home Work-1
#  Find  outputs  (Home  work)

a = "Rama Rao" #Here a is assigned to string object "Rama Rao"
print(a) #Returns the string object "Rama Rao"
print(type(a)) #Returns the type of object i,e <class 'str'>
print(id(a)) #Returns the address of string object
b = 'Hyd' #Here also b is assigned to string object 'Hyd'
print(b) #Returns the string object i,e 'Hyd'
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.''' #It is a multiline string using triple codes(''') and yes it is valid 
print(c) #Returns the entire 3 lines string

#Day-2 #Home Work-2
#Index   demo  program  (Home  work)

a = 'Hyd' #Here we are assigning string object 'Hyd' to reference a
#print(How  to  print  'H'  of  object  'a') #By using indexing i,e 
print(a[0])
#print(How  to  print  'y'  of  object  'a') #By using indexing i,e a[1]
#print(How  to  print  'd'  of  object  'a') #By using indexing i,e a[2]
print(a[3]) #Gives the error because indexes for string hyd is 0,1,2 and we are accessing the 3 it gives string out of range error
#print(How  to  print  'd'  of  object  'a') #By using negative indexing we can print 'd' i.e 
print(a[-1])
#print(How  to  print  'y'  of  object  'a') #By using negative indexing we can print 'y' i,e 
print(a[-2])
#print(How  to  print  'H'  of  object  'a') #By using negative indexing we can print 'h' i,e 
print(a[-3])
print(a[-4]) #Gives the error because negative indexes for string 'hyd' is -1,-2,-3 and we are accessing the -4 it gives string out of range error
print(a[0] ==  a[-3]) #We are using compare operator so it returns the bool object i,e a[0] is 'H' and a[-3] is also 'H' it returns True
a[2] = 'c' #As we know string is a sequence type and it is immutable so we cannot modify the string it gives you an error
print(25[0]) #It gives you an error beacuse we are using integer which is non sequence object type
print('25'[0]) #Return the 2 as we are giving 25 in single codes so it takes as string an accessing index 0 so it gives 2
print(True[1]) #It gives you an error as we are using bool object
print('True'[1]) #Returns the r as we are specifying the True in '' so it takes that as string object

#Day-2 #Home Work-3
#  Find  outputs  (Home work)

a = 'Hyd' #Here we are assigning reference a to string object 'Hyd'
print(a * 3) #Returns the string object 'Hyd' 3 times as single string i,e 'HydHydHyd' # '*' is used to for String repeatations
print(a * 2) #Returns the string object 'Hyd' 2 times as single string i,e 'HydHyd'
print(a * 1) #Returns the string object 'Hyd' 1 times as single string i,e 'Hyd'
print(a * 0) #Returns the empty string 
print(a * -1) #Returns the empty string
print(25 * 3) #Returns the 75 as we are multiplying the int object
print('25' * 3) #Returns the string object '25' 3 times i,e '252525'
print('25' * 4.0) #Returns an error that we cannot multiply string with float
print(3 * 'Hyd') #Returns the string object 'Hyd' 3 times i,e 'HydHydHyd'
print('25' * True) #As we know that True is equal to 1 and here we are multiplying string object '25' with 1 i,e Bool object True(1) so we get 25

#Day-2 #Home Work-4
# Find  outputs  (Home work)

a = 'Hyd' #Here we are assigning string object 'Hyd' to reference a
print(a , id(a)) #Returns the Hyd and it's Address 
a = a * 3 #Here we are multiplying string object 'Hyd' with 3 
print(a , id(a)) #Returns the string object 'Hyd'*3 = HydHydHyd and returns the different address

#Day-2 #Home Work-5
# len()  function  (Home  work)

print(len('Hyd')) #Returns the length of string object 'Hyd' i,e 3
print(len('Rama Rao')) #Returns the length of string object 'Rama Rao' i,e 8
print(len('9247')) #Returns the length of string object '9247' i,e 4
print(len('')) #Returns the length of string object '' i,e 0
print(len(' ')) #Returns the length of string object '<space>' i,e 1
print(len(689)) #Returns an error that int is a non-sequence which holds only 1 element so there is no length for int

#Day-2 #Home Work-6
# Find  outputs  (Home  work)

a = """"Hyd""" #Here we are assigning a to string object "Hyd i,e """"Hyd"""
print(a) #Returns the "Hyd as it takes equal codes from left and right and remaining as string if correctly specified
print(len(a)) #Returns 4 as it takes " also a character in the string "Hyd
print(a[0]) #Return " as index 0
#print("""Hyd"""") #Returns an error that string is incomplete it is considering """") also a string object so it is expecting a " and )
b = """""Hyd""" #Returns the ""Hyd as it is enclosing the string in """string"""
print(b) #Returns string object ""Hyd
print(len(b)) #Returns the length of the string ""Hyd i,e 5


# Find  outputs
a = 'Sankar Dayal Sarma'  #Here we are assigning reference a to string object 'Sankar Dayal Sarma'
print(a[7 : 12]) #Returns the new string 'Dayal' as we are giving starting index from 7 and ending index 12 (12-1) and default step will be 1
print(a[7 : ]) #Returns the new string 'Dayal sarma' we are giving starting index as 7 to and by default it takes end as stringlength and step as 1
print(a[ : 6]) #Returns the new string 'Sankar' we are giving end index as 6(6-1) and by default it takes start as 0 and step as 1 
print(a[ : ])  #  a[ 0 :  18  : 1]  --->   string  from  indexes  0  to  17  in  steps  of   1  i.e.  Sankar<space>Dayal<space>Sarma
print(a[:  : ]) #Returns the entire string i,e 'Sankar Dayal sarma' as it takes default a[ 0 : strlen : 1 ]
print(a[1 : 10 : 2]) #Returns the new string as 'akrdy' as we are giving start as 1 and end will be 10(10-1) and step as 2
print(a[0 : : 2]) #Returns the new string as 'Sna<space>aa<space>am' as we are giving the start as 0 and end will be default i,e stringlength and step 2
print(a[1 : : 2]) #Returns the new string as 'akrDylSra' as we are giving the start as 1 and end will be default i,e stringlength and step 2
print(a[-5 : -1]) #Returns the new string as 'Sarm' as we are giving the start as -5 and end as -1 and step default -1
print(a[::-1]) #Returns the reverse of a string as default it takes start as -1 and end as -len-1 and step is -1 i,e 'amraS layaD raknaS'
print(a[-1:-5:-1]) #Returns the new string as 'amra' as it starts from -1 and end with -5(-4) and step will be -1
print(a[ : : -2]) #   a[-1 :  -19 : -2]  --->  string  from  indexes  -1  to  -18  in  steps  of   -2  i.e.  arSlyDrka
print(a[3 : -3]) #Returns a new string i,e 'kar<space>Dayal<space>Sa' as the starting is 3 and end is -3 and step will be deafault 1
print(a[2 : -5]) #Returns a new string i,e 'nkar<space>Dayal<space>' as the starting string is 2 and end will be -5 and step will be default 1
print(a[-1:-5]) #Returns an empty string because the default step will be always 1 so here start is -1 and stop is -5 but -5 is behind -1 but we are going forward so it gives an empty string
print(a[3 : 3]) #Returns an empty string as you are giving start as 3 and end as 3 so it starts from 3 and ends at 3 same place so it gives empty


#   0      1      2      3      4       5       6           7       8       9     10     11     12           13     14       15      16     17
#   S      a      n      k      a       r                    D       a       y      a       l                     S       a         r       m       a
#  -18   -17   -16   -15    -14   -13    -12        -11     -10    -9     -8    -7      -6          -5      -4       -3      -2      -1


#  Find  outputs  (Home  work)

a =  'A' #Here we are referencing a to string object 'A'
print(a[1]) #Returns an error as we are accessing the index which is not their it gives index out of Range
print(a[1:]) #Returns empty string as we are starting from index 1 but we have only index 0'

#Day-2 #Home work-9
# int()  function  demo  program
print(int(10.8))  #  Converts  float   object  10.8  to  int  object  10
print(int(True))  #  Converts  bool   object    True  to  int  object 1
print(int(False)) # Converts the bool object false to int object 0
print(int('25')) # Converts the string object '25' to int object 25
print(int('0075')) #Converts the string object '0075' to int object 0075
print(int(0B11010)) #Converts the binary number 0B11010 to decimal integer 26 
print(0B11010) #Returns the decimal equivalent of binary number i,e 26 
print(int(0O6247)) #Converts the octal number i,e 0O6247 into decimal integer i,e 3239
print(0O6247) #Returns the decimal equivalent of octal number i,e 3239
print(int(0XA7B9)) #Converts the hexa-decimal number into integer i,e 42937
print(0XA7B9) #Returns the decimal equivalent of the hexa-decimal number i,e 42937
print(int(3 + 4j)) #We will get an error that we cannot convert the complex to int
print(int('25.4')) #We wull get an error that float string cannot be converted to int obj
print(int('Ten')) #We will get an error that string obj 'Ten' cannot be converted to int obj as it contains characters



'''
int()  function
----------------
1) What  does  int(x)  do  ?  --->  Converts  object  'x'  to  integer



# int()  function  demo  program
print(int(10.8))  #  Converts  float   object  10.8  to  int  object  10
print(int(True))  #  Converts  bool   object    True  to  int  object 1
print(int(False)) # Converts the bool object false to int object 0
print(int('25')) # Converts the string object '25' to int object 25
print(int('0075')) #Converts the string object '0075' to int object 0075
print(int(0B11010)) #Converts the binary number 0B11010 to decimal integer 26 
print(0B11010) #Returns the decimal equivalent of binary number i,e 26 
print(int(0O6247)) #Converts the octal number i,e 0O6247 into decimal integer i,e 3239
print(0O6247) #Returns the decimal equivalent of octal number i,e 3239
print(int(0XA7B9)) #Converts the hexa-decimal number into integer i,e 42937
print(0XA7B9) #Returns the decimal equivalent of the hexa-decimal number i,e 42937
print(int(3 + 4j)) #We will get an error that we cannot convert the complex to int
print(int('25.4')) #We wull get an error that float string cannot be converted to int obj
print(int('Ten')) #We will get an error that string obj 'Ten' cannot be converted to int obj as it contains characters
'''



'''
int()  function
----------------
1) What  does  int(x)  do  ?  --->  Converts  object  'x'  to  integer
'''
# complex()  function  demo  program

print(complex(3 , 4)) #Converts the int to complex i,e 3+4j
print(complex(0 , 4)) #Converts the int to complex i,e 0+4j
print(complex(3)) #Converts the int to complex i,e 3+0j
print(complex(3.8 , 4.6)) #Converts the float object into complex i,e 3.8+4.6j
print(complex(3.8)) #Converts the float object into complex i,e 3.8+0j
print(complex(3 , 4.5)) #Converts the int and float obj into complex i,e 3+4.5j
print(complex(True , False)) #Converts the bool objects into complex i,e 1+0j
print(complex(True)) #Converts the bool object into complex i,e 1+0j
print(complex(False)) #Converts the bool object into complex i,e 0j
print(complex(True , 4)) #Converts the bool and int objects into complex i,e 1+4j
print(complex('3')) #Converts the string obj into complex object i,e 3+0j
print(complex('3.8')) #Converts the float string object into complex obj i,e 3.8+0j 
print(complex(3 , '4')) #We will get an error that second number should not be a string to convert complex
print(complex('3' , 4)) #We will get an error that first number should not be a string to convert into complex
print(complex('3' , '4')) #We will get the same error it stops at the 1st number and says it is string
print(complex('Ten')) #Error #Character string cannot be converted into complex


#  bool()  function  demo  program
print(bool(0)) #   False
print(bool(10)) #   True :  10  is  non-zero
print(bool(-25)) # True : -25 is non-zero
print(bool(0.0)) #False : 0.0 is zero
print(bool(0.1)) #True : 0.1 is non-zero
print(bool(0 + 0j)) #False : because it is 0
print(bool(10 + 20j)) #True : it is non-zero
print(bool(-15j)) #True : it is non-zero
print(bool('False')) #True : String is non-empty
print(bool('')) #False : string is empty
print(bool('Hyd')) #True : string is non-empty
print(bool(' ')) #True : string is non-empty it is consists of space
print(bool('True')) #True : string is non-empty


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
print(str(10.8)) #Converts the float obj 10.8 to string obj '10.8'
print(str(3 + 4j)) #Converts the complex obj 3+4j to string obj 3+4j
print(str(True)) #Returns the True 
print(str(False)) #Returns the False
print(str(None)) #Returns None


'''
What  does  str(x)  do ?  --->  Converts  object  'x'  to  string
'''


# oct()  function  demo  program
print(oct(195)) #Converts the int obj into octal number i,e 0o303
print(oct(0B10101110010)) #converts the Binary to octal i,e 2562
print(oct(0xA7B9)) #Converts the hexa-decimal into octal i,e 0o123671


'''
oct()  function
-----------------
1) What  does  oct(x)  do ?  --->  Converts  object  'x'  to  octal  number  where
								                    'x'  can  be  binary / decimal / hexa-decimal  number


# hex()  function  demo  program
print(hex(25)) #Converts the int obj into Hexa-decimal i,e 0X19
print(hex(0B10101111010111)) #Converts the Binary obj into Hexa-decimal number i,e 0X2BD7
print(hex(0O6247)) #Converts the octal obj into Hexa-decimal number i,e 0xcac7

'''
'''
hex()  function
------------------
1) What  does  hex(x)  do ?  --->  Converts  object  'x'  to  hexa-decimal  number  where
								                     'x'  can  be  binary / decimal / octal  number

'''
