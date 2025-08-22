a = "Rama Rao" # stores the string obj rama rao in reference a
print(a) #prints the object stored in a i.e rama rao
print(type(a)) #print the type of object a i.e class str
print(id(a)) #prints the address of the object a
b = 'Hyd' # stores the string obj hyd in reference b
print(b) #prints the object stored in a i.e hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.''' #stores the multi line string in the reference c
print(c) # prints the multi line string

a = 'Hyd' # stores the string obj hyd in reference a
print(How  to  print  'H'  of  object  'a') #by using index h is in 1st position so we use index 0 i.e a[0]
print(How  to  print  'y'  of  object  'a') # y is second letter so a[1]
print(How  to  print  'd'  of  object  'a') # a[2]
print(a[3]) #error because we can access only 3 elemnts in a i.e index should not be >2
print(How  to  print  'd'  of  object  'a') #now we are accessing from back so index will be negative a[-1]
print(How  to  print  'y'  of  object  'a') # 2nd letter from end so a[-2]
print(How  to  print  'H'  of  object  'a') #3rd letter from end so a[-3]
print(a[-4]) #error because we have only 3 elemnts in a so max index should be -3
print(a[0] ==  a[-3]) #compares the 0th element from start and -3 element from end as both are same prints true
a[2] = 'c' # error because string is immutable
print(25[0]) # error because class int has single element indexing elements is not possible
print('25'[0]) # prints 2 because 25 is a string and oth element of 25 is 2
print(True[1]) #error because class bool has single element indexing elements is not possible
print('True'[1]) # prints r because True is a string and 1st element of True is r

a = 'Hyd' # stores the string obj hyd in reference a
print(a * 3) # Repeats the string hyd 3 times 
print(a * 2) # Repeats the hyd 2 times
print(a * 1) # repeat the string 1 time
print(a * 0) # repeat the string hyd 0 time
print(a * -1) # returns the empty string 
print(25 * 3) # as 25 is int so it multiplies 25 3 times
print('25' * 3) # 25 is a string so repates 3 times as a single character
print('25' * 4.0) # error because repeatition can done only with int numbers
print(3 * 'Hyd') # Repeats the string hyd 3 times 
print('25'*True) # as we have operation here true acts as 1 so 25 is repeated 1 time

a = 'Hyd' #assigns string object hyd to a
print(a , id(a)) #prints the object in a ansd its adress
a = a * 3 # repeats the a string into 3 times and assigns it to a 
print(a,id(a)) #prints the updated a and its id

print(len('Hyd')) # len means length of a string so it prints the number of characters in string
print(len('Rama Rao')) # counts the characters in string
print(len('9247')) # as 9247 is a string so it counts the number of characters
print(len('')) # lenght of empty string is 0
print(len(' ')) # there is space as string so length 1
print(len(689)) # 689 is not a string len function is applicable to string

