1.# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a)								# {10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}
print(type(a))								# <class 'dict'>
print(How  to  obtain  value  key  10)					# print(a[10]) -----> Ramesh
print(How  to  obtain  value  key  20)					# print(a[20]) -----> Kiran
print(How  to  obtain  value  key  15)					# print(a[15]) -----> Amar
print(How  to  obtain  value  key  18)					# print(a[18]) -----> Sita
print(a[19])								# Error because key 19 is not present
print(a[0])								# Error key 0 is not present
print(a['Amar'])							# Error because 'Amar' is a value not a key
How  to  moify  value  of   key  15  to  'Krishna'			# a[15] = 'Krishna'
How  to  remove  20 :  'Kiran'  from  dict  'a'				# del a(20)
How  to  append  25 : 'Vamsi'  to  dict  'a'				# a[25] = 'Vamsi'
print(a)								# {10: 'Ramesh', 15: 'Krishna', 18: 'Sita', 25: 'Vamsi'}
print(len(a))								# 4
print(a * 2)								# Error because dictionaries cannot be multiplied




2.# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a)								# {10: 'Sec'}
print(len(a))								# 1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b)								# {'R': 'Red', 'G': 'Gray', 'B': 'Black', 'Y': 'Yellow'}
print(len(b))								# 4




3.#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a)							# {True: 'May  be'}
print(len(a))							# 1




4.# Find  outputs
a = { [ ] : 25}							# Error  because list cannot be used as Dictionary keys 
b = { ( ) : 25}
print(b)							# {(): 25}
c = { { } : 25}							# Error {} is an empty dictionary it cannot be used as dict keys
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d)							# {'Ramesh': [9948250500, 9848565090, 9440250404]}
print(len(d))							# 1
e = {set() : 10.8}						# Error because sets are mutable it cannot be used




5.# Find  outputs
a = {}
print(type(a))			# Type of 'a' is <class 'dict'>
print(len(a))			# 0
print(a)			# {}
b = dict()
print(type(b))			# Type of 'b' is <class 'dict'>
print(len(b))			# 0
print(b)			# {}