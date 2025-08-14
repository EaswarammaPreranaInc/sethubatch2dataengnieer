# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a).  # {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a)). #. class Dictionary
print(How  to  obtain  value  key  10).  # print(a[10])
print(How  to  obtain  value  key  20) # print(a[20])
print(How  to  obtain  value  key  15). # print(a[15])
print(How  to  obtain  value  key  18)  #.  print(a[18])
print(a[19]). # Error Due to a[19] is not available in dict
print(a[0]).  # # Error Due to a[0] is not available in dict
print(a['Amar']). #. Error Due to Dict allowed only using keys not values
How  to  moify  value  of   key  15  to  'Krishna'. #. a[15] = 'Krishna'
How  to  remove  20 :  'Kiran'  from  dict  'a'.  # del a[20]
How  to  append  25 : 'Vamsi'  to  dict  'a'. #. a[25]= 'Vamshi'
print(a). #. {10 : 'Ramesh' , 15 : 'Krishnal' , 18 : 'Sita' , 20: 'Vamshi'}
print(len(a)). # 4
print(a * 2). # Error

# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a). #.  { 10 : 'Sec'}
print(len(a)) # 1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'} 
print(b)  #. {'R' : 'Red'  , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'} 
print(len(b)) # 4


#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a). #. {1.0: 'May  be'}
print(len(a)) # 1


# Find  outputs
a = { [ ] : 25}. #. Error
b = { ( ) : 25}.  #. Error
print(b).  # Error

c = { { } : 25} # Error
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d). {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d)) # 1
e = {set() : 10.8}  #. Error Set not allowed in Dict

# Find  outputs
a = {}
print(type(a)). #. class Dict
print(len(a)) #. 0
print(a) # empty Dict
b = dict()
print(type(b)) # class 'Dict'
print(len(b)) #. 0
print(b). #. empty Dict