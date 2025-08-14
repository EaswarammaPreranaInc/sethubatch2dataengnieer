# Find  outputs    (Home  work)

a = range(10 , 50 , 5) #reference a is assigned to the range object indexes 10 t0 49 in steps of 5

print(type(a)) #<class 'range'>

print(a) #range(10,50,5)

print(*a) #printed 10 15 20 25 30 35 40 45

print(id(a)) #prints address 

print(len(a)) #8

print(*a[2 : 7] , sep = ' , ') #printed [20,25,30,35,40]

print(*a[ : : -1]) #45 40 35 30 25 20 15 10

a[4] = 32

print(a * 2) #invalid 

#  Find  outputs  (Home  work)
a = range(10 , 20)  #a is assigned to range object 
print(*a , sep = ',') # 10,11,12,13,14,15,16,17,18,19
b = range(5) #0 1 2 3 4 
print(*b) #0 1 2 3 4 
c = range(10 , 1 , -1)  #c is assigned to range object
print(*c , sep = '...') # 10...9...8...7...6...5...4...3...2
d = range(-10 , 0)
print(*d) #-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10) #invalid
print(*e) #invalid
f = range(2 , 2)
print(*f)
g = range(10 , 11 , 0.1) #error due to steps must be integer but not float number
h = range('A' , 'F') #range contains only integer not string

#  Find  outputs  (Home  work)
r = range(10 ,  17 , 3) # r reference is assigned to range object
a , b , c = r #a=10, b=13, c=16
print(a , b , c) #10 13 16
r = range(3) #created elements 0 1 2
x , y = r #invalid
p , q  , r , s = r #error
a , b , c = *r #invalid
