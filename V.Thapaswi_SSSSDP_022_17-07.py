# Find  outputs    (Home  work)

a = range(10 , 50 , 5)  # creates a range object with start=10, stop=50, step=5
print(type(a))  #<class 'range'>
print(a) # range(10, 50, 5)
print(*a)  # 10 15 20 25 30 35 40 45 . range object is unpacked to elements
print(id(a))  # prints the address of range object
print(len(a)) # 8: length of range object
print(*a[2 : 7] , sep = ' , ') # 20 , 25 , 30 , 35 , 40
print(*a[ : : -1])  # 45 40 35 30 25 20 15 10
#print(a * 2)  # TypeError: range object can't be multiplied

#  Find  outputs  (Home  work)
a = range(10 , 20) # creates a range object with start=10, stop=20, step=1
print(*a , sep = ',') # 10,11,12,13,14,15,16,17,18,19
b = range(5) # range(0,5,1)
print(*b)  # 0 1 2 3 4
c = range(10 , 1 , -1) # range(10,1,-1)
print(*c , sep = '...')  # 10...9...8...7...6...5...4...3...2
d = range(-10 , 0) # range(-10,0,1)
print(*d)  # -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10) # range(0,-10,-1)
print(*e)  # When the start is greater than stop, it returns an empty range object
f = range(2 , 2) # range(2,2,1)
print(*f) # When the start is equal to stop, it returns an empty range object
#g = range(10 , 11 , 0.1) # TypeError: range is homogeneous
#h = range('A' , 'F')  # TypeError: cann't use strings in range

#  Find  outputs  (Home  work)
r = range(10 ,  17 , 3)  # creates a range object with start=10, stop=17, step=3
a , b , c = r # unpacking the 3 values from r into a,b,c
print(a , b , c)  # 10 13 16
r = range(3)  # range(0,3,1)
#x , y = r  # error: not enough values to unpack (expected 2, got 3)
#p , q  , r , s = r  # error: too many values to unpack (expected 3)
#a , b , c = *r # error: can't use * in unpacking
