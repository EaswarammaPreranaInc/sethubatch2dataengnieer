
 a = range(10 , 50 , 5)
print(type(a))         # Output: <class 'range'>
print(a)               # Output: range(10, 50, 5)
print(*a)              # Output: 10 15 20 25 30 35 40 45
print(id(a))           # Output: (Some  ID, like 140462429170960)
print(len(a))          # Output: 8
print(*a[2 : 7] , sep = ' , ')  
# Output: 20 , 25 , 30 , 35 , 40
print(*a[ : : -1])     
# Output: [] 
a[4] = 32        #ERROR
print(a * 2)

 # Range from 10 to 19
a = range(10 , 20)
print(*a , sep = ',')
# Range from 0 to 4
b = range(5)
print(*b)
# Range from 10 to 2 (descending)
c = range(10 , 1 , -1)
print(*c , sep = '...')
# Range from -10 to -1
d = range(-10 , 0)
print(*d)
# Empty range since stop < start and step is +1
e = range(-10)
print(*e)
# Empty range since start == stop
f = range(2 , 2)
print(*f)
# Error: float step not allowed
# g = range(10 , 11 , 0.1)
# Error:
# h = range('A' , 'F')

 # Valid unpacking from range(10, 17, 3) → [10, 13, 16]
r = range(10, 17, 3)
a, b, c = r
print(a, b, c)  # Output: 10 13 16
# Now using range(3) → [0, 1, 2]
r = range(3)
# Correct unpacking into 3 variables
x, y, z = r
print(x, y, z)  # Output: 0 1 2
# ERROR: Too few values (only 3) for 4 variables
# p, q, r, s = r
# ERROR: Too many values (3) for 2 variables
# x, y = r
# SYNTAX ERROR: Can't unpack using *r without wrapping in list or tuple
# a, b, c = *r
Correct usage with unpacking using *r
a, b, c = [*r]
print(a, b, c)  # Output: 0 1 2