a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) # prints the dict object {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a)) # as the object is dict type a will also be class <dict>
print(How  to  obtain  value  key  10) # the value of key 10 is printed by using a[10]
print(How  to  obtain  value  key  20) # the value of key 20 is printed by using a[20]
print(How  to  obtain  value  key  15) # the value of key 15 is printed by using a[15]
print(How  to  obtain  value  key  18) # the value of key 18 is printed by using a[18]
print(a[19]) # error becuase we dont have key as 19
print(a[0]) # error becuase we dont have key as 0
print(a['Amar']) # error becuase we dont have key as Amar
How  to  moify  value  of   key  15  to  'Krishna' # a[15]='krishna'
How  to  remove  20 :  'Kiran'  from  dict  'a' # del a[20]
How  to  append  25 : 'Vamsi'  to  dict  'a' # a[25]='vamsi'
print(a) # {10: 'Ramesh', 15: 'krishna', 18: 'Sita', 25: 'vamsi'}
print(len(a)) # counts the key value pairs i.e 4
print(a*2) # error because dict is not repeaatable

a = {10 : 'Hyd' , 10 : 'Sec'} # assigns dict to a
print(a) # {10: 'Sec'} as 2nd key is also 10 sec replaces hyd
print(len(a)) # 1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'} # assigns dict to b
print(b) # {'R': 'Red', 'G': 'Gray', 'B': 'Black', 'Y': 'Yellow'} as G key is repeated green is replaced with greu and b is repeated so blue is replaced with black
print(len(b)) # after the duplicats are removed key value pairs are 4

a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'} # assigns dict to a
print(a) # as True , 1, 1.0 are same yes and no are replaced by may be i.e {True: 'May  be'}
print(len(a)) # as we have only 1 key value pair len is 1

a = { [ ] : 25} # error because key cannot be mutable object list is a mutable object
b = { ( ) : 25} # creates a dict with key as tuple and value as 25 as tuple is immutable object
print(b) # {(): 25}
c = { { } : 25} # error because key cannot be mutable object dict is a mutable object
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]} # assigs the dict obj with key ramesh and value with a list
print(d) # {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d)) # the number of key value pairs is 1 only so len is 1
e ={set():10.8} # error because key cannot be mutable object set is a mutable object

a = {} # empty dict object is assigned to a
print(type(a)) # as empty dict is assigned type will be class dict
print(len(a)) # as there are no arguments in dict len will be 0
print(a) # empty dict {} is printed
b = dict() # a dict object with no arguments is created and assigned
print(type(b))  # as empty dict is assigned type will be class dict
print(len(b)) # as there are no arguments in dict len will be 0
print(b) # empty dict {} is printed