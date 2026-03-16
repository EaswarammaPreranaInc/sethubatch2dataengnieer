#Day-3 #Home Work-1
# Find  outputs    (Home  work)

a = range(10 , 50 , 5) #Here range object is assigned to reference a

print(type(a)) #Returns the type of object i,e <class 'range'>

print(a) #Returns only the range object i,e range(10,50,5)

print(a) #Returns the elements of the specified range #Here we are using '' it is used to unpack the range object and here we are printing the elements from range 10 to 50 in steps of 5

print(id(a)) #Returns the address of the range object

print(len(a)) #Returns the number of elements in the specified range

print(*a[2 : 7] , sep = ' , ') #Returns the elements from 20 to  with ',' seperation i.e.[20,25,30,35,40]

print(*a[ : : -1]) #Returns the elements from right to left order i.e. [45 40 35 30 25 20]

a[4] = 32 #Error #Because range is immuatable it cannot be modified

print(a * 2) #Range cannot be repeated because it allows only unique elements so when we apply multiplication it creates duplicate elements


#indexes            0   1  2  3  4  5  6  7
range(10,50,5)    # 10 15 20 25 30 35 40 45

#Day-3 #Home Work-2
#  Find  outputs  (Home  work)

a = range(10 , 20) #Here we are assigning range object to reference a and by default the step is 1 so it looks like this range(10,20,1)
print(*a , sep = ',') #Returns the elements from 10 to 20 in steps of 1 by seperating each element with ',' and by default it take <space> as a seperator 
b = range(5) #Here we are assigning the range object i.e. range(0,5,1) elements from 0 to 5 in steps of 1
print(*b) #Returns the elements from 0 to 4 i.e. [0 1 2 3 4]
c = range(10 , 1 , -1) #Here we are assigning the range object to reference c i.e range(10,1,-1) elements from 10 to 1 in steps of -1
print(*c , sep = '...') #Returns the elements from 10 to 1 in steps of -1 and with '...' seperation i.e [10...9...8...7...6...5...4...3...2]
d = range(-10 , 0) #Here we are assigning the range object to reference d i.e elements from -10 to 0 in steps of 1
print(*d) #Returns the elements from -10 to -1 i.e [-10 -9 -8 -7 -6 -5 -4 -3 -2 -1]
e = range(-10) #Here we are assigning the range object to reference e i.e. range(0,-10,1)
print(*e) #Returns no elements (empty) because here the start is 0 and end is -10 and here default step is 1 so it goes beyond the -10 
f = range(2 , 2) #Here we are assigning a range object i.e range(2,2,1) to the reference f
print(*f) #Returns the empty range as here start is 2, and end is 2 and by default step is 1 so it increases step by 1 so it never reaches 2 so it gives you empty
g = range(10 , 11 , 0.1) #Returns an error as we already know that range only accepts the integer values no float no complex only integers
h = range('A' , 'F') #Error range only allows integers

#Day-3 #Home Work-3
#  Find  outputs  (Home  work)
r = range(10 ,  17 , 3) #Here we are assigning the range object to the reference r i.e. elements from 10 to 17 in steps of 3
a , b , c = r #Here we are assigning the same range object to 3 different references a,b,c
print(a , b , c) #Returns the range object i.e (10,17,3)
r = range(3) #Here we are assigning range object to reference r i.e. elements from 0 to 3 in steps of 1
x , y = r #Same here also we are assigning same range object to 2 different references
p , q  , r , s = r #Here also we are assigning same range object to 4 different references
a , b , c = r #Here we are using unpack operator '' so it gives an error as we are unpacking the range object to different references it is not possible