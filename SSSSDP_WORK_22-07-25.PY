# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function')  #Dictionary  with  print  function
How  to  print  dictionary  with  print()  function
for i,j in a.items():
	print(f"key:{i} and value:{j}")


print('Keys  of  dictionary')
How  to  print  each  key  of  dict  'a'
for i in a.keys():
	print(f"key:{i}")
	
for i in a:
	print(i)

print('Values  of  dictionary')
How  to  print  each  value  of  dict  'a'
for j in a.values():
	print(f" value:{j}")
print('All  the  tuples  of  dict_items   object')
How  to  print  each  tuple  of  the  list  in  dict_items  object
for i,j in a.items():
	print(f"key:{i} and value:{j}")
print('Elements  of  each   tuple')
How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object
print('Keys  and  values  of  dictionary')
How  to  print  each  key  and  corresponding  value  in  dict  'a'


#  Find  outputs (Home  work)
a = {
		print('Hyd') ,         Hyd
		print('Sec') ,         Sec
		print('Cyb')           Cyb
	}
print(type(a)) <class set>
print(a) # {None}  # print(10) is a function call it prints 10 return NOne {NOne+None}={None}
print(len(a)) #1

#  Anonymous  object  demo  program
_ = 25
print(_) #25
print(type(_))  # <class int>
a , _ , c = 10 , 20 , 30
print(a) #10
print(_) #20
print(c) #30
for  _  in  range(5):
	print(_ , 'Hello')  # 0, Hello <nextline> 1,Hello <nL> 2,Hello <nl> 3,Hello <nl> 4,Hello

#  Find  outputs
a = 25
print(id(a))
a = 35
print(id(a)

# Find  outputs (Home  work)
a = 25.7
print(id(a))  # 1000
print(a) #25.7
a = 35.6
print(id(a))  #1001   new object is created 
print(a)  #35.6
b = True
print(id(b))   #1003
b = False
print(id(b))  #1004
c = None
print(id(c)) #1005
c = None
print(id(c)) #1005

#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a))  #1000
a[1] = 'e'  #error immutable
a = 'Sec'
print(id(a))  #1002
b = (10 , 20 , 15 , 18)
print(id(b))  #1003
b[2] = 19   #error immutable
b = (30 , 40 , 35 , 32)
print(id(b))  # 1004
c = range(5)  
print(id(c)) #1005
c[3] = 10  # error
c = range(5)  # new object range object is immutable 
print(id(c)) #1006

# Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b) # True
c = 'Hyd'
d = 'Hyd'
print(c  is  d)  # True
e = False
f = False
print(e  is  f) #True
g = range(10)
h = range(10)
print(g  is  h) #False

#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b) #False
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)  #False
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)#True
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)  #False

# Find outputs (Home work)
print(10 + 20) #30
print(10.8 + 20.6) #31.4
print(3 + 4j + 5 + 6j) #8+10j
print(True + False) # 1
print('Hyder' + 'abad') # Hyderabad
print('Sankar' + 'Dayal' + 'Sarma') #SankarDayalSarma
print('10' + '20') #1020
print([10 , 20 , 30] + [1 , 2 , 3]) # [10,20,30,1,2,3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None))# (25 , 10.8 , 'Hyd',3 + 4j , True , None)
print({10 , 20} + {30 , 40}) # error
print({10 : 'Hyd'} + {20 : 'Sec'}) # error
print(range(4) + range(5)) # error
print(10 + '20') # error
print([10 , 20 , 30] + 5) # error only list +list not int
print([10 , 20 , 30] + (40 , 50 , 60)) # error

# Find outputs (Home work)
print(25 * 3) #75
print(10.8 * 25.6) #276.48
print(True * False) #0
print((3 + 4j) * (5 + 6j)) #(-9+38j)
print(3 + 4j * 5 + 6j) #(3+26j)
print('25' * 3) #252525
print(3 * '25') #252525
print('Hyd' * 4)#HydHydHydHyd
print([10 , 20 , 15] * 2) # [10 , 20 , 15,10 , 20 , 15]
print((25, 10.8, 'Hyd', True) * 3) #(25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0) # errror 
print({10 , 20 , 15} * 2) # errror 
print({10 : 20 , 30 : 40} * 2) # errror 
print([10] * [20]) # errror 

#  /  operator  demo  program
print(9.0 / 2) # 4.5
print(9 / 2.0) # 4.5
print(9.0 / 2.0) #4.5
print(9 / 2)  #  4.5
print(10.5 / 2) #5.25
print(10 / 3) #3.33
print(10 / 2) # 5.0
print(-18 / 4) #4.5

