#Name: Tarun Banala    19-07-2025

 HOME WORK 1

a = {10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}  # Creating a dictionary with integer keys and string values
print(a)  # Prints the entire dictionary
print(type(a))  # Prints the type of 'a', which is <class 'dict'>

print(a[10])  # Access value by key 10 is Ramesh
print(a[20])  # Access value by key 20 is Kiran
print(a[15])  # Access value by key 15 is Amar
print(a[18])  # Access value by key 18 is Sita

# print(a[19])  #  KeyError, 19 does not exist in the dictionary
# print(a[0])  #  KeyError, 0 is not a valid key in the dictionary
# print(a['Amar'])  #  KeyError: 'Amar' is a value, not a key

a[15] = 'Krishna'  # Modifies the value of key 15 to 'Krishna'

a.pop(20)  # Removes the key-value pair with key 20 from the dictionary

a[25] = 'Vamsi'  # Appends a new key-value pair 25: 'Vamsi' to the dictionary

print(a)  # Prints the updated dictionary is  {10: 'Ramesh', 15: 'Krishna', 18: 'Sita', 25: 'Vamsi'}

print(len(a))  # Prints the number of items in the dictionary is 4

# print(a * 2)  # TypeError, Dictionary cannot be multiplied by an integer

HOME WORK 2

a = {10: 'Hyd', 10: 'Sec'}  # Duplicate key: 10 is repeated, last value 'Sec' will overwrite 'Hyd'

print(a)  # {10: 'Sec'} Only one key 10 with value 'Sec' remains

print(len(a))  #  1  Only one unique key (10) in the dictionary

b = {'R': 'Red', 'G': 'Green', 'B': 'Blue', 'Y': 'Yellow', 'G': 'Gray', 'B': 'Black'}  
# Duplicate keys 'G' and 'B': only last values ('Gray' and 'Black') are kept

print(b)  # Output: {'R': 'Red', 'G': 'Gray', 'B': 'Black', 'Y': 'Yellow'} Only latest values kept for duplicate keys

print(len(b))  # Output is 4 , Keys: 'R', 'G', 'B', 'Y'. duplicates are overwritten

HOME WORK 3

a = {True: 'Yes', 1: 'No', 1.0: 'May be'}  # All keys (True, 1, 1.0) are treated as the same key, so last value 'May be' remains

print(a)  #{True: 'May be'} is Only one entry, as all keys are equal (True == 1 == 1.0)

print(len(a))  #  1 is Only one unique key is stored in the dictionary

HOME WORK 4


 a = { [] : 25}  # Error: lists are unhashable and can't be used as dictionary keys.

b = {() : 25}  # Empty tuple is hashable, valid as a dictionary key

print(b)  #{(): 25} Dictionary with an empty tuple as key and 25 as value

 c = { {} : 25}  # Error: dicts are unhashable and can't be used as keys

d = {'Ramesh': [9948250500, 9848565090, 9440250404]}  # Valid dictionary: key is a string, value is a list of numbers

print(d)  # {'Ramesh': [9948250500, 9848565090, 9440250404]}  Dictionary with one key-value pair

print(len(d))  # 1 Only one key ('Ramesh') in thedictionary

 e = {set() : 10.8}  #Error, sets are unhashable and can't be used as keys .

HOME WORK 5

a = {}  # Creates an empty dictionary
print(type(a))  # <class 'dict'> — '{}' by default creates a dictionary
print(len(a))  # 0 , dictionary is empty, so length is 0
print(a)  # {} ,prints the empty dictionary

b = dict()  # Creates an empty dictionary using the dict() constructor
print(type(b))  # <class 'dict'>   b is a dictionary.
print(len(b))  # 0 , dictionary is empty, so length is 0
print(b)  # {} ,prints the empty dictionary
