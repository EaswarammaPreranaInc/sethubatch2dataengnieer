a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a,'Dictionary  with  print  function') # print(a)
#How  to  print  dictionary  with  print()  function
print(a.keys() )#'Keys  of  dictionary') #print(a.keys())
#How  to  print  each  key  of  dict  'a'
print(a.values(),'Values  of  dictionary')
#How  to  print  each  value  of  dict  'a'
print(a.items(),'All  the  tuples  of  dict_items   object')
#How  to  print  each  tuple  of  the  list  in  dict_items  object
print('Elements  of  each   tuple')
for  i  in  a.items():
	print(i)
#How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object

#How  to  print  each  key  and  corresponding  value  in  dict  'a'


a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
	} # a set is create with a object  
print(type(a)) # type of object is set so a is a set
print(a) # Hyd,sec,Cyb is printe
print(len(a)) # it is a whole object so len is 1

_ = 25 #an int object is create assigne to anonymous object
print(_) # printing anonymous object 25
print(type(_)) # as object is class int the anonymous object type is also class int
a , _ , c = 10 , 20 , 30 # int objects are create assigne to anonymous object
print(a) # as 1st object is 10 a is 10
print(_) # as 2n object is 20 anonymous objectr is 20
print(c)  # as 3r object is 30 anonymous objectr is 30
for  _  in  range(5): # anonymous object is range from 0 to 5
	print(_ , 'Hello') # prints the anonymous value rangefrom 0 to 4 , 'Hello'
	
a = 25
print(id(a)) # stores object 25 in ref a so prints the id of object 25 
a = 35
print(id(a)) # stores object 35 in ref & removes the 25 so prints the id of object 35 

a = 25.7 # initially 25 is assigned to a
print(id(a)) #prints id of a
print(a) # prints a
a = 35.6 # now here reference is modified to 35.6
print(id(a)) # the id of a is now modified an printed
print(a) # prints a
b = True # True is assigned to b
print(id(b)) # prints id of b
b = False # False is assigned to b & the false object is removed
print(id(b)) # prints id of b
c = None # None is assigned to c
print(id(c)) # prints id of c
c = None # None is assigned to c as none tpe is reusable new none object is not created
print(id(c)) # same id is printed


a = 'Hyd' # 'Hyd is a string and assigned to a
print(id(a)) #prints the id of a
#a[1] = 'e' # error because a is immutable stirng object
a = 'Sec' # 'Sec is a string and assigned to a
print(id(a)) #prints the id of a
b = (10 , 20 , 15 , 18) # a tuple is assigne to b
print(id(b)) # prints the id of b
b[2] = 19 # error because b is immutable tuple object
b = (30 , 40 , 35 , 32) # a tuple is assigne to b
print(id(b)) # prints the id of 
c = range(5) # a range is assigne to c from range 0 to 4
print(id(c)) # prints the id of c
c[3] = 10 # error because c is immutable range object
c = range(5) # a range is assigne to c from range 0 to 4
print(id(c)) # prints the id of c is not same as above because range is immutable but not reusable



a = 25 #  assigns 25 to a
b = 25 #  assigns 25 to b
print(a  is  b) #  prints True becuase int is reusable an only one 25 object is create
c = 'Hyd' #  assigns 'Hyd' to c
d = 'Hyd' #  assigns 'Hyd' to d
print(c  is  d) #  prints True becuase string is also reusable an only one 'Hyd' object is create
e = False #  assigns False to e
f = False #  assigns False to f
print(e  is  f) #  prints True becuase bool is also reusable an only one False object is create
g = range(10) #  assigns range(10) to g
h = range(10) #  assigns range(10) to h
print(g  is  h) #  prints False becuase range is not reusable

