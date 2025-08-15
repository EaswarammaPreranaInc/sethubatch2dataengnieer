#Home Work-1
# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) #'Dictionary  with  print  function')
How  to  print  dictionary  with  print()  function
print(a.keys())# 'Keys  of  dictionary')
How  to  print  each  key  of  dict  'a'
for x in a.keys():
    print(x)
print(a.values()) #'Values  of  dictionary')
How  to  print  each  value  of  dict  'a'
for x in a.values():
    print(x)
print(a.items()) #'All  the  tuples  of  dict_items   object')

How  to  print  each  tuple  of  the  list  in  dict_items  object
for x in a.items():
    print(x)
print('Elements  of  each   tuple')
How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object
print('Keys  and  values  of  dictionary')
How  to  print  each  key  and  corresponding  value  in  dict  'a'
for x in a.items():
    print(x[0],x[1])

#Home Work-2
#  Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
	}
print(type(a)) #<class 'set'>
print(a) #{
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
	}
print(len(a)) #3

#Home Work-3
#  Anonymous  object  demo  program
_ = 25
print(_) #25
print(type(_)) #<class 'anonymous'>
a , _ , c = 10 , 20 , 30
print(a) #10
print(_) #20
print(c) #30
for  _  in  range(5):
	print(_ , 'Hello')
# 0 Hello <new line> 1 Hello <new line> 2 Hello <new line> 3 Hello <new line> 4 Hello

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

#Home Work-4
#  Find  outputs
a = 25
print(id(a)) #4000, say the address of integer object 25 be 4000
a = 35
print(id(a)) #4001, say the address of integer object 35 be 40001

#Home Work-5
# Find  outputs (Home  work)
a = 25.7 #say address as 5000
print(id(a)) #5000
print(a) #25.7
a = 35.6 #say address be 5001
print(id(a)) #5001
print(a) #35.6
b = True #say address be 5002
print(id(b)) #5002
b = False #say address be 5003
print(id(b)) #5003
c = None #say address be 5004
print(id(c)) #5004
c = None 
print(id(c)) #5004

#Home Work-6
#  Find  outputs  (Home  work)
a = 'Hyd' #add: 6001
print(id(a)) #6001
a[1] = 'e' #error
a = 'Sec' #say add :6002
print(id(a)) #6002
b = (10 , 20 , 15 , 18) #say add 6003
print(id(b)) #6003
b[2] = 19 #error
b = (30 , 40 , 35 , 32) #say add: 6004
print(id(b)) #6004
c = range(5) #say add : 6005
print(id(c)) #6005
c[3] = 10 #error
c = range(5) #say add: 6006
print(id(c)) #6006

#Home Work-7
# Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b) #True
c = 'Hyd' 
d = 'Hyd'
print(c  is  d) #True
e = False 
f = False
print(e  is  f) #True
g = range(10)
h = range(10)
print(g  is  h) #False


#Home Work-8
#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b) #False
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d) #false
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f) #true
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h) #false

#Home Work -9
# Find outputs (Home work)
print(10 + 20) #30
print(10.8 + 20.6) #31.4
print(3 + 4j + 5 + 6j) #8+10j
print(True + False) #1
print('Hyder' + 'abad') #Hyderabad
print('Sankar' + 'Dayal' + 'Sarma') #SankarDatalSarma
print('10' + '20')#1020
print([10 , 20 , 30] + [1 , 2 , 3])#[10,20,30,1,2,3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) #(25 , 10.8 , 'Hyd', 3 + 4j , True , None)
print({10 , 20} + {30 , 40}) #{10,20,30,40}
print({10 : 'Hyd'} + {20 : 'Sec'}) #{10 : 'Hyd', 20 : 'Sec'}
print(range(4) + range(5)) #range(9)
print(10 + '20') #error
print([10 , 20 , 30] + 5)#error
print([10 , 20 , 30] + (40 , 50 , 60))#error

#Home Work-10
# Find outputs (Home work)
print(25 * 3)#75
print(10.8 * 25.6)#276.48
print(True * False)#0
print((3 + 4j) * (5 + 6j))#error
print(3 + 4j * 5 + 6j)#3+26j
print('25' * 3)#252525
print(3 * '25')#252525
print('Hyd' * 4)#HydHydHydHyd
print([10 , 20 , 15] * 2) #[10 , 20 , 15, 10 , 20 , 15, 10 , 20 , 15]
print((25, 10.8, 'Hyd', True) * 3) #(25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0) #error
print({10 , 20 , 15} * 2)#error
print({10 : 20 , 30 : 40} * 2)#error
print([10] * [20]) #error

#Home Work-11
#  /  operator  demo  program
print(9.0 / 2)#4.5
print(9 / 2.0)#4.5
print(9.0 / 2.0)#4.5
print(9 / 2)  #  4.5
print(10.5 / 2)#5.25
print(10 / 3)#3.3333
print(10 / 2)#5


'''
What  does  /  operator  do  ?  --->  Peforms  division   and  returns  float  quotient
'''

