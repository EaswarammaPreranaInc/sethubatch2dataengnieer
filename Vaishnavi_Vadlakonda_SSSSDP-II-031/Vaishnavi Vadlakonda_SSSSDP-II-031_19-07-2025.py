# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) # prints dictionary 'a' i.e., {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a)) # prints type of object 'a' i.e., <class 'dict'>
print(a[10]) # prints the value of key 10 from the dictionary i.e., Ramesh
print(a[20]) # prints the value of key 20 from the dictionary i.e., Kiran
print(a[15]) # prints the value of key 15 from the dictionary i.e., Amar
print(a[18]) # prints the value of key 18 from the dictionary i.e., Sita
print(a[19]) # Error because key 19 is not there in the dictionary 'a'
print(a[0]) # Error because key 0 is not there in the dictionary 'a'
print(a['Amar']) # Error because when given value, key is not printed but when given key,value is printed
a[15] =  'Krishna' # Amar at key 15 is replaced with Krishna in the dictionary 'a'
a.remove[20] # removes key value pair at key 20  in the dictionary
a[25]: 'Vamsi' # appends new key value pair to the dictionary i.e., 25 : 'Vamsi'
print(a) # prints the modified dictionary 'a' i.e., {10 : 'Ramesh' , 15 : ;Krishna , 18 : 'Sita' , 25 : 'Vamsi'}
print(len(a)) # prints number of key value pairs in the dictionary 'a' i.e., 4
print(a * 2) # Error because dictionary cannot have duplicate keys













# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'} # key 10 is repeated so 'Hyd' is replaced with 'Sec'
print(a) # prints the dictionary 'a' after modifying value 'Hyd' of key 10 with 'Sec' because dictionary cannot have duplicate keys i.e., {10 : 'Sec'}
print(len(a)) # prints number of key value pairs in the dictionary 'a' i.e., 1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b) # prints the dictionary 'b' i.e., {'R' : 'Red', 'G' : 'Gray', 'B' : 'Black' 'Y' : 'Yellow'}
print(len(b)) # prints number of key value pairs in the dictionary i.e., 4









#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a) # prints {True: 'May be'},because in dictionary 'a' True,1 and 1.0 are treated as same,so only one key is printed and its values modified 1st it is 'Yes',2nd it is 'No' and 3rd it is 'May be'
print(len(a)) # prints number of key value pairs in the dictionary 'a' i.e., 1










# Find  outputs
a = {[] : 25}  # Error because in dictionary 'a' , key is [] and list is mutable,but dictionary does not contain duplicate keys 
b = {() : 25} # key can be tuple because tuple is immutable
print(b) # prints dictionary 'b' i.e., { () : 25},because tuple is immutable
c = {{} : 25} # Error because key is dictionary and dictionary is mutable
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d)  # prints dictionary 'd' i.e., {'Ramesh': [9948250500, 9848565090, 9440250404]}
print(len(d)) # prints number of key value pairs in dictionary 'd' i.e., 1
e = {set() : 10.8} # Error because set is mutable and dictionary cannot have duplicate keys










# Find  outputs
a = {} # Ref 'a' points to empty dictionary
print(type(a)) # prints type of object 'a' i.e., <class 'dict'>
print(len(a)) # prints number of key value pairs in the dictionary 'a' i.e., 0
print(a) # prints the dictionary 'a' i.e., {}
b = dict() # Returns empty dictionary
print(type(b)) # prints type of object 'b' i.e., <class 'dict'>
print(len(b)) # prints number of key value pairs in the dictionary 'b' i.e., 0
print(b) # prints the dictionary 'b' i.e., {}
