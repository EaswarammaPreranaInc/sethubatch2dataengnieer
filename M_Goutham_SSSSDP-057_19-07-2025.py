#Day-5 #Home Work-1
# Find  outputs  (Home  work)

a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'} #Here a Dict-object is assigned to reference a with 4 key value pairs
print(a) #Returns the dict-object with all key value pairs i.e {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a)) #Returns the type i.e <class 'dict'>
#print(How  to  obtain  value  key  10) #dict[key] i.e print(a[10])
#print(How  to  obtain  value  key  20) #dict[key] i.e print(a[20])
#print(How  to  obtain  value  key  15) #dict[key] i.e print(a[15])
#print(How  to  obtain  value  key  18) #dict[key] i.e print(a[18])
print(a[19]) #Error as there is no key value pair where key is 19
print(a[0]) #Error as there is no key value pair where key is 0
print(a['Amar']) #We can only access the value using key but not key using value
#How  to  moify  value  of   key  15  to  'Krishna' dict[valid-key] = 'newvalue' i.e 
a[15] = 'Krishna'
#How  to  remove  20 :  'Kiran'  from  dict  'a' #To remove we use del del dict[key] i.e 
del a[20]
#How  to  append  25 : 'Vamsi'  to  dict  'a' #To append new key value pair dict[new-key] = 'new-value' i.e 
dict[25] = 'Vamsi'
print(a) #Now it will prints the dict-object with the elements i.e {10: 'Ramesh', 15: 'Krishna', 18: 'Sita', 25: 'Vamsi'}
print(len(a)) #Returns the number of key value pairs present in the dict-object
print(a * 2) #Gives an error we cannot repeat the dict as it generates the duplicate keys so it is not possible


#Day-5 #Home Work-2
# Find  outputs  (Home  work)

a = {10 : 'Hyd' , 10 : 'Sec'} #Here a dict-object is assigned to reference a 
print(a) #Returns the key-value pairs which are the dict-object
print(len(a)) #Returns the number of elements in the dict-object i.e 2
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'} #Here dict-object is assigned to reference b
print(b) #Returns the dict-object i.e {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(len(b)) #Returns the number of key-value pairs i.e 6

#Day-5 Home Work-3
#  Tricky  program
# Find output  (Home  work)

a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'} 
#Here dict-object is assigned to reference a and initially 
#True:'yes' is a key-value pair 
#1:'No' #Here yes is replaced with no because python treats True/1/1.0 as same i.e True = 1/1.0 so here 'yes' is replaced with 'No'.
#1.0:'May be' #Here 'No' is replaced with 'May be' so the final dict-obj key-value pair is True:'May be'
print(a) #Returns the dict-object key value pair i.e {True:'May be'}
print(len(a)) #Returns the number of elements i,e 1

#Day-5 #Home Work-4
# Find  outputs

a = { [ ] : 25} #We get an error that always key should be immutable here key is list which is mutable
b = { ( ) : 25} #Here a dict object is assigned to reference b and here the key is tuple so it is possible as tupple is immutable
print(b) #Returns the dict-object i.e { () : 25 }
c = { { } : 25} #We will get an error that we are assigning the dict as a key as we know dict is mutable
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]} #Here we are assigning the dict-object to reference d and here the value is list as we know that value can be mutuable or immutable but key should be immutable
print(d) #Returns the dict-obj i.e {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d)) #Returns the number of key-value pairs i.e 1
e = {set() : 10.8} #Error as we know that set() is mutable object so key cannot be a mutable object


#Day-5 #Home Work-5
# Find  outputs

a = {} #An empty dict-obj is assigned to reference a
print(type(a)) #Returns the type i.e <class 'dict'>
print(len(a)) #Returns the number of elements in the dict-obj i.e 0
print(a) #Returns the empty dict-object
b = dict() #This is another way of creating an empty dict-object
print(type(b)) #Returns the type i.e <class 'dict'>
print(len(b)) #Returns the number of elements in the dict-obj i.e 0
print(b) #Returns the empty dict-object