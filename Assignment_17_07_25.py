#Range
a = range(10 , 20)
print(*a , sep = ',')#10,11,12,13,14,15,16,17,18,19
b = range(5)
print(*b)#0 1 2 3 4
c = range(10 , 1 , -1)
print(*c , sep = '...')#10...9...8...7...6...5...4...3...2
d = range(-10 , 0)
print(*d)#-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10)
print(*e)#empty
f = range(2 , 2)
print(*f)#empty
g = range(10 , 11 , 0.1)#TypeError: 'float' object cannot be interpreted as an integer

h = range('A' , 'F')#SyntaxError: invalid non-printable character U+00A0

r = range(10 ,  17 , 3)
a , b , c = r
print(a , b , c)#10 13 16
r = range(3)
x , y = r#ValueError: too many values to unpack (expected 2)
p , q  , r , s = r#ValueError: not enough values to unpack (expected 4, got 3)
a , b , c = *r#SyntaxError
