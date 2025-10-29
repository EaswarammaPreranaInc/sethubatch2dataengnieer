a = {10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}
print(a)           # Prints the dictionary a {10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}
print(type(a))     # Prints the type of a which is <class 'dict'>
print(a[10])       # How  to  obtain  value  key  10
print(a[20])       # How  to  obtain  value  key  20
print(a[15])       # How  to  obtain  value  key  15
print(a[18])       # How  to  obtain  value  key  18
a[15] = 'Krishna'  # Modify the Amar to Krishna
a.pop(20)          # Remove key 20
a[25] = 'Vamsi'    # Add new key 25
print(a)           # Prints the new dictionary a{10: 'Ramesh', 15: 'Krishna', 18: 'Sita', 25: 'Vamsi'}
print(len(a))      # Prints the length of the dict which is 4


# Find outputs (Home work)
a = {10 : 'Hyd' , 10 : 'Sec'}  # Duplicate key 10, only the last value 'Sec' is kept
print(a)                       # Prints the dictionary a {10: 'Sec'}
print(len(a))                  # Length is 1 since duplicate keys are overwritten
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'} # Duplicate keys 'G' and 'B', so last values ('Gray' and 'Black') 
print(b)                       # Prints b {'R': 'Red', 'G': 'Gray', 'B': 'Black', 'Y': 'Yellow'}
print(len(b))                  # Length is 4 (R, G, B, Y — duplicates not counted)


# Tricky program
# Find output (Home work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May be'}  # All keys are considered equal, so final key is 1.0 with value 'May be'
print(a)                                        # Prints {True: 'May be'} 
print(len(a))                                   # Prints 1 because all keys are treated as the same


# Find outputs

a = {[]: 25}                                           # Error list is unhashable, cannot be a dictionary key
b = {(): 25}                                           # empty tuple is hashable
print(b)                                               # Output {(): 25}
c = {{}: 25}                                           # Error dict is unhashable, cannot be a key
d = {'Ramesh': [9948250500, 9848565090, 9440250404]}   # string key with list value
print(d)                                               # Output {'Ramesh': [9948250500, 9848565090, 9440250404]}
print(len(d))                                          # Output 1
e = {set(): 10.8}                                      # Error set is unhashable, cannot be a dictionary key


# Find outputs

a = {}                      # Creates an empty dictionary
print(type(a))              # Output <class 'dict'>
print(len(a))               # Output 0 (no elements)
print(a)                    # Output {}
b = dict()                  # Another way to create an empty dictionary
print(type(b))              # Output <class 'dict'>
print(len(b))               # Output 0 (no elements)
print(b)                    # Output {}