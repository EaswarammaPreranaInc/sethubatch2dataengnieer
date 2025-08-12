# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'} # ref 'a' is assigned to dict obj
print('Dictionary  with  print  function') # print(a)
How  to  print  dictionary  with  print()  function
print('Keys  of  dictionary') # print(a.keys())
How  to  print  each  key  of  dict  'a'
print('Values  of  dictionary') # print(a.values())
How  to  print  each  value  of  dict  'a'
print('All  the  tuples  of  dict_items   object') # print(a.items())
How  to  print  each  tuple  of  the  list  in  dict_items  object
print('Elements  of  each   tuple') # print(*a.items())
How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object
print('Keys  and  values  of  dictionary')
How  to  print  each  key  and  corresponding  value  in  dict  'a'
 # for key, value in a.items():
    print(key, ":", value)


#  Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
	}  # ref 'a' is assigned to set object
print(type(a)) # <class  'set'>
print(a) # none
print(len(a)) # 1


#  Anonymous  object  demo  program
_ = 25 # ref _ is assigned to anonymous function
print(_) # 25
print(type(_)) <class  'int'>
a , _ , c = 10 , 20 , 30 # anonymous object
print(a) # 10
print(_) # 20
print(c) # 30
for  _  in  range(5):
	print(_ , 'Hello') # 0, 1, 2, 3, 4


'''
1) What  is   _   called ?   --->  Anonymous  object  (or) Nameless  object

2) How  many  nameless  objects  can  be  a  program ?  --->  Just  one  (or)  zero

3) What  happens  when  another  nameless  object  is  created ?  --->  Existing  nameless  object  gets  deleted

4) Can  there  be  multiple  nameless  objects  in  a  program ?  --->  No

5) _ = 10
    _ = 20
   What  happens  when  _ = 20  is  executed ?  --->  A  new  nameless  object  is  created  with  value  20  and
																				  old  nameless  object  with  10  is  lost
'''


#  Find  outputs
a = 25 # int class object
print(id(a)) # prints address of obj exp: 1000
a = 35 # int class object
print(id(a)) # prints address of obj where previous addres is deleted


# Find  outputs (Home  work)
a = 25.7 # float class object
print(id(a)) # prints address
print(a) # 25.7
a = 35.6 # float class object
print(id(a)) # previous address is updated with 35.6
print(a) # 35.6
b = True # bool class object
print(id(b)) # prints address of b
b = False # bool class object
print(id(b)) # prints address of previous which is updated with False
c = None # nonetype class object
print(id(c)) # prints address
c = None # nonetype class object
print(id(c)) # prints address 


#  Find  outputs  (Home  work)
a = 'Hyd' # string class object
print(id(a)) # prints address of object
a[1] = 'e' # error
a = 'Sec' # string class object
print(id(a)) # prints address obj new object
b = (10 , 20 , 15 , 18) # tuple class object
print(id(b)) # address of object b
b[2] = 19 # error
b = (30 , 40 , 35 , 32) # tuple class object
print(id(b)) # new address of obj b
c = range(5) # range class object
print(id(c)) # prints address of obj
c[3] = 10 # error because range is immutable
c = range(5) # range class object
print(id(c)) # new address


# Find  outputs  (Home  work)
a = 25 # int obj
b = 25 # int obj
print(a  is  b) # prints True becuse it chechs ref obj
c = 'Hyd' # str obj
d = 'Hyd' # str obj
print(c  is  d) # True
e = False # bool obj
f = False # bool obj
print(e  is  f) # True
g = range(10) # range obj
h = range(10) # range obj
print(g  is  h) # prints True


#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18] # list object 
b = [10 , 20 , 15 , 18] # list object
print(a  is  b) # prints True
c =  {10 : 20, 30 : 40} # dict object
d =  {10 : 20, 30 : 40} # dict object
print(c  is  d) # True
e = (10 , 20 , 15 , 18) # tuple object
f = (10 , 20 , 15 , 18) # tuple object
print(e  is  f) # True 
g = {10 , 20 , 15 , 18} # set object
h = {10 , 20 , 15 , 18} # set object
print(g  is  h) # True

