#  Find  outputs

print({10 , 20}  |  {30 , 20})  # {10, 20, 30} 
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'})  # {10: 'Hyd', 20: 'Vja', 30: 'Cyb'} 
print(range(4) | range(5))  # Error 
print([10 , 20]  |  [30 , 20])  #Error 

#  Assignment  operators  demo  program  (Home  work)

a = 25
print(a)  # 25
b = a
print(b)  # 25
print(a is b)  # True 
x = 4
y = 5
z = x + y * 6
print(z)  # 34 
25 = a  # Error 
a + b = x + y  # Error 

# Find outputs (Home work)
a = b = c = 25  # all three variables point to the same integer object
print(id(a))  # prints memory address of 25
print(id(b))  # same as id(a)
print(id(c))  # same as id(a) and id(b)
print(a , b , c)  # 25 25 25

# Multiple  Assignment (Home work)
x , y , z = 25 , 10.8 , 'Hyd'
print(x)  # 25
print(y)  # 10.8
print(z)  # Hyd

# Find outputs (Home work)
a , b , c = 3 , 4 , 5
a *= b + c  # 27
print(a)  # 27

# Find outputs (Home work)
a = 20
a %= 3 + 2 * 4  # 9
print(a)  # 9

# Find outputs (Home work)
a = 3
a **= 4  # 81
print(a)  # 81

# Identity operators demo program
a = 25
b = 25
print(a is b)  # True 
print(a is not b)  # False 
print(a == b)  # True 

# Identity operators demo program
a = 25
b = 25
print(a is b)  # True 
print(a is not b)  # False 
print(a == b)  # True 
# Find outputs (Home work)
a = 25
b = 25.0
print(a is b)  # False 
print(a is not b)  # True 
print(a == b)  # True 

# Find outputs (Home work)
a = 'Hyd'
b = 'Hyd'
print(a is b)  # True 
print(a is not b)  # False 
print(a == b)  # True 
print()
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 3 , 4]
print(x is y)  # False 
print(x is not y)  # True 
print(x == y)  # True 
print()
m = (1 , 2 , 3 , 4)
n = (1 , 2 , 3 , 4)
print(m is n)  # True 
print(m is not n)  # False 
print(m == n)  # True 
print(x == m)  # False 

# Membership operators demo program (Home work)
list = [10 , 20 , 15 , 12 , 18]
print(15 in list)  # True 
print(19 in list)  # False 
print(14 not in list)  # True 
print(15 not in list)  # False 
s = 'Hyd is green city'
print('is' in s)  # True 
print('was' in s)  # False 
print('g' in s)  # True 
print('z' in s)  # False 
print('gre' in s)  # True 
print('' in s)  # True 
print('' not in s)  # False 

# Find outputs (Home work)
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 4 , 3]
print(x == y)  # False 
a = (4 , 1 , 3 , 2)
b = (4 , 2 , 3 , 1)
print(a == b)  # False 
p = {1 , 2 , 3 , 4}
q = {4 , 1 , 3 , 2}
print(p == q)  # True 
m = range(5)
n = range(5)
print(m == n)  # True 

# Find outputs (Home work)
a = [10, 20, 30]
b = (10, 20, 30)
print(a is b)  # False 
print(a == b)  # False
