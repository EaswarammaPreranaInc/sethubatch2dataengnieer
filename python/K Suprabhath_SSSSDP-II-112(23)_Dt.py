#  intersection()   method  demo  program (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . intersection(b)
print(c)#  {30 , 40}
print(type(c))#  <class 'set'>
d = a & b
print(d)#  {30 , 40}
print(type(d))#  <class 'set'>
print(c  is  d)#  False
print(c  ==  d)#  True

# difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b)
print(c)#  {10 , 20}
print(type(c))#  <class 'set'>
d = a - b
print(d)#  {10 , 20}
print(type(d))#  <class 'set'>
print(c  is  d)#  False
print(c  ==  d)#  True
# symmetric_difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)
print(c)# {10, 20, 50, 60}
print(type(c))# <class 'set'>
d = a ^ b
print(d)# {10, 20, 50, 60}
print(type(d))# <class 'set'>
print(c   is   d)# False
print(c  ==   d)# True


# Find  outputs  (Home  work)
a = {x * x  for   x   in   range(10)}
print(a)# {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
print(type(a))# <class 'set'>

##remove duplicates from a string while preserving order
def remove_duplicates_using_set(input_str):
    seen = set()
    result = ''
    for char in input_str:
        if char not in seen:
            seen.add(char)
            result += char
    return result

# Test
input_str = "Rama Rao"
output_str = remove_duplicates_using_set(input_str)
print("Output:", output_str)  # Output: Ram o

##remove duplicates from a list while preserving order
def remove_duplicates(input_list):
    seen = set()
    result = []
    for item in input_list:
        # Check if item is not in the set, add it to both set and result list
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Test
input_list = [False, 25, 10.8, 1, 25, 0, 'Hyd', 10.8, 1.0, None, 'Sec', 'Hyd', True]
output_list = remove_duplicates(input_list)
print("Output:", output_list)  # Output: [False, 25, 10.8, 1, 'Hyd', None, 'Sec']

# Find common elements between two lists
def find_common_elements(list1, list2):
    # Convert both lists to sets and get the intersection
    common_elements = list(set(list1) & set(list2))
    return common_elements

# Test
list1 = [10, 20, 30, 40, 50, 60]
list2 = [30, 40, 70, 80, 20]

output = find_common_elements(list1, list2)
print("Output:", output)  # Output: [20, 30, 40]

a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}

# Accessing and printing values using the keys
print(a['Empno'])  # Output: 25
print(a['Ename'])  # Output: Rama Rao
print(a['Sal'])    # Output: 1000.65

## Initial dictionary
a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}

# Print the initial dictionary and its id
print("Before Modification:")
print(a)             # Output: {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(id(a))         # Shows the memory id of the dictionary

# Modify the values in the dictionary
a['Sal'] = 2000      # Modify the salary
a['Ename'] = 'Sita'  # Modify the name
a['Empno'] = 35      # Modify the employee number 
# Print the modified dictionary and its id
print("\nAfter Modification:")
print(a)             # Output: {'Empno': 35, 'Ename': 'Sita', 'Sal': 2000}
print(id(a))         # Shows the same memory id, dictionary is mutable

## Demonstration of appending key-value pairs to a dictionary
# Initial dictionary
a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}

# Print the initial dictionary
print("Before Appending:")
print(a)

# Append new key-value pairs to the dictionary
a['Gender'] = 'M'      # Add 'Gender' : 'M'
a['Married'] = True     # Add 'Married' : True

# Print the updated dictionary
print("\nAfter Appending:")
print(a)

## Demonstration of appending key-value pairs to an empty dictionary
# Initialize an empty dictionary
a = {}

# Append key-value pairs
a[10] = 'Rama'      # Add 10: 'Rama'
a[20] = 'Sita'      # Add 20: 'Sita'
a[15] = 'Rajesh'    # Add 15: 'Rajesh'
a[18] = 'Kiran'     # Add 18: 'Kiran'

# Print the updated dictionary
print(a)

## Demonstration of removing a key-value pair from a dictionary using del
# Initial dictionary
a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}

# Print the dictionary before removal
print("Before Removal:")
print(a)

