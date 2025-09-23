#  Find  outputs

print({10 , 20}  |  {30 , 20}) #{10,20,30} 

print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'}) # {10:'Hyd',20:'Vja',30:'Cyb'}

print(range(4) | range(5)) # error range wont support 

print([10 , 20]  |  [30 , 20] # error these doesnot support for list



#  Assignment  operators  demo  program  (Home  work)
a = 25 # ref a points to object a i.e 25 
print(a) # 25
b =  (a is  b) # 
x = 4a # ref b points to object a i.e 25 , here ref is modified not the object 
print(b) # 25
print(a 
y = 5
z = x + y * 6 # 4 + 5*6 = 34
print(z) # 34
25 = a # error 
a + b = x + y # error 50 != 9 



# Find outputs (Home work)
a = b = c = 25
print(id(a)) # 25
print(id(b))  #25
print(id(c))  #25
print(a , b , c)  #(25,25,25)


# Multiple  Assignment (Home work)
x , y , z = 25 , 10.8 , 'Hyd'
print(x)  # 25  
print(y)  #10.8
print(z)  #'Hyd'


# Find outputs (Home work)
a , b , c = 3 , 4 , 5
a *= b + c # a=a*(b+c) , i.e means 27
print(a) # 27


# Find outputs (Home work)
a = 20 # ref a points to object a i.e 20 
a %= 3 + 2 * 4  # 20/(3 +2*4 ).i.e is 20/11 = 9 remainder 
print(a) # 9


# Find outputs (Home work)
a = 3 # ref a points to object 3 
a **= 4 # 3 **4 = 81
print(a) # 81 



# Identity operators demo program
a = 25 # ref a points to object a i.e is 25
b = 25 # ref b points to same object i.e is 25 
print(a  is  b) # true
print(a  is  not  b) # false 
print(a == b) # true


# Find outputs (Home work)
a = 25  # ref a points to object 25 
b = 25.0 # ref b points to different object 
print(a  is  b) # false
print(a  is  not  b) # true
print(a == b) # false


# Find outputs (Home work)
a = 'Hyd' # ref a points to object a 
b = 'Hyd' # ref b points to same object i.e 'Hyd'
print(a  is  b) # true 
print(a  is  not  b) # false 
print(a == b) # true 
print() # prints new line 
x = [1 , 2 , 3 , 4] # ref a points to object list x 
y = [1 , 2 , 3 , 4] # ref b points to different object of new list 
print(x is y) # false
print(x  is  not  y) # true
print(x == y) # true 
print() # print new line 
m = (1 , 2 , 3 , 4) # ref m points to object tuple 
n = (1 , 2 , 3 , 4) # ref n points to different  tuple
print(m  is  n) # true 
print(m  is  not  n) # false
print(m == n) # true
print(x == m) # false




# Find outputs (Home work)
x = [1 , 2 , 3 , 4] # ref x points to object list x 
y = [1 , 2 , 4 , 3] # ref y points to object list y 
print(x == y) # false 
a = (4 , 1 , 3 , 2) # ref a points to object  tuple elements 
b = (4 , 2 , 3 , 1) # ref b points to object tuple elements 
print(a == b)  # false 
p = {1 , 2 , 3 , 4} # ref p points to object set 
q = {4 , 1 , 3 , 2} # ref q points to object set 
print(p == q) # true set is an unordered 
m = range(5) # ref m points to object range 0 1 2 3 4 
n = range(5) # ref n points to object range 0 1 2 3 4
print(m == n) #True 



# Find outputs (Home work)
a = [10,20,30] # ref a points to object tuple
b = (10,20,30) # ref b points to object tuple 
print(a  is  b) # false
print(a  ==  b) # false
