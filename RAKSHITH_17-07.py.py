# Find outputs (Home work)

a = range(10, 50, 5)               # Creates a range object from 10 to 49 in steps of 5 
print(type(a))                     # Prints the class of object a <class 'range'>
print(a)                           # Prints the range object range(10, 50, 5) 
print(*a)                          # Unpacking the range elements using * 10 15 20 25 30 35 40 45
print(id(a))                       # Prints the address of the range object a
print(len(a))                      # Prints 8
print(*a[2:7], sep=' , ')          # Prints from index 2 to 6 and with commas 20 , 25 , 30 , 35 , 40
print(*a[::-1])                    # Prints the reverse of elements 
a[4] = 32                          # Error range object are immutable
print(a * 2)                       # Error range object doesn't perform the repetition


# Find outputs (Home work)

a = range(10 , 20)                 # Creates a range from 10 to 19 in steps of 5
print(*a , sep = ',')              # Prints: 10,11,12,13,14,15,16,17,18,19
b = range(5)                       # Creates a range from 0 to 4
print(*b)                          # Prints: 0 1 2 3 4
c = range(10 , 1 , -1)             # Creates a reverse range from 10 to 2 decreasing by 1
print(*c , sep = '...')            # Prints: 10...9...8...7...6...5...4...3...2
d = range(-10 , 0)                 # Creates a range from -10 to -1
print(*d)                          # Prints: -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10)                     # Creates a range from 0 to -10, Since step is +1 by default                                  
print(*e)                          # Doesn't Prints any value
f = range(2 , 2)                   # Creates an empty range because start and stop are equal
print(*f)                          # Doesn't Prints any value
g = range(10 , 11 , 0.1)           # Error because step must be an integer, 0.1 is a float
h = range('A' , 'F')               # Error because arguments must be integers but 'A' and 'F' are strings


# Find outputs (Home work)

r = range(10, 17, 3)       # Creates a range object with values from 10 to 16 in steps of 3
a, b, c = r                # Unpacks the 3 values of the range into variables: a = 10, b = 13, c = 16
print(a, b, c)             # Prints the values of a, b, and c  Output: 10 13 16
r = range(3)               # Creates a new range object r with values [0, 1, 2]
x, y = r                   # Error Trying to unpack 3 values into only 2 variables 
p, q, r, s = r             # Error Trying to unpack 3 values into 4 variables
a, b, c = *r               # Error: Cannot use * unpacking outside of a range
