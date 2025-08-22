#  Find  outputs
print({10 , 20}  |  {30 , 20})
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'})
print(range(4) | range(5))   : error 
print([10 , 20]  |  [30 , 20]) : error 
#  Assignment  operators  demo  program  (Home  work)
a = 25
print(a) 25
b =  a
print(b)   25
print(a  is  b)  : yes // true 
x = 4
y = 5
z = x + y * 6
print(z)   
4+30 =34
25 = a   : error
a + b = x + y  : error  
# Find outputs (Home work)
a = b = c = 25
print(id(a))      : 140711434028312
print(id(b))       : 140711434028312
print(id(c))           :  140711434028312
print(a , b , c)
# Find outputs (Home work)
a , b , c = 3 , 4 , 5
a *= b + c
print(a) : 3(4+5)=27
# Find outputs (Home work)
a = 20
a %= 3 + 2 * 4
print(a)  :   9 
# Find outputs (Home work)
a = 3
a **= 4
print(a)   : 81
# Identity operators demo program
a = 25
b = 25
print(a  is  b)   : true 
print(a  is  not  b)  : false 
print(a == b)   : true 
# Find outputs (Home work)
a = 25
b = 25.0
print(a  is  b)        : falsr
print(a  is  not  b)   : ys/ true 
print(a == b)   : true 
# Find outputs (Home work)
a = 'Hyd'
b = 'Hyd'
print(a  is  b)  : yes / true 
print(a  is  not  b)   : false 
print(a == b)  : yes / true 
print()
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 3 , 4]
print(x is y)  : false 
print(x  is  not  y)   : true  
print(x == y)  : true  
print()
m = (1 , 2 , 3 , 4)
n = (1 , 2 , 3 , 4)
print(m  is  n)   : true 
print(m  is  not  n) : fasle
print(m == n) : true 
print(x == m)  : false 

# Membership operators demo program (Home work)
list = [10 , 20 , 15 , 12 , 18]
print(15 in list)   : true 
print(19 in list)   : true 
print(14 not in list)   : true 
print(15 not in list)  : false 
s = 'Hyd is green city'  :
print( 'is' in s)   : true 
print('was' in s)  : true
print('g' in s)  : true 
print('z' in s)   : false 
print(' ' in s) :  true 
print('gre' in s)  : true 
print('yd i' in s) :ttrue 
print('' in s)  “ true 
print('' not in s)  :falsee 

# Find outputs (Home work)
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 4 , 3]
print(x == y)        :false
a = (4 , 1 , 3 , 2) 
b = (4 , 2 , 3 , 1)
print(a == b)  : false
p = {1 , 2 , 3 , 4} 
q = {4 , 1 , 3 , 2}
print(p == q)   : true 
m = range(5)
n = range(5)
print(m == n)  : true 

# Find outputs (Home work)
a = [10,20,30]
b = (10,20,30)
print(a  is  b)    : false 
print(a  ==  b)    : false 