#  //  operator  demo  program
print(9 // 2)  #   prev  integer  of (4.5) = 4
print(9.0 // 2) #4.0
print(9 // 2.0) #4.0
print(9.0 // 2.0) #4.0
print(10.5 // 2) #5.0
print(10 // 3) # 3
print(10.0 // 3)  #    prev  integer  of  3.33 = 3.0
print(8.5 // 3) # 2.0
print(18 // 4) # 4
print(-18 // 4) # -5 floor(-4.5) = -5
print(-(18 // 4)) -4

# % operator demo program
print(9 % 5) # 4
print(9.0 % 5) #4.0
print(9 % 5.0) # 4.0
print(9.0 % 5.0) #4.0
print(10.5 % 2)  #   0.5
print(8.9 % 3) #2.9


# Find outputs
print(7 / 0) #error
print(7 // 0) #error
print(7 % 0) #error

# ** operator demo program
print(3 ** 4) #81
print(10 ** -2) # 0.01
print(4 * 3 * 2) # 24
print(3 + 4 * 5 - 32 / 2 ** 3)# 19


#  Relational  operators  demo  program (Home  work)
print(9 >= 5)  #   True :  >  is  satisfied
print(9 >= 9)   #   True :  =  is  satisfied
print(9 >= 12)   #  False :  Both  are  not  satisfied
print(6 <= 8) #True
print(6 <= 6) #True
print(6 <= 4) #False
print(9 != 7) # True
print(6 == 8) #False
print(True  >  False) #True
print(3 + 4j == 3 + 4j) #true
print(3 + 4j == 5 + 6j) #False
print(3 + 4j != 5 + 6j)  #True
print(10 == 10.0) #True
print(3 + 4j >  3 + 4j) #error complex > complex

#  Find  outputs  (Home  work)
print('Rama'   >  'Rajesh')  #   True :  'm' > 'j'
print('Rama'  <  'Sita') #  True : 'R' < 'S'
print('Hyd'  ==  'Hyd')  #  True
print('Rama'  <=   'Ramana')  #  True 
print('Rama  Rao'  >=  'Rama')  #  True space 
print('Hyd'  != 'Sec')  #  True
print('HYD'  <   'hyd')  #  True
print('Rama' > 'Ramana') # False


# Chaining  relational  opeartors  (Home work)
print(10 < 20 < 30)  #   True
print(10 >= 20 < 30)  #   False : 10  is  not  >= 20
print(10 < 20 > 30) #   False
print(1 < 2 < 3 < 4) #   True
print(1 < 2 > 3 > 1) #   False
print(4 > 3 >= 3 > 2) #True


#  or  operator  demo program  the first truthy value, or the last value if none are truthy.
print(True  or  False) #  True
print(False  or  True) #   True
print(True  or  True) #  True
print(False  or   False)   #  False
print(10  or  20)#  10
print(0   or  20)  #  20
print(-25  or  0) # -25
print(''  or  35) # 35
print(6j  or  'Hyd') # 6j
print(0.0  or  3 + 4j) # 3+4j
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


# not  operator  demo  program
print(not  True) #   False
print(not  False) #  True
print(not  25) # False
print(not  0) #True
print(not  'Hyd') # False
print(not  '') # True
print(not  -10) # False
print(not  not  'Hyd') # True


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
i = not  i > 14 #True
print(i) #True
print(not(6 < 4  or  9 >= 5  and  6 != 6)) #True

# Find outputs (Home work)
a = [10,20,30] #list
b = (10,20,30) # tuple
print(a  is  b) # false
print(a  ==  b) # False

# Find outputs (Home work)
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 4 , 3]
print(x == y) # false lists are not in order
a = (4 , 1 , 3 , 2)
b = (4 , 2 , 3 , 1)
print(a == b) # false tuple values are not in order
p = {1 , 2 , 3 , 4}
q = {4 , 1 , 3 , 2}
print(p == q) # True sets are unordered
m = range(5)
n = range(5)
print(m == n) # True ranges of both are same 

# Membership operators demo program (Home work)
list = [10 , 20 , 15 , 12 , 18]
print(15 in list)# True
print(19 in list) # false
print(14 not in list) # True
print(15 not in list)# false
s = 'Hyd is green city'
print( 'is' in s) # True
print('was' in s)# false
print('g' in s) # True
print('z' in s)# false
print(' ' in s) # True
print('gre' in s) # True
print('yd i' in s) # True
print('' in s) # True
print('' not in s)# false

# Find outputs (Home work)
a = 'Hyd'
b = 'Hyd'
print(a  is  b) # true
print(a  is  not  b) #false
print(a == b) # true
print() # empty space
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 3 , 4]
print(x is y) #  false
print(x  is  not  y) # true
print(x == y) # true
print() # empty
m = (1 , 2 , 3 , 4)
n = (1 , 2 , 3 , 4)
print(m  is  n) # true
print(m  is  not  n) #false
print(m == n) # true
print(x == m) # false

# Find outputs (Home work)
a = 25
b = 25.0
print(a  is  b) # false
print(a  is  not  b) # true
print(a == b)# true

# Find outputs (Home work)
a = 3
a **= 4 # 3*3*3*3=81
print(a)# 81

# Find outputs (Home work)
a = 20
a %= 3 + 2 * 4 # 8+3=11
print(a) # 9

#  Assignment  operators  demo  program  (Home  work)
a = 25
print(a) # 25
b =  a
print(b) # 25
print(a  is  b) #True
x = 4
y = 5
z = x + y * 6 # 34
print(z)# 34
25 = a #error
a + b = x + y # error

# Find outputs (Home work)
a = b = c = 25
print(id(a)) # address of object a
print(id(b)) # address of object b same id as a
print(id(c))#address of object c same id
print(a , b , c) # 25 25 25