a = [10 , 20 , 15 , 18] # a list is assigned to a
b = [10 , 20 , 15 , 18] # even though both are same lists another new list is created as list is not reusable
print(a  is  b) # false
c =  {10 : 20, 30 : 40} # a dictionary is assigned to c
d =  {10 : 20, 30 : 40} # even though both are same dictionaries another new dictionary is created as dictionary is not reusable
print(c  is  d) # false
e = (10 , 20 , 15 , 18) # a tuple is assigned to e
f = (10 , 20 , 15 , 18) # as both are same tuples another new tuple is not created as tuple is reusable
print(e  is  f) # true
g = {10 , 20 , 15 , 18} # a set is assigned to g
h = {10 , 20 , 15 , 18}  # even both are same sets another new set is  created as set is not reusable
print(g  is  h) # false


# Find outputs (Home work)
print(10 + 20) # both are non sequence so addition takes place
print(10.8 + 20.6) # both are non sequence so addition takes place
print(3 + 4j + 5 + 6j)  # both are non sequence so addition takes place
print(True + False) # both are non sequence so addition takes place
print('Hyder' + 'abad') # as both are sequence both strings are concatenated
print('Sankar' + 'Dayal' + 'Sarma') # as 3 are sequence both strings are concatenated
print('10' + '20') # as both are sequence both strings are concatenated
print([10 , 20 , 30] + [1 , 2 , 3]) # as both are sequence both lists are concatenated
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) # as both are sequence both tuples are concatenated
print({10 , 20} + {30 , 40})  # error because set cant be concatenate using +
print({10 : 'Hyd'} + {20 : 'Sec'}) # error because ict cant be concatenate using +
print(range(4) + range(5)) # error because range cant be concatenate using +
print(10 + '20') # error because if 1 operan is sequence other shouls also be sequence
print([10 , 20 , 30]+ 5) # error because if 2 operan is sequence other shouls also be sequence
print([10 , 20 , 30] +(40,50,60))  # if one operan is list other shoul also be list

# Find outputs (Home work)
print(25 * 3) # both are non sequence so multiplication takes place
print(10.8 * 25.6) # both are non sequence so multiplication takes place
print(True * False) # both are non sequence so multiplication takes place
print((3 + 4j) * (5 + 6j)) # both are non sequence so multiplication takes place
print(3 + 4j * 5 + 6j) # here * is only for 4j an 5 so 20j+6j
print('25' * 3) #if one operan is sequence an other is int repeatition takes place
print(3 * '25')  #if one operan is sequence an other is int repeatition takes place
print('Hyd' * 4)#if one operan is sequence an other is int repeatition takes place
print([10 , 20 , 15] * 2) #if one operan is sequence an other is int repeatition takes place
print((25, 10.8, 'Hyd', True) * 3) #if one operan is sequence an other is int repeatition takes place an new tuple is create
#print([10 , 20 , 15] * 3.0) #if one operan is sequence an other should be int onlu
#print({10 , 20 , 15} * 2) # error because set cant be repate
print({10 : 20 , 30 : 40} * 2) # error because dict cant be repeate
print([10]*[20]) #if one operan is sequence an other should be int only

print(9.0 / 2) # 4.5 because / gives float quotient only
print(9 / 2.0)  # 4.5 because / gives float quotient only 
print(9.0 / 2.0) # 4.5
print(9 / 2)  #  4.5
print(10.5 / 2) # 5.25
print(10 / 3) # 3.3333333333333335 
print(10 / 2) # 5.0


