# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a)
How  to  print  dictionary  with  print()  function
print('Keys  of  dictionary')
How  rintto  print  each  key  of  dict  'a'
print('Values  of  dictionary')
How  to  print  each  value  of  dict  'a'
print('All  the  tuples  of  dict_items   object')
How  to  print  each  tuple  of  the  list  in  dict_items  object
print('Elements  of  each   tuple')
How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object
print('Keys  and  values  of  dictionary')
How  to  print  each  key  and  corresponding  value  in  dict  'a'


print(a)
print(a.keys())
print(a.values())
print(a.items())



#  Find  outputs (Home  work)
a = {
		print('Hyd') ,		#Hyd
		print('Sec') ,		#Sec
		print('Cyb')		#Cyb
	}
print(type(a))				#class Set
print(a)				#None
print(len(a))				#1


#  Anonymous  object  demo  program
_ = 25
print(_)				#25
print(type(_))				#class int
a , _ , c = 10 , 20 , 30
print(a)				#10
print(_)				#20
print(c)				#30
for  _  in  range(5):
	print(_ , 'Hello')    		#0 Hello
					 1 Hello
					 2 Hello
					 3 Hello
					 4 Hello


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
a = 25
print(id(a))		#prints address
a = 35
print(id(a))		#prints new address


# Find  outputs (Home  work)
a = 25.7 
print(id(a))		#prints address
print(a)
a = 35.6
print(id(a))		##prints address
print(a)
b = True
print(id(b))		#prints address
b = False
print(id(b))		#prints address
c = None
print(id(c))		#prints address
c = None
print(id(c))		#prints address


#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a))
a[1] = 'e'		#str cannot be modified
a = 'Sec'
print(id(a))		#prints address
b = (10 , 20 , 15 , 18)
print(id(b))		#pritns address
b[2] = 19		#tuple is immutable
b = (30 , 40 , 35 , 32)
print(id(b))		#print address
c = range(5)	
print(id(c))		#print address
c[3] = 10		#range object cannot be modified
c = range(5)			
print(id(c))		#prints address




 # Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b)			#True
c = 'Hyd'
d = 'Hyd'
print(c  is  d)			#True
e = False
f = False
print(e  is  f)			#True
g = range(10)
h = range(10)			
print(g  is  h)			#False



#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b)			#false
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)			#False
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)			#false
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)			#False


# Find outputs (Home work)
print(10 + 20)   			#30
print(10.8 + 20.6)			#31.4
print(3 + 4j + 5 + 6j)			#(8+10j)
print(True + False)			#1
print('Hyder' + 'abad')			#Hyderabad
print('Sankar' + 'Dayal' + 'Sarma')	#SankarDayalSarma
print('10' + '20')			#1020
print([10 , 20 , 30] + [1 , 2 , 3])	#[10,20,30,1,2,3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None))	#(25, 10.8, 'Hyd', (3+4j), True, None)
print({10 , 20} + {30 , 40})				#Error
print({10 : 'Hyd'} + {20 : 'Sec'})			#Error
print(range(4) + range(5))				#Error
print(10 + '20')					#Error
print([10 , 20 , 30] + 5)				#Error
print([10 , 20 , 30] + (40 , 50 , 60))			#Error


# Find outputs (Home work)
print(25 * 3)				#75
print(10.8 * 25.6)			#276.48
print(True * False)			#0
print((3 + 4j) * (5 + 6j))
print(3 + 4j * 5 + 6j)
print('25' * 3)				#252525
print(3 * '25')				#252525
print('Hyd' * 4)			#HYdHydHydHyd
print([10 , 20 , 15] * 2)		#[10,20,15,10,20,15]
print((25, 10.8, 'Hyd', True) * 3)	#(25, 10.8, 'Hyd', True,25, 10.8, 'Hyd', True,25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0)		#Error
print({10 , 20 , 15} * 2)		#Error
print({10 : 20 , 30 : 40} * 2)		#Error
print([10] * [20])			#Error


#  /  operator  demo  program
print(9.0 / 2)             
print(9 / 2.0)
print(9.0 / 2.0)
print(9 / 2)  #  4.5
print(10.5 / 2)
print(10 / 3)
print(10 / 2)

4.5
4.5
4.5
4.5
5.25
3.3333333333333335
5.0


'''
What  does  /  operator  do  ?  --->  Peforms  division   and  returns  float  quotient
'''


#  //  operator  demo  program
print(9 // 2)  #   prev  integer  of (4.5) = 4
print(9.0 // 2)		#4.0
print(9 // 2.0)		#4.0
print(9.0 // 2.0)	#4.0
print(10.5 // 2)	#5.0
print(10 // 3)          #3.0
print(10.0 // 3)  #    prev  integer  of  3.33 = 3.0
print(8.5 // 3)		#2.0
print(18 // 4)		#4
print(-18 // 4)		#-5
print(-(18 // 4))	#-4



'''
//  operator
--------------
1) What  does  //  operator do ?  --->  Same  as  /  operator  but  returns  previous  integer  of  /  result

2) What  is  the  result  of  integer // integer ?  --->  Integer  quotient
    What  is  the  result  of  integer // float ?  ---> Float  quotient  with  .0
    What  is  the  result  of  float // integer ?  ---> Float  quotient  with  .0
    What  is  the  result  of  float // float ?  ---> Float  quotient  with  .0

3) What  is  the  resul…




# % operator demo program
print(9 % 5)
print(9.0 % 5)
print(9 % 5.0)
print(9.0 % 5.0)
print(10.5 % 2)  #   0.5
print(8.9 % 3)



'''
or  operator
--------------
1) When  is  the  result  of  or  operator  True ?  ---> When  at  least  one  operand  is  True
    When  is  the  result  of  or  operator  False ?  ---> When  both  the  operands  are  False

2) What  is  the  result  of  op1  or  op2  when  op1  is  False ?  ---> op2
    What  is  the  result  of  op1  or  op2  when  op1  is  True ?  ---> op1

3) and ,  or  operators  are  quite  opposite
'''
[12:40 PM, 7/21/2025] +91 99482 50500: # not  operator  demo  program
print(not  True) #   False
print(not  False) #  True
print(not  25)    #False
print(not  0)	  #True
print(not  'Hyd')	#False
print(not  '')		#true
print(not  -10)		#False
print(not  not  'Hyd')	#True


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
print(i)					#True
print(not(6 < 4  or  9 >= 5  and  6 != 6))	#True