# Find outputs (Home work)
print(10 + 20) # arthematic operator prints 30
print(10.8 + 20.6) # 31.4
print(3 + 4j + 5 + 6j) # (8+10j)
print(True + False) # 1
print('Hyder' + 'abad') # Hyderabad
print('Sankar' + 'Dayal' + 'Sarma') # SankarDayalSarma
print('10' + '20') # 1020
print([10 , 20 , 30] + [1 , 2 , 3]) # [10,20,30,1,2,3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) # (25, 10.8, 'Hyd' , 3+4j, True, None)
print({10 , 20} + {30 , 40}) # {10, 20, 30, 40}
print({10 : 'Hyd'} + {20 : 'Sec'}) # error
print(range(4) + range(5)) # error
print(10 + '20') # error
print([10 , 20 , 30] + 5) # error
print([10 , 20 , 30] + (40 , 50 , 60)) # error


# Find outputs (Home work)
print(25 * 3) # 75
print(10.8 * 25.6) # 276.48
print(True * False) # 0
print((3 + 4j) * (5 + 6j)) # (-9+38j)
print(3 + 4j * 5 + 6j) # (3+26j)
print('25' * 3) # 252525
print(3 * '25') # 252525
print('Hyd' * 4) # HydHydHydHyd
print([10 , 20 , 15] * 2) # [10 , 20 , 15 , 10 , 20 , 15]
print((25, 10.8, 'Hyd', True) * 3) # (25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0) # error
print({10 , 20 , 15} * 2)# error
print({10 : 20 , 30 : 40} * 2) # error
print([10] * [20]) # [10,20]


#  /  operator  demo  program
print(9.0 / 2) # 4.5
print(9 / 2.0) # 4.5
print(9.0 / 2.0) # 4.5
print(9 / 2)  #  4.5
print(10.5 / 2) # 5.25
print(10 / 3) # 3.33
print(10 / 2) # 5.0


'''
What  does  /  operator  do  ?  --->  Peforms  division   and  returns  float  quotient
'''

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



'''
//  operator
--------------
1) What  does  //  operator do ?  --->  Same  as  /  operator  but  returns  previous  integer  of  /  result

2) What  is  the  result  of  integer // integer ?  --->  Integer  quotient
    What  is  the  result  of  integer // float ?  ---> Float  quotient  with  .0
    What  is  the  result  of  float // integer ?  ---> Float  quotient  with  .0
    What  is  the  result  of  float // float ?  ---> Float  quotient  with  .0

3) What  is  the  result  of  integer / integer ?  ---> Float  quotient
    What  is  the  result  of  integer / float ?  ---> Float  quotient
    What  is  the  result  of  float / integer ?  ---> Float  quotient
    What  is  the  result  of  float / float ?  ---> Float  quotient

4) When  is  the  result  of  //  operator  integer ?  ---> When  both  the  operands  are  integers
    When  is  the  result  of   //  operator  float  with  .0 ?  ---> When  at  least  one  operand  is  float
'''


# % operator demo program
print(9 % 5) # 4
print(9.0 % 5) # 4.0
print(9 % 5.0) # 4.0
print(9.0 % 5.0) # 4.0
print(10.5 % 2)  # 0.5
print(8.9 % 3) # 2.9


'''
%   operator
---------------
1) What  does  %  operator  do ?  ---> Performs  division  and  returns  remainder

2) When  is  the  result  of  %  operator  integer ?  ---> When  both  the  operands  are  integers
    When  is  the  result  of  %  operator  float ?  ---> When  at  least  one  operand  is  float
'''


# Find outputs
print(7 / 0) # error
print(7 // 0)# error
print(7 % 0) # error


# ** operator demo program
print(3 ** 4) # 81
print(10 ** -2) # 0.01
print(4 ** 3 ** 2) #262144
print(3 + 4 * 5 - 32 / 2 ** 3) #19.0




'''
**  operator
---------------
1) What  is  **  operator  called ?  --->  Exponential  operator

2) What  is  the  result  of  a ** b ?  ---> a ^ b

3) What  is  the  result  of  a ** b  ** c ?   --->  a ^ b ^ c

4) What  is  the  associativity  of  **  operator ?  ---> Right  to  left
    What  is  the  associativity  of  remaining  arithmetic  operators ?  ---> Left  to  right


#  Relational  operators  demo  program (Home  work)
print(9 >= 5)  #   True :  >  is  satisfied
print(9 >= 9)   #   True :  =  is  satisfied
print(9 >= 12)   #  False :  Both  are  not  satisfied
print(6 <= 8) # True
print(6 <= 6) # True
print(6 <= 4) # False
print(9 != 7) # True
print(6 == 8) # False
print(True  >  False) # True
print(3 + 4j == 3 + 4j) # True
print(3 + 4j == 5 + 6j) # false
print(3 + 4j != 5 + 6j) # True
print(10 == 10.0) # True
print(3 + 4j >  3 + 4j) # error


'''
1) Can  complex  numbers   be  compared ?   ---> Yes  with  ==  and  !=

