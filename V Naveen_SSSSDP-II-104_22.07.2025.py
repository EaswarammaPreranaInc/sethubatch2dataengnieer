#1. Find outputs
print({10 , 20}  |  {30 , 20}) # {10, 20, 30}
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'}) # {10: 'Hyd', 20: 'Vja', 30: 'Cyb'}
print(range(4) | range(5)) # range objects do not support the | operator
print([10 , 20]  |  [30 , 20]) # Lists do not support the | operator

#2.  Assignment  operators  demo  program  (Home  work)
a = 25
print(a) # 25 8977311856
b =  a
print(b) # 25
print(a  is  b) # True
x = 4
y = 5
z = x + y * 6
print(z) # 34
25 = a
a + b = x + y

#3.  Find outputs (Home work)
a = b = c = 25
print(id(a)) # Address of object a
print(id(b)) # Address of object b is the same as a
print(id(c)) # Address of object c is the same as b
print(a , b , c) # 25 25 25

#4. Multiple  Assignment (Home work)
x , y , z = 25 , 10.8 , 'Hyd'
print(x) # 25
print(y) # 10.8
print(z) # 'Hyd'

#5. Find outputs (Home work)
a , b , c = 3 , 4 , 5
a *= b + c # 3*9
print(a) # 27

#6. Find outputs (Home work)
a = 20
a %= 3 + 2 * 4
print(a) # 9

#7. Find outputs (Home work)
a = 3
a **= 4 # =a=a**4=3**4
print(a) # 81

#8. Identity operators demo program
a = 25
b = 25
print(a  is  b) # True
print(a  is  not  b) # False
print(a == b) # True

#9. Find outputs (Home work)
a = 25
b = 25.0
print(a  is  b) # False a is int, b is float
print(a  is  not  b) # True
print(a == b) # True

# 10.Find outputs (Home work)
a = 'Hyd'
b = 'Hyd'
print(a  is  b) # True
print(a  is  not  b) # False
print(a == b) # True
print()
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 3 , 4]
print(x is y) # False
print(x  is  not  y) # True
print(x == y) # True
print()
m = (1 , 2 , 3 , 4)
n = (1 , 2 , 3 , 4)
print(m  is  n) # True
print(m  is  not  n) # False
print(m == n) # True
print(x == m) # False

#11. Membership operators demo program (Home work)
list = [10 , 20 , 15 , 12 , 18]
print(15 in list) # True as 15 is present in the list
print(19 in list) # False as 19 is not present in the list
print(14 not in list) # True as it is not present in the list
print(15 not in list) # False as it is present in the list
s = 'Hyd is green city'
print( 'is' in s) # True as 'is' is present in s
print('was' in s) # False as 'was' is not present in s
print('g' in s)   # True as 'g' is present in s
print('z' in s)   # False as 'z' is not present in s
print(' ' in s)   # True as '' is present in s
print('gre' in s) # True as 'gre' is present in s
print('yd i' in s)# True 'yd i' is present in s
print('' in s)    # True '' is present in s
print('' not in s)# False '' is present in s

#12. Find outputs (Home work)
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 4 , 3]
print(x == y) # False because the elements are different in both lists
a = (4 , 1 , 3 , 2)
b = (4 , 2 , 3 , 1)
print(a == b) # False because the elements are different in both lists
p = {1 , 2 , 3 , 4}
q = {4 , 1 , 3 , 2}
print(p == q) # True because the set contains unordered in this both sets have the same elements
m = range(5)
n = range(5)
print(m == n) # True if the start, end are the same



#13. Find outputs (Home work)
a = [10,20,30]
b = (10,20,30)
print(a  is  b) # False 'a' is a list b is tuple
print(a  ==  b) # False 'a' is a list b is tuple