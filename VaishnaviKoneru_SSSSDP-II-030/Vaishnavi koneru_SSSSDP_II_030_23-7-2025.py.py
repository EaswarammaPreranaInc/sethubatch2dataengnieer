# Assignment  operators  demo  program  (Home  work)
a = 25
print(a) #prints 25 
b =  a
print(b) # prints 25
print(a  is  b) #True because int object is immuatble and can be resued.so,a and b pointing to the same object. 
x = 4
y = 5
z = x + y * 6 
print(z)# 34
25 = a # we cannot assign reference to an object in this way it has to be vice versa
a + b = x + y 
# Find outputs (Home work)
a = b = c = 25
print(id(a))#reference of object 25 
print(id(b))#reference of same object 25
print(id(c))#reference of same object 25  
print(a , b , c)# 25 25 25
# Multiple  Assignment (Home work)
x , y , z = 25 , 10.8 , 'Hyd'
print(x)#25
print(y)#10.8
print(z)#'Hyd'
# Find outputs (Home work)
a , b , c = 3 , 4 , 5
a *= b + c 
print(a)#27
# Find outputs (Home work)
a = 20
a %= 3 + 2 * 4
print(a)#9
# Find outputs (Home work)
a = 3
a **= 4
print(a) #81
# Identity operators demo program
a = 25
b = 25
print(a  is  b)#True because refrences are same and immutable object
print(a  is  not  b)#False because refrences are same and immutable object
print(a == b)#True because both are pointing to the same object 25
# Find outputs (Home work)
a = 25
b = 25.0
print(a  is  b)#False because 25 and 25.0 are of different objects and refrences.
print(a  is  not  b)#True because 25 and 25.0 are of different objects.
print(a == b)#True because 25 and 25.0 are of same value.
# Find outputs (Home work)
a = 'Hyd'
b = 'Hyd'
print(a  is  b) #True because string is immutable and can be reused
print(a  is  not  b)#True because string is immutable and can be reused
print(a == b)#True because they both points to the same object string.
print()
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 3 , 4]
print(x is y)#False beacuse list object is mutable and can be reused
print(x  is  not  y)#True beacuse list object is mutable and can be reused
print(x == y)#False beacuse list object is same and can be reused
print()
m = (1 , 2 , 3 , 4)
n = (1 , 2 , 3 , 4)
print(m  is  n)#True beacuse tuple objects are immutable and can be reused
print(m  is  not  n)#False beacuse tuple objects are immutable and can be reused
print(m == n)#True both are pointing to the same object.
print(x == m)#False because both objects types are different.
# Membership operators demo program (Home work)
list = [10 , 20 , 15 , 12 , 18]
print(15 in list)#True because 15 is in list object.
print(19 in list)#False because 19 is not in list object.
print(14 not in list)#True because 14 is not present in list object.
print(15 not in list)#False because 15 is in list object.
s = 'Hyd is green city'
print( 'is' in s)#True because 'is' is in string s
print('was' in s)#False because 'was' is not in string s
print('g' in s)#True because 'g' is in string s
print('z' in s)#False because 'z' is not in string s
print(' ' in s)#True because '<space>' is in string s
print('gre' in s)#True because 'gre' is in string s
print('yd i' in s)#True because 'yd i' is in string s
print('' in s)#False because 'empty string' is not in string s
print('' not in s)#True because 'empty string' is in any string s
Find  outputs
print({10 , 20}  |  {30 , 20})#output : {10,20,30} after removing duplicates
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'}) #{10 : 'Hyd' , 20 : 'Vja',30 : 'Cyb'}#changes its value at key 20 and previous value is removed automatically by PVM.
print(range(4) | range(5))#range doesnot have this operator to concatinate
print([10 , 20]  |  [30 , 20])#list doesnot have this operator to concatinate
# Find outputs (Home work)
a = [10,20,30]
b = (10,20,30)
print(a  is  b) #False because they both have different sequences 
print(a  ==  b) #False because they both have different sequences

