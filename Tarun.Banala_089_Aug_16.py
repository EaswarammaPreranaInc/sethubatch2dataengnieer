a = input('Enter list: ')  # User inputs: [25, 10.8, 'Hyd', True]
print(type(a))  # Output: <class 'str'>
print(a)  # Output: "[25, 10.8, 'Hyd', True]"
b = eval(a)
print(b)  # Output: [25, 10.8, 'Hyd', True]
print(type(b))  # Output: <class 'list'>

a = [10, 20, 15, 18]
b = a
print(a is b)  # Output: True
print(a == b)  # Output: True
b[2] = 12
print(a)  # Output: [10, 20, 12, 18]

a = [10, 20, 15, 18]
b = [100, 200, 150]
print(a + b)  # Output: [10, 20, 15, 18, 100, 200, 150]
print(a + 5)  # Output: TypeError
print(a + '5')  # Output: TypeError
print([10, 20] + (30, 40))  # Output: TypeError

# Fourth Code Snippet (Tricky Program 1)
a = [1, 2, 3]
b = [4, 5, 6]
print(a, id(a))  # Output: [1, 2, 3] <memory address>
a += b
print(a, id(a))  # Output: [1, 2, 3, 4, 5, 6] <same memory address>

# Tricky Program 
a = [1, 2, 3]
b = [4, 5, 6]
print(a, id(a))  # Output: [1, 2, 3] <memory address>
a = a + b
print(a, id(a))  # Output: [1, 2, 3, 4, 5, 6] <new memory address>

# List Packing
a = 25
b = 10.8
c = 'Hyd'
d = True
e = [a, b, c, d]
print(e)  # Output: [25, 10.8, 'Hyd', True]
print(type(e))  # Output: <class 'list'>

# Unpacking
lst = [25, 10.8, 'Hyd', True]
a, *b, c = lst
print('a:', a)  # Output: a: 25
print('b:', b)  # Output: b: [10.8, 'Hyd']
print('c:', c)  # Output: c: True
print(type(b))  # Output: <class 'list'>

x, *y = lst
print('x:', x)  # Output: x: 25
print('y:', y)  # Output: y: [10.8, 'Hyd', True]

*p, q = lst
print('p:', p)  # Output: p: [25, 10.8, 'Hyd']
print('q:', q)  # Output: q: True

#Unpacking Errors
lst = [25, 10.8, 'Hyd', True]
# a, b, c, d, e = lst  # Output: ValueError
a, b, *c, d, e = lst
print('a:', a)  # Output: a: 25
print('b:', b)  # Output: b: 10.8
print('c:', c)  # Output: c: []
print('d:', d)  # Output: d: 'Hyd'
print('e:', e)  # Output: e: True

# a, b, *c, d, e, f = lst  # Output: ValueError

# Underscore in Unpacking
lst = [25, 10.8, 'Hyd', True]
a, b, _, d = lst
print('a:', a)  # Output: a: 25
print('b:', b)  # Output: b: 10.8
print('_:', _)  # Output: _: 'Hyd'
print('d:', d)  # Output: d: True

lst = [25, 10.8, 'Hyd', True, 3 + 4j]
a, b, a, d, a = lst
print('a:', a)  # Output: a: (3+4j)
print('b:', b)  # Output: b: 10.8
print('d:', d)  # Output: d: True

# Underscore Reuse
lst = [25, 10.8, 'Hyd', True, 3 + 4j]
a, b, _, d, _ = lst
print('a:', a)  # Output: a: 25
print('b:', b)  # Output: b: 10.8
print('_:', _)  # Output: _: (3+4j)
print('d:', d)  # Output: d: True

# Nested List Unpacking
lst = [[25, 10.8], 'Hyd', True]
a, b, c = lst
print('a:', a)  # Output: a: [25, 10.8]
print('b:', b)  # Output: b: 'Hyd'
print('c:', c)  # Output: c: True

lst = [[25, 10.8], 'Hyd', True]
[a, b], c, d = lst
print('a:', a)  # Output: a: 25
print('b:', b)  # Output: b: 10.8
print('c:', c)  # Output: c: 'Hyd'
print('d:', d)  # Output: d: True

# Comparing Lists
a = [10, 20, 15, 18]
b = [10, 20, 15, 18]
c = [10, 20, 25, 9]
d = [10, 20, 7, 22]
print(a == b)  # Output: True
print(a is b)  # Output: False
print(a < c)  # Output: True
print(a > d)  # Output: True
print(a >= c)  # Output: False
print(a <= d)  # Output: False
print(a != c)  # Output: True

a = [10, 20, 15, 18]
b = [20, 18, 15, 10]
print(a == b)  # Output: False
print(a is b)  # Output: False
