# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) # o/p: {10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}

#How  to  print  dictionary  with  print()  function
print(a.keys()) # o/p: dict_keys([10, 20, 15, 18])

#How  to  print  each  key  of  dict  'a'
print(a.values()) # o/p: dict_values(['Ramesh', 'Kiran', 'Amar', 'Sita'])

#How  to  print  each  value  of  dict  'a'
print(a.items()) # o/p: dict_items([(10, 'Ramesh'), (20, 'Kiran'), (15, 'Amar'), (18, 'Sita')])

#How  to  print  each  tuple  of  the  list  in  dict_items  object
print(list(a.items())) # o/p: [(10, 'Ramesh'), (20, 'Kiran'), (15, 'Amar'), (18, 'Sita')]

#How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object
for key, value in a.items():
    print(key, value)  # o/p: 10 Ramesh <nextline> 20 Kiran <nextline> 15 Amar <nextline> 18 Sita

#How  to  print  each  key  and  corresponding  value  in  dict  'a'
for key in a:
    print(key, a[key])  # o/p: 10 Ramesh <nextline> 20 Kiran <nextline> 15 Amar <nextline> 18 Sita

#  Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
	}  # print() returns None, so the set will contain None
print(type(a)) # o/p: <class 'set'>
print(a) # o/p: {None} : set contains only one element None
print(len(a)) # o/p: 1 : length of set 'a' is 1

#  Anonymous  object  demo  program
_ = 25 # assigns 25 to the _
print(_)# 25
print(type(_)) # <class 'int'>
a , _ , c = 10 , 20 , 30
print(a) # 10
print(_) # 20
print(c) # 30
for  _  in  range(5):
	print(_ , 'Hello') # o/p: 0 Hello <nextline> 1 Hello <nextline> 2 Hello <nextline> 3 Hello <nextline> 4 Hello
     
#  Find  outputs
a = 25
print(id(a)) # prints the memory address of the object 25
a = 35
print(id(a)) # prints the memory address of the object 35

# Find  outputs (Home  work)
a = 25.7 # reference 'a' points to float object 25.7
print(id(a)) # prints the address of the object 25.7
print(a) # 25.7
a = 35.6 # 'a' is reassigned to a new float object 35.6 and pvm deletes object 25.7
print(id(a)) # prints the address of the object 35.6
print(a) # 35.6
b = True # reference 'b' points to bool object True
print(id(b)) # prints the address of the object True
b = False # 'b' is reassigned to a new bool object False and pvm deletes object True
print(id(b))  # prints the address of the object False
c = None # reference 'c' points to None object
print(id(c)) # prints the address of the None object
c = None 
print(id(c)) # prints the address of the None object (same as above)

#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a)) # prints the address of the object 'Hyd'
#a[1] = 'e' #Typeerror: strings are immutable
a = 'Sec'
print(id(a)) # prints the address of the object 'Sec' (new object created)
b = (10 , 20 , 15 , 18) # reference 'b' points to tuple object (10, 20, 15, 18)
print(id(b)) # prints the address of the tuple object (10, 20, 15, 18)
#b[2] = 19 # TypeError: tuples are immutable
b = (30 , 40 , 35 , 32) # 'b' is reassigned to a new tuple object (30, 40, 35, 32) and pvm deletes the old tuple object
print(id(b)) # prints the address of the new tuple object (30, 40, 35, 32)
c = range(5) # reference 'c' points to range object range(0,5,1)
print(id(c)) # prints the address of the range object range(0,5,1)
#c[3] = 10 # error: range object is immutable
c = range(5) # 'c' is reassigned to range(5)
print(id(c)) # prints the address of the range object range(5)

# Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b) # True: both a and b refer to the same object 25
c = 'Hyd'
d = 'Hyd'
print(c  is  d) # True: both c and d refer to the same string object 'Hyd'
e = False
f = False
print(e  is  f) # True: both e and f refer to the same bool object False
g = range(10)
h = range(10)
print(g  is  h) # False: g and h are different range objects 


#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b) # False: a and b are different list objects
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d) # False: dict's are mutable
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f) # true: tuples are immutable
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h) # False: sets are mutable

# Find outputs (Home work)
print(10 + 20) # 30
print(10.8 + 20.6) # 31.4
print(3 + 4j + 5 + 6j) # (8+10j)
print(True + False) # 1
print('Hyder' + 'abad') # 'Hyderabad'
print('Sankar' + 'Dayal' + 'Sarma') # 'SankarDayalSarma'
print('10' + '20') # '1020'
print([10 , 20 , 30] + [1 , 2 , 3]) # [10, 20, 30, 1, 2, 3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) # (25, 10.8, 'Hyd', (3+4j), True, None)
#print({10 , 20} + {30 , 40}) # error : + operator is not defined for sets
#print({10 : 'Hyd'} + {20 : 'Sec'}) # error : + operator is not defined for dicts
#print(range(4) + range(5)) # error : to concatenate range we have to convert them to list
#print(10 + '20')# error
#print([10 , 20 , 30] + 5) #error
#print([10 , 20 , 30] + (40 , 50 , 60)) # error: + operator is not defined for list and tuple

