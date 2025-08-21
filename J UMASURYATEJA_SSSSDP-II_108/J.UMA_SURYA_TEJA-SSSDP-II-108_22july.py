print({10 , 20} | {30 , 20}) # {10, 20, 30}
print({10 : 'Hyd' , 20 : 'Sec'} | {30 : 'Cyb' , 20 : 'Vja'}) # {10: 'Hyd', 20: 'Vja', 30: 'Cyb'}
#print(range(4) | range(5)) # TypeError
#print([10 , 20] | [30 , 20]) # TypeError
a = 25
print(a) # 25
b = a
print(b) # 25
print(a is b) # True (because a and b refer to the same object)
x = 4
y = 5
z = x + y * 6
print(z) # 34 (because y * 6 is evaluated first, resulting in 30, then x + 30 is 34)
#25 = a # SyntaxError: cannot assign to literal
#a + b = x + y # SyntaxError: cannot assign to expression
a = b = c = 25
print(id(a)) # some id (e.g., 140244044795472), ids may vary
print(id(b)) # same id as a (e.g., 140244044795472)
print(id(c)) # same id as a and b (e.g., 140244044795472)
print(a , b , c) # 25 25 25
x , y , z = 25 , 10.8 , 'Hyd'
print(x) # 25
print(y) # 10.8
print(z) # Hyd
a , b , c = 3 , 4 , 5
a *= b + c
print(a) # 27
a = 20
a %= 3 + 2 * 4
print(a) # 9
a = 3
a **= 4
print(a) # 81
a = 25
b = 25
print(a is b) # True 
print(a is not b) # False
print(a == b) # True (because a and b have the same value)
a = 25
b = 25.0
#print(a is b) # False (because a is an integer and b is a float, so they are different objects)
print(a is not b) # True
print(a == b) # True (because a and b have the same numeric value)
a = 'Hyd'
b = 'Hyd'
print(a is b) # True 
print(a is not b) # False
print(a == b) # True
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 3 , 4]
#print(x is y) # False (because x and y are different list objects)
print(x is not y) # True
print(x == y) # True (because x and y have the same elements)
m = (1 , 2 , 3 , 4)
n = (1 , 2 , 3 , 4)
print(m is n) # True 
print(m is not n) # False
print(m == n) # True
print(x == m) # True
list = [10 , 20 , 15 , 12 , 18]
print(15 in list) # True
print(19 in list) # False
print(14 not in list) # True
print(15 not in list) # False
s = 'Hyd is green city'
print('is' in s) # True
print('was' in s) # False
print('g' in s) # True
print('z' in s) # False
print(' ' in s) # True
print('gre' in s) # True
print('yd i' in s) # True
print('' in s) # True 
print('' not in s) # False
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 4 , 3]
print(x == y) # False 
a = (4 , 1 , 3 , 2)
b = (4 , 2 , 3 , 1)
print(a == b) # False 
p = {1 , 2 , 3 , 4}
q = {4 , 1 , 3 , 2}
print(p == q) # True 
m = range(5)
n = range(5)
print(m == n) # True
a = [10,20,30]
b = (10,20,30)
print(a is b) # False (because a is a list and b is a tuple, so they are different objects)
print(a == b) # False (because a and b are different types, even though they have the same elements)
