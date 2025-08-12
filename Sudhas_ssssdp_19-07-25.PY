# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a)) #<class dict>
print(How  to  obtain  value  key  10) Ramesh
print(How  to  obtain  value  key  20) Kiran
print(How  to  obtain  value  key  15) Amar
print(How  to  obtain  value  key  18) Sita
print(a[19]) #error
print(a[0])#error
print(a['Amar']) #error
How  to  moify  value  of   key  15  to  'Krishna' a[15]="Krishna
How  to  remove  20 :  'Kiran'  from  dict  'a' del a[20]
How  to  append  25 : 'Vamsi'  to  dict  'a' a[25]='Vamsi'
print(a) {10 : 'Ramesh'  , 15 : 'Krishna' , 18 : 'Sita', 25 : 'Vamsi'}
print(len(a)) #4
print(a * 2) #error

# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a) #{10: 'Sec'}
print(len(a)) #1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b) #{'R' : 'Red' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(len(b)) # 4

#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a) #{ 1.0 : 'May  be'}
print(len(a)) #1

# Find  outputs
a = { [ ] : 25} #error
b = { ( ) : 25} 
print(b) #{(): 25}
c = { { } : 25}  #error
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d)  #{'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d))# 1
e = {set() : 10.8} #error

# Find  outputs
a = {}
print(type(a)) #<class dict>
print(len(a)) #0
print(a)# {}
b = dict()
print(type(b)) #<class dict>
print(len(b)) #0
print(b) #{}
