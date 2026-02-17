# Find  outputs  (Home  work)

a = {10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}	    # Creates a dictionary with 4 key-value pairs.
print(a)	        # Output: {10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}
print(type(a))	# Output: <class 'dict'> 
print(a[10])	# the value of key 10 Output: 'Ramesh'
print(a[20])	# the value of key 20 Output: 'Kiran'
print(a[15])	# the value of key 15 Output: 'Amar'
print(a[18])	# the value of key 18 Output: 'Sita'

print(a[19])	# error as key doesn't exist in dictionary 
print(a[0])	# error as key 0 is invalid key
print(a['Amar'])# error as key can't be accessed by values

# How  to  modify  value  of   key  15  to  'Krishna'
a[15] = 'Krishna'     # Changes key 15's value from 'Amar' : 'Krishna'
# How  to  remove  20 :  'Kiran'  from  dict  'a'
del a[20]	               # Removes 20: 'Kiran' from dict 'a'
# How  to  append  25 : 'Vamsi'  to  dict  'a'
a[25] = 'Vamsi'        # Appends new pair 25: 'Vamsi' in dict 'a'

print(a) 	        # modified output: {10: 'Ramesh', 15: 'Krishna', 18: 'Sita', 25: 'Vamsi'}
print(len(a))	# no. of key-value pairs: 4 
print(a * 2)	# error as we can't multiply a dictionary by an integer




# Find  outputs  (Home  work)

a = {10: 'Hyd', 10: 'Sec'}     # the 'Hyd' will be replaced with 'sec' for key 10
print(a)	       # Output: {10: 'Sec'}
print(len(a))	# no. of key-value pair: 1 

b = {'R': 'Red', 'G': 'Green', 'B': 'Blue', 'Y': 'Yellow', 'G': 'Gray', 'B': 'Black'}    # keys overwrite earlier ones with new values
print(b)	        # Output: {'R': 'Red', 'G': 'Gray', 'B': 'Black', 'Y': 'Yellow'}
print(len(b))	# Output: 4 (unique keys)




#  Tricky  program
# Find output  (Home  work)

a = {True: 'Yes', 1: 'No', 1.0: 'May be'} # here true, 1, 1.0 keys are same 
print(a)	        # Output: {True: 'May be'}
print(len(a))	# no. of key-value pair: 1 




# Find  outputs

a = {[]: 25}	# error as lists can't be dictionary keys
b = {(): 25}	# dictionary with tuple key 
print(b)	        # Output: {(): 25}
c = {{}: 25}	# error as dicts can't be dictionary keys
d = {'Ramesh': [9948250500, 9848565090, 9440250404]}
print(d)	         # Output: {'Ramesh': [9948250500, 9848565090, 9440250404]}
print(len(d))      # no. of key-value pair: 1 
e = {set(): 10.8} # error as sets can't be dictionary keys




# Find  outputs

a = {}		# empty dictionary
print(type(a)) 	# Output: <class 'dict'>
print(len(a))	# Output: 0 
print(a)	        # Output: {}

b = dict()	        # empty dictionary
print(type(b))	# Output: <class 'dict'>
print(len(b))	# Output: 0
print(b)	        # Output: {}