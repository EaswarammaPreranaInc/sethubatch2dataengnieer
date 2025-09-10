# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) # prints dictionary i.e., {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
for k in a.keys():
    print(k) # prints all the keys in the dictionary i.e., 10<nextline>20<nextline>15<nextline>18
for v in a.values():
    print(v) # prints all the values in the dictionary i.e., Ramesh<nextline>Kiran<nextline>Amar<nextline>Sita
for i in a.items():
    print(i) # prints each tuple of the listin dict_items object i.e., (10, 'Ramesh')<nextline>(20, 'Kiran')<nextline>(15, 'Amar')<nextline>(18, 'Sita')
for k, v in a.items():
    print(k, v) # prints elements of each tuple in the list of dict_items i.e., 10 Ramesh<nextline>20 Kiran<nextline>15 Amar<necxtline>18 Sita
for key in a:
    print("Key:", key, "Value:", a[key]) # prints each key and  corresponding value  in  dict  'a' i.e., Key: 10 Value: Ramesh<nextline>Key: 20 Value: Kiran<nextline>Key: 15 Value: Amar<nextline>Key: 18 Value: Sita



#  Find  outputs (Home  work)
a = {
		print('Hyd') , 
		print('Sec') , 
		print('Cyb')   
	}                     # prints set of None i.e., {None}
print(type(a))  # prints <class 'set'>
print(a)  # prints set 'a' i.e. {None}
print(len(a)) # prints number of elements in the set 'a' i.e., 1



#  Anonymous  object  demo  program
_ = 25
print(_) # prints object _ i.e., 25
print(type(_)) # prints type of _ i.e., <class 'int'>
a , _ , c = 10 , 20 , 30 # multiple assignment
print(a) # prints 10
print(_) # prints 20
print(c) # prints 30
for  _  in  range(5):
	print(_ , 'Hello') # 0 Hello<next line>1 Hello<next line>2 Hello<next line>3 Hello<next line>4 Hello<nextline>



#  Find  outputs
a = 25 # Ref 'a' points to int object 25
print(id(a)) # prints address of object 25
a = 35  # Ref 'a' is modified and points to object 35
print(id(a)) # prints new address of object 'a'



# Find  outputs (Home  work)
a = 25.7 # ref 'a' points to float object 25.7
print(id(a)) # prints the address of float object 
print(a) # prints float object 'a' i.e., 25.7
a = 35.6 # ref 'a' is modified and points to float object 35.6
print(id(a)) # prints new address of float object 'a'
print(a) # prints float object 'a' i.e., 35.6
b = True # ref 'b' points to bool object True
print(id(b)) # prints address of bool object True
b = False  # ref 'b' is modified and points to bool object False
print(id(b)) # prints new address of object False
c = None # ref 'c' points to  object None
print(id(c)) # prints address of object None
c = None  # ref points to same NoneType object None 
print(id(c))# prints same address of object None



#  Find  outputs  (Home  work)
a = 'Hyd' # ref 'a' points to object 'Hyd'
print(id(a)) # prints address of object 'Hyd'
a[1] = 'e' # Error because string is immutable 
a = 'Sec' # ref 'a' points to new object 'Sec'
print(id(a)) # prints new address of object 'a'
b = (10 , 20 , 15 , 18) # Ref 'b' points to tuple of 4 elements
print(id(b)) # prints address of the tuple 'b' 
b[2] = 19 # Error because tuple is immutable 
b = (30 , 40 , 35 , 32) # ref 'b' is modified and points to new tuple
print(id(b)) # prints address of the new tuple
c = range(5) # ref 'c' points to range object
print(id(c)) # prints address of range object 'c'
c[3] = 10 # Error because range object is immutable
c = range(5) # ref 'c' is modified  and points to new range object
print(id(c)) # prints address of new range object



# Find  outputs  (Home  work)
a = 25 # ref 'a' points to int object 25
b = 25 # ref 'b' also points to same int object 25
print(a  is  b) # prints True because a = 25 and b = 25 and same address
c = 'Hyd' # ref 'c' points to str object 'Hyd'
d = 'Hyd' # ref 'd' also points to same str object 'Hyd'
print(c  is  d) # prints True because c = 'Hyd' and d = 'Hyd' and same address
e = False # ref 'e' points to bool object False
f = False # ref 'f' also points to same bool object False
print(e  is  f) # prints True because e = False and f = False and same address
g = range(10) # ref 'g' points to range object from 0 to 9
h = range(10) # ref 'h' points to another range object from 0 to 9
print(g is h) # False, because address of both objects is different even though values are same



