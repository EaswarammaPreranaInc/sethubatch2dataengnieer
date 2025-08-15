# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a)# {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a)) ##class dict
print(How  to  obtain  value  key  10)#a[10]
print(How  to  obtain  value  key  20)#a[20]
print(How  to  obtain  value  key  15)#a[15]
print(How  to  obtain  value  key  18)#a[18]
print(a[19])#error no key
print(a[0])#no index
print(a['Amar'])#error
How  to  moify  value  of   key  15  to  'Krishna'##a[15]='Krishna'
How  to  remove  20 :  'Kiran'  from  dict  'a'#del[20]
How  to  append  25 : 'Vamsi'  to  dict  'a'#a[25]= 'vamsi'
print(a)#{10 : 'Ramesh'  , 15 : 'krishna' , 18 : 'Sita',25:'vamsi'}
print(len(a))3
print(a * 2)#error no repetition


# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a)#{10 : 'Hyd'}
print(len(a))#1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b)#{'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' }
print(len(b))#4



 #  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a)# {True : 'Yes' , 1 : 'No' }
print(len(a))2


# Find  outputs
a = { [ ] : 25}#error list is mutable
b = { ( ) : 25}
print(b)#{(): 25}
c = { { } : 25}#error it's mutable
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d)#{'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d))#1
e = {set() : 10.8}#error key can't be immutable


# Find  outputs
a = {}
print(type(a))#class dict
print(len(a))#0
print(a)#{}
b = dict()
print(type(b))#class dict
print(len(b))#0
print(b){}