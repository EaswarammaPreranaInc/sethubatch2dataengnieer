#index() and count() methods demo program (Home work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)

#0 1 2 3 4 5 6 7 8 9 10
try:
    i=a . index(15) # Finds first occurrence of 15 at index 2
    while True:
        print('15 is found at index : ' , i) # Prints index where 15 is found
    i = a . index(15 , i + 1) # Finds next occurrence starting from i+1
except:
    print(F'15 is found {a . count(15)} times') # Prints total count of 15 (3 times)

#How to modify an element of tuple ? (Home work)
a = 10 , 20 , 30 , 40 , 50

#0 1 2 3 4
a[2] = 35 # Error: tuples are immutable, cannot modify elements
print(a) # This line won't execute due to error
print(id(a)) # This line won't execute due to error
#How to modify 30 in tuple to 35 # Answer: Convert to list, modify, then convert back to tuple
print(a) # This line won't execute due to error
print(id(a)) # This line won't execute due to error

#How to delete an element of tuple ? (Home work)
a = 10 , 20 , 30 , 40 , 50

#0 1 2 3 4
a . remove(30) # Error: tuples don't have remove() method
del a[2] # Error: tuples are immutable, cannot delete elements
a . pop(2) # Error: tuples don't have pop() method
print(a) # This line won't execute due to error
print(id(a)) # This line won't execute due to error
#How to remove 30 from tuple 'a' # Answer: Convert to list, remove, then convert back to tuple
print(a) # This line won't execute due to error
print(id(a)) # This line won't execute due to error

#Nested tuple (Home work)
a = ( (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90) )
print(a) # Prints ((10, 20), (30, 40, 50), (60, 70, 80, 90))
print(type(a)) # Prints <class 'tuple'>
print(len(a)) # Prints 3 (number of inner tuples)
# print("How to print 1st inner tuple") # Answer: 
print(a[0])
# print(How to print 2nd inner tuple) # Answer: 
print(a[1])
# print(How to print 3rd inner tuple) # Answer:
print(a[2])
# print(How to print 20) # Answer: 
print(a[0][1])
# print(How to print 50) # Answer: 
print(a[1][2])
# print(How to print 90) # Answer: 
print(a[2][3])

#Find outputs (Home work)
a = ((10 , 20 , 30),)
# print(How to print inner tuple) # Answer: 
print(a[0])
# print(How to print inner tuple in another way) # Answer: 
print(a[-1])
# print(How to print 10) # Answer: 
print(a[0][0])
# print(How to print 20) # Answer: 
print(a[0][1])
# print(How to print 30) # Answer: 
print(a[0][2])
# b = ((),)
# print(How to print inner tuple of tuple 'b') # Answer:
print(b[0])
# print(How to print inner tuple of tuple 'b' in another way) # Answer: 
print(b[-1])

#Find outputs (Home work)
a = ((10 , 20 , 30)) # This is not a tuple, just parentheses around values
print(a) # Prints (10, 20, 30) - but this is a tuple due to comma separation
print(*a) # Prints 10 20 30 (unpacked values)
b = (()) # This creates an empty tuple
print(b) # Prints ()
print(*b) # Prints nothing (empty tuple unpacked)

#What are the outputs if input is {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter Set : ') # User enters: {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(a) # Prints exactly what user entered: "{10 , 20 , 15 , 18 , 20 , 12 , 18}"
print(type(a)) # Prints <class 'str'> (input returns string)
b = eval(a) # Evaluates the string as Python expression
print(b) # Prints {10, 20, 12, 15, 18} (duplicates removed, order may vary)
print(type(b)) # Prints <class 'set'>

#Find outputs (Home work)
print({(10 , 20 , 30)}) # Valid: set with one tuple element, prints {(10, 20, 30)}
print({[10 , 20 , 30]}) # Error: lists are unhashable, cannot be set elements
print({{10 , 20 , 30}}) # Error: sets are unhashable, cannot be set elements
print({{}}) # Error: sets are unhashable, cannot be set elements

#How to print set in differnet ways (Home work)
a = {25 , True , 'Hyd' , 10.8}
print('set with print function') # Prints: set with print function
print(a) # Prints set elements in arbitrary order, e.g., {True, 10.8, 'Hyd', 25}
print('Iterate elements of set with for loop') # Prints: Iterate elements of set with for loop
#How to iterate set with for loop Answer: for item in a: print(item)

#Find outputs (Home work)
a = 'Hyd'
b = True
c = 25
d = 1 # This equals True in boolean context
e = 'Hyd' # Duplicate of 'a'
s = {a , b , c , d , e} # Creates set with unique elements
print(s) # Prints {True, 25, 'Hyd'} (d is treated as True, e is duplicate of a)
print(len(s)) # Prints 3
print(type(s)) # Prints <class 'set'>

#Find outputs (Home work)
s = {'Hyd', 25, True, 10.8 } # Set with 4 elements
print(s) # Prints elements in arbitrary order, e.g., {True, 10.8, 'Hyd', 25}
a , b , c , d = s # Unpacks set elements (order depends on set iteration)
print(a) # Prints first element (could be any of the four)
print(b) # Prints second element (could be any of the remaining three)
print(c) # Prints third element (could be any of the remaining two)
print(d) # Prints fourth element (the last remaining one)

#Find outputs (Home work)
s = {'Hyd', 25, True, 10.8 }
print(s) # Prints elements in arbitrary order
a , *b = s # Unpacks first element to 'a', rest to list 'b'
print(a) # Prints first element
print(b) # Prints list with remaining 3 elements
print(type(b)) # Prints <class 'list'>

#Find outputs (Home work)
s = {'Hyd', 25, True, 10.8 }
print(s) # Prints elements in arbitrary order
a , *b , c = s # Unpacks first to 'a', last to 'c', middle to list 'b'
print(a) # Prints first element
print(b) # Prints list with middle 2 elements
print(c) # Prints last element

#Find outputs (Home work)
s = {20 , 10 , 20 , 10} # Creates set with {10, 20}
print(s) # Prints {10, 20} or {20, 10} (order may vary)
x , y = s # Unpacks the two elements
print(x) # Prints first element (10 or 20)
print(y) # Prints second element (the other one)

#set() function demo program (Home work)
a = range(100 , 151 , 10) # Creates range(100, 151, 10)
b = set(a) # Converts to set {100, 110, 120, 130, 140, 150}
print(b) # Prints the set (order may vary)
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18] # List with duplicates
d = set(c) # Converts to set, removes duplicates {10, 12, 15, 18, 20, 50}
print(d) # Prints the set (order may vary)
e = set('Rama rAo') # Converts string to set of characters
print(e) # Prints {'R', 'a', 'm', ' ', 'r', 'A', 'o'} (order may vary)
print(set(25)) # Error: integer is not iterable/sequence
print(set()) # Returns empty set: set()
