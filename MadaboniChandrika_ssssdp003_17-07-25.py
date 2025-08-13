#first program
a = range(10 , 50 , 5)
print(type(a))
print(a)
print(*a)
print(id(a))
print(len(a))
print(*a[2 : 7] , sep = ' , ')
print(*a[ : : -1])
#a[4] = 32
#print(a * 2)

#second program
a = range(10 , 20)
print(*a , sep = ',')
b = range(5)
print(*b)
c = range(10 , 1 , -1)
print(*c , sep = '...')
d = range(-10 , 0)
print(*d)
e = range(-10)
print(*e)
f = range(2 , 2)
print(*f)
#g = range(10 , 11 , 0.1)
#h = range('A' , 'F')

#third program
#  Find  outputs  (Home  work)
r = range(10 ,  17 , 3)
a , b , c = r
print(a , b , c)
r = range(3)
#x , y = r
#p , q  , r , s = r
#a , b , c = *r
