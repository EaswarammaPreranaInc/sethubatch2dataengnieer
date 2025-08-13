#first program
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a)
print(type(a))
print(a[10])
print(a[20])
print(a[15])
print(a[18])
#print(a[19])
#print(a[0])
#print(a['Amar'])
print(a[15])
del (a[20])
print(a[25])
print(a)
print(len(a))
#print(a * 2)

#second program
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a)
print(len(a))
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b)
print(len(b))

#third program
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a)
print(len(a))

# fourth program
a = { [ ] : 25}
b = { ( ) : 25}
print(b)
c = { { } : 25}
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d)
print(len(d))
#e = {set() : 10.8}

#fifth program
a = {}
print(type(a))
print(len(a))
print(a)
b = dict()
print(type(b))
print(len(b))
print(b)