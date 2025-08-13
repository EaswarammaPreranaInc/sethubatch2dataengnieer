a = range(10, 46, 5)
print(type(a))                 # <class 'range'>
print(*a)                      # 10 15 20 25 30 35 40 45
print(id(a))                   # Random unique memory address 
print(len(a))                  # 8  
print(*a[2 : 7], sep=',')    # 20,25,30,35,40
print(*a[ : : -1])         # 45 40 35 30 25 20 15 10
a[4] = 32                      # Error: 'range' object does not support item assignment
print(a * 2)                   # Error: can't multiply a 'range' object

a = range(10 , 20)
print(*a , sep = ',')          # 10,11,12,13,14,15,16,17,18,19
b = range(5)
print(*b)                      # 0 1 2 3 4
c = range(10 , 1 , -1)
print(*c , sep = '...')        # 10...9...8...7...6...5...4...3...2
d = range(-10 , 0)
print(*d)                      # -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10)
print(*e)                      #  (prints nothing - empty output)
f = range(2 , 2)
print(*f)                      #  (prints nothing - empty output)
g = range(10 , 11 , 0.1)       # Error: step must be an integer
h = range('A' , 'F')           # Error: 'str' object cannot be interpreted as an integer

r = range(10, 17, 3)
a, b, c = r
print(a, b, c)  # 10 13 16
r = range(3)
x, y = r        # Error: not enough values to unpack 
p, q, r, s = r  # Error: too many values to unpack 
a, b, c = *r    # Error: can't use starred expression in assignment
