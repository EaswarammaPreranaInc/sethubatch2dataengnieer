print({10 , 20}  |  {30 , 20}) # pipe operator concatemates the set an set removes the duplicates
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'}) # pipe operator concatemates the dict and dict removes the duplicates
#print(range(4) | range(5)) # pipe operator concatenates the range and range removes the duplicates
#print([10 , 20]|[30,20]) # error: pipe operator cannot be used with list

a = 25 # assigns reference a to object 25
print(a) # prints 25
b =  a # assigns reference b to the same object which a is pointed to i.e 25
print(b) # prints 25
print(a  is  b) # prints True as both a and b are pointing to the same object
x = 4 # assigns reference x to object 4
y = 5 # assigns reference y to object 5
z = x + y * 6 # does the arithmetic operation and assigns the result to z
print(z) # prints 34 as 4 + 5 * 6 = 4 + 30 = 34
#25 =a # error: operand 1 cant be a object
#a+b=x+y # error: operand 1 cant be a object

a = b = c = 25 # assigns reference a, b, c to the same object 25
print(id(a)) # prints the memory address of the object 25
print(id(b)) # prints the same address of the object 25
print(id(c)) # prints the same address of the object 25
print(a,b,c) # prints 25 25 25 with default separator space

x , y , z = 25 , 10.8 , 'Hyd' # assigns 25 to x, 10.8 to y, and 'Hyd' to z
print(x)    # prints 25
print(y)    # prints 10.8
print(z)    # prints 'Hyd'

a , b , c = 3 , 4 , 5 # multiple assignment assigns 3 to a, 4 to b, and 5 to c
a *= b+c # a = a * (b + c) i.e a = 3 * (4 + 5) = 3 * 9 = 27
print(a) # prints 27

a = 20 # assigns reference a to object 20
a %= 3 + 2 *4 # a = a % (3 + 2 * 4) i.e a = 20 % (3 + 8) = 20 % 11 = 9
print(a) # prints 9

a = 3 # assigns reference a to object 3
a **= 4 # a = a ** 4 i.e a = 3 ** 4 = 81
print(a) # prints 81

a = 25 # assigns reference a to object 25
b = 25  # assigns reference b to object 25
print(a  is  b) # prints True as both a and b are pointing to the same object
print(a  is  not  b) # prints False as both a and b are pointing to the same object
print(a==b) # prints True as both a and b have the same value

a = 25 # assigns reference a to object 25
b = 25.0 # assigns reference b to object 25.0
print(a  is  b) # prints False as a and b are different objects (int and float)
print(a  is  not  b) # prints True as a and b are different objects
print(a==b) # prints True as both a and b have the same value (25 == 25.0)

a = 'Hyd' # assigns reference a to the string 'Hyd'
b = 'Hyd' # assigns reference b to the string 'Hyd'
print(a  is  b) # prints True as both a and b are pointing to the same string object
print(a  is  not  b) # prints False as both a and b are pointing to the same string object
print(a == b) # prints True as both a and b have the same value
print() # prints a new empty line
x = [1 , 2 , 3 , 4] # assigns reference x to the list [1, 2, 3, 4]
y = [1 , 2 , 3 , 4] # assigns reference y to another list [1, 2, 3, 4]
print(x is y) # prints False as x and y are different list objects
print(x  is  not  y) # prints True as x and y are different list objects
print(x == y) # prints True as both x and y have the same values
print() # prints a new empty line
m = (1 , 2 , 3 , 4) # assigns reference m to the tuple (1, 2, 3, 4)
n = (1 , 2 , 3 , 4) # assigns reference n to another tuple (1, 2, 3, 4)
print(m  is  n) # prints truwue as m and n are pointing to the same tuple object
print(m  is  not  n) # prints False as m and n are pointing to the same tuple object
print(m == n) # prints True as both m and n have the same values
print(x==m) # prints False as x is a list and m is a tuple, even though they have the same values


list = [10 , 20 , 15 , 12 , 18] # assigns reference list to the list [10, 20, 15, 12, 18]
print(15 in list) # prints True as 15 is present in the list
print(19 in list) # prints False as 19 is not present in the list
print(14 not in list) # prints True as 14 is not present in the list
print(15 not in list) # prints False as 15 is present in the list
s = 'Hyd is green city' # assigns reference s to the string 'Hyd is green city'
print( 'is' in s) # prints True as 'is' is present in s
print('was' in s) # prints False as 'was' is not present in s
print('g' in s) # prints True as 'g' is present in s
print('z' in s) # prints False as 'z' is not present in s
print(' ' in s) # prints True as space is present in s
print('gre' in s) # prints True as 'gre' is there in s
print('yd i' in s) # prints True as 'yd i' is there in s
print('' in s) # true because empty string is always there in any string
print('' not in s) # false because empty string is always there in any strin



x = [1 , 2 , 3 , 4] # assigns reference x to the list [1, 2, 3, 4]
y = [1 , 2 , 4 , 3] # assigns reference y to another list [1, 2, 4, 3]
print(x == y)  # prints False as x and y have different values
a = (4 , 1 , 3 , 2) # assigns reference a to the tuple (4, 1, 3, 2)
b = (4 , 2 , 3 , 1) # assigns reference b to another tuple (4, 2, 3, 1)
print(a == b) # prints False as a and b have different values
p = {1 , 2 , 3 , 4} # assigns reference p to the set {1, 2, 3, 4}
q = {4 , 1 , 3 , 2} # assigns reference q to another set {4, 1, 3, 2}
print(p == q) # prints True as sets are unordered and contain the same elements
m = range(5) # assigns reference m to the range object  from 0 to 4
n = range(5) # assigns reference n to another range object from 0 to 4
print(m==n) # prints True as both m and n represent the same range of numbers

a = [10,20,30] # assigns reference a to the list [10, 20, 30]
b = (10,20,30) # assigns reference b to the tuple (10, 20, 30)
print(a  is  b)  # prints False as a is a list and b is a tuple, they are different types
print(a==b) # prints False as a and b have different types (list vs tuple)