print(9 // 2)  #   prev  integer  of (4.5) = 4
print(9.0 // 2)  #   prev  integer  of (4.5) = 4 and if 1 operand is float we shoul place .0 at en so 4.0
print(9 // 2.0)  #   prev  integer  of (4.5) = 4 and if 1 operand is float we shoul place .0 at en so 4.0
print(9.0 // 2.0) #   prev  integer  of (4.5) = 4 and if 1 operand is float we shoul place .0 at en so 4.0
print(10.5 // 2)  #   prev  integer  of (5.25) = 5.0
print(10 // 3)  #   prev  integer  of (3.33) = 3
print(10.0 // 3)  #    prev  integer  of  3.33 = 3.0
print(8.5 // 3)  #   prev  integer  of  2.83 = 2.0
print(18 // 4)  #   prev  integer  of  4.5 = 4
print(-18 // 4)  #   prev  integer  of  -4.5 = -5
print(-(18 // 4))  #   prev  integer  of  -4.5 = -5

print(9 % 5)  #   4 because the remainer is 4
print(9.0 % 5)  #   4.0 because one  operand  is  float
print(9 % 5.0)  #   4.0
print(9.0 % 5.0)  #   4.0
print(10.5 % 2)  #   0.5
print(8.9 % 3) # 2.9 because one  operand  is  float

print(7 / 0) # error because we cant DiviDe any integer with 0
print(7 // 0) # error because we cant DiviDe any integer with 0
print(7%0) # error because we cant DiviDe any integer with 0


print(3 ** 4) # 3^4 = 81
print(10 ** -2) # 10^-2 = 0.01
print(4 ** 3 ** 2) # ** is from right to left evaluation so 3^2=9 an then 4^9
print(3 + 4 * 5 - 32 / 2 ** 3) # high priority is for ** so 2**3=2^3=8 next is for * so 4*5=20 next /so 32/8=4 ; now we have 3+20-4 
#next proirty is for + so 3+20=23 an then - so 23-4 i.e 19.0


print(9 >= 5)  #   True :  >  is  satisfied
print(9 >= 9)   #   True :  =  is  satisfied
print(9 >= 12)   #  False :  Both  are  not  satisfied
print(6 <= 8)  #   True :  <  is  satisfied
print(6 <= 6)  #   True :  =  is  satisfied
print(6 <= 4)  #  False :  Both  are  not  satisfied
print(9 != 7)  #   True :  !=  is  satisfied
print(6 == 8)  #   False :  ==  is  not  satisfied
print(True  >  False) # true 1 > 0 which is true
print(3 + 4j == 3 + 4j) # true
print(3 + 4j == 5 + 6j) # false
print(3 + 4j != 5 + 6j) # true
print(10 == 10.0) # true
print(3 + 4j >  3 + 4j) # error because complexes are comapre using only == & !=


print('Rama'   >  'Rajesh')  #   True :  'm' > 'j'
print('Rama'  <  'Sita') #  True : 'R' < 'S'
print('Hyd'  ==  'Hyd') #  True
print('Rama'  <=   'Ramana') #  True because '' <= n
print('Rama  Rao'  >=  'Rama') # true because ' ' >=''
print('Hyd'  != 'Sec') #  True
print('HYD'  <   'hyd') #true H <h

print(10 < 20 < 30)  #   True
print(10 >= 20 < 30)  #   False : 10  is  not  >= 20
print(10 < 20 > 30)  #   False : 20  is  not  >  30
print(1 < 2 < 3 < 4)  #   True :  <  is  satisfied
print(1 < 2 > 3 > 1)  #   False :  >  is  not  satisfied
print(4>3>=3>2) # True

print(True  or  False) #  True
print(False  or  True) #   True
print(True  or  True) #  True
print(False  or   False)   #  False
print(10  or  20)#  10 if 1 operan is true result is 1st operan
print(0   or  20)  #  20 if 1 operan is false result is 2n operan
print(-25  or  0)  #  -25
print(''  or  35) # 35
print(6j  or  'Hyd') # 6j
print(0.0  or  3 + 4j) # 3+4J
print('Hyd'   or   10.8) #HYd


print(not  True) #   False
print(not  False) #  True
print(not  25) #false because 25 is non zero which is true compliment of true is false
print(not  0) # true
print(not  'Hyd') #false because 'Hyd' is non empty string which is true compliment of true is false
print(not  '') # true
print(not  -10) # false because -10 is non zero which is true compliment of true is false
print(not  not  'Hyd') # 'Hyd' is non empty string which is true compliment of true is false not false is true


i = 10
i = not  i > 14 # i>14 i.e 10>14 is false not of false is true
print(i) # true
print(not(6 < 4  or  9 >= 5 and 6!=6)) # 1st priority is for relational in relationa >= has 1st priority so 9>=5 true  ,6<4 false 
#true or false an false here an has 1st priority so false an false =false so true or false is true
