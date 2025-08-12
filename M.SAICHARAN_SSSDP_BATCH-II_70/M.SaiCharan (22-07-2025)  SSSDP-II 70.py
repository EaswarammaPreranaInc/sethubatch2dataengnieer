1.#  Find  outputs
print({10 , 20}  |  {30 , 20})                        # {10, 20, 30} (removes duplicates)
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'})# {10: 'Hyd', 20: 'Vja', 30: 'Cyb'}
print(range(4) | range(5))                             # Error because unsupported operand type(s) for |: 'range' and 'range'
print([10 , 20]  |  [30 , 20])                         # Error because unsupported operand type(s) for |: 'list' and 'list'




2.#  Assignment  operators  demo  program  (Home  work)
a = 25                                  # Assigns 25 to Reference 'a'
print(a)                                # 25
b =  a                                  # Assigns the value of 'a' to 'b'
print(b)                                # 25
print(a  is  b)                         # True because 'a' and 'b' refers to same object
x = 4                                   
y = 5
z = x + y * 6                           # 4 + 5 * 6 = 4 + 30 = 34
print(z)                                # 34
25 = a                                  # Error
a + b = x + y                           # Error




3.# Find outputs (Home work)
a = b = c = 25                       # All three References are assigned to same object 25          
print(id(a))                         # Address of 'a' may be 1000
print(id(b))                         # Same Address
print(id(c))                         # Same Address
print(a , b , c)                     # 25 25 25.




4.# Multiple  Assignment (Home work)
x , y , z = 25 , 10.8 , 'Hyd'        
print(x)                           # 25    (integer)
print(y)                           # 10.8   (Float)
print(z)                           # 'Hyd'  (String)




5.# Find outputs (Home work)
a , b , c = 3 , 4 , 5             # a = 3
                                  # b = 4
                                  # c = 5

a *= b + c                        # a = 3 * (4 + 5)
                                  # a = 3 * 9 = 27                  
print(a)                          # 27.




6.# Find outputs (Home work)
a = 20
a %= 3 + 2 * 4                   # a %= 3 + 8 = 11
print(a)                         # a = a%11 
                                 #  a = 20 % 11 = 9.




7.# Find outputs (Home work)
a = 3               
a **= 4                          # a = a ** 4
                                 # a = 3 ** 4
print(a)                         # a = 81.




8.# Identity operators demo program
a = 25                           # Reference 'a' is assigned to object 25
b = 25                           # Reference 'b' is assigned to object 25
print(a  is  b)                  # True because both 'a' and 'b' refers to same object 25.
print(a  is  not  b)             # False 
print(a == b)                    # True both 'a' and 'b' are Equal.




9.# Find outputs (Home work)
a = 25                           # Reference 'a' is points to 'int'object 25             
b = 25.0                         # Reference 'b' is points to 'Float' object 25.0
print(a  is  b)                  # False because 'int and 'Float' are not same.
print(a  is  not  b)             # True completely opposite of is.
print(a == b)                    #True 25 == 25.0




10.# Find outputs (Home work)
a = 'Hyd'
b = 'Hyd'
print(a  is  b)                # True  because 'a' and 'b' points to same memory   
print(a  is  not  b)           # False because it is quite opposite of above.
print(a == b)                  # True  both 'a' and 'b' are having same objects 
print()
x = [1 , 2 , 3 , 4]            # Here X is first list 
y = [1 , 2 , 3 , 4]            # Here y is new list with same list values of X
print(x is y)                  # False because X and Y two seperate list objects
print(x  is  not  y)           # True  
print(x == y)                  # True 
print()
m = (1 , 2 , 3 , 4)            
n = (1 , 2 , 3 , 4)
print(m  is  n)                # True because both M and n object values are same            
print(m  is  not  n)           # False because quite opposite of is.
print(m == n)                  # True both m and n are equal
print(x == m)                  # False




11.# Membership operators demo program (Home work)
list = [10 , 20 , 15 , 12 , 18]
print(15 in list)                # True
print(19 in list)                # False
print(14 not in list)            # True
print(15 not in list)            # False
s = 'Hyd is green city' 
print( 'is' in s)                # True
print('was' in s)                # False
print('g' in s)                  # True
print('z' in s)                  # False
print(' ' in s)                  # True
print('gre' in s)                # True
print('yd i' in s)               # True
print('' in s)                   # True
print('' not in s)               # False




12.# Find outputs (Home work)
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 4 , 3]
print(x == y)                    # False
a = (4 , 1 , 3 , 2)
b = (4 , 2 , 3 , 1)
print(a == b)                    # False
p = {1 , 2 , 3 , 4}
q = {4 , 1 , 3 , 2}
print(p == q)                    # True
m = range(5)
n = range(5)
print(m == n)                    # True
 



13.# Find outputs (Home work)
a = [10,20,30]                  # Here a is list object 
b = (10,20,30)                  # Here b is tuple object
print(a  is  b)                 # False 
print(a  ==  b)                 # False