2) When  can  complex  numbers   be  not  compared  ?  ---> Wiith  > , <  , >=  and  <=
'''


#  Find  outputs  (Home  work)
print('Rama'   >  'Rajesh')  #   True :  'm' > 'j'
print('Rama'  <  'Sita') #  True : 'R' < 'S'
print('Hyd'  ==  'Hyd') # True
print('Rama'  <=   'Ramana') # true
print('Rama  Rao'  >=  'Rama') # True
print('Hyd'  != 'Sec') # true
print('HYD'  <   'hyd') # False


'''
1) Can  strings  be  compared  with  > ,  < , == ,  >= , <=  and  != ?  --->  Yes  only  in  python  but  not  in  other  languages

2) What  are  compared  internally  when  strings  are  compared ? --->  1st  non-matching  characters

3) Are  characters  compared  (or)  their  unicode  values ?  --->  Unicode  values

4) How  many  unicode  values  exist ?  ---> 512

5) What  is  the  range  of  unicode  values ?  ---> 0  to  511

6) What  are  the  unicode  values  of  'A'  to  'Z'  ?  ---> 65  to  90
     What  are  the  unicode  values  of  'a'  to   'z'  ?  --->  97  to  122
     What  are  the  unicode  values  of   '0'  to  '9' ?  ---> 48  to  57
     What  is  the  unicode  value  of   '$' ?  --->  36
     What  is  the  unicode  value  of  space ?  ---> 32

7) What  is  another  name  of  unicode ?  --->  Extended  Ascii (American  standard  code  for  information  and  interchange)
'''

# Chaining  relational  opeartors  (Home work)
print(10 < 20 < 30)  #   True
print(10 >= 20 < 30)  #   False : 10  is  not  >= 20
print(10 < 20 > 30) # false
print(1 < 2 < 3 < 4) # true
print(1 < 2 > 3 > 1) # false
print(4 > 3 >= 3 > 2) # true


#  or  operator  demo program
print(True  or  False) #  True
print(False  or  True) #   True
print(True  or  True) #  True
print(False  or   False)   #  False
print(10  or  20)#  10
print(0   or  20)  #  20
print(-25  or  0) # -25
print(''  or  35) # 35
print(6j  or  'Hyd') # 6j
print(0.0  or  3 + 4j) # 3 + 4j
print('Hyd'   or   10.8) # Hyd


'''
or  operator
--------------
1) When  is  the  result  of  or  operator  True ?  ---> When  at  least  one  operand  is  True
    When  is  the  result  of  or  operator  False ?  ---> When  both  the  operands  are  False

2) What  is  the  result  of  op1  or  op2  when  op1  is  False ?  ---> op2
    What  is  the  result  of  op1  or  op2  when  op1  is  True ?  ---> op1

3) and ,  or  operators  are  quite  opposite
'''


# not  operator  demo  program
print(not  True) #   False
print(not  False) #  True
print(not  25) # False
print(not  0) # true
print(not  'Hyd') # False
print(not  '') # true
print(not  -10) # false
print(not  not  'Hyd') # error


'''
not  operator
----------------
1) What  does  not  operator  do ?  ---> Complement  operation

2) Is  not  a  unary  operator  ?  ---> Yes  due  to  single  operand
    What  about  and ,  or ? ---> Binary  operators  due  to  two  operands

3) What  is  the  associativity  of  unary  operators ?  --->  Right  to  Left
    What  is  the  associativity  of  binary  operators ?  --->  Left  to  Right  except  for  **
'''


#  Find   outputs (Home work)
i = 10 # int obj
i = not  i > 14 # 
print(i) True
print(not(6 < 4  or  9 >= 5  and  6 != 6)) # True