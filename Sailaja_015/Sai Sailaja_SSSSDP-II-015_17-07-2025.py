# Find  outputs    (Home  work)
a = range(10 , 50 , 5) # creates a range object from 10 to 49 in steps of 5
print(type(a))   # prints type of range object i.e., <class 'range'>
print(a)   # prints the range object i.e., range(10, 50, 5)
print(*a)  # unpacks and prints all elements in the range i.e., 10 15 20 25 30 35 40 45
print(id(a))  # prints address of the range object 
print(len(a))  # prints number of elements in the range i.e., 8
print(*a[2 : 7] , sep = ' , ')  # prints indexes from 2 to 6 in steps of 1 with , seperator i.e., 20, 25 30, 35, 40 
print(*a[ : : -1])  # prints reverse of the range object i.e., 45 40 35 30 25 20 15 10
a[4] = 32  # Error because range object is immutable
print(a * 2) # Error range object does not support multiplication diectly with an integer



#  Find  outputs  (Home  work)
a = range(10 , 20) # creates range object from indexes 10 to 19 in steps of 1 i.e., 10 11 12 13 14 15 16 17 18 19
print(*a , sep = ',')  # prints range object with comma seperator i.e., 10, 11, 12, 13, 14, 15, 16, 17, 18, 19
b = range(5) # creates range object from indexes 0 to 4 in steps of 1 i.e., 0<space>1<space>2<space>3<space>4
print(*b)  # prints range object i.e., 0 1 2 3 4
c = range(10 , 1 , -1)  # creates range object from indexes 10 to 2 in steps of -1 
print(*c , sep = '...')  # prints range object with 3 dot separator i.e., 10...9...8...7...6...5...4...3...2
d = range(-10 , 0)  # creates range object from indexes -10 to -1 in steps of 1
print(*d)  # prints the range object i.e., -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10) 
print(*e)  # indexes from 0 to -11 i.e., empty line
f = range(2 , 2)
print(*f)  # prints the range object from indexes 2 to 2 in steps of 1 i.e., empty line
g = range(10 , 11 , 0.1) # Error because range object cannot accept float as the step,it only accepts int types as the stap
h = range('A' , 'F') # Error because range object cannot accept strings or characters 



#  Find  outputs  (Home  work)
r = range(10 ,  17 , 3)  # creates range object from indexes 10 to 16 in steps of 3 i.e., 10 13 16
a , b , c = r
print(a , b , c) # prints range object i.e., 10<space>13<space>16
r = range(3)
x , y = r  # Error i.e., ValueError because in range we have 3 indexes and here we are giving 2 values
p , q  , r , s = r # Error i.e., ValueError because in range we only have 3 elements and trying to access 4 elements
a , b , c = *r # Error because * cannot be used in an assignment, it should be used in functions