#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18] # ref 'a' points to list
b = [10 , 20 , 15 , 18] # ref 'b' points to another list
print(a  is  b) # False because both have different address
c =  {10 : 20, 30 : 40} # ref 'c' points to dictionary
d =  {10 : 20, 30 : 40} # ref 'd' points to another dictionary
print(c  is  d) # False because both have different address
e = (10 , 20 , 15 , 18) # ref 'e' points to tuple
f = (10 , 20 , 15 , 18) # ref 'f' points to same tuple
print(e  is  f)  # True because both have same address
g = {10 , 20 , 15 , 18} # ref 'g' points to set
h = {10 , 20 , 15 , 18} # ref 'h' points to another tuple
print(g is h) # False because both have different address



# Find outputs (Home work)
print(10 + 20) # prints 30
print(10.8 + 20.6) # prints 31.4
print(3 + 4j + 5 + 6j) # prints (8 + 10j)
print(True + False) # prints 1 because True is treated as 1 and False is treated as 0
print('Hyder' + 'abad')  # concatenates the string and prints 'Hyderabad'
print('Sankar' + 'Dayal' + 'Sarma') # concatenates the string and prints 'SankarDayalSarma
print('10' + '20') # concatenates the strings and prints '1020'
print([10 , 20 , 30] + [1 , 2 , 3]) # concatenates the lists and prints [10, 20, 30, 1, 2, 3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) # concatenates the tuples and prints '(25, 10.8, 'Hyd', (3 + 4j), True, None)
print({10 , 20} + {30 , 40}) # Error because sets cannot be added 
print({10 : 'Hyd'} + {20 : 'Sec'}) # Error because dictionaries cannot be added
print(range(4) + range(5)) # Error because range cannot be added
print(10 + '20') # # Error because int and str cannot be added
print([10 , 20 , 30] + 5) # Error because list and int cannot be added
print([10 , 20 , 30] + (40 , 50 , 60)) # Error because list and tuple cannot be added



# Find outputs (Home work)
print(25 * 3) # 25 is multiplied with 3 and prints 75
print(10.8 * 25.6) # 10.8 is multiplied with 25.6 and prints 276.48
print(True * False) # True is treated as 1 and False is treated as o and prints 0
print((3 + 4j) * (5 + 6j)) # Error because complex object cannot be multiplied
print(3 + 4j * 5 + 6j) # Error because complex object cannot be multiplied
print('25' * 3) # when an str object multiplied with int object then str object is repeated and prints '252525'
print(3 * '25') # when an str object multiplied with int object then str object is repeated and prints '252525'
print('Hyd' * 4) # 'Hyd' repeats 4 times i.e., 'HydHydHydHyd'
print([10 , 20 , 15] * 2) # list repeats twice i.e., [10, 20, 15, 10, 20, 15]
print((25, 10.8, 'Hyd', True) * 3) # Tuple repeats thrice i.e., (25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0) # Error because list cannot be multiplied with float object,only int object is allowed
print({10 , 20 , 15} * 2) # Error because set cannot allow duplicates, so it cannot be allowed
print({10 : 20 , 30 : 40} * 2) # Error because dictionary cannot have duplicates, so it cannot be allowed
print([10] * [20]) # Error because sequence cannot be multiplied by set,it can only multiplied by int type object



#  /  operator  demo  program
print(9.0 / 2) # prints 4.5
print(9 / 2.0) # prints 4.5
print(9.0 / 2.0) # prints 4.5
print(9 / 2)  # prints 4.5
print(10.5 / 2) # prints 5.25
print(10 / 3) # prints 3.33
print(10 / 2) # prints 5.0



