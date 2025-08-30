#  Find outputs
print({10 , 20}  |  {30 , 20}) # prints {10, 20, 30}
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'}) # prints {10 : 'Hyd' , 20 : 'Vja' , 30 : 'Sec'}
print(range(4) | range(5)) # Error range cannot be concatenated
print([10 , 20] | [30 , 20]) # Error because '+' should be used to concatenate lists










#  Assignment  operators  demo  program  (Home  work)
a = 25 # ref 'a' is assigned to object 25
print(a) # prints 25
b = a # ref 'b' points where ref 'a' points
print(b) # prints 25
print(a  is  b) # True because both a and b pointing to same object 25
x = 4 # ref 'x' assigned to object 4
y = 5 # ref 'y' assigned to object 5
z = x + y * 6 # ref 'z' is assigned to result of the expression
print(z) # prints 34
25 = a # Error because operand 1 is object but it should be reference
a + b = x + y # Error because operand 1 is expression but it should be reference










# Find outputs (Home work)
a = b = c = 25 # references 'a', 'b' and 'c' are assigned to same object 25
print(id(a)) # prints address of the object 25
print(id(b)) # prints same address of the object 25
print(id(c)) # prints same address of the object 25
print(a , b , c) # prints 25<space>25<space>25









# Multiple  Assignment (Home work)
x , y , z = 25 , 10.8 , 'Hyd' # ref 'a' assigned to object 25, ref 'b' points to object 10.8 and ref 'z' assigned to object 'Hyd'
print(x) # prints 25
print(y) # prints 10.8
print(z) # prints 'Hyd'









# Find outputs (Home work)
a , b , c = 3 , 4 , 5 # ref 'a' is assigned to object 3, ref 'b' points to object 4 and ref 'c' points to object 5
a *= b + c # a = a * (b + c) first () operator b + c i.e.,  4 + 5 = 9 and 3 * 9 = 27 so, ref 'a' is assigned to object 27
print(a) # prints 27 









# Find outputs (Home work)
a = 20 # ref 'a' points to object 20
a %= 3 + 2 * 4 # a = a % (3 + 2 *4),first evaluates expression in bracket i.e., 2 * 4 = 8,  3 + 8 = 11 and 20 % 11 = 9
print(a) # prints 9










# Find outputs (Home work)
a = 3 # ref 'a' points to object 3
a **= 4 # a = a ** 4 i.e., a = 3 ** 4, a = 81
print(a) # prints 81










# Identity operators demo program
a = 25 # ref 'a' points to object 25
b = 25 # ref 'b' points to same object 25
print(a  is  b) # True because a and b both points to same object
print(a  is  not  b) # False because a and b both points to same object
print(a == b) # True because object of a and b are same i.e., 25









# Find outputs (Home work)
a = 25 # ref 'a' points to object 25
b = 25.0 # ref 'b' points to object 25.0
print(a is b) # False because a and b both pointing to different objects 
print(a is not b) # True because a and b both pointing to different objects
print(a == b) # True because objects a and b are same 










# Find outputs (Home work)
a = 'Hyd' # ref 'a' points to object 'Hyd'
b = 'Hyd' # ref 'b' points to object 'Hyd'
print(a  is  b) # True because a and b both pointing to same object 'Hyd'
print(a  is  not  b) # False because a and b both pointing to same object 'Hyd' 
print(a == b) # True because objects of a and b are same
print()
x = [1 , 2 , 3 , 4] # ref 'x' points to list
y = [1 , 2 , 3 , 4] # ref 'y' points to another list
print(x is y) # False because x and y both points to different lists
print(x  is  not  y) # True because x and y both points to different lists
print(x == y) # True because objects of both x and y are same
print()
m = (1 , 2 , 3 , 4) # ref 'm' points to tuple
n = (1 , 2 , 3 , 4) # ref 'n' points to same tuple
print(m  is  n) # True because m and n both points to same tuple
print(m  is  not  n) # False because m and n both points to same tuple
print(m == n) # True because objects of both m and n are same
print(x == m) # False because 'x' is a list and 'm' is a tuple











# Membership operators demo program (Home work)
list = [10 , 20 , 15 , 12 , 18] 
print(15 in list) # True because 15 is present in the list
print(19 in list) # False because 19 is not present in the list
print(14 not in list) # True because 14 is not present in the list
print(15 not in list) # False because 15 is present in the list
s = 'Hyd is green city'
print( 'is' in s) # True because 'is' present in s
print('was' in s) # False because 'was' not present in s
print('g' in s) # True because 'g' is present in s
print('z' in s) # False because 'z' is not present in s
print(' ' in s) # True because ' ' is present in s
print('gre' in s) # True because 'gre' is present in s
print('yd i' in s) # True because 'yd i' is present in s
print('' in s) # False because '' is not present in s
print('' not in s) # True because '' is not present in s










# Find outputs (Home work)
x = [1 , 2 , 3 , 4] # ref 'x' points to list
y = [1 , 2 , 4 , 3] # ref 'y' points to another list
print(x == y) # False because both lists are same but in different order
a = (4 , 1 , 3 , 2) # ref 'a' points to tuple 
b = (4 , 2 , 3 , 1) # ref 'b' points to another tuple
print(a == b) # False because both tuples are same but in different order
p = {1 , 2 , 3 , 4} # ref 'p' points to set
q = {4 , 1 , 3 , 2} # ref 'q' points to another set
print(p == q) # True because both sets are same and set has no order
m = range(5) # ref 'm' points to range object from indexes 0 to 4
n = range(5) # ref 'n' points to another range object from indexes 0 to 4
print(m == n) # True because values in both the ranges are same










# Find outputs (Home work)
a = [10,20,30] # ref 'a' points to list
b = (10,20,30) # ref 'b' points to tuple
print(a  is  b)  # False because a is list and b is tuple
print(a == b) # False because a and b are two different types
