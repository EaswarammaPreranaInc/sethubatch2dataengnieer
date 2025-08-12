a = 25
print(a)# prints a
b =  a# the reference b points to reference a and refernce a points to object 25
print(a  is  b)# operators compared with is 
x = 4
y = 5
z = x + y * 6#* is performs first and then + opertor
print(z)#5*6=30,30+4=34
#25 = a becoz int cant be an reference
#a + b = x + y expressions cant be compared
 a = b = c = 25
print(id(a))# prints address of a
print(id(b))# prints address of b
print(id(c))# prints address of c
print(a,b,c)# prints a b c


x , y , z = 25 , 10.8 , 'Hyd'
print(x)# prints x assigns to 25
print(y)# prints y assigns to 10.8
print(z)# prints z assigns to hyd


a , b , c = 3 , 4 , 5
a *= b+c
print(a)# prints b+c(4+5)=9,a*9(3*9)=27

a = 20
a %= 3+2*4
print(a)# prints first 2*4=8 and then 8+3=11 and the remainder is 9

a = 3
a **= 4
print(a)# prints 3 power of 4

# Identity operators demo program
a = 25
b = 25
print(a  is  b)#opertors are compared with is 
print(a  is  not  b)
print(a==b)

# Find outputs (Home work)
a = 25
b = 25.0
print(a  is  b)# if a and b is asitis it is true another words its false 
print(a  is  not  b)
print(a==b)# its jst compare the values
print()

# Find outputs (Home work)
a = 'Hyd'
b = 'Hyd'
print(a  is  b)# prints true becoz a is exactly to b
print(a  is  not  b)#prints false becoz a and b are pointing to same obejct 'Hyd'
print(a==b)#prints true becoz a is exactly to b
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 3 , 4]
print(x is y)#prints false because x one list  and y is another list becuase list is mutable it can be change'''
print(x  is  not  y)#prints  true x is not y
print(x == y)#prints true becoz it jst compares the values of the list
m = (1 , 2 , 3 , 4)
n = (1 , 2 , 3 , 4)
print(m  is  n)# prints true becoz m and n are pointing to same object
print(m  is  not  n)#prints false becoz m ad n are two defferent references 
print(m==n)# true becoz valuse are equal 
print(x==m)# false becoz x is list and m is tuple so cant be compared

print()
# Membership operators demo program (Home work)
list = [10 , 20 , 15 , 12 , 18]
print(15 in list)# prints true becoz 15 is there
print(19 in list)#  prints false becoz 19 is not there
print(14 not in list)#true
print(15 not in list)#flase
s = 'Hyd is green city'
print()
print( 'is' in s)# true
print('was' in s)#false
print('g' in s)#true
print('z' in s)#false
print(' ' in s)#true
print('gre' in s)#true
print('yd i' in s)#true
print('' in s)#true
print(' ' not in s)#false


print()
# Find outputs (Home work)
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 4 , 3]
print(x==y)# prints true
a = (4 , 1 , 3 , 2)
b = (4 , 2 , 3 , 1)
print(a == b)#prints true
p = {1 , 2 , 3 , 4}
q = {4 , 1 , 3 , 2}
print(p == q)#prints true
m = range(5)
n = range(5)
print(m==n)#prints true

