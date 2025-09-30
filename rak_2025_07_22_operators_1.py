#Pipe Operator
#  Find  outputs
print({10 , 20}  |  {30 , 20})                                #2 set objects are concatanated,{10,20,30}
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'}) #2 dict objects are concatanated, {10:'Hyd', 20:'Vja', 30:'Cyb'}
#print(range(4) | range(5))                                   #TypeError, 2 range objects cannot be concatanated
#print([10 , 20] | [30 , 20])                                 #TypeError, 2 list objects cannot be concatanated with |



#Assignment Operators
#  Assignment  operators  demo  program  (Home  work)
a = 25           #Assigns reference   'a'  to object 25
print(a)         #25
b =  a           #Assigns  ref  'b'  to  the  same object   where  'a'  points
print(b)         #25
print(a  is  b)  #True :  References 'a'  and  'b'  point  to  same  object
x = 4
y = 5
z = x + y * 6    #Assigns  ref  'z' to  object  34
print(z)         #34
#25 = a          #SyntaxError: cannot assign to literal here, 25  is  not  a  reference
#a + b = x + y   #SyntaxError: cannot assign to expression here, a + b  is  not  a  reference, expression gives object

# Find outputs (Home work)
a = b = c = 25   #chained assignment, Assigns  references  a , b  and  c  to  object 25
print(id(a))     #Address  of  object  25 (say 1000)
print(id(b))     #Address  of  object  25 (1000)
print(id(c))     #Address  of  object  25 (1000)
print(a , b , c) #25  <space> 25  <space>  25

# Multiple  Assignment (Home work)
x , y , z = 25 , 10.8 , 'Hyd'   #Multiple  assignment, also called tuple unpacking(elements with , separated)
print(x)                        #25
print(y)                        #10.8
print(z)                        #Hyd

#  Find  outputs
a = 7
print(a , id(a))   #7  <space> Address  of  object  7
a += 5             #a = a + (5)   --->  a = 7 + (5) = 12
print(a , id(a))   #12 <space> Address  of  object  12

# Find outputs (Home work)
a , b , c = 3 , 4 , 5
a *= b + c             # a = a * (b + c)  --->  a =  3 * (4 + 5) = 27
print(a)               # 27

# Find outputs (Home work)
a = 20
a %= 3 + 2 * 4         #a = a % (3 + 2 * 4)   --->  a = 20 % 11 = 9
print(a)               #9

# Find outputs (Home work)
a = 3
a **= 4     #a = a ** (4)  --->  a =  81
print(a)    #81




#Identity Operators
# Identity operators demo program
a = 25               #Assigns  reference  'a'  to  object  25
b = 25               #Assigns  ref  'b'  to  same  object  25
print(a  is  b)      #True  :  References  'a'  and  'b'  point  to  same  object  25
print(a  is  not  b) #False
print(a == b)        #True  :  Objects  'a'  and  'b'  have  same  value   25

# Find outputs (Home work)
a = 25               #Ref  'a'  points  to   int   object  25
b = 25.0             #Ref  'b'  points  to  float object  25.0
print(a  is  b)      #False :  'a'   and  'b'  point  to  different  objects
print(a  is  not  b) #True
print(a == b)        #True :  Objects  'a'  and  'b' have  same  value  i.e.  25  and  25.0

# Find outputs (Home work)
a = 'Hyd'             #Ref  'a'  points  to  object  'Hyd'
b = 'Hyd'             #Ref  'b'  points  to  same  object  'Hyd'
print(a  is  b)       #True  :  References  'a'  and  'b'  point  to  same  object  'Hyd'
print(a  is  not  b)  #False
print(a == b)         #True  : Objects  'a'  and 'b' have  same  string  'Hyd'
print()
x = [1 , 2 , 3 , 4]   #Ref  'x'  points  to  list
y = [1 , 2 , 3 , 4]   #Ref  'y'  points  to  a  different  list  as  list  is  mutable  and  not  reusable
print(x  is  y)       #False  :  References  'x'  and  'y'  point  to  different  lists
print(x  is  not  y)  #True
print(x == y)         #True :  Lists  'x'  and 'y'  have  same  elements
print()
m = (1 , 2 , 3 , 4)   #Ref  'm'  points  to   tuple
n = (1 , 2 , 3 , 4)   #Ref  'n'  points  to  same  tuple
print(m  is  n)       #True  :  References  'm'  and  'n'  point  to  same  tuple
print(m  is  not  n)  #False
print(m == n)         #True  :  Tuples  'm'  and 'n'  have  same  elements
print(x == m)         #False :  References  x  and  m  point  to  different  objects

# Find outputs (Home work)
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 4 , 3]
print(x == y)         # False :  3 == 4  is  False
a = (4 , 1 , 3 , 2)
b = (4 , 2 , 3 , 1)
print(a == b)         # False  :  1 == 2  is  False
p = {1 , 2 , 3 , 4}
q = {4 , 1 , 3 , 2}
print(p == q)         # True :  Sets  p  and  q  have  same  elements
m = range(5)
n = range(5)
print(m == n)         #   True  :  Objects  'm'  and  'n'  have   same  elements

# Find outputs (Home work)
a = [10,20,30]  
b = (10,20,30)  
print(a  is  b) #False, becoz both points to different object
print(a == b)   #False, becoz when objects are different == compares the references



#Memebership Operators
# Membership operators demo program (Home work)
list = [10 , 20 , 15 , 12 , 18]
print(15 in list)         #True
print(19 in list)         #False
print(14 not in list)     #True
print(15 not in list)     #False
s = 'Hyd is green city'
print( 'is' in s)         #True
print('was' in s)         #False
print('g' in s)           #True
print('z' in s)           #False
print(' ' in s)           #True
print('gre' in s)         #True
print('yd i' in s)        #True
print('' in s)            #True : Every  string  has  empty string
print('' not in s)        #False