# Remove the key 'Sal' using del
del a['Sal']

# Print the dictionary after removal
print("\nAfter Removal:")
print(a)

#  in  and  not  in  operators  (Home  work)
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys())# True
print(60  in  a . keys())# False
print(60  in  a . values())# True
print(30  in  a . values())# False
print(50  in  a)# True
print(20  in  a)# False
print(70  not  in  a . keys())# False
print(40  not  in  a . values())# True
print(25  not  in  a)# True
      
#  What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a = input('Enter  dictionary  :  ')
print(a)# {'10': 'A', '20': 'D', '15': 'C'}
print(type(a))# <class 'str'>
b = eval(a)
print(b)# {'10': 'A', '20': 'D', '15': 'C'}
print(type(b))# <class 'dict'>      

#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a}
print(b)# {10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
print(a  is  b)# False
print(a  ==  b)# True
c = a
print(a  is   c)# True
print(a  ==  c)# True
      
#Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c}
print(d)# {10, 14, 15, 18, 19, 20, 25}
print(type(d))# <class 'set'>
e = {**a , **b , **c}
print(e)# {10: 'Rama', 20: 'Manohar', 15: 'Radha', 18: 'Kiran', 14: 'Srinivas', 25: 'Ramesh', 19: 'Krishna'}
print(type(e))# <class 'dict'>      

#  Find  outputs  (Home  work)
a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
print(a + b)# TypeError
c = {**a , **b}
print(c)# {10: 60, 30: 50}
d = a | b
print(d)# {10: 60, 30: 50}


## Demonstration of appending employee names and salaries to a dictionary
# Initialize an empty dictionary
a = {}

# Append employee names and salaries to the dictionary
a['John'] = 50000  # Employee 'John' with salary 50000
a['Alice'] = 60000  # Employee 'Alice' with salary 60000
a['Bob'] = 55000    # Employee 'Bob' with salary 55000
a['Eve'] = 45000    # Employee 'Eve' with salary 45000

# Print the dictionary
print(a)


## Convert a formatted string into a dictionary
# Input string
input_str = "Emp no = 25 , Emp name = Rama Rao , sal = 10000.0 , gender = m"

# Initialize an empty dictionary
result_dict = {}

# Split the string by ', ' to separate each key-value pair
pairs = input_str.split(' , ')

# Loop through the pairs and split by '=' to extract key and value
for pair in pairs:
    key, value = pair.split(' = ')  # Split by '='
    result_dict[key.strip()] = value.strip()  # Remove any extra spaces

# Print the resulting dictionary
print(result_dict)

# len()  function  demo  program  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(len(a))# 3
b = {}
print(len(b))# 0

#  sum()  function demo  program  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(sum(a . keys()))# 90
print(sum(a . values()))# 120
print(sum(a))# 90
print(sum(a . items()))# TypeError

# max()  and  min()   functions  demo  program  (Home  work)
a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}
print(max(a . keys()))# 40
print(min(a . keys()))# 7
print(max(a . values()))# 50
print(min(a . values()))# 5
print(max(a . items()))# (40, 5)
print(min(a . items()))# (7, 28)
print(max(a))# 40
print(min(a))# 7

#  dict()  function  demo program (Home  work))
a = [ (10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')]
b = dict(a)
print(b)# {10: 'Hyd', 20: 'Pune', 15: 'Cyb'}
c = ( ['R' , 'Red'] , ['G' , 'Green'] , ['B' , 'Blue'] , ['G' , 'Gray'])
d = dict(c)
print(d)# {'R': 'Red', 'G': 'Gray', 'B': 'Blue'}
e = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
print(dict(e))# ValueError
f = [[10] , [20] , [30]]
print(dict(f))# {10: None, 20: None, 30: None}
print(dict([10 , 20]))# ValueError
g = [[10 , [20 , 30]] , [40 , [50 , 60]] , [70 , [80 , 90]]]
print(dict(g))# {10: [20, 30], 40: [50, 60], 70: [80, 90]}
h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]]
print(dict(h))# {[10, 20]: 30, [40, 50]: 60, [70, 80]: 90}# TypeError
i = [[(10 , 20) , 30] , [(40 , 50) , 60] , [(70 , 80) , 90]]
print(dict(i))# {(10, 20): 30, (40, 50): 60, (70, 80): 90}

