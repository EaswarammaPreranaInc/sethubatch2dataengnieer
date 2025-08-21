1.
a="Rama Rao"
print(a)  #Rama Rao
print(type(a))  #<class 'str'>
print(id(a))  #something like 21132132323 etc which is address of object Rama Rao
b='Hyd'
print(b)  #Hyd
c='''Hyd is green city
Hyd is Hitec city
Hyd is beautiful city'''
print(c) #c is a multi line string which is enclosed between ''', output will be
Hyd is green city
Hyd is Hitec city
Hyd is beautiful city

2.
a='Hyd'
print(How  to  print  'H'  of  object  'a')  #print(a[0])
print(How  to  print  'y'  of  object  'a')  #print(a[1])	
print(How  to  print  'd'  of  object  'a')  #print(a[2])
print(a[3])  #we get error as we don't have any element at a[3] out of range
print(How  to  print  'd'  of  object  'a')  #print(a[-1])
print(How  to  print  'y'  of  object  'a')  #print(a[-2])
print(How  to  print  'H'  of  object  'a')  #print(a[-3])
print(a[-4])  #error as there is no element at -4 in HYD out of range
print(a[0] ==  a[-3])  #True
a[2] = 'c' #a[2] #string is immutable, item assignment is not possible in string
print(25[0])  #error, int is non indexed
print('25'[0]) #25 becomes string as it is enclosed in '', hence output is 2
print(True[1]) #error
print('True'[1]) #True becomes str as it is enclosed in '', o/p is r


3.
a = 'Hyd'
print(a * 3)   #HydHydHyd   sequence*3 gives repeatition, non sequence* does arithmetic operations
print(a * 2)  #HydHyd
print(a * 1)  #Hyd
print(a * 0)  #empty
print(a * -1)  #empty
print(25 * 3)   #75
print('25' * 3)   #252525
print('25' * 4.0)   #error, sequence * non seq type float is error
print(3 * 'Hyd')   #HydHydHyd
print('25' * True)  #25


4.
#  Find  outputs  (Home work)
a = 'Hyd'
print(a , id(a))  #Hyd address of obj Hyd
a = a * 3    #HydHydHyd
print(a , id(a))  #HydHydHyd address of obj HydHydHyd

5.
# len()  function  (Home  work)
print(len('Hyd'))  #3
print(len('Rama Rao')) #8
print(len('9247'))  #4
print(len('')) #0
print(len(' ')) #1
print(len(689))  #int type has no length


6.
a = """"Hyd"""
print(a)   #"Hyd
print(len(a))  #4
print(a[0])  #"
print("""Hyd"""")  #error as we get excess closing quotes
b = """""Hyd"""  
print(b)  #""Hyd
print(len(b))  #5


7.

# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12])  #default step is 1, string from indexes 7 to 11(12-1) in steps of 1  Dayal
print(a[7 : ])  #default step is 1, end is not mentioned(len of str-1  -->18-1-->17)17 in steps of 1  Dayal Sarma
print(a[ : 6])  #default step is 1, default begin 0, end is 6(6-1=5), 0-5 in steps of 1, Sankar
print(a[ : ])  #  a[ 0 :  18  : 1]  --->   string  from  indexes  0  to  17  in  steps  of   1  i.e.  Sankar<space>Dayal<space>Sarma
print(a[:  : ])  #a[0:18:1] ---> string  from  indexes  0  to  17  in  steps  of   1  i.e.  Sankar<space>Dayal<space>Sarma
print(a[1 : 10 : 2])  #start is 1, end is 10, step is 2, psotive step end-1 which is 9, [1:9:2]-->#akrDy
print(a[0 : : 2])   #[0:17:2]--> Sna<space>aa<space>am
print(a[1 : : 2])  #[1:17:2]-->  akrDylSra
print(a[-5 : -1])  #default step is 1[-5:-1-1(-2):1]-->  Sarm
print(a[::-1])  #default step is -1, [-1:-18(-1) -19:-1]    #
print(a[-1:-5:-1])  #[-1:-4:-1]-->amra
print(a[ : : -2]) #   a[-1 :  -19 : -2]  --->  string  from  indexes  -1  to  -18  in  steps  of   -2  i.e.  arSlyDrka
print(a[3 : -3])  #[3:-4:1]-->
print(a[2 : -5])  #[2:-6:1]--> 
print(a[-1:-5])  #[-1:-6:1]==>empty string
print(a[3 : 3])  #[3:2:1]-->empty string as postive step cannot go reverse

8.

a =  'A'
print(a[1])  #error as there is no index a[1]
print(a[1:])  ##empty string indexing throws error but slicing never throws error


9.

# int()  function  demo  program
print(int(10.8))  #  Converts  float   object  10.8  to  int  object  10
print(int(True))  #  Converts  bool   object    True  to  int  object 1
print(int(False))  #0
print(int('25'))   #25
print(int('0075'))  #75
print(int(0B11010))  #26
print(0B11010)  #26
print(int(0O6247))  #6*8**3+2*8**2+4*8**1+7*8**0= 3239
print(0O6247)  #6*8**3+2*8**2+4*8**1+7*8**0= 3239
print(int(0XA7B9))   #10*16^3+7*16^2+11*16^1+9*16^0=42937
print(0XA7B9)  #10*16^3+7*16^2+11*16^1+9*16^0=42937
print(int(3 + 4j))  #error complex cannot be converted to int
print(int('25.4'))  #string float cannot be converted to int
print(int('Ten'))  #error  


10.

# float()  function  demo  program
print(float(25))  #  Converts  int  object  25  to  float  object   25.0
print(float(True))   #  Converts  bool  object   True   to  float  object   1.0
print(float(False))  #0.0
print(float('92'))  #92.0
print(float('36.4'))  #36.4
print(float('0075'))  #75.0
print(float(0B1010101))  #64+16+4+1=85-->85.0
print(float(0O6247))  #3239.0
print(float(0XA7B9))  #42937.0
print(float(3 + 4j))  #error
print(float('Ten')) #error


11.
# complex()  function  demo  program
print(complex(3 , 4))
print(complex(0 , 4))
print(complex(3))
print(complex(3.8 , 4.6))
print(complex(3.8))
print(complex(3 , 4.5))
print(complex(True , False))
print(complex(True))
print(complex(False))
print(complex(True , 4))
print(complex('3'))
print(complex('3.8'))
print(complex(3 , '4'))
print(complex('3' , 4))
print(complex('3' , '4'))
print(complex('Ten'))


