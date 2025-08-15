# Find  outputs    (Home  work)

a = range(10 , 50 , 5) # ref 'a' is assigned to range object

print(type(a)) # prints <class 'range'>

print(a) # range(10, 50 , 5)

print(*a) # 10  15  20   25  30  35  40  45  

print(id(a))# address of obj 'a'

print(len(a)) # 50

print(*a[2 : 7] , sep = ' , ') # 2, 3, 4, 5, 6

print(*a[ : : -1]) # 6, 5 , 4, 3, 2, 1, 0 prints reverse elements

a[4] = 32 # obj 'a' at index 4 is assigned with 32 

print(a * 2) # prints all the obj value multiplied by 2

#  Find  outputs  (Home  work)
a = range(10 , 20) # ref 'a' is assigned to range obj with index 10 , 20 with step 1
print(*a , sep = ',') # 10, 11, 12, 13, …..19
b = range(5)# ref 'b' assigned to range obj with index 4
print(*b) # 0  1  2  3  4 
c = range(10 , 1 , -1)# range obj with step index -1
print(*c , sep = '...')# 10...9...8...7...6...5...4...3...2
d = range(-10 , 0)# range obj with step 1
print(*d)# -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10) # range obj with end index -10 with step 1
print(*e) # 0,1,2,3...n where it never goes to -9 so it prints empty
f = range(2 , 2) # range obj with index 2, 2 with step +ve1
print(*f) #empty
g = range(10 , 11 , 0.1) # error step shouldn't be float type
h = range('A' , 'F') # arg shouldn't be string type

#  Find  outputs  (Home  work)
r = range(10 ,  17 , 3) # ref 'r' is assigned to range obj 
a , b , c = r # step elements are assigned to a, b, c with step 3
print(a , b , c) # prints 10, 13, 16
r = range(3)# range obj with index 2 and with step 1
x , y = r# to many values to unpack , error
p , q  , r , s = r # same error
a , b , c = *r # error