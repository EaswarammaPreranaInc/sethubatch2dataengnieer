# Find  outputs    (Home  work)
a = range(10 , 50 , 5)
print(type(a)) # <class 'range'>
print(a) # range(10 , 50 , 5)
print(*a) # 10 <space> 15 <space> 20 <space> 25 <space> 30 <space> 35 <space> 40 <space> 45 <space>
print(id(a)) # addres of range object 'a'
print(len(a)) # 8
print(*a[2 : 7] , sep = ' , ') # a[2 : 7 : 1] --> from indexes 2 to 6 in steps of 1 ---> 20 , 25 , 30 , 35 , 40 , 45 
print(*a[ : : -1]) # a[-1 : -9 : -1]--> from indexes -1 to -8 in steps of -1 ---> 45 <space> 40 <space> 35 <space> 30 <space> 25 <space> 20 <space> 15 <space> 10 <space>
a[4] = 32 # error becoz range object is not modified
print(a * 2) # error becoz range object cannot be repeated becoz it can not have duplicates

#  Find  outputs  (Home  work)
a = range(10 , 20)
print(*a , sep = ',') # 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19
b = range(5)
print(*b) # 0 <space> 1 <space> 2 <space> 3 <space> 4
c = range(10 , 1 , -1) 
print(*c , sep = '...') # 10...9...8...7...6...5...4...3...2
d = range(-10 , 0)
print(*d) # -10 <space> -9 <space> -8 <space> -7 <space> -6 <space> -5 <space> -4 <space> -3 <space> -2 <space> -1
e = range(-10) # range(0 , 10 , -1)
print(*e) # empty object becoz -10 <= 0
f = range(2 , 2) # range(2 , 2 , 1)
print(*f) # empty object becoz 2 <= 2
g = range(10 , 11 , 0.1) # error as range object cannot hold float
h = range('A' , 'F') # error as range object cannot hold string

#  Find  outputs  (Home  work)
r = range(10 ,  17 , 3) # 
a , b , c = r # 10 <space> 13 <space> 16 assigns to a , b , c 
print(a , b , c) # 10 <space> 13 <space> 16
r = range(3) 
x , y = r # error becoz there are 3 elements but only 2 references are there
p , q  , r , s = r  # error becoz there are 3 elements but 4 references are there
a , b , c = *r