# sorted()  function  (Home  work)
a = {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
b = sorted(a . keys())
print(b)# [5, 10, 15, 18, 20]
c = sorted(a . values())
print(c)# ['Blue', 'Green', 'Red', 'White', 'Yellow']
d = sorted(a . items())
print(d)# [(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')]
f  = sorted(a  , reverse = True)
print(f)# [20, 18, 15, 10, 5]
print(a)# {10: 'Red', 20: 'Green', 15: 'Blue', 18: 'Yellow', 5: 'White'}


## Sort a dictionary by keys
# Input dictionary
input_dict = {10: 'A', 20: 'B', 15: 'C', 5: 'D', 12: 'E'}

# Sort the dictionary by keys
sorted_dict = {key: input_dict[key] for key in sorted(input_dict)}

# Print the sorted dictionary
print(sorted_dict)

# clear()  method  demo  program (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(a)# {10: 20, 30: 40, 50: 60}
a . clear()
print(a)# {}
del  a
print(a)# NameError

# copy()  method demo  program  (Home  work)
a = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
b = a . copy()
print(b)# {'R': 'Red', 'G': 'Green', 'B': 'Blue'}
print(a  is  b)# False
print(a  ==  b)# True
      
#  keys()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . keys()
print(b)# dict_keys([10, 20, 15, 18])
print(type(b))# <class 'dict_keys'>
for  x  in   b:
        print(x)# 10 20 15 18

# values()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . values()
print(b)# dict_values(['Hyd', 'Sec', 'Cyb', 'Pune'])
print(type(b))# <class 'dict_values'>
for  x   in   b:
	print(x)# Hyd Sec Cyb Pune

#  items()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . items()
print(b)# dict_items([(10, 'Hyd'), (20, 'Sec'), (15, 'Cyb'), (18, 'Pune')])
print(type(b))# <class 'dict_items'>
for  x   in   b:
        print(x)# (10, 'Hyd') (20, 'Sec') (15, 'Cyb') (18, 'Pune')
for  x , y   in  b:
        print(x , y , sep = ' ... ')# 10 ... Hyd 20 ... Sec 15 ... Cyb 18 ... Pune

# Find  outputs (Home  work)
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
for  x , y   in  a . items():
       print(x , y , sep = ' ... ')# 10 ... Hyd 20 ... Sec 15 ... Cyb 18 ... Pune
for  x , y   in  a . keys():
       print(x , y , sep = ' ... ')# ValueError
for  x , y   in  a . values():
       print(x , y , sep = ' ... ')# ValueError
for  x , y   in  a:
       print(x , y , sep = ' ... ')# ValueError

#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
x , y , z = a . keys()
print(x)# 10
print(y)# 20
print(z)# 15
print()# new line
x , y , z = a . values()
print(x)# 'Rama'
print(y)# 'Sita'
print(z)# 'Rajesh'
print()# new line
x , y ,  z = a . items()
print(x)# (10, 'Rama')
print(y)# (20, 'Sita')
print(z)# (15, 'Rajesh')
print()# new line
(rno1 , sname1) , (rno2 , sname2) , (rno3 , sname3) = a . items()
print(rno1 , sname1)# 10 Rama
print(rno2 , sname2)# 20 Sita
print(rno3 , sname3)# 15 Rajesh

## Count frequency of each character in a string and store in a dictionary
# Input string
input_str = "RamA raO"

# Convert string to uppercase
input_str = input_str.upper()

# Initialize an empty dictionary to store the frequencies
freq_dict = {}

# Loop through each character in the string
for char in input_str:
    if char.isalpha():  # Ignore spaces and non-alphabet characters
        freq_dict[char] = freq_dict.get(char, 0) + 1

# Sort the dictionary by key (alphabetical order)
sorted_freq_dict = dict(sorted(freq_dict.items()))

# Print the result
print(sorted_freq_dict)



