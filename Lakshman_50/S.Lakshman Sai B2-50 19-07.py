# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita',}
print(a)
print(type(a))
print(How  to  obtain  value  key  10)  #a[10]
print(How  to  obtain  value  key  20)  #a[20]
print(How  to  obtain  value  key  15)  #a[15]
print(How  to  obtain  value  key  18)  #a[18]
print(a[19])    #Error: because key 19 is not present in the dict
print(a[0])     #Error: because key 0 is not present in the dict
print(a['Amar'])  # Error: because key 'Amar' is not present in the dict 
How  to  moify  value  of   key  15  to  'Krishna' #a[15]='Krishna'
How  to  remove  20 :  'Kiran'  from  dict  'a'  # del a[20]
How  to  append  25 : 'Vamsi'  to  dict  'a'  #a[25]='Vamsi'
print(a)     # {10: 'Ramseh', 15: 'Krishna', 18: 'sita',25:'Vamsi'}
print(len(a))  #4
print(a * 2)   # Error: dict does not support multiplication becauuse it is not a sequence type


# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a)    #{10: 'Sec'}
print(len(a))    #1 
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b)    #{'R': 'Red', 'G': 'Gray', 'B': 'Black', 'Y': 'Yellow'}
print(len(b))   #4


#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a)   #{True: 'May be'}
print(len(a))   #1



# Find  outputs
a = { [ ] : 25}    #Error: dict keys must be immutable
b = { ( ) : 25}      
print(b)            ##{(): 25}  
c = { { } : 25}      #Error: dict keys must be immutable
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d)    #{'Ramesh': [9948250500, 9848565090, 9440250404]}
print(len(d))   #1
e = {set() : 10.8}   # error because it creates an empty set which is mutable


# Find  outputs
a = {}
print(type(a))     #<class 'dict'>
print(len(a))       #0
print(a)            #{}
b = dict() 
print(type(b))     #<class 'dict'>
print(len(b))       #0
print(b)           #{}