# Find outputs (Home work)
print(25 * 3) # 75
print(10.8 * 25.6) # 276.48
print(True * False) # 0
print((3 + 4j) * (5 + 6j)) # (-9+38j)
print(3 + 4j * 5 + 6j) # (3+26j)
print('25' * 3) # 252525
print(3 * '25') # 252525
print('Hyd' * 4) # HydHydHydHyd
print([10 , 20 , 15] * 2) # [10, 20, 15, 10, 20, 15]
print((25, 10.8, 'Hyd', True) * 3) # (25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True)
#print([10 , 20 , 15] * 3.0) # error: cannot repeat list with float
#print({10 , 20 , 15} * 2) # error: cannot repeat set
#print({10 : 20 , 30 : 40} * 2) # error: cannot repeat dict
#print([10] * [20]) # error: cannot repeat list with another list

#  /  operator  demo  program
print(9.0 / 2) # 4.5
print(9 / 2.0) # 4.5
print(9.0 / 2.0) # 4.5
print(9 / 2)  #  4.5
print(10.5 / 2) # 5.25
print(10 / 3) # 3.333333
print(10 / 2) # 5.0

#  //  operator  demo  program
print(9 // 2)  #   prev  integer  of (4.5) = 4
print(9.0 // 2) # 4.0
print(9 // 2.0) # 4.0
print(9.0 // 2.0) # 4.0
print(10.5 // 2) # 5.0
print(10 // 3) # 3
print(10.0 // 3)  #    prev  integer  of  3.33 = 3.0
print(8.5 // 3) # 2.0
print(18 // 4) # 4
print(-18 // 4) # -5
print(-(18 // 4)) # -4


 # % operator demo program
print(9 % 5) # 4
print(9.0 % 5)  # 4.0
print(9 % 5.0)  # 4.0
print(9.0 % 5.0)    # 4.0
print(10.5 % 2)  #   0.5
print(8.9 % 3)  # 2.9

# Find outputs
#print(7 / 0) # ZeroDivisionError: division by zero
#print(7 // 0) # ZeroDivisionError
#print(7 % 0) # ZeroDivisionError

# ** operator demo program
print(3 ** 4) # 81
print(10 ** -2) # 0.01
print(4 ** 3 ** 2) # 262144 :evaluates from right to left: 4 ** (3 ** 2) = 4 ** 9 = 262144
print(3 + 4 * 5 - 32 / 2 ** 3) # 3 + 20 - 4 = 19.0

#  Relational  operators  demo  program (Home  work)
print(9 >= 5)  #   True :  >  is  satisfied
print(9 >= 9)   #   True :  =  is  satisfied
print(9 >= 12)   #  False :  Both  are  not  satisfied
print(6 <= 8) # True :  <  is  satisfied
print(6 <= 6)   # True :  =  is  satisfied
print(6 <= 4) # False :  Both  are  not  satisfied
print(9 != 7) # True :  !=  is  satisfied
print(6 == 8) # False :  =  is  not  satisfied
print(True  >  False) # True :  True  is  greater  than  False
print(3 + 4j == 3 + 4j) # True : both are equal
print(3 + 4j == 5 + 6j) # False :  both  are  not  equal
print(3 + 4j != 5 + 6j) # True : both are not equal
print(10 == 10.0) # True :  int  and  float  are  equal
#print(3 + 4j >  3 + 4j) # error: cannot compare complex numbers with <, >, <=, >=

#  Find  outputs  (Home  work)
print('Rama'   >  'Rajesh')  #   True :  'm' > 'j'
print('Rama'  <  'Sita') #  True : 'R' < 'S'
print('Hyd'  ==  'Hyd') # True 
print('Rama'  <=   'Ramana') # True : 'R' < 'R'
print('Rama  Rao'  >=  'Rama') # True : 'R' = 'R'
print('Hyd'  != 'Sec') # True : 'Hyd' is not equal to 'Sec'
print('HYD'  <   'hyd') # True : unicode of 'H' < 'h'

# Chaining  relational  opeartors  (Home work)
print(10 < 20 < 30)  #   True
print(10 >= 20 < 30)  #   False : 10  is  not  >= 20
print(10 < 20 > 30) # False : 20  is  not  > 30
print(1 < 2 < 3 < 4) # True 
print(1 < 2 > 3 > 1) # False : 2 > 3 is not satisfied
print(4 > 3 >= 3 > 2) # True 

#  or  operator  demo program
print(True  or  False) #  True
print(False  or  True) #   True
print(True  or  True) #  True
print(False  or   False)   #  False
print(10  or  20)#  10
print(0   or  20)  #  20
print(-25  or  0) # -25
print(''  or  35) #  35
print(6j  or  'Hyd') #  6j
print(0.0  or  3 + 4j) # (3+4j)
print('Hyd'   or   10.8) # 'Hyd'

# not  operator  demo  program
print(not  True) #   False
print(not  False) #  True
print(not  25) # False : 25 is non-zero
print(not  0) # True : 0 is zero
print(not  'Hyd') # False : 'Hyd' is non-empty string
print(not  '') # True : '' is empty string
print(not  -10) # False : -10 is non-zero
print(not  not  'Hyd') # True : not 'Hyd' is False, so not False is True

#  Find   outputs (Home work)
i = 10
i = not  i > 14 # true: i > 14 = False, not False = True
print(i) # 10 > 14 = False, not False =True
print(not(6 < 4  or  9 >= 5  and  6 != 6)) # True



