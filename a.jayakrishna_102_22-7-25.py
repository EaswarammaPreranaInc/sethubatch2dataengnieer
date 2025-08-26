print({10 , 20}  |  {30 , 20}) # '|' operator to remove a duplicate {10, 20, 30}
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'}) # remove a duplicate in second dict  ({10: 'Hyd',20: 'Vja',30: 'Cyb'})
#print(range(4) | range(5)) #Error due to not supported two range
#print([10 , 20]  |  [30 , 20]) # Error due to ' | ' is not valid for list operator


#  Assignment  operators  demo  program  (Home  work)
a = 25 # 'a' assig the value of 25
print(a) # print the object of 'a'  25
b =  a  #'b' is assig the value of 'a' 
print(b)  # print the object of 'b'  25
print(a  is  b)  #'a' is 'b'  True
x = 4  
y = 5
z = x + y * 6    # z = 4 + (5 * 6) = 34
print(z)  # print the value of 'z'  34
25 = a  # Error 
a + b = x + y  #Error 





# Find outputs (Home work)
a = b = c = 25  #a,b,c is all the one value is '25'
print(id(a))   # print the addres of object 'a'  123456789
print(id(b))   # print the addres of object 'b'  123456789 same addres of a
print(id(c))    # print the addres of object 'c'  123456789 same addres of a,b
print(a , b , c)  # print the a,b,c values i.e. 25




# Multiple  Assignment (Home work)
x , y , z = 25 , 10.8 , 'Hyd'
print(x)  # print the value of x i.e. 25
print(y)  #print the value of y i.e. 10.8
print(z)   # print the value of z i.e. 'Hyd'






# Find outputs (Home work)
a , b , c = 3 , 4 , 5
a *= b + c    # b+c=4+5=9 so *=  => a=a*9 =3 * 9 = 27
print(a)  #print the value of a i.e. 27





# Find outputs (Home work)
a = 20
a %= 3 + 2 * 4  # 2 * 4 =8 ,3 + 8 = 11
print(a) # output is 11





# Find outputs (Home work)
a = 3
a **= 4  # 3 ** 4 = 81
print(a)  #output is 81




# Identity operators demo program
a = 25
b = 25
print(a  is  b)  #True
print(a  is  not  b)  #False
print(a == b)  #True



# Find outputs (Home work)
a = 25
b = 25.0
print(a  is  b)  # False
print(a  is  not  b)  # True
print(a == b)   #True




# Find outputs (Home work)
a = 'Hyd'
b = 'Hyd'
print(a  is  b)  # True
print(a  is  not  b)  #False
print(a == b)  # True
print() # empty space
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 3 , 4]
print(x is y)  # True
print(x  is  not  y)  #False
print(x == y)  #True
print()  #Empty space
m = (1 , 2 , 3 , 4)
n = (1 , 2 , 3 , 4)
print(m  is  n)  # True
print(m  is  not  n)  # False
print(m == n)  # True 
print(x == m)   #True





# Membership operators demo program (Home work)
list = [10 , 20 , 15 , 12 , 18]
print(15 in list)   # True
print(19 in list)   # False
print(14 not in list)   #True
print(15 not in list)   # False
s = 'Hyd is green city'
print( 'is' in s)  #True
print('was' in s)   #False
print('g' in s)  #True
print('z' in s)   #False
print(' ' in s)  #True
print('gre' in s)  #True
print('yd i' in s)  #True
print('' in s)   #True
print('' not in s)   #False




# Find outputs (Home work)
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 4 , 3]
print(x == y)        #False
a = (4 , 1 , 3 , 2)
b = (4 , 2 , 3 , 1)
print(a == b)        #False
p = {1 , 2 , 3 , 4}
q = {4 , 1 , 3 , 2}
print(p == q)        #True
m = range(5)
n = range(5)
print(m == n)     #True





# Find outputs (Home work)
a = [10,20,30]
b = (10,20,30)
print(a  is  b)    # False
print(a  ==  b)  #False