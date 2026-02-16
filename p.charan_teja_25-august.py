# intersection() method demo program
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
c = a.intersection(b)
print(c)
print(type(c))
d = a & b
print(d)
print(type(d))
print(c is d)
print(c == d)





# difference() method demo program
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
c = a.difference(b)
print(c)
print(type(c))
d = a - b
print(d)
print(type(d))
print(c is d)
print(c == d)






# symmetric_difference() method demo program
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
c = a.symmetric_difference(b)
print(c)
print(type(c))
d = a ^ b
print(d)
print(type(d))
print(c is d)
print(c == d)





# Find outputs (Home work)
a = {x * x for x in range(10)}
print(a)
print(type(a))





# Program to remove duplicate characters of the string using set
input_string = "Rama Rao"
unique_chars = set(input_string)
output_string = "".join(sorted(list(unique_chars)))
print(f"String without duplicates: {output_string}")





# Program to remove duplicate elements of a list using set
input_list = [False, 25, 10.8, 1, 25, 0, 'Hyd', 10.8, 1.0, None, 'Sec', 'Hyd', True]
unique_elements_set = set(input_list)
output_list = list(unique_elements_set)
print(f"List without duplicates: {output_list}")






# Program to obtain common elements between two lists using sets
list1 = [10, 20, 30, 40, 50, 60]
list2 = [30, 40, 70, 80, 20]
set1 = set(list1)
set2 = set(list2)
common_elements_set = set1.intersection(set2)
common_elements_list = list(common_elements_set)
print(f"Common elements between the 2 lists: {common_elements_list}")





# How to access values of a dictionary
a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(a['Empno'])
print(a['Ename'])
print(a['Sal'])






# How to modify values of a dictionary
a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(a)
print(id(a))
a['Sal'] = 2000
a['Ename'] = 'Sita'
a['Empno'] = 35
print(a)
print(id(a))






# How to append key: value pairs to a dictionary
a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(a)
a['Gender'] = 'M'
a['Married'] = True
print(a)







# Find outputs (Home work)
a = {}
a[10] = 'Rama'
a[20] = 'Sita'
a[15] = 'Rajesh'
a[18] = 'Kiran'
print(a)






# How to remove key: value pairs of a dictionary
a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(a)
del a['Sal']
print(a)






# in and not in operators (Home work)
a = {10: 20, 30: 40, 50: 60, 70: 80}
print(30 in a.keys())
print(60 in a.keys())
print(60 in a.values())
print(30 in a.values())
print(50 in a)
print(20 in a)
print(70 not in a.keys())
print(40 not in a.values())
print(25 not in a)







# What are the outputs if input is {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
user_input = "{10: 'A', 20: 'B', 15: 'C', 20: 'D'}"
print(user_input)
print(type(user_input))
b = eval(user_input)
print(b)
print(type(b))






