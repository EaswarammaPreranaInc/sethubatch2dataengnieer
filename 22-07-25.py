
#first program
print({10 , 20}  |  {30 , 20})
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'})
#print(range(4) | range(5))
#print([10 , 20]  |  [30 , 20])

#second program
#  Assignment  operators  demo  program  (Home  work)
a = 25
print(a)
b =  a
print(b)
print(a  is  b)
x = 4
y = 5
z = x + y * 6
print(z)
#25 = a
#a + b = x + y

#third program
a = b = c = 25
print(id(a))
print(id(b))
print(id(c))
print(a , b , c)

#fourth program
# Multiple  Assignment (Home work)
x , y , z = 25 , 10.8 , 'Hyd'
print(x)
print(y)
print(z)

#fifth program
a , b , c = 3 , 4 , 5
a *= b + c
print(a)

#sixth program
a = 20
a %= 3 + 2 * 4
print(a)

#seventh program
a = 3
a **= 4
print(a)

#eighth program
# Identity operators demo program
a = 25
b = 25
print(a  is  b)
print(a  is  not  b)
print(a == b)

#ninth program
a = 25
b = 25.0
print(a  is  b)
print(a  is  not  b)
print(a == b)

#tenth program
a = 'Hyd'
b = 'Hyd'
print(a  is  b)
print(a  is  not  b)
print(a == b)
print()
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 3 , 4]
print(x is y)
print(x  is  not  y)
print(x == y)
print()
m = (1 , 2 , 3 , 4)
n = (1 , 2 , 3 , 4)
print(m  is  n)
print(m  is  not  n)
print(m == n)
print(x == m)

#eleventh program
# Membership operators demo program (Home work)
list = [10 , 20 , 15 , 12 , 18]
print(15 in list)
print(19 in list)
print(14 not in list)
print(15 not in list)
s = 'Hyd is green city'
print( 'is' in s)
print('was' in s)
print('g' in s)
print('z' in s)
print(' ' in s)
print('gre' in s)
print('yd i' in s)
print('' in s)
print('' not in s)

#twelfth program
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 4 , 3]
print(x == y)
a = (4 , 1 , 3 , 2)
b = (4 , 2 , 3 , 1)
print(a == b)
p = {1 , 2 , 3 , 4}
q = {4 , 1 , 3 , 2}
print(p == q)
m = range(5)
n = range(5)
print(m == n)

#thirteenth program
a = [10,20,30]
b = (10,20,30)
print(a  is  b) 
print(a  ==  b)