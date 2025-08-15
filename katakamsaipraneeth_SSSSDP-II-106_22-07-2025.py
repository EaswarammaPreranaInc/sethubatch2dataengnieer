#  Find  outputs
print({10 , 20}  |  {30 , 20}) # '|' used for concatenation --> {10,20,30}
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'}) # {10 : 'Hyd' , 20 : 'Vja', 30 : 'Cyb'}
print(range(4) | range(5)) # error
print([10 , 20]  |  [30 , 20]) # error


#  Assignment  operators  demo  program  (Home  work)
a = 25 # Assigned reference 'a' to int object 25
print(a) # 25
b =  a # assigned ref 'b' to ref obj 'a' --> ref of a is copied to ref b
print(b) # 25
print(a  is  b) # True
x = 4 # ref x assigned to int obj
y = 5 # int class obj
z = x + y * 6 # ref x is assigned to obj 
print(z) # 34
25 = a # error --left side should be ref not obj
a + b = x + y # error because it is product not ref


# Find outputs (Home work)
a = b = c = 25 # multiple assignment
print(id(a)) # address of a
print(id(b)) # address of b
print(id(c)) # address of c
print(a , b , c) # 25, 25, 25


# Multiple  Assignment (Home work)
x , y , z = 25 , 10.8 , 'Hyd' # valid because of multiple assignment
print(x) # 25
print(y) # 10.8
print(z) # 'Hyd'


# Find outputs (Home work)
a , b , c = 3 , 4 , 5 # multiple assignment in single line
a *= b + c # 3*= 4+5
print(a) # 27

# Find outputs (Home work)
a = 20 # ref of a is pointed to obj 20
a %= 3 + 2 * 4 # a= 20 % 11
print(a) # 9

# Find outputs (Home work)
a = 3 # int obj
a **= 4 # a= 3**4
print(a) # 81

# Identity operators demo program
a = 25 # int obj 
b = 25 # int obj
print(a  is  b) # True
print(a  is  not  b) # False
print(a == b) # True


# Find outputs (Home work)
a = 25 # int obj
b = 25.0 # float obj
print(a  is  b) # True
print(a  is  not  b) # False
print(a == b) # True

# Find outputs (Home work)
a = 'Hyd' # str obj
b = 'Hyd' # str obj
print(a  is  b) # True
print(a  is  not  b) # False
print(a == b) # True
print() # goes to next line
x = [1 , 2 , 3 , 4] # list obj
y = [1 , 2 , 3 , 4] # list obj
print(x is y) # False
print(x  is  not  y) # True
print(x == y) # True
print() # next line
m = (1 , 2 , 3 , 4) # tuple obj
n = (1 , 2 , 3 , 4) # tuple obj
print(m  is  n) # True
print(m  is  not  n) False
print(m == n) # True
print(x == m) # False


# Membership operators demo program (Home work)
list = [10 , 20 , 15 , 12 , 18] # list obj
print(15 in list) # True
print(19 in list) # False
print(14 not in list) # True
print(15 not in list) # False
s = 'Hyd is green city' # str obj
print( 'is' in s) # True
print('was' in s) # False
print('g' in s) # True
print('z' in s) # False
print(' ' in s) # True
print('gre' in s) # True
print('yd i' in s) # True
print('' in s) # False
print('' not in s) # True

# Find outputs (Home work)
x = [1 , 2 , 3 , 4] # list obj
y = [1 , 2 , 4 , 3] # list obj
print(x == y) # False
a = (4 , 1 , 3 , 2) # tuple obj
b = (4 , 2 , 3 , 1) # tuple obj
print(a == b) # False
p = {1 , 2 , 3 , 4} # set obj
q = {4 , 1 , 3 , 2} # set obj
print(p == q) # True
m = range(5) # range obj
n = range(5) # range obj
print(m == n) # True

# Find outputs (Home work)
a = [10,20,30] # list obj
b = (10,20,30) # tuple obj
print(a  is  b) # False
print(a  ==  b) # False