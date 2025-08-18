# Find  outputs 

a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a)  #  {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a)) #<class 'dict'>
print(How  to  obtain  value  key  10) #a[10]
print(How  to  obtain  value  key  20) #a[20]
print(How  to  obtain  value  key  15) #a[15]
print(How  to  obtain  value  key  18) #a[18]
print(a[19]) #Error  No key value 19 in dict a
print(a[0]) #Error No key value 10 in dict a
print(a['Amar']) #Error 'Amar' is not a key 
How  to  moify  value  of   key  15  to  'Krishna' #a[15]='Krishna'
How  to  remove  20 :  'Kiran'  from  dict  'a' # del a[20]
How  to  append  25 : 'Vamsi'  to  dict  'a' #a[25]='Vamsi'
print(a)  #{10 : 'Ramesh' , 15 : 'Krishna' , 18 : 'Sita',25 :'Vamsi'}
print(len(a)) #4
print(a * 2) #Error 
--------------------------------------------------------------------------

# Find  outputs  
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a) #{10 : 'Sec'}
print(len(a))#1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b) {'R' : 'Red' , 'G' : 'Gray' , 'B' : 'Blue' , 'Y' : 'Yellow' ,'B' : 'Black'}
print(len(b)) #5
--------------------------------------------------------------------------
#  Tricky  program
# Find output 
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a) #{True: 'May  be'}
print(len(a)) #1
--------------------------------------------------------------------------
 # Find  outputs
a = { [ ] : 25} #Error
b = { ( ) : 25} #valid
print(b) #{ ( ) : 25}
c = { { } : 25} #error
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d) #{'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d)) #1
e = {set() : 10.8} #Error
--------------------------------------------------------------------------
# Find  outputs
a = {} #empty dictionary
print(type(a)) # <class 'dict'>
print(len(a)) #0
print(a) #{}
b = dict() #empty dictionary
print(type(b)) #<class 'dict'>
print(len(b))#0
print(b) #{}