
# Find  outputs    (Home  work)
a = range(10 , 50 , 5)

print(type(a))#<class 'range'>

print(a)#range(10,50,5)

print(*a)#unpacks object 'a' to elements i.e 10<space>15<space>20<space>25<space>30<spacee>35<space>40<space>45

print(id(a))#address of the object

print(len(a))#8

print(*a[2 : 7] , sep = ' , ')#a[2:6:1]i.e 20,25,30,35,40
print(*a[ : : -1])#[-1:-9:-1]i.e 45<space>40<spcace>35<spcace>30<spcace>25<spcace>20<spcace>15<spcace>10

#a[4] = 32#error

#print(a * 2)#error
print()
#  Find  outputs  (Home  work)
a = range(10 , 20)
print(*a , sep = ',')
b = range(5)
print(*b)#0 1 2 3 4
c = range(10 , 1 , -1)
print(*c , sep = '...')
d = range(-10 , 0)
print(*d)
e = range(-10)
print(*e)
f = range(2 , 2)
print(*f)
#g = range(10 , 11 , 0.1)#error
#h = range('A','F')#error

print()

#  Find  outputs  (Home  work)
r = range(10 ,  17 , 3)
a , b , c = r
print(a , b , c)
r = range(3)
#x , y = r#error
#p , q  , r , s = r#error
#a , b , c = * r#error


