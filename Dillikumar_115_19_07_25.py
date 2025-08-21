ASSIGNMENT _19_07_25
# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a)
	{10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a))
	<class   ‘dict’>
print(How  to  obtain  value  key  10)   :    error 
print(How  to  obtain  value  key  20)    :  error
print(How  to  obtain  value  key  15)    :    error
print(How  to  obtain  value  key  18)     : error  
print(a[19])     :error , no key value pair at 19  key 
print(a[0])   :   error 
print(a['Amar'])    : error , only values print based on  key , but not printed keys based on values 
How  to  moify  value  of   key  15  to  'Krishna' 
	a[15]=’krishna’
How  to  remove  20 :  'Kiran'  from  dict  'a'
	a.pop(20)
How  to  append  25 : 'Vamsi'  to  dict  'a'
	a[25]=’Vamsi’
print(a) : {10: 'Ramesh', 15: 'Krishna', 18: 'Sita', 25: 'Vamsi'}
print(len(a)) : 4
print(a * 2) “error ,  its not possible to multiply dict with integer 

# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a)
	{10 : 'Hyd' , 10 : 'Sec'} {10 : 'Hyd' } , beacuese dicto t allowed duplicates 

print(len(a))  : 1 


b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b)
	{'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' }

print(len(b))   :  4
#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a)
	= {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(len(a)) : 2   // because true == 1 and 1==1.0
# Find  outputs
a = { [ ] : 25}
	Empty list 
b = { ( ) : 25}
print(b)
………………………… no idea .,,,,,,,,,,,,,,,,,,,,,,,,,,,
c = { { } : 25}
	Error 
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d)
	{'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d)) : 1 
e = {set() : 10.8}
	Error 
# Find  outputs
a = {}
print(type(a))	
	<class  ‘dict’>
	Empty dictionary will be printed 
print(len(a))  : 0  , i.e., no values in dict 
print(a)  : { }
b = dict()   : error  , invalid expression of b 
print(type(b))
	<class ‘dict’ >
print(len(b))  : 0 beacause no elements  are added
print(b) 
	{ }
