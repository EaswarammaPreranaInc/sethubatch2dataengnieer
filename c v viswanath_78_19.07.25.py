a = {10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}
print(a)  # {10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}
print(type(a))  # <class 'dict'>
print(a[10])  # Ramesh
print(a[20])  # Kiran
print(a[15])  # Amar
print(a[18])  # Sita
print(a[19])  # Error: key 19 not present in dictionary
print(a[0])  # Error: key 0 not present in dictionary
print(a['Amar'])  # Error: key 'Amar' not present (value, not key)
a[15] = 'Krishna'  # modifies value of key 15
a.del(20)  # removes key 20 and its value
a[25] = 'Vamsi'  # appends new key-value pair
print(a)  # {10: 'Ramesh', 15: 'Krishna', 18: 'Sita', 25: 'Vamsi'}
print(len(a))  # 4
print(a * 2)  # Error: dict can't be multiplied by int

a = {10: 'Hyd', 10: 'Sec'}
print(a)               # {10: 'Sec'}
print(len(a))          # 1
b = {'R': 'Red', 'G': 'Green', 'B': 'Blue', 'Y': 'Yellow', 'G': 'Gray', 'B': 'Black'}
print(b)               # {'R': 'Red', 'G': 'Gray', 'B': 'Black', 'Y': 'Yellow'}
print(len(b))          # 4

a = {True: 'Yes', 1: 'No', 1.0: 'May  be'}
print(a)               # {True: 'May  be'}
print(len(a))          # 1

a = { [ ] : 25 }  # Error: list is unhashable and can't be used as dict key
b = { ( ) : 25 } # Valid: tuple is hashable and can be used as dict key
print(b)           # {(): 25}
c = { { } : 25 }  # Error: dict is unhashable and can't be used as dict key
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d)  
# {'Ramesh': [9948250500, 9848565090, 9440250404]}
print(len(d)) # 1
e = {set() : 10.8} # Error: set is unhashable and can't be used as dict key

a = {}
print(type(a))        # <class 'dict'>
print(len(a))         # 0
print(a)              # {}
b = dict()
print(type(b))        # <class 'dict'>
print(len(b))         # 0
print(b)              # {}
