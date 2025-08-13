# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) # {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a)) # <class 'dict'>
print(a[10])#How  to  obtain  value  key  10) # print(a[10])
print(a[20])#How  to  obtain  value  key  20) # print(a[20])
print(a[15])#How  to  obtain  value  key  15) # print(a[15])
print(a[15])#How  to  obtain  value  key  18) # print(a[18])
print(a[19]) # There is no key 19 in the dictionary
print(a[0])  # There is no key 0 in the dictionary
print(a['Amar']) # 'Amar' is a value, not a key in the dictionary.
a[15]='krishna'#How  to modify value  of   key  15  to  'Krishna' # a[15]='krishna'
del a[20] #How  to  remove  20 :  'Kiran'  from  dict  'a'   # del a[20]
a[25]='vamsi'#How  to  append  25 : 'Vamsi'  to  dict  'a'      # a[25]='vamsi'
print(a)      # {10 : 'Ramesh' , 15 : 'krishna' , 18 : 'Sita',25 : 'vamsi'}
print(len(a)) # 4
print(a * 2)  # Multiplication is not done in dict

# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a)      # {10:'Sec'}
print(len(a)) # 2 
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b) # {'R': 'Red', 'G': 'Gray', 'B': 'Black', 'Y': 'Yellow'} (Dictionary in Python do not allow duplicate keys.)
print(len(b)) # 4

#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'} # In dictionary Python treats True, 1, and 1.0 as the same key
print(a)      # {True: 'May  be'}
print(len(a)) # 1

# Find  outputs
a = { [ ] : 25} # [] is a list mutable, so it cannot be used as a dictionary key
b = { ( ) : 25} # () is a tuple  immutable, so it can be used as a dictionary key
print(b) # { () :25} 
c = { { } : 25} # {} is mutable
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d) # {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d)) # 1
e = {set() : 10.8}

# Find  outputs
a = {}
print(type(a)) # <class 'dict'>
print(len(a))  # 0
print(a)       # {}
b = dict()
print(type(b)) # <class 'dict'>
print(len(b))  # 0 
print(b)       # {}
