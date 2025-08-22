# Find  outputs    (Home  work)


a = range(10 , 50 , 5) #
print(type(a)) #<Class 'range'>
print(a) # range(10, 50, 5)
print(*a) # 10 15 20 25 30 35 40 45
print(id(a)) # Address of 'a'
print(len(a)) # 8 (10 15 20 25 30 35 40 45)
print(*a[2 : 7] , sep = ' , ') #20,25,30,35,40
print(*a[ : : -1]) #45 40 35 30 25 20 15 10
a[4] = 32 # adding the value is not possible in range as it is immutable 
print(a * 2) #range object can't be multiplied 

#  Find  outputs  (Home  work)
a = range(10 , 20)
print(*a , sep = ',') # 10,11,12,13,14,15,16,17,18,19
b = range(5)          # b=range(0:5:1)
print(*b)             # 0 1 2 3 4
c = range(10 , 1 , -1)
print(*c , sep = '...')#10...9...8...7...6...5...4...3...2
d = range(-10 , 0)
print(*d) #-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10) 
print(*e)      #0 to -10 not valid with +1 step- Empty
f = range(2 , 2)
print(*f)       # Empty 
g = range(10 , 11 , 0.1) # Not valid as in range only integers are accepted
h = range('A' , 'F') # Not valid as in range only integers are accepted

#  Find  outputs  (Home  work)
r = range(10 ,  17 , 3) # 10 13 16
a , b , c = r # a=10, b=13,c=16
print(a , b , c) #10 13 16
r = range(3) #In this, the range is 3, so we need 3 objects: x,y,z
x, y = r # There are 2 objects, so not possible
p , q  , r , s = r # They are 4 Objects so not possible
#a , b , c = *r # It can not be done as unpacks