#  //  operator  demo  program
print(9 // 2)  #   prints previous integer of (4.5) i.e., 4
print(9.0 // 2) # prints previous integer of (4.5) i.e., 4.0
print(9 // 2.0) # prints previous integer of (4.5) i.e., 4.0
print(9.0 // 2.0) # prints previous integer of (4.5) i.e., 4.0
print(10.5 // 2) # prints previous integer of (5.25) i.e., 5.0
print(10 // 3) # prints previous integer of (3.33) i.e., 3
print(10.0 // 3) # prints previous integer of (3.33) i.e., 3.0
print(8.5 // 3) # prints previous integer of (2.83) i.e., 2.0
print(18 // 4) # prints previous integer of (4.45) i.e., 4
print(-18 // 4) # prints previous integer of (4.45) i.e., -4
print(-(18 // 4)) # prints previous integer of (4.45) i.e., -4



#  //  operator  demo  program
print(9 // 2)  #   prints previous integer of (4.5) i.e., 4
print(9.0 // 2) # prints previous integer of (4.5) i.e., 4.0
print(9 // 2.0) # prints previous integer of (4.5) i.e., 4.0
print(9.0 // 2.0) # prints previous integer of (4.5) i.e., 4.0
print(10.5 // 2) # prints previous integer of (5.25) i.e., 5.0
print(10 // 3) # prints previous integer of (3.33) i.e., 3
print(10.0 // 3) # prints previous integer of (3.33) i.e., 3.0
print(8.5 // 3) # prints previous integer of (2.83) i.e., 2.0
print(18 // 4) # prints previous integer of (4.45) i.e., 4
print(-18 // 4) # prints previous integer of (4.45) i.e., -4
print(-(18 // 4)) # prints previous integer of (4.45) i.e., -4



# Find outputs
print(7 / 0) # Error because division by zero is not possible
print(7 // 0) # Error because division by zero is not possible
print(7 % 0) #Error because modulo by zero is not possible



# ** operator demo program
print(3 ** 4) # 3 power of 4, prints 81
print(10 ** -2) # 10 power of -2,prints 0.01
print(4 ** 3 ** 2) # first evaluates 3 power 2,i.e., 9 and 4 power 9 i.e., 262144
print(3 + 4 * 5 - 32 / 2 ** 3) # first evaluates 2 power 3 i.e., 8,next evaluates 32/2 i.e., 4.0,next evaluates 4*5 i.e., 20 and 3 + 20 - 4.0 i.e., 19.0



#  Relational  operators  demo  program (Home  work)
print(9 >= 5) # True :  >  is  satisfied
print(9 >= 9) # True : =  is  satisfied
print(9 >= 12) # False : Both  are  not  satisfied
print(6 <= 8) # True : < is satisfied
print(6 <= 6) # True : = is satisfied
print(6 <= 4) # False : Both are not satisfied 
print(9 != 7) # True : Both are not satisfied
print(6 == 8) # False : Both are not satisfied
print(True  >  False) # True : > is satisfied
print(3 + 4j == 3 + 4j) # True : == is satisfied
print(3 + 4j == 5 + 6j) # False : == is not satisfied
print(3 + 4j != 5 + 6j) # True : != is not satisfied
print(10 == 10.0) # True : == is satisfied
print(3 + 4j >  3 + 4j) # Error because > is not supported complex



#  Find  outputs  (Home  work)
print('Rama'   >  'Rajesh')  #   True :  'm' > 'j'
print('Rama'  <  'Sita') #  True : 'R' < 'S'
print('Hyd'  ==  'Hyd') # True : 'Hyd' == 'Hyd'
print('Rama'  <=   'Ramana') # True : '' <= 'n'
print('Rama  Rao'  >=  'Rama') # True : ' ' >= ''
print('Hyd'  != 'Sec') # True : 'H' != 'S'
print('HYD'  <   'hyd') # True : 'HYD' < 'Hyd'



# Chaining  relational  opeartors  (Home work)
print(10 < 20 < 30) # True :10 is < 20 and 20 is < 30
print(10 >= 20 < 30) # False : 10  is  not  >= 20
print(10 < 20 > 30) # False : 10 is < 20 but 20 is not > 30
print(1 < 2 < 3 < 4) # True : 1 is < 2, 2 is < 3 and 3 is < 4
print(1 < 2 > 3 > 1) # False : 1 is < 2 and 2 is not > 3 
print(4 > 3 >= 3 > 2) # True : 4 is > 3, 3 is >= 3 and 3 is > 2



#  or  operator  demo program
print(True  or  False) # prints True
print(False  or  True) # prints True
print(True  or  True) # prints True
print(False  or   False)   # prints False
print(10  or  20) #  prints 10
print(0   or  20)  # prints 20
print(-25  or  0) # prints -25
print(''  or  35) # prints 35
print(6j  or  'Hyd') # prints 6j
print(0.0  or  3 + 4j) # prints (3 + 4j)
print('Hyd'   or   10.8) # prints 'Hyd'



# not  operator  demo  program
print(not  True) # prints False
print(not  False) # prints True
print(not  25) # prints False
print(not  0) # prints True
print(not  'Hyd') # prints False
print(not  '') # prints True
print(not  -10) # prints False
print(not  not  'Hyd') # prints True



#  Find   outputs (Home work)
i = 10 
i = not  i > 14 
print(i) # prints True because i is 10 and here not 10 is > 14
print(not(6 < 4  or  9 >= 5 and 6 != 6)) # prints True 