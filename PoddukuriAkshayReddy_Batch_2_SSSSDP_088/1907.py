
190725


# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a)  #  {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a)) # <class 'dict'>
print(How  to  obtain  value  key  10)  # a[10]
print(How  to  obtain  value  key  20)  # a[20]
print(How  to  obtain  value  key  15)  # a[15]
print(How  to  obtain  value  key  18)  # a[18]
print(a[19]) # Error
print(a[0])  # Error 
print(a['Amar']) # Error
How  to  moify  value  of   key  15  to  'Krishna' # a[15] = 'krishna'
How  to  remove  20 :  'Kiran'  from  dict  'a'  # del a[20]
How  to  append  25 : 'Vamsi'  to  dict  'a'  # a[25]='vamsi'
print(a)   # {10 : 'Ramesh' , 25 : 'Vamsi' , 15 : 'krishna' , 18 : 'Sita'}
print(len(a)) # 4
print(a * 2)  #Error


# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'} 
print(a)  # {10 : 'Hyd' , 10 : 'Sec'}
print(len(a)) # 2
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b)  # {'R' : 'Red' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(len(b))  # 4


#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a)  # {True:'May be'}
print(len(a)) # 1


# Find  outputs
a = { [ ] : 25} # Error
b = { ( ) : 25} # Error
print(b)  
c = { { } : 25} # Error
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d)   #  {'Ramesh': [9948250500, 9848565090, 9440250404]}
print(len(d))  # 1
e = {set() : 10.8}


# Find  outputs
a = {}
print(type(a)) # <class 'dict'>
print(len(a))  #  0
print(a) # {}
b = dict()
print(type(b))  # <class 'dict'>
print(len(b))   # 0
print(b)        # {}