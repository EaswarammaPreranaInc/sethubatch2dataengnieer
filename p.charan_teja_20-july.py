
Dictionary Basics and Key Access
Python

a = {10 : 'Ramesh', 20 : 'Kiran', 15 : 'Amar', 18 : 'Sita'}

# Print the entire dictionary
print(a)

# Print the data type of the variable
print(type(a))

# Access values by key
print(a[10])
print(a[20])
print(a[15])
print(a[18])

# Demonstrate errors when accessing non-existent keys or values
try:
    print(a[19])
except KeyError as e:
    print(f"Output: Key Error: {e}")

try:
    print(a[0])
except KeyError as e:
    print(f"Output: Key Error: {e}")

try:
    print(a['Amar'])
except KeyError as e:
    print(f"Output: Key Error: {e}")

# Modify, remove, and add key-value pairs
a[15] = 'Krishna'
print("The dictionary is now:", a)

del a[20]
print("The dictionary is now:", a)

a[25] = 'Vamsi'
print("The dictionary is now:", a)

print(a)
print(len(a))

# Demonstrate unsupported operations
try:
    print(a * 2)
except TypeError as e:
    print(f"Output: Type Error: {e}")






Duplicate Keys
Python

# Keys with the same hash value
a = {True : 'Yes', 1 : 'No', 1.0 : 'May be'}
print(a)
print(len(a))

# Repeated integer keys
a = {10 : 'Hyd', 10 : 'Sec'}
print(a)
print(len(a))

# Repeated string keys
b = {'R' : 'Red', 'G' : 'Green', 'B' : 'Blue', 'Y' : 'Yellow', 'G' : 'Gray', 'B' : 'Black'}
print(b)
print(len(b))







Empty Dictionaries
Python

# Creating an empty dictionary using literal syntax
a = {}
print(type(a))
print(len(a))
print(a)

# Creating an empty dictionary using the dict() constructor
b = dict()
print(type(b))
print(len(b))
print(b)







Hashable vs. Unhashable Keys
Python

# Unhashable list as a key
try:
    a = {[] : 25}
except TypeError as e:
    print(f"Output: Type Error: {e}")

# Hashable tuple as a key
b = ((), 25)
print(b)

# Unhashable set as a key
try:
    c = ({}, 25)
except TypeError as e:
    print(f"Output: Type Error: {e}")

# Valid string key and mutable list value
d = {"Ramesh": [9940250500, 9848565090, 9440250404]}
print(d)
print(len(d))

# Another example of an unhashable set as a key
try:
    k = ({}, 10.8)
except TypeError as e:
    print(f"Output: Type Error: {e}")






