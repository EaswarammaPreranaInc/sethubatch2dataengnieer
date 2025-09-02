#index()  and  count()  methods  demo  program   (Home  work)

a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1      2     3    4     5     6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i)
		i = a . index(15 , i + 1)
except:
		print(F'15  is  found  {a . count(15)} times')
		
'''
Output:
15 is found at index : 2
15 is found at index : 5
15 is found at index : 8
15 is found 3 times
'''


#  How to modify an element of tuple ?    (Home work)

a = 10, 20, 30, 40, 50
#    0   1   2   3   4
a[2] = 35         # Tuple is immutable assigning values is not possible
print(a)          # (10, 20, 30, 40, 50)
print(id(a))      # Prints address of the tuple a
a = a[:2] + (35,) + a[3:]  # Correct way to modify 30 in tuple to 35
print(a)          # (10, 20, 35, 40, 50)
print(id(a))      # Prints the new address of the tuple a


#  How to modify an element of tuple ?    (Home work)

a = 10, 20, 30, 40, 50
#    0   1   2   3   4
a[2] = 35         # Tuple is immutable, assigning values is not possible
print(a)          # (10, 20, 30, 40, 50)
print(id(a))      # Prints address of the tuple a
a = a[:2] + (35,) + a[3:]   # Correct way: recreate tuple with 35 instead of 30
print(a)          # (10, 20, 35, 40, 50)
print(id(a))      # Prints new address of the tuple different from a


#  Nested tuple  (Home work)

a = ((10, 20), (30, 40, 50), (60, 70, 80, 90))
print(a)             # ((10, 20), (30, 40, 50), (60, 70, 80, 90))
print(type(a))       # <class 'tuple'>
print(len(a))        # 3, since it has 3 inner tuples
print(a[0])          # Prints 1st inner tuple, (10, 20)
print(a[1])          # Prints 2nd inner tuple, (30, 40, 50)
print(a[2])          # Prints 3rd inner tuple, (60, 70, 80, 90)
print(a[0][1])       # Prints 20 (2nd element of 1st tuple)
print(a[1][2])       # Prints 50 (3rd element of 2nd tuple)
print(a[2][3])       # Prints 90 (4th element of 3rd tuple)


# Find outputs (Home work)

a = ((10, 20, 30),)
print(a[0])        # Prints inner tuple, (10, 20, 30)
print(a[-1])       # Another way to print inner tuple, (10, 20, 30)
print(a[0][0])     # Prints 10 (1st element of inner tuple)
print(a[0][1])     # Prints 20 (2nd element of inner tuple)
print(a[0][2])     # Prints 30 (3rd element of inner tuple)
b = ((),)
print(b[0])        # Prints inner tuple of 'b', ()
print(b[-1])       # Another way to print inner tuple of 'b', ()


# Find outputs (Home work)

a = ((10, 20, 30))    
print(a)        # (10, 20, 30)  
print(*a)       # 10 20 30       
b = (())        
print(b)        # ()             
print(*b)       # Nothing printed, because empty tuple has no elements


# What are the outputs if input is {10 , 20 , 15 , 18 , 20 , 12 , 18}

a = input('Enter Set : ')   # {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(a)                    # {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(a))              # <class 'str'>
b = eval(a)                 # eval() evaluates the string as a set 
print(b)                    # {10, 12, 15, 18, 20}   
print(type(b))              # <class 'set'>


# Find outputs (Home work)

print({(10 , 20 , 30)})     # {(10, 20, 30)} 
print({[10 , 20 , 30]})     # Error list cannot be element of a set
print({{10 , 20 , 30}})     # Error set cannot be element of a set
print({{}})                 # Error dictionary not allowed inside set


# How to print set in different ways (Home work)

a = {25, True, 'Hyd', 10.8}
print('set with print function')
print(a)             # {25, 10.8, 'Hyd', True}
print('Iterate elements of set with for loop')
for i in a:
    print(i)

'''
Output (order may vary):
25
10.8
Hyd
True
'''


# Find outputs (Home work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a, b, c, d, e}
print(s)          # {'Hyd', 25, True}   (duplicates removed, True == 1)
print(len(s))     # 3
print(type(s))    # <class 'set'>


# Find outputs (Home work)
s = {'Hyd', 25, True, 10.8}
print(s)          # {'Hyd', 25, 10.8, True} (order may vary)
a, b, c, d = s
print(a)          # Hyd
print(b)          # 25
print(c)          # 10.8
print(d)          # True


# Find outputs (Home work)
s = {'Hyd', 25, True, 10.8}
print(s)          # {'Hyd', 25, 10.8, True}
a, *b = s
print(a)          # First element 
print(b)          # Remaining elements as list
print(type(b))    # <class 'list'>


# Find outputs (Home work)
s = {'Hyd', 25, True, 10.8}
print(s)          # {'Hyd', 25, 10.8, True}
a, *b, c = s
print(a)          # First element
print(b)          # Middle elements as list
print(c)          # Last element


# Find outputs (Home work)
s = {20, 10, 20, 10}
print(s)          # {10, 20} (duplicates removed)
x, y = s
print(x)          # 10 or 20
print(y)          # 20 or 10


# set() function demo program (Home work)
a = range(100, 151, 10)
b = set(a)
print(b)          # {100, 110, 120, 130, 140, 150}
c = [10, 20, 15, 18, 10, 50, 20, 12, 18]
d = set(c)
print(d)          # {10, 12, 15, 18, 20, 50} (duplicates removed)
e = set('Rama  rAo')
print(e)          # {'R', 'o', 'm', ' ', 'r', 'A', 'a'} (set of unique characters)
print(set(25))    # ERROR due to the 'int' 
print(set())      # set()



