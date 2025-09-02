# Find outputs (Home work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) # prints dictionary i.e. {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a)) #<class 'dict'>
print(a[10])#How to obtain value key 10
print(a[20])#How to obtain value key 20
print(a[15])#How to obtain value key 15
print(a[18])#How to obtain value key 18)
print(a[19]) # error
print(a[0]) # error
print(a['Amar']) # error
a[15] = krishna #How to moify value of key 15 to 'Krishna'
del a[20]#How to remove 20 : 'Kiran' from dict 'a'
a[25] = 'Vamsi' #How to append 25 : 'Vamsi' to dict 'a'
print(a) # prints updated dictionary
print(len(a)) # 4
print(a * 2) #error
# Find outputs (Home work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a)# prints dict {10 : 'Sec'}
print(len(a))# length is 1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b)#prints dict {'R' : 'Red' ,'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(len(b))# length is 4
# Tricky program
# Find output (Home work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May be'}
print(a) # {True : 'Yes'}
print(len(a))# length is 1
# Find outputs
a = { [ ] : 25} #error
b = { ( ) : 25}
print(b) # valid prints { ( ) : 25}
c = { { } : 25} #error
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d) # print {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d)) # length is 1
e = {set() : 10.8}#error
# Find outputs
a = {}
print(type(a)) #<class 'dict'>
print(len(a)) # 0
print(a) # prints {}
b = dict() #empty dict
print(type(b)) #<class 'dict'>
print(len(b))# length 1
print(b) #empty dict {}
