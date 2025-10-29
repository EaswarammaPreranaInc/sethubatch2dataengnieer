# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function')
print(a)
print()
#How  to  print  dictionary  with  print()  function
print('Keys  of  dictionary')
print(a.keys())
print()
#How  to  print  each  key  of  dict  'a'
for key in a.keys():
	print(key)
print('Values  of  dictionary')
print(a.values())
print()
#How  to  print  each  value  of  dict  'a'
for value in a.values():
	print(value)
print('All  the  tuples  of  dict_items   object')
print(a.items())
print()
#How  to  print  each  tuple  of  the  list  in  dict_items  object
print('Elements  of  each   tuple')
for items in a.items():
	print(items)
print()
#How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object
print('Keys  and  values  of  dictionary')
print(a)
#How  to  print  each  key  and  corresponding  value  in  dict  'a'

a=25
print(id(a))
a=35
print(id(a))
print(a)
	