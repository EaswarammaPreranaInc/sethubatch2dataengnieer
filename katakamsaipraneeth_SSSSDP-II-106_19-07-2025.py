# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'} # ref 'a' is pointed to dictionary object
print(a) # {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a)) # <class  'dict'> because it contains key-value pairs in { }
print(How  to  obtain  value  key  10) # a[10]
print(How  to  obtain  value  key  20) # a[20]
print(How  to  obtain  value  key  15) # a[15]
print(How  to  obtain  value  key  18) # a[18]
print(a[19]) # error -no key 
print(a[0]) # error - no index 0
print(a['Amar']) # error - cannot use value as key
How  to  moify  value  of   key  15  to  'Krishna' # a[15] = 'Krishna'
How  to  remove  20 :  'Kiran'  from  dict  'a' # del a[20]
How  to  append  25 : 'Vamsi'  to  dict  'a' # a[25] = 'Vamsi'
print(a) # {10 : 'Ramesh' ,15 : 'Krishna' , 18 : 'Sita', 25 : 'Vamsi'}
print(len(a)) # 4
print(a * 2) # error

# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'} # no duplicate key are permited --{10: 'Sec'}
print(a) # -{10: 'Sec'}
print(len(a)) # 1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'} # dict object with keys-values
print(b) # {'R' : 'Red' , 'G' : 'Gray' , 'B' : 'Black' , 'Y' : 'Yellow'}
print(len(b)) # 4

#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'} # ref a is pointed to dict obj--no dup keys are allowed
print(a) # { True : 'May be'}
print(len(a)) # 1

# Find  outputs
a = { [ ] : 25}# error - no mutable object are allowed as key
b = { ( ) : 25} # dict object -- with no error
print(b)
c = { { } : 25} # error
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]} # dict obj
print(d) #{'Ramesh' : [9948250500, 9848565090, 9440250404]} 
print(len(d)) # 1
e = {set() : 10.8} # error


# Find  outputs
a = {}  # dict object 
print(type(a)) # <class  'dict'>
print(len(a)) # 0
print(a) # { }
b = dict() # empty dict
print(type(b)) # <class  'dict'>
print(len(b)) # 0
print(b) # { }