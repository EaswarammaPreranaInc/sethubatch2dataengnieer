#  Find  outputs  (Home  work)
a = "Rama Rao" # REF a points to object i.e "Rama Rao"
print(a) # Rama Rao 
print(type(a)) # <class str">
print(id(a)) # address of object "Rama Rao"
b = 'Hyd'  # ref b points to object i.e 'Hyd'
print(b) # Hyd 
c = '''Hyd is green city.  #multi line string 
Hyd is hitec city.
Hyd is beautiful city.'''
print(c) # Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.



# Index   demo  program  (Home  work)
a = 'Hyd' #ref a points to object hyd 
print(How  to  print  'H'  of  object  'a') # print('Hyd'[0])
print(How  to  print  'y'  of  object  'a') # print('Hyd'[1])
print(How  to  print  'd'  of  object  'a') # print('Hyd'[2])
print(a[3])  # error index value not assigned 
print(How  to  print  'd'  of  object  'a')  # print('Hyd'[-1])
print(How  to  print  'y'  of  object  'a')  # print('Hyd'[-2])
print(How  to  print  'H'  of  object  'a')  # print('Hyd'[-3])
print(a[-4]) # error due to no value is there 
print(a[0] ==  a[-3]) # true i.e is H == H 
a[2] = 'c' # d cannot be replaced because str is immutable object 
print(25[0]) # error due to non sequence int cannot be indexed 
print('25'[0]) # str can be indexed i.e 2 
print(True[1]) # error bool cannot be indexed 
print('True'[1]) # str can be indexed i.e r 



#  Find  outputs  (Home work)
a = 'Hyd'  # ref a points to object hyd
print(a * 3) # hydhydhyd
print(a * 2) # hydhyd
print(a * 1) # hyd
print(a * 0) # empty str
print(a * -1) # string repeats -1 times i.e empty string
print(25 * 3)  # 75
print('25' * 3) # 252525
print('25' * 4.0) # error due to float operand 
print(3 * 'Hyd') # hydhydhyd
print('25' * True) # repaeats string ones that is str



#  Find  outputs  (Home work)
a = 'Hyd' # ref a points to object hyd
print(a , id(a)) #value of object a i.e hyd , address of object i.e is <class 'str'>
a = a * 3 # hydhydhyd i.e means reference a is modified to the new string element ,
and object is not modified because str is immutable 
print(a , id(a)) # value of object a i.e hyd , address of object i.e is <class 'str'>


# len()  function  (Home  work)
print(len('Hyd')) # 3
print(len('Rama Rao')) # 8 
print(len('9247')) #4
print(len('')) # 0 due to empty str 
print(len(' ')) # 1 empty space 
print(len(689)) # error argument should be sequence but here 689 is not a sequence 



# Find  outputs  (Home  work)
a = """"Hyd""" # EXCESS OPENING QUOTE IS CHARACTERS OF THE STRING 
print(a) # "Hyd 
print(len(a))  # length of a I.E 4
print(a[0]) # "
print("""Hyd"""") # ERROR DUE TO EXCESS CLOSING STR
b = """""Hyd"""    # HERE EXCESS OPENING OF STRING 
print(b)  # ""HYD
print(len(b)) # 5 




# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12])  # start from 7 to 11 objects that are dayal 
print(a[7 : ])   # start from  7 to end of the string i.e dayal sarma 
print(a[ : 6])   # character of object from sankar
print(a[ : ])  #  a[ 0 :  18  : 1]  --->   string  from  indexes  0  to  17  in  steps  of   1  i.e.  Sankar<space>Dayal<space>Sarma
print(a[:  : ]) # a[0:18:1] ---> string from indexes length in  steps of 1 
print(a[1 : 10 : 2]) # strings from indexes 0 to 9 in steps of 2 i.e  akr<space>dy
print(a[0 : : 2]) # strings from indexes 0 to 17 in steps of 2 i.e 
print(a[1 : : 2])
print(a[-5 : -1])
print(a[::-1])
print(a[-1:-5:-1])
print(a[ : : -2]) #   a[-1 :  -19 : -2]  --->  string  from  indexes  -1  to  -18  in  steps  of   -2  i.e.  arSlyDrka
print(a[3 : -3])
print(a[2 : -5])
print(a[-1:-5])
print(a[3 : 3])


#   0      1      2      3      4       5       6           7       8       9     10     11     12          13     14       15      16     17
#   S      a      n      k      a       r                   D       a       y      a       l                S       a         r       m     a
#   -18    -17    -16    -15    -14     -13     -12         -11   -10     -9       -8      -7    -6         -5      -4        -3      -2    -1 

















