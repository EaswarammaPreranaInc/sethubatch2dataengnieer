#Dict Object

# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a)          #{10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a))    #<class 'dict'>
print(a[10])      #Value  of   key  10  i.e. Ramesh
print(a[20])      #Value of   key  20  i.e Kiran
print(a[15])      #Value  of   key  15  i.e Amar
print(a[18])      #Value  of  key  18  i.e sita
#print(a[19])     #Error :  Key  19  does  not  exist  in  dict  'a'
#print(a[0])      #Error :  Key  0  does  not  exist  in  dict  'a'
#print(a['Amar']) #Error :  Key  'Amar'  does  not  exist  in  dict  'a'
a[15] = 'Krishna' #Value of   key  15  is  modified  to  'Krishna'  in  dict  'a'
del   a[20]       #Removes  20 :  'Kiran'   from  dict  'a'
a[25] = 'Vamsi'   #Appends  25 : 'Vamsi'  to  dict  'a'
print(a)          #{10 : 'Ramesh', 15 : 'Krishna', 18 : 'Sita' , 25:'Vamsi'}
print(len(a))     #4
#print(a * 2)     #Error : Dict can not be repeated as duplicate keys are obtained it is repeated

# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}  #Replaces  'Hyd'  with  'Sec'  as   key  10  is  repeated
print(a)                       #{10: 'Sec'}
print(len(a))                  #1
b = {'R' : 'Red', 'G' : 'Green', 'B' : 'Blue', 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b)                       #{'R': 'Red', 'G': 'Gray', 'B': 'Black', 'Y': 'Yellow'}
print(len(b))                  #4

#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a)                #{True : 'May  be'}
print(len(a))           #1

# Find  outputs
#a = { [ ] : 25}       #TypeError: unhashable type: 'list',key  can  not  be  a  mutable  object  such  as  list
b = { ( ) : 25}        #Valid :  key  can  be  immutable  object such  as  tuple
print(b)               #{ ( ) : 25}
#c = { { } : 25}       #TypeError: unhashable type: 'dict', key  can  not  be  a  mutable  object  such  as  dict
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]} #  Valid :  key  can  be  immutable  object such  as  string
print(d)               #{'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d))          #1
#e = {set() : 10.8}    #TypeError: unhashable type: 'set',  key  can  not  be  a  mutable  object  such  as  set

# Find  outputs
a = {}         #Empty  dictionary
print(type(a)) #<class 'dict'>
print(len(a))  #0
print(a)       #{}
b = dict()     #Functions  returns  an  empty  dictionary
print(type(b)) #<class 'dict'>
print(len(b))  #0
print(b)       #{}