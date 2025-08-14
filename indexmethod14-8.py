'''  (Home  work)
index()  method  demo  program
Modify  the  following  program  with  index()  method
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')
index()  method
-------------------
It  is  same  as  find()  method  except  that  it  throws   error (but  not  -1) when  string  is  not  found
Syntax :  Same  as   find()  method'''


a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
b = a .index('is')
while  b != -1:
	print(b)
	b=a.index('is',b+1)
print('End')


