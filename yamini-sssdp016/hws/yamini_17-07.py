# Find  outputs    (Home  work)

a = range(10 , 50 , 5) #prints the elements from range 10 to 49 in step of 5 such as 10,15,20...

print(type(a)) # class range

print(a)  #prints the range object itself I.e range(10,50,5)

print(*a) # unpacks the elements of the range object and prints them 10 15 20 25 30 35 40 45

print(id(a)) # prints the address of the range object a

print(len(a)) # prints the length or the number of elements of object a I.e 8

print(*a[2 : 7] , sep = ' , ') #we sliced the range object and created new object from index 2 to 6 in step of 1 I.e 20,25,30,35,40

print(*a[ : : -1]) # prints the same range object in reverse order I.e 45,40,35,30,25,20,15,10

a[4] = 32 #error because range is immutable
 
print(a * 2) #error because if we repeat elements we will get duplicate elements which is not applicable

#  Find  outputs  (Home  work)
a = range(10 , 20) #assigns the elements of the range from 10 to 19 in step of 1
print(*a , sep = ',') #unpacks and prints the range object I.e 10,11,12,13,14,15,16,17,18,19
b = range(5) # assigns the elements of the range from default start 0 to 4 in step of 1
print(*b) # 0 1 2 3 4
c = range(10 , 1 , -1) # assigns the range object from elements 10 to 2 in step of -1 I.e in descending order
print(*c , sep = '...') # we have used separator as ... so 10...9...8...7...6...5...4...3...2
d = range(-10 , 0) # assigns the range object from range -10 to -1 in range of 1
print(*d) #-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10) #assigns the range object with elements starting from 0 to -9 with step 1
print(*e) #empty string because when we keep adding 1 to 0 we will get 1,2,3.. but we are not moving to -9
f = range(2 , 2) #assigns the range object from elements 2 t0 1 in step of 1
print(*f) # we get empty string because when we add step 1 to 2 we get 3 we are not going towards 1
g = range(10 , 11 , 0.1) # error because range function doesn't allow float values In any case
h = range('A' , 'F') # error because range function doesn't allow strings

r = range(10 ,  17 , 3) # assigns the range object from the elements 10 to 116 in step of 3 i.e 10 13 16
a , b , c = r #assign#assigns the 3 elements of r to references a b c
print(a , b , c) # prints 10 13 16
r = range(3) # assigns the range object elements 0 to 2 in step of 1
x , y = r # error because we have  3 values in R but assigning to 2 valuess only
p , q  , r , s = r # error because we have  3 values in R but assigning to 4 valuess 
a , b , c = *r # error because we should not give * operator while assigning