# Find  outputs    (Home  work)

a = range(10 , 50 , 5)

print(type(a))#output : class = int

print(a)#prints range function /output : range(10,50,5)

print(*a)#to openup the elements of the object /output : 10 15 20 25 30 35 40 45 

print(id(a))# prints the address of the range object.

print(len(a))#prints length pf range elements i.e, 8

print(*a[2 : 7] , sep = ' , ')#prints element 2 to 7-1 = 6 th index-element /output : 20,25,30,35,40 

print(*a[ : : -1])#prints reverse of elements of range.i.e;45 40 35 30 25 20 15 10

a[4] = 32#gives error because range is immutable so the elements of range cannot be changed

print(a * 2)#sequence cannot be multiplied with number
#  Find  outputs  (Home  work)
a = range(10 , 20)
print(*a , sep = ',')#prints numbers 10 to 19 with commas in the default step of 1/output : 10,11,12,13,14,15,16,17,18,19
b = range(5)
print(*b)#opens-up the elements of the range and prints till 0-4/output : 0 1 2 3 4
c = range(10 , 1 , -1)
print(*c , sep = '...')#prints the elements of range function by decreasing every step to -1/output : 10...9...8...7...6...5...4...3...2 
d = range(-10 , 0)
print(*d)#-10,-10+1=-9,-9+1=-8,-7,-6,-5,-4,-3,-2,-1
e = range(-10)
print(*e)# doesnot give any output because range starts with 0 and the end step is < 0. so,it cannot go anywhere hence no ouput
f = range(2 , 2)
print(*f)#doesnot give any output because default step is 1 and start and steps are same.
g = range(10 , 11 , 0.1)#gives error because range function takes inputs only of integers and not float type.
h = range('A' , 'F')#gives error because range function takes inputs only of integers and not string type.
#  Find  outputs  (Home  work)
r = range(10 ,  17 , 3)
a , b , c = r
print(a , b , c)#prints 10 13 16 and assigns a b c to them. 
r = range(3)
x , y = r #prints error because range has 3 values and no enough assignments 
p , q  , r , s = r#prints error because range has 3 values and excess assignments 
a , b , c = *r #throws error