# Find  outputs    (Home  work)

a = range(10 , 50 , 5)

print(type(a)) #<class range>

print(a) # range(10,50,5)

print(*a) #10 15 20 25 30 35 40 45

print(id(a)) #memoryaddress of ref a

print(len(a)) #8

print(*a[2 : 7] , sep = ' , ')  # 20,25,30,35,40

print(*a[ : : -1]) # 45 40 35 30 25 20 15 10

a[4] = 32 # error range object is immutable

print(a * 2) # no repeat error

#  Find  outputs  (Home  work)
a = range(10 , 20) # range(10,20,1)
print(*a , sep = ',') # 10,11,12,13,14,15,16,17,18,19
b = range(5) # range(0,5,1)
print(*b) # 0 1 2 3 4
c = range(10 , 1 , -1) # 10...9...8...7...6...5...4...3...2
print(*c , sep = '...')
d = range(-10 , 0)  # range(-10,0,1)
print(*d) # -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10)  # range(0,-10,1)
print(*e) # empty
f = range(2 , 2)  #range(2,2,1)
print(*f) #  empty
g = range(10 , 11 , 0.1)
h = range('A' , 'F')

#  Find  outputs  (Home  work)
r = range(10 ,  17 , 3)  r=[10,13,16]
a , b , c = r  # unpacking the r with seperate variables
print(a , b , c) # 10 13 16 
r = range(3)  # [0,1,2]
x , y = r  # to many values unpacking
p , q  , r , s = r  #not enough the values to unpack
a , b , c = *r  # error
