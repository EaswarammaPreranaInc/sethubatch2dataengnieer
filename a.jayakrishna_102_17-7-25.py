# Find  outputs    (Home  work)

a = range(10 , 50 , 5)
print(type(a)) # type of the object 'a' i.e, <class 'range'>
print(a) # range(10 , 50 , 5)
print(*a) # elements in range (a) i.e, 10 15 20 25 30 35 40 45 
print(id(a)) # address of the object 'a' ex:- 500
print(len(a)) # 8
print(*a[2 : 7] , sep = ' , ') # 20, 25, 30, 35, 40
print(*a[ : : -1]) # 45 40 35 30 25 20 15 10 
a[4] = 32 # error
print(a * 2) # error





#  Find  outputs  (Home  work)
a = range(10 , 20)
print(*a , sep = ',') # 11, 12, 13, 14, 15, 16, 17, 18, 19
b = range(5) 
print(*b) # 0 1 2 3 4 
c = range(10 , 1 , -1)
print(*c , sep = '...') # 10...9...8...7...6...5...4...3...2... 
d = range(-10 , 0)
print(*d) # -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10)
print(*e) #  
f = range(2 , 2)
print(*f) #
g = range(10 , 11 , 0.1) # error 
h = range('A' , 'F') # error




#  Find  outputs  (Home  work)
r = range(10 ,  17 , 3)
a , b , c = r
print(a , b , c) # (10 , 17 , 3)
r = range(3)
x , y = r
p , q  , r , s = r
#a , b , c = *r

