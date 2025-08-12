(22-07-2025)


#  Find  outputs

print({10 , 20}  |  {30 , 20})		# two sets are concatinating: {10 , 20, 30}
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'})	# two dicts are concatinating: {10 : 'Hyd' , 20 : 'Sec', 30 : 'Cyb' , 20 : 'Vja'}
print(range(4) | range(5))		# error as '|' not supported for range objects
print([10 , 20]  |  [30 , 20])		# error as '|' not supported for list objects




#  Assignment  operators  demo  program  (Home  work)

a = 25		# Ref  'a'  points  to  object 25 
print(a)	# output: 25
b =  a		# Ref  'b'  points  to same object of ref 'a' i.e., 25
print(b)	# output: 25
print(a  is  b) # output: True
x = 4		# Ref  'x'  points  to  object 4
y = 5		# Ref  'y'  points  to  object 5
z = x + y * 6   # 4+5*6= 4+30= 34 
print(z)	# output: 34
25 = a		# error as left operand should be ref only not object
a + b = x + y	# error as left operand should be ref only not expression




# Find outputs (Home work)

a = b = c = 25		# here Ref  'a','b','c'  points  to same object 25
print(id(a))		# address of object 25
print(id(b))		# same address of object 25
print(id(c))		# same address of object 25
print(a , b , c)	# 25 25 25




# Multiple  Assignment (Home work)

x , y , z = 25 , 10.8 , 'Hyd'	# here Ref  'x','y','z'  points  to objects 25, 10.8 , 'Hyd'
print(x)			# output: 25
print(y)			# output: 10.8
print(z)			# output: 'Hyd'




# Find outputs (Home work)

a , b , c = 3 , 4 , 5	# here Ref  'a','b','c'  points  to objects 3, 4, 5
a = b + c		# a= a(b+c): 3*(4+5)= 3*9= 27
print(a)		# output: 27




# Find outputs (Home work)

a = 20		# Ref  'a'  points  to  object 20
a %= 3 + 2 * 4	# a=a%(3+2*4): 20%(3+8)= 20%(11)= 9
print(a)	# output: 9

 


# Find outputs (Home work)

a = 3		# Ref  'a'  points  to  object 3
a *= 4		# a=a4: 3*4=81
print(a)	# output: 81




# Identity operators demo program

a = 25			# Ref  'a'  points  to  object 25
b = 25			# Ref  'b'  points  to  object 25
print(a  is  b)		# both refs pointing same object output: True
print(a  is  not  b)	# opposite of 'is' operation output: False
print(a == b)		# both object Values are equal output: True




# Find outputs (Home work)

a = 25			# Ref  'a'  points  to  object 25
b = 25.0		# Ref  'b'  points  to  object 25.0
print(a  is  b)		# both refs pointing 2 different objects output: False
print(a  is  not  b)	# opposite of 'is' operation output: True
print(a == b)		# both object Values are equal output: True




# Find outputs (Home work)

a = 'Hyd'		# Ref  'a'  points  to str object 'Hyd'
b = 'Hyd'		# Ref  'b'  points  to same str object 'Hyd'
print(a  is  b)		# both refs pointing same str output: True
print(a  is  not  b)	# opposite of 'is' operation output: False
print(a == b)		# both object Values are equal output: True
print()
x = [1 , 2 , 3 , 4]	# Ref  'x'  points  to list [1 , 2 , 3 , 4]
y = [1 , 2 , 3 , 4]	# Ref  'y'  points  to another object [1 , 2 , 3 , 4]
print(x is y)		# both refs pointing 2 different list output: False
print(x  is  not  y)	# opposite of 'is' operation output: True
print(x == y)		# both object Values are equal output: True
print()
m = (1 , 2 , 3 , 4)	# Ref  'a'  points  to tuple (1 , 2 , 3 , 4)
n = (1 , 2 , 3 , 4)	# Ref  'a'  points  to same tuple (1 , 2 , 3 , 4)
print(m  is  n)		# both refs pointing same tuple output: True
print(m  is  not  n)	# opposite of 'is' operation output: False
print(m == n)		# both object Values are equal output: True
print(x == m)		# both object Values are not equal output: False




# Membership operators demo program (Home work)

list = [10, 20, 15, 12, 18]

print(15 in list)        # 15 is present in the list : True
print(19 in list)        # 19 is not in the list : False
print(14 not in list)    # 14 is not in the list: True
print(15 not in list)    # 15 is present, so "not in" is False : False

s = 'Hyd is green city'

print('is' in s)         # 'is' exists in the string : True
print('was' in s)        # 'was' not exists in the string : False
print('g' in s)          # 'g' is present in "green" : True
print('z' in s)          # 'z' is not present : False
print(' ' in s)          # space character exists between words : True
print('gre' in s)        # 'gre' is part of "green" : True
print('yd i' in s)       # 'yd i' appears in "Hyd is" : True
print('' in s)           # empty string is always present in any string : True
print('' not in s)       # because '' is always present, "not in" is False : False




# Find outputs (Home work)

x = [1 , 2 , 3 , 4]	# Ref  'x'  points  to list [1 , 2 , 3 , 4]
y = [1 , 2 , 4 , 3]	# Ref  'y'  points  to new list [1 , 2 , 4 , 3]
print(x == y)		# elements positions differs: False
a = (4 , 1 , 3 , 2)	# Ref  'a'  points  to tuple (4 , 1 , 3 , 2)
b = (4 , 2 , 3 , 1)	# Ref  'b'  points  to new tuple (4 , 2 , 3 , 1)	
print(a == b)		# elements positions differs : False
p = {1 , 2 , 3 , 4}	# Ref  'p'  points  to set {1 , 2 , 3 , 4}
q = {4 , 1 , 3 , 2}	# Ref  'q'  points  to new set {4 , 1 , 3 , 2}
print(p == q)		# same unique elements : True
m = range(5)		# Ref  'm'  points  to range(5)
n = range(5)		# Ref  'n'  points  to new range(5)
print(m == n)		# Both has same sequence : True 





# Find outputs (Home work)

a = [10, 20, 30]	# Ref  'a'  points  to list 
b = (10, 20, 30)	# Ref  'b'  points  to tuple
print(a is b)		# list and tuple are different objects : False
print(a == b)        	# list values are not equal to tuple values : False