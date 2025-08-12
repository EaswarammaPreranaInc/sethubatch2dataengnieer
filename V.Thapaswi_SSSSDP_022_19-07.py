# Find  outputs  
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'} 
print(a)  # o/p: {10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}
print(type(a))  # o/p: <class 'dict'>
print(a[10]) # o/p: Ramesh
print([20]) # o/p: Kiran
print(a[15]) # o/p: Amar
print(a[18]) # o/p: Sita
#print(a[19]) #error: key 19 does not exist in dict 'a'
#print(a[0]) #error: key 0 does not exist in dict 'a'
#print(a['Amar']) #error: key 'Amar' does not exist in dict 'a'
#How  to  moify  value  of   key  15  to  'Krishna'
a[15] = 'Krishna'  # modifies the value of key 15 to 'Krishna'
#How  to  remove  20 :  'Kiran'  from  dict  'a'
del a[20]
#How  to  append  25 : 'Vamsi'  to  dict  'a'
a[25]= 'vamsi'
print(a) # o/p: {10: 'Ramesh', 15: 'Krishna', 18: 'Sita', 25: 'vamsi'}
print(len(a)) # o/p: 4: length of dict 'a'
#print(a * 2) #TypeError: dict object can't be multiplied

# Find  outputs 
a = {10 : 'Hyd' , 10 : 'Sec'}  # keys must be unique, so the last value 'Sec' will overwrite the first 'Hyd'
print(a) # o/p: {10: 'Sec'}
print(len(a)) # o/p: 1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b) # o/p: {'R': 'Red', 'G': 'Gray', 'B': 'Black', 'Y': 'Yellow'}
print(len(b)) # o/p: 4: length of dict 'b'

# Find output 
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a)  # o/p: {True: 'May  be'}
print(len(a)) # 1

# Find  outputs
#a = { [ ] : 25} # error: dict keys are immutable. lists are mutable ,so, they cannot be used as keys
b = { ( ) : 25}  # tuples are immutable, so they can be used as keys
print(b)  # o/p: {(): 25} 
c = { { } : 25} # error: dict keys are immutable. dicts are mutable, so they cannot be used as keys
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d) # o/p: {'Ramesh': [9948250500, 9848565090, 9440250404]}
print(len(d)) # o/p: 1
e = {set() : 10.8}  # error: dict keys are immutable. sets are mutable, so they cannot be used as keys

# Find  outputs
a = {}
print(type(a)) # o/p: <class 'dict'>
print(len(a)) # o/p: 0: empty dict has no keys
print(a) #o/p: {}
b = dict() # another way to create an empty dict
print(type(b)) # o/p: <class 'dict'>
print(len(b)) #o/p: 0: empty dict has no keys
print(b) # {}