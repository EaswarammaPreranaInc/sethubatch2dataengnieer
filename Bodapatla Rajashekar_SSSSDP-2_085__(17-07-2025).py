# Find outputs

a = range(10, 50, 5)

print(type(a))  # Output: <class 'range'> — 'a' is a range object (not int)

print(a)  # Output: range(10, 50, 5) — displays the range definition

print(*a)  # Output: 10 15 20 25 30 35 40 45 — unpacked elements of the range

print(id(a))  # Output: memory address (e.g., 140246875445600) — shows object's ID

print(len(a))  # Output: 8 — there are 8 elements in the range

print(*a[2:7], sep=' , ')  
# Output: 20 , 25 , 30 , 35 , 40 — sliced from index 2 to 6 (7 is exclusive)

print(*a[::-1])  
# Output: 45 40 35 30 25 20 15 10 — reverse order using slicing

a[4] = 32  # Error: 'range' object does not support item assignment (immutable)

print(a * 2)#sequence cannot be multiplied with number

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

r = range(10 ,  17 , 3)
a , b , c = r
print(a , b , c)#prints 10 13 16 and assigns a b c to them. 
r = range(3)
x , y = r #prints error because range has 3 values and no enough assignments 
p , q  , r , s = r#prints error because range has 3 values and excess assignments 
a , b , c = *r #throws error