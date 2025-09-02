a = range(10, 50, 5) 
print(type(a)) # <class 'range'> # range object 
print(a) #range(10, 50, 5) range object representation
print(*a) #10 15 20 25 30 35 40 45 unpacked range values
print(id(a)) # id(a) will print a unique identifier 21289128732 random number 
print(len(a)) # 8 length of the range object
print(*a[2:7], sep=' , ') # 20 , 25 , 30 , 35 , 40 sliced range values
print(*a[::-1])# 45 40 35 30 25 20 15 10 # reversed range values
#a[4] = 32 #This will raise a TypeError because range objects are immutable in Python # error
#print(a * 2) #This will raise a TypeError because range objects don't support multiplication # error
a = range(10, 20) 
print(*a, sep=',') # 10,11,12,13,14,15,16,17,18,19
b = range(5)#This creates a range object starting from 0 and stopping at 5.
print(*b) # 0 1 2 3 4
c = range(10, 1, -1) #This creates a range object starting from 10 and stopping at 1 with a step of -1.
print(*c, sep='...') # 10...9...8...7...6...5...4...3...2 
d = range(-10, 0) #This creates a range object starting from -10 and stopping at 0.
print(*d) # -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10) #This creates an empty range object because the stop value is negative.
print(*e) # (empty output)
f = range(2, 2) #This creates an empty range object because the start and stop values are the same.
print(*f) # (empty output)
#g = range(10, 11, 0.1) # This will raise a TypeError because the step value must be an integer.
#print(g) # TypeError: 'float' object cannot be interpreted as an integer
#h = range('A', 'F') #This will raise a TypeError because the start and stop values must be integers.
#print(h) # TypeError: 'str' object cannot be interpreted as an integer
r = range(10, 17, 3) 
a, b, c = r #a = 10, b = 13, c = 16 #10 13 16
print(a, b, c) # 10 13 16
r = range(3) 
#x, y = r # x = 0, y = 1 " ValueError won't occur here because the number of variables matches the number of values in the range object when considering only two variables. However, if we try to unpack it into more variables than it has values, a ValueError will occur."
#p, q, r, s = r #This will raise a ValueError because there are not enough values to unpack (expected 4, got 3) # ValueError
#a, b, c = *r #This syntax is incorrect and will raise a SyntaxError.