# Find outputs (Home work)
a = {10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
b = {**a}
print(b)
print(a is b)
print(a == b)
c = a
print(a is c)
print(a == c)






# Find outputs (Home work)
a = {10: 'Rama', 20: 'Sita', 15: 'Rajesh'}
b = {18: 'Kiran', 14: 'Amar', 20: 'Manohar'}
c = {25: 'Ramesh', 19: 'Krishna', 15: 'Radha', 14: 'Srinivas'}
d = {*a, *b, *c}
print(d)
print(type(d))
e = {**a, **b, **c}
print(e)
print(type(e))







# Find outputs (Home work)
a = {10: 20, 30: 40}
b = {30: 50, 10: 60}
# print(a + b) # This will raise a TypeError
c = {**a, **b}
print(c)
# d = a | b # This will raise a TypeError
# print(d)







# Program to create a dictionary with emp names and salaries
num_employees = 4
employee_salaries = {}
for i in range(num_employees):
    emp_name = input(f"Enter Emp Name : ")
    salary = float(input(f"Enter Salary : "))
    employee_salaries[emp_name] = salary
print(employee_salaries)






# Program to convert a string to a dictionary
input_string = "Emp no = 25 , Emp name = Rama Rao , sal = 10000.0 , gender = m"
parts = input_string.split(' , ')
output_dict = {}
for part in parts:
    key, value = part.split(' = ')
    output_dict[key.strip()] = value.strip()
print(output_dict)






# len() function demo program
a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(len(a))
b = {}
print(len(b))






# sum() function demo program
a = {10: 20, 30: 40, 50: 60}
print(sum(a.keys()))
print(sum(a.values()))
print(sum(a))
# print(sum(a.items())) # This will raise a TypeError






# max() and min() functions demo program
a = {10: 20, 30: 25, 40: 5, 7: 28, 9: 50}
print(max(a.keys()))
print(min(a.keys()))
print(max(a.values()))
print(min(a.values()))
print(max(a.items()))
print(min(a.items()))
print(max(a))
print(min(a))








# dict() function demo program
a = [(10, 'Hyd'), (20, 'Sec'), (15, 'Cyb'), (20, 'Pune')]
b = dict(a)
print(b)
c = [['R', 'Red'], ['G', 'Green'], ['B', 'Blue'], ['G', 'Gray']]
d = dict(c)
print(d)
e = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
# print(dict(e)) # This will raise a ValueError
f = [[10], [20], [30]]
# print(dict(f)) # This will raise a ValueError
# print(dict([10, 20])) # This will raise a ValueError
g = [[10, [20, 30]], [40, [50, 60]], [70, [80, 90]]]
print(dict(g))
h = [[[10, 20], 30], [[40, 50], 60], [[70, 80], 90]]
print(dict(h))
i = [[(10, 20), 30], [(40, 50), 60], [(70, 80), 90]]
print(dict(i))








# sorted() function
a = {10: 'Red', 20: 'Green', 15: 'Blue', 18: 'Yellow', 5: 'White'}
b = sorted(a.keys())
print(b)
c = sorted(a.values())
print(c)
d = sorted(a.items())
print(d)
f = sorted(a, reverse=True)
print(f)
print(a)






# Program to sort dictionary wrt keys
input_dict = {10: 'A', 20: 'B', 15: 'C', 5: 'D', 12: 'E'}
sorted_keys = sorted(input_dict.keys())
sorted_dict = {key: input_dict[key] for key in sorted_keys}
print(sorted_dict)







# clear() method demo program
a = {10: 20, 30: 40, 50: 60}
print(a)
a.clear()
print(a)
# del a
# print(a) # This will raise a NameError






# copy() method demo program
a = {'R': 'Red', 'G': 'Green', 'B': 'Blue'}
b = a.copy()
print(b)
print(a is b)
print(a == b)





# keys() method demo program
a = {10: 'Hyd', 20: 'Sec', 15: 'Cyb', 18: 'Pune'}
b = a.keys()
print(b)
print(type(b))
for x in b:
    print(x)





# values() method demo program
a = {10: 'Hyd', 20: 'Sec', 15: 'Cyb', 18: 'Pune'}
b = a.values()
print(b)
print(type(b))
for x in b:
    print(x)





# items() method demo program
a = {10: 'Hyd', 20: 'Sec', 15: 'Cyb', 18: 'Pune'}
b = a.items()
print(b)
print(type(b))
for x in b:
    print(x)
for x, y in b:
    print(x, y, sep=' ... ')







# Find outputs (Home work)
a = {10: 'Hyd', 20: 'Sec', 15: 'Cyb', 18: 'Pune'}
for x, y in a.items():
    print(x, y, sep=' ... ')
# for x, y in a.keys():
#    print(x, y, sep=' ... ') # This will raise a ValueError
# for x, y in a.values():
#    print(x, y, sep=' ... ') # This will raise a ValueError
# for x, y in a:
#    print(x, y, sep=' ... ') # This will raise a ValueError






# Find outputs (Home work)
a = {10: 'Rama', 20: 'Sita', 15: 'Rajesh'}
x, y, z = a.keys()
print(x)
print(y)
print(z)
print()
x, y, z = a.values()
print(x)
print(y)
print(z)
print()
x, y, z = a.items()
print(x)
print(y)
print(z)
print()
(rno1, sname1), (rno2, sname2), (rno3, sname3) = a.items()
print(rno1, sname1)
print(rno2, sname2)
print(rno3, sname3)







# Program to determine frequency of each alphabet in the string
input_string = "RamA raO"
freq_dict = {}
for char in sorted(input_string.upper()):
    if 'A' <= char <= 'Z':
        freq_dict[char] = freq_dict.get(char, 0) + 1
print(freq_dict)
