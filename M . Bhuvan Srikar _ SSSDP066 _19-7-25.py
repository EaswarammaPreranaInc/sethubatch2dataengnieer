# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) # {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a)) # <class 'dict'>
print(a[10]) # How  to  obtain  value  key  10
print(a[20]) # How  to  obtain  value  key  20
print(a[15]) # How  to  obtain  value  key  15
print(a[18]) # How  to  obtain  value  key  18)
print(a[19]) # error as there is no value for key 19
print(a[0]) # error as there is no value for key 0 
print(a['Amar']) # error with value key cannot be founded
a[15] = 'Krishna' # How  to  moify  value  of   key  15  to  'Krishna'
del(a[20]) # How  to  remove  20 :  'Kiran'  from  dict  'a'
a[25] = 'Vamsi' # How  to  append  25 : 'Vamsi'  to  dict  'a'
print(a) # {10 : 'Ramesh' , 15 : 'Krishna' , 18 : 'Sita' , 25 : 'Vamsi'}
print(len(a)) # 4
print(a * 2) # error as dict cannot be repeated

# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a) # {10 : 'Sec'}
print(len(a)) # 1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b) # {'R' : 'Red' , 'G' : 'Gray' , 'B' : 'Black' ,  , 'Y' : 'Yellow'}
print(len(b)) # 4

#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a) # {True : 'May be'}
print(len(a)) # 1

# Find  outputs
a = { [ ] : 25} # error as key cannot hold mutable elements
b = { ( ) : 25} 
print(b) # { ( ) : 25}
c = { { } : 25} # error as key cannot hold mutable elements
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d) # {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d)) # 1


# Find  outputs
a = {}
print(type(a)) # <class 'dict'>
print(len(a)) # 0
print(a) # {}
b = dict()
print(type(b)) # <class 'dict'>
print(len(b)) # 0
print(b) # {}
