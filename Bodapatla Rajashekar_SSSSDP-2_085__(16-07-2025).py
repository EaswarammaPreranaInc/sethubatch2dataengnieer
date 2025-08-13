#  Find  outputs 
a = "Rama Rao"
print(a)#prints string Rama Rao
print(type(a))#prints the object type = string
print(id(a))#prints the address or id of the object
b = 'Hyd'
print(b)#prints string Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c)#prints thriple line string of c 
# Index   demo  program  (Home  work)
a = 'Hyd'
print(How  to  print  'H'  of  object  'a')#string[0]=a[0]
print(How  to  print  'y'  of  object  'a')#a[1]
print(How  to  print  'd'  of  object  'a')#a[2]
print(a[3])#error because the index not in the range
print(How  to  print  'd'  of  object  'a')#a[-1]
print(How  to  print  'y'  of  object  'a')#a[-2]
print(How  to  print  'H'  of  object  'a')#a[-3]
print(a[-4])#error because the index not in the range
print(a[0] ==  a[-3])#returns True because a[0] index-value and a[-3] index-value is same.i.e,H
a[2] = 'c'#error because string cannot be modified because it is immutable
print(25[0])#error because int is immutable and non sequence 
print('25'[0])#returns 2 because method to access element of string is string[index-number]
print(True[1])#error because bool object only contains true and false keywords and non sequence.
print('True'[1])#returns 'r' as Output.
#  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3)#output : 'HydHydHyd' /because string*int repeats the string in same line.
print(a * 2)#output : 'HydHyd' /because string*int repeats the string in same line.
print(a * 1)#output : 'Hyd'
print(a * 0)#doesnot return anything because the string is 0 times mutltiplied in prints nothing
print(a * -1)#doesnot return anything because the string is -1 times mutltiplied in prints nothing
print(25 * 3)#75 
print('25' * 3)#'252525'because 25 is in string format
print('25' * 4.0)#erroe because only string can be multiplied with number but not with float 
print(3 * 'Hyd')#output : 'HydHydHyd' /because string*int repeats the string in same line.
print('25' * True)#ouput = 25 / 25*1=25 True value is 1 and string is repeated only once and prints..
#  Find  outputs  (Home work)
a = 'Hyd'
print(a , id(a))#Prints 'Hyd' and address of a.
a = a * 3
print(a , id(a))#prints 'HydHydHyd' and address of modified new string a
# len()  function  (Home  work)
print(len('Hyd'))#prints length of the string = 3
print(len('Rama Rao'))#prints length of the string = 8
print(len('9247'))#prints length of the string = 4
print(len(''))#prints length of the string = 0
print(len(' '))#prints length of the string = 1
print(len(689))#error because length method doesnot support for non sequence or immutable objects.
# Find  outputs  (Home  work)
a = """"Hyd"""
print(a)#Prints the object of a
print(len(a))#prints the len of a =3
print(a[0])# prints H
print("""Hyd"""") #error because closed quotes are not equal to open quotes.
b = """""Hyd""" #
print(b)#as the three double quotes are equal extra 2 double quotes are treated as string enclosed 
print(len(b))#prints the len of a =5
# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12])#prints Dayal as output because startstep is 7 and end step is -1 that is 12-1 =11 .
print(a[7 : ])#prints Dayal Sarma
print(a[ : 6])#prints sankar 6-1=5.
print(a[ : ])  #  a[ 0 :  18  : 1]  --->   string  from  indexes  0  to  17  in  steps  of   1  i.e.  Sankar<space>Dayal<space>Sarma
print(a[:  : ])#prints wholestring as ouput.
print(a[1 : 10 : 2])#ouput: akrDy as new string with step 2 and index runs till index number no 9 from string step as 1.
print(a[0 : : 2])#akrDylSra as ouput till end with two steps as the end is not specified
print(a[1 : : 2])##akrDylSra as ouput till end with two steps as the end is not specified
print(a[-5 : -1])#prints Sarm -len-1=end step
print(a[::-1])#prints reverse of the string
print(a[-1:-5:-1])#prints amra
print(a[ : : -2]) #   a[-1 :  -19 : -2]  --->  string  from  indexes  -1  to  -18  in  steps  of   -2  i.e.  arSlyDrka
print(a[3 : -3])#output as :kar Dayal Sa
print(a[2 : -5])#ouput as nkar Dayal
print(a[-1:-5])#output as:amra
print(a[3 : 3]) #no output because the step size start and end point are sAME
a =  'A'
print(a[1])#error because string length is 1 
print(a[1:])#produces no ouput because index 1 is not present
# int()  function  demo  program
print(int(10.8))  #  Converts  float   object  10.8  to  int  object  10
print(int(True))  #  Converts  bool   object    True  to  int  object 1
print(int(False))#  Converts  bool   object    True  to  int  object 0
print(int('25'))#  Converts  string   object    25  to  int  object 25
print(int('0075'))#  Converts  string   object    0075  to  int  object 0075
print(int(0B11010))#  Converts  binary number   object   to  int  decimal equivalent 26
print(0B11010) #prints decimal equivalent 3239
print(int(0O6247))#prints decimal equivalent 3247
print(0O6247)#prints decimal equivalent 3247
print(int(0XA7B9))#prints decimal equivalent 42937
print(0XA7B9)#prints decimal equivalent 42937
print(int(3 + 4j))#prints float equivalent 3.0+4.0j
print(int('25.4'))#prints float equivalent 25.4
print(int('Ten'))#error because string Ten is not keyword
#  bool()  function  demo  program
print(bool(0)) #   False
print(bool(10)) #   True :  10  is  non-zero
print(bool(-25))#   True :  -25  is  non-zero
print(bool(0.0))#   False
print(bool(0.1))#   True :  0.1  is  non-zero
print(bool(0 + 0j))#   False because img or real number atleast 1 should be non zero 
print(bool(10 + 20j))#   True :  10 + 20j  is  non-zero
print(bool(-15j))# #   True :  -15j  is  non-zero  
print(bool('False'))#string means it has some value so returns true
print(bool(''))#   False inside there is no element so assumed as o length
print(bool('Hyd'))#string means it has some value so returns true
print(bool(' '))#string means it has some value so returns true
print(bool('True'))#string means it has some value so returns true
print(str(25))  #  Converts   25  to  '25'
print(str(10.8))#  Converts   10.8  to  '10.8'
print(str(3 + 4j))#  Converts   3 +4j  to  3+4j everything is assumed as string after conversion
print(str(True))#  Converts   True  to  string object 'True'
print(str(False))#  Converts   True  to  string object 'False'
print(str(None))#  Converts   True  to  string object 'None'
# oct()  function  demo  program
print(oct(195))#ouput is 0o303
print(oct(0B10101110010))#output is 0o2652
print(oct(0xA7B9))#output is 0X123671
# hex()  function  demo  program
print(hex(25))#output is : 0x19 
print(hex(0B10101111010111))#output is : 0x15F7
print(hex(0O6247))#output is : 0xca7