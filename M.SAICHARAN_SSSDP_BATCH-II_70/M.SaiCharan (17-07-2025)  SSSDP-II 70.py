1.# Find  outputs    (Home  work)
a = range(10 , 50 , 5)
print(type(a))				# type of object 'a'is<class 'range'>
print(a)				# range(10, 50, 5)
print(*a)				# 10 15 20 25 30 35 40 45 prints each element seperated by a space 
print(id(a))				# Address of range object 'a'
print(len(a))				# 8
print(*a[2 : 7] , sep = ' , ')		# 20,25,30,35,40 seperates each element by comma and space
print(*a[ : : -1])			# 45 40 35 30 25 20 15 10 (reversing the range elements)
a[4] = 32				# Error because we can not change, range is immutable
print(a * 2)				# Error because unsupported operand types for *:'range' and 'int'




2.#  Find  outputs  (Home  work)
a = range(10 , 20)
print(*a , sep = ',')		# 10,11,12,13,14,15,16,17,18,19
b = range(5)
print(*b)			# 0 1 2 3 4
c = range(10 , 1 , -1)
print(*c , sep = '...')		# 10...9...8...7...6...5...4...3...2
d = range(-10 , 0)
print(*d)			# -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10)
print(*e)			# Empty Range
f = range(2 , 2)
print(*f)			# Empty range beacause start and stop are same
g = range(10 , 11 , 0.1)	# Error because 'float object cannot be interpreted
h = range('A' , 'F')		# Error because 'str'object cannot be interpreted




3.#  Find  outputs  (Home  work)
r = range(10 ,  17 , 3)
a , b , c = r
print(a , b , c)		# 10 13 16
r = range(3)
x , y = r			# Error because values are too many to unpack
p , q  , r , s = r		# Error because there are not enough values to unpack
a , b , c = *r			# Error cannot use *r right side without parenthesis.