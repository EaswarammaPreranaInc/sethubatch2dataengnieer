#Home Work-1
# Find  outputs    (Home  work)

a = range(10 , 50 , 5)

print(type(a))# <class 'range'>

print(a)# range(10,50,5)

print(*a)#placing * infront of the object results in unpacking the range, 10 15 20 25 30 35 40 45

print(id(a))#the address of the range object say 1000

print(len(a))# number of elements present in the range object which is 8

print(*a[2 : 7] , sep = ' , ')# unpack the range and print elements of range object from index 2 to 6 in steps of 1 separated by ',' which is 20,25,30,35,40,45

print(*a[ : : -1])#elements of the range from -1 to -n (where n is number of elements in range) which is 45 40 35 30 25 20 15 10

a[4] = 32#error: range objects are immutable so this returns error

print(a * 2)# error: range objects cannot be repeated as it doesn't allow duplicates

#Home Work-2
#  Find  outputs  (Home  work)
a = range(10 , 20)
print(*a , sep = ',') #10 to 19 in steps of 1, which is 10,11,12,13,14,15,16,17,18,19
b = range(5) 
print(*b) #0 to 4 in steps of 1, which is 0,1,2,3,4
c = range(10 , 1 , -1)
print(*c , sep = '...') #10 to 2 in steps of -1, which is 10...9...8...7...6...5...4...3...2
d = range(-10 , 0)
print(*d)# -10 to -1 in steps of 1, which is -10 -9 -8 -7 -6 -5 -4 -3 -2 -2
e = range(-10)
print(*e)# 0 to -10 in steps of 1 which returns empty 
f = range(2 , 2) 
print(*f) # 2 to 1 in steps of 1 , which returns empty
g = range(10 , 11 , 0.1)#error: only int elements are allowed in range float objects are not allowed
h = range('A' , 'F')  # error: only int objects are allowed strings are not allowed

#Home Work-3
#  Find  outputs  (Home  work)
r = range(10 ,  17 , 3) # 10 to 16 in steps of 3 which is , 10, 13,16
a , b , c = r # a=10, b=13, c=16
print(a , b , c)# 10 13 16
r = range(3)#0 to 2 in steps of 1, which is 0, 1, 2
x , y = r # error: we need to assign range of 3 elements to 3 references we cannot do it to 2 objects
p , q  , r , s = r #error: we need to assign range of 3 elements to 3 references we cannot do it to 4 objects
a , b , c = *r #range of 3 elements will get a,b,c references