#Home Work-12
#  //  operator  demo  program
print(9 // 2)  #   prev  integer  of (4.5) = 4
print(9.0 // 2)#4.0
print(9 // 2.0)#4.0
print(9.0 // 2.0)#4.0
print(10.5 // 2)#5.0
print(10 // 3)#3
print(10.0 // 3)  #    prev  integer  of  3.33 = 3.0
print(8.5 // 3)#2.0
print(18 // 4)#4
print(-18 // 4)#-4
print(-(18 // 4))#-4



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

#Home Work-13
# % operator demo program
print(9 % 5) #4
print(9.0 % 5)#4.0
print(9 % 5.0)#4.0
print(9.0 % 5.0)#4.0
print(10.5 % 2)  #   0.5
print(8.9 % 3)#2.9


'''
%   operator
---------------
1) What  does  %  operator  do ?  ---> Performs  division  and  returns  remainder

2) When  is  the  result  of  %  operator  integer ?  ---> When  both  the  operands  are  integers
    When  is  the  result  of  %  operator  float ?  ---> When  at  least  one  operand  is  float
'''

#Home Work-14
# Find outputs
print(7 / 0) #error
print(7 // 0) #error
print(7 % 0) #error

#Home Work-15
# ** operator demo program
print(3 ** 4) #81
print(10 ** -2) #0.01
print(4 ** 3 ** 2)#262144
print(3 + 4 * 5 - 32 / 2 ** 3) #(3+20-32/8) -> (23-4) -> 19.0




'''
**  operator
---------------
1) What  is  **  operator  called ?  --->  Exponential  operator

2) What  is  the  result  of  a ** b ?  ---> a ^ b

3) What  is  the  result  of  a ** b  ** c ?   --->  a ^ b ^ c

4) What  is  the  associativity  of  **  operator ?  ---> Right  to  left
    What  is  the  associativity  of  remaining  arithmetic  operators ?  ---> Left  to  right

#Home Work-16
#  Relational  operators  demo  program (Home  work)
print(9 >= 5)  #   True :  >  is  satisfied
print(9 >= 9)   #   True :  =  is  satisfied
print(9 >= 12)   #  False :  Both  are  not  satisfied
print(6 <= 8) #True
print(6 <= 6) #True
print(6 <= 4) #False
print(9 != 7) #True
print(6 == 8) #False
print(True  >  False) #True
print(3 + 4j == 3 + 4j) #True
print(3 + 4j == 5 + 6j) #False
print(3 + 4j != 5 + 6j) #True
print(10 == 10.0) #True
print(3 + 4j >  3 + 4j) #error


'''
1) Can  complex  numbers   be  compared ?   ---> Yes  with  ==  and  !=

2) When  can  complex  numbers   be  not  compared  ?  ---> Wiith  > , <  , >=  and  <=
'''

#Home Work-17
#  Find  outputs  (Home  work)
print('Rama'   >  'Rajesh')  #   True :  'm' > 'j'
print('Rama'  <  'Sita') #  True : 'R' < 'S'
print('Hyd'  ==  'Hyd') #True
print('Rama'  <=   'Ramana') #True
print('Rama  Rao'  >=  'Rama') #True
print('Hyd'  != 'Sec') #True
print('HYD'  <   'hyd') #True


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

#Home Work-18
# Chaining  relational  opeartors  (Home work)
print(10 < 20 < 30)  #   True
print(10 >= 20 < 30)  #   False : 10  is  not  >= 20
print(10 < 20 > 30) #False
print(1 < 2 < 3 < 4) #True
print(1 < 2 > 3 > 1) #False
print(4 > 3 >= 3 > 2) #True

#Home Work-19
#  or  operator  demo program
print(True  or  False) #  True
print(False  or  True) #   True
print(True  or  True) #  True
print(False  or   False)   #  False
print(10  or  20)#  10
print(0   or  20)  #  20
print(-25  or  0) #-25
print(''  or  35) #35
print(6j  or  'Hyd') #6j
print(0.0  or  3 + 4j) #3+4j
print('Hyd'   or   10.8) #Hyd


'''
or  operator
--------------
1) When  is  the  result  of  or  operator  True ?  ---> When  at  least  one  operand  is  True
    When  is  the  result  of  or  operator  False ?  ---> When  both  the  operands  are  False

2) What  is  the  result  of  op1  or  op2  when  op1  is  False ?  ---> op2
    What  is  the  result  of  op1  or  op2  when  op1  is  True ?  ---> op1

3) and ,  or  operators  are  quite  opposite
'''

#Home Work-20
# not  operator  demo  program
print(not  True) #   False
print(not  False) #  True
print(not  25) #False
print(not  0) #True
print(not  'Hyd') #False
print(not  '') #True
print(not  -10) #False
print(not  not  'Hyd') #True


'''
not  operator
----------------
1) What  does  not  operator  do ?  ---> Complement  operation

2) Is  not  a  unary  operator  ?  ---> Yes  due  to  single  operand
    What  about  and ,  or ? ---> Binary  operators  due  to  two  operands

3) What  is  the  associativity  of  unary  operators ?  --->  Right  to  Left
    What  is  the  associativity  of  binary  operators ?  --->  Left  to  Right  except  for  **
'''

#Home Work-21
#  Find   outputs (Home work)
i = 10
i = not  i > 14
print(i) #True
print(not(6 < 4  or  9 >= 5  and  6 != 6)) #True
