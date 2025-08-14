# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'} #
print('Dictionary  with  print  function')
How  to  print  dictionary  with  print()  function
print('Keys  of  dictionary')
How  to  print  each  key  of  dict  'a'
print('Values  of  dictionary')
How  to  print  each  value  of  dict  'a'
print('All  the  tuples  of  dict_items   object')
How  to  print  each  tuple  of  the  list  in  dict_items  object
print('Elements  of  each   tuple')
How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object
print('Keys  and  values  of  dictionary')
How  to  print  each  key  and  corresponding  value  in  dict  'a'



#  Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
	}
print(type(a))
print(a)
print(len(a))



#  Anonymous  object  demo  program
_ = 25
print(_)
print(type(_))
a , _ , c = 10 , 20 , 30
print(a)
print(_)
print(c)
for  _  in  range(5):
	print(_ , 'Hello')


'''
1) What  is   _   called ?   --->  Anonymous  object  (or) Nameless  object

2) How  many  nameless  objects  can  be  a  program ?  --->  Just  one  (or)  zero

3) What  happens  when  another  nameless  object  is  created ?  --->  Existing  nameless  object  gets  deleted

4) Can  there  be  multiple  nameless  objects  in  a  program ?  --->  No

5) _ = 10
    _ = 20
   What  happens  when  _ = 20  is  executed ?  --->  A  new  nameless  object  is  created  with  value  20  and
																				  old  nameless  object  with  10  is  lost
''     




#  Find  outputs
a = 25
print(id(a))
a = 35
print(id(a)







# Find  outputs (Home  work)
a = 25.7
print(id(a))
print(a)
a = 35.6
print(id(a))
print(a)
b = True
print(id(b))
b = False
print(id(b))
c = None
print(id(c))
c = None
print(id(c)



#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a))
a[1] = 'e'
a = 'Sec'
print(id(a))
b = (10 , 20 , 15 , 18)
print(id(b))
b[2] = 19
b = (30 , 40 , 35 , 32)
print(id(b))
c = range(5)
print(id(c))
c[3] = 10
c = range(5)
print(id(c)



# Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b)
c = 'Hyd'
d = 'Hyd'
print(c  is  d)
e = False
f = False
print(e  is  f)
g = range(10)
h = range(10)
print(g  is  h)




#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b)
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)



# Find outputs (Home work)
print(10 + 20)
print(10.8 + 20.6)
print(3 + 4j + 5 + 6j)
print(True + False)
print('Hyder' + 'abad')
print('Sankar' + 'Dayal' + 'Sarma')
print('10' + '20')
print([10 , 20 , 30] + [1 , 2 , 3])
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None))
print({10 , 20} + {30 , 40})
print({10 : 'Hyd'} + {20 : 'Sec'})
print(range(4) + range(5))
print(10 + '20')
print([10 , 20 , 30] + 5)
print([10 , 20 , 30] + (40 , 50 , 60))






# Find outputs (Home work)
print(25 * 3)
print(10.8 * 25.6)
print(True * False)
print((3 + 4j) * (5 + 6j))
print(3 + 4j * 5 + 6j)
print('25' * 3)
print(3 * '25')
print('Hyd' * 4)
print([10 , 20 , 15] * 2)
print((25, 10.8, 'Hyd', True) * 3)
print([10 , 20 , 15] * 3.0)
print({10 , 20 , 15} * 2)
print({10 : 20 , 30 : 40} * 2)
print([10] * [20])




#  /  operator  demo  program
print(9.0 / 2)
print(9 / 2.0)
print(9.0 / 2.0)
print(9 / 2)  #  4.5
print(10.5 / 2)
print(10 / 3)
print(10 / 2)


'''
What  does  /  operator  do  ?  --->  Peforms  division   and  returns  float  quotient
'''




#  //  operator  demo  program
print(9 // 2)  #   prev  integer  of (4.5) = 4
print(9.0 // 2)
print(9 // 2.0)
print(9.0 // 2.0)
print(10.5 // 2)
print(10 // 3)
print(10.0 // 3)  #    prev  integer  of  3.33 = 3.0
print(8.5 // 3)
print(18 // 4)
print(-18 // 4)
print(-(18 // 4))



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
print(9 % 5)
print(9.0 % 5)
print(9 % 5.0)
print(9.0 % 5.0)
print(10.5 % 2)  #   0.5
print(8.9 % 3)


'''
%   operator
---------------
1) What  does  %  operator  do ?  ---> Performs  division  and  returns  remainder

2) When  is  the  result  of  %  operator  integer ?  ---> When  both  the  operands  are  integers
    When  is  the  result  of  %  operator  float ?  ---> When  at  least  one  operand  is  float
'''








# Find outputs
print(7 / 0)
print(7 // 0)
print(7 % 0)





#  Relational  operators  demo  program (Home  work)
print(9 >= 5)  #   True :  >  is  satisfied
print(9 >= 9)   #   True :  =  is  satisfied
print(9 >= 12)   #  False :  Both  are  not  satisfied
print(6 <= 8)
print(6 <= 6)
print(6 <= 4)
print(9 != 7)
print(6 == 8)
print(True  >  False)
print(3 + 4j == 3 + 4j)
print(3 + 4j == 5 + 6j)
print(3 + 4j != 5 + 6j)
print(10 == 10.0)
print(3 + 4j >  3 + 4j)


'''
1) Can  complex  numbers   be  compared ?   ---> Yes  with  ==  and  !=

2) When  can  complex  numbers   be  not  compared  ?  ---> Wiith  > , <  , >=  and  <=
'''



#  Find  outputs  (Home  work)
print('Rama'   >  'Rajesh')  #   True :  'm' > 'j'
print('Rama'  <  'Sita') #  True : 'R' < 'S'
print('Hyd'  ==  'Hyd')
print('Rama'  <=   'Ramana')
print('Rama  Rao'  >=  'Rama')
print('Hyd'  != 'Sec')
print('HYD'  <   'hyd')


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
print(10 < 20 > 30)
print(1 < 2 < 3 < 4)
print(1 < 2 > 3 > 1)
print(4 > 3 >= 3 > 2)






#  or  operator  demo program
print(True  or  False) #  True
print(False  or  True) #   True
print(True  or  True) #  True
print(False  or   False)   #  False
print(10  or  20)#  10
print(0   or  20)  #  20
print(-25  or  0)
print(''  or  35)
print(6j  or  'Hyd')
print(0.0  or  3 + 4j)
print('Hyd'   or   10.8)


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
print(not  25)
print(not  0)
print(not  'Hyd')
print(not  '')
print(not  -10)
print(not  not  'Hyd')


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
i = 10
i = not  i > 14
print(i)
print(not(6 < 4  or  9 >= 5  and  6 != 6))


