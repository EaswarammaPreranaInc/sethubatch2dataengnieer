a = {10 : 'Hyd' , 10 : 'Sec'}
print(a)#{10:'Sec'}
print(len(a))#1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b)#{'R': 'Red', 'G': 'Gray', 'B': 'Black', 'Y': 'Yellow'}
print(len(b))#4

a = {10 : 'Hyd' , 10 : 'Sec'}
print(a)#{10:'Sec'}
print(len(a))#1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b)#{'R': 'Red', 'G': 'Gray', 'B': 'Black', 'Y': 'Yellow'}
print(len(b))#4

a = { [ ] : 25}#TypeError: unhashable type: 'list'
b = { ( ) : 25}
print(b)#{(): 25}
c = { { } : 25}#TypeError: unhashable type: 'dict'
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d)#{'Ramesh': [9948250500, 9848565090, 9440250404]}
print(len(d))#1
e = {set() : 10.8}#SyntaxError: invalid non-printable character U+00A0      

a = {}
print(type(a))#<class 'dict'>
print(len(a))#0
print(a)#{}
b = dict()
print(type(b))#<class 'dict'>
print(len(b))#0
print(b)#{}