a = """"Hyd"""  #assigns string to a
print(a) # it consider intial 3 quote and ending quotes as """ """ so it prints "Hyd
print(len(a)) # as a contains 4 chars so len is 4
print(a[0]) # 1st letter of the string is "
print("""Hyd"""") # error because string is considered between triple quotes and one quote is remaining so syntax error
b = """""Hyd""" #assigns string to b
print(b)  # it consider intial 3 quote and ending quotes as """ """ so it prints ""Hyd
print(len(b)) # as a contains 5 chars so len is 5

a = 'Sankar Dayal Sarma' #stores sankar dayal sarma into a 
print(a[7 : 12]) # string  from  indexes  7  to  11  in  steps  of   1 i.e Dayal
print(a[7 : ]) # string  from  indexes  7  to  end of string  in  steps  of   1 i.e dayal sarma 
print(a[ : 6]) #string  from  indexes  0  to  5  in  steps  of   1 i.e sankar
print(a[ : ])  #  a[ 0 :  18  : 1]  --->   string  from  indexes  0  to  17  in  steps  of   1  i.e.  Sankar<space>Dayal<space>Sarma
print(a[:  : ]) # it takes default values 0 to end in steps of 1 so prints the entire string
print(a[1 : 10 : 2]) #string  from  indexes  1  to  9  in  steps  of   2 i.e akrDy
print(a[0 : : 2]) #string  from  indexes  0  to  end   in  steps  of   2
print(a[1 : : 2]) #string  from  indexes  1  to  end  in  steps  of   2
print(a[-5 : -1]) #string  from  indexes  -5  to    -2
print(a[::-1]) #string  from  indexes  end i.e -1  to  start i.e -15  in  steps  of   -1
print(a[-1:-5:-1]) #string  from  indexes  -1  to  -6  in  steps  of   -1
print(a[ : : -2]) #   a[-1 :  -19 : -2]  --->  string  from  indexes  -1  to  -18  in  steps  of   -2  i.e.  arSlyDrka
print(a[3 : -3]) # string from indexes 3 to 14 in steps of 1, i.e. kar Dayal Sa
print(a[2 : -5]) #string from indexes 2 to 12 in steps of 1, i.e. nkar Dayal
print(a[-1:-5])  #string from indexes -1 to -4 in steps of +1 so empty string
print(a[3 : 3]) #string from index 3 to 3 so empty

a =  'A' #assigns A to a
print(a[1]) # error because only one element so we can acces max index is 0
print(a[1:]) # starting from 1 tor end so empty string

print(int(10.8))  #  Converts  float   object  10.8  to  int  object  10
print(int(True))  #  Converts  bool   object    True  to  int  object 1
print(int(False)) #  Converts  bool   object    True  to  int  object 0
print(int('25')) #  Converts  string   object    25  to  int  object 25
print(int('0075')) #  Converts string   object    0075  to  int  object 75
print(int(0B11010)) #  Converts  binary   object 0B11010 to  int  object 26
print(0B11010) #prints the decimal equalent of the binary number i.e 26
print(int(0O6247))  #  Converts  octal object 0O6247 to  int  object  3239
print(0O6247) #prints the decimal equalent of the octal number i.e 3239
print(int(0XA7B9)) #  Converts  hexa decimal object 0XA7B9 to  int  object  42937
print(0XA7B9) #prints the decimal equalent of the hexa decimal number 42397
print(int(3 + 4j)) #error as complex cannot be converted to int
print(int('25.4')) #error as string cannot be converted to int
print(int('Ten')) #error as string cannot be converted to int

print(float(25))  #  Converts  int  object  25  to  float  object   25.0
print(float(True))   #  Converts  bool  object   True   to  float  object   1.0
print(float(False)) #  Converts  bool  object   False   to  float  object   0.0
print(float('92'))#  Converts  int  object   to  float  object   92.0
print(float('36.4')) #  Converts  float  object    to  float  object  
print(float('0075')) #  Converts  int  object   to  float  object   75.0
print(float(0B1010101)) #  Converts  binary  0B1010101   to  float  object    (internal decimal equalent to float) 
print(float(0O6247)) #  Converts octal 0O6247  to  float  object    (internal decimal equalent to float) 
print(float(0XA7B9)) #  Converts hexa decimal 0XA7B9  to  float  object    (internal decimal equalent to float) 
print(float(3 + 4j))  #error as complex cannot be converted to int
print(float('Ten')) #error as string cannot be converted to float

print(complex(3 , 4)) #converts int to complex obj considering 3 as real and 4 as imag
print(complex(0 , 4)) #converts int to complex obj considering 0 as real and 4 as imag
print(complex(3)) #converts int to complex obj considering 3 as real and 0 as imag
print(complex(3.8 , 4.6)) #converts float to complex obj considering 3.8 as real and 4.6 as imag
print(complex(3.8)) #converts float to complex obj considering 3.8 as real and 0 as imag
print(complex(3 , 4.5)) #converts int and float to complex obj considering 3 as real and 4.5 as imag
print(complex(True , False)) #converts bool to complex obj considering true (1) as real and false(0) as imag
print(complex(True)) #converts bool to complex obj considering true (1) as real and false(0) as imag
print(complex(False))#converts bool to complex obj considering false (0) as real and (0) as imag
print(complex(True , 4)) #converts bool and int to complex obj considering true (1) as real and 4 as imag
print(complex('3'))#converts string to complex obj considering '3' as real and 0 as imag
print(complex('3.8')) #converts string to complex obj considering '3.8' as real and 0 as imag
print(complex(3 , '4')) #error because imag should not be complex
print(complex('3' , 4)) #error because if real aprt is string imag should not be there
print(complex('3' , '4')) #error because if real aprt is string imag should not be there
print(complex('Ten')) #error because complex cant take string

print(bool(0)) #   False
print(bool(10)) #   True :  10  is  non-zero
print(bool(-25)) #   True :  -25  is  non-zero
print(bool(0.0)) #false because 0
print(bool(0.1)) #  True :  0.1 is  non-zero
print(bool(0 + 0j)) #false because 0
print(bool(10 + 20j)) #  True :  10+20j is  non-zero
print(bool(-15j)) #  True :  -15j is  non-zero
print(bool('False')) #  True :  'false' is  non-empty
print(bool('')) #false as empty string is there
print(bool('Hyd')) #  True :  'hyd' is  non-empty string
print(bool(' ')) #  True :  '<space>' is  non-empty
print(bool('True')) #  True :  'true' is  non-empty

print(str(25))  #  Converts   25  to  '25'
print(str(10.8)) #converts 10.8 float to '10.8'
print(str(3 + 4j))  #converts 3+4j complex to '3+4j'
print(str(True)) #converts True bool to 'True'
print(str(False)) #converts False bool to 'False'
print(str(None)) #converts None Nonetype to 'None'

print(oct(195)) #converts decimal 195 to octal
print(oct(0B10101110010)) #converts decimal equalent of binary to octal
print(oct(0xA7B9)) #converts decimal equalent of hexa decimal to octal

print(hex(25)) #converts decimal 25 to hexa decimal
print(hex(0B10101111010111)) #converts decimal equalent of binary to hexa decimal
print(hex(0O6247)) #converts decimal equalent of octal to hexa decimal