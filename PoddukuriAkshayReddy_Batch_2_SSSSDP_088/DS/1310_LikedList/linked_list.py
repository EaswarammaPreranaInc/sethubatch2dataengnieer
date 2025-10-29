 #  Write  a  program   to  determine  length  of  linked  list
class  sll(linked_list):
	def  length(a):
			return  number  of  nodes  in  the  linked  list
# End  of  the  class
if  _name_  ==  '_main_':
	How  to  create  linked  list
	print('Number  of  nodes : ' , ???)


'''
Write  a  progam  to  determine  data  of  ith  node

1) What  does  method  do  when  ith  node  exists ?  --->  Return  data  of  ith  node

2) What  does  method  do  when  ith  node  does  not  exist ?  --->  Return  None
'''
class   linkedlist(sll):
	def  find(a , i):
			return  data  of  ith  node
			and  return  None  when  ith  node  does  not  exist
# End  of  the  class
How  to  create  linked  list
while  True:
	i = int(input("Enter  value  of  'i':  "))
	How  to   obtain  data  of  ith  node
	if  ???
		print(F'Node  {i}  does  not  exist')
	else:
		print(F'Data   of  node  {i}  is  :  ???')
	ch = input('Do  you  wish  to  continue (y / n) :  ')
	if  ch == 'N'  or  ch == 'n':
			break
# End  of  while  loop
print('Good  Bye')



'''
Write  a  method  to  search  for  a  value  in  the  linked  list.

1) What  action  to  be  made  when  'x'  is  not  in  the  node  of  linked  list ?  --->  Move  reference  to  the  next  node

2) What  action  to  be  made  when  'x'  is  in  the  current  node  ?  --->  Return  address  of  that  node

3) What  action  to  be  made  when  'x'  is  not  found  in  the  linked  list  ?  --->  return  None  outside  the  loop
'''
class  sll(linked_list):
	def  search(a , x):
			return  address  of  that  node  where  'x'  is  found  and  None  otherwise
# End  of  the  class
How  to  create  linked  list
while  True:
	x = eval(input("Enter  value  to  be  searched :  "))
	How  to  call  search()  method
	if  ???
		print(F'{x}  is  not  found')
	else:
		print(F'Found  at  address  :  ???')
	ch = input('Do  you  wish  to  continue (y / n) :  ')
if  ch == 'N'  or  ch == 'n':
			reak
# End  of  while  loop
print('Good  Bye')

    
    
    
'''
Write  a  method  to  insert  a  node  in  the  linked  list
1) How  many  links  have  to  be  modified  for  insertion ?  --->  Two  links

2) How  to  insert  a  node  at  the  begining  of  linked list ?  --->  Modify  new  node  link  to  1st  node
																														and
																										modify  the  reference  a . first  to  new  node

3) How  to  insert  a  node  at  the  end  of  linked list ?  --->  Modify  new  node  link  to  None
																												and
																								modify  last  node  link  to  new  node

4) How  to  insert  a  node  after  ith  node ?  --->  Modify  new  node  link  to  (i + 1)th  node  and
																		        modify  ith  node  link   to  new  node

5) In  which  order  can  links  be  modified ?  --->  Modify  new  node  link  first  and  then  existing  node  link

6) Is  logic  same  for  middle  insertion  and  insertion  at  the  end  ? --->  Yes

7) What  is  the  difference  between  insertion  at  the  begining  and  insertion  anywhere  else ?  --->
															a . first  is  modified  when  node  is   inserted  at  the  begining  and
															a . first  reference  remains  unchanged  when  node  is   inserted  anywhere  else
'''
class  linkedlist(sll):
	def  insert(a , i , x):
		if  'i'  is  an  invalid  node  number:
				print(F'Node  {i}  does  not  exist')
		elif  insertion  at  the  begining  of  LL:
				How  to  create  a  new  node
				How  to  insert  new  node  at  the  begining  of  LL
		else:
			How  to  create  a  new  node
			How  to  insert  new  node  after  ith  node  of  LL
# End  of  the  class
How  to  create  a  linked  list
while  True:
	i = int(input("Enter  value  of  'i' :  "))
	x = eval(input('Enter  value  to  be  inserted  :  '))
	How  to  insert   new  node  after   ith  node
	print('Linked  List  :  ' , end = '')
	How  to  print  linked  list
	ch = input('Would  you  like  to  insert  another  node (Y  or   N) ?  :  ')
	if  ch == 'n'  or  ch == 'N':
		break


''
rite  a method  to  delete  ith  node  of  linked  list

1) How  many  links  have  to  be  modifed  for  deletion ?  --->  Single  link

2) How  to  remove  ith  node  of  linked list ?  --->  Modify  (i - 1)th  node  link  to  (i + 1)th  node

3) How  to  remove  first  node  of  linked list ?  --->  Move  a . first  to  2nd  node

4) How  to  remove  last  node  of  linked list ?  --->  Modify  last  but  one  node  link  to  None

5) How  to  remove  the  node  when  there  is  a  single  node  in  linked  list  ?  --->  Reinitialize  a . first  to  None

6) Logic  for  middle  node  and  last  node  deletion  is  same

7) Similarly  logic  for  first  node  and  single  node  deletion  is  same
' ''
class  linkedlist(sll):
	def  delete(a , i):
		if   'i'  is  an  invalid  node  number:
			return   ???
		elif  deletion of  1st  node:
			How  to  delete  first  node  logically
			How  to  delete  first  node  physically
			How  to  return  data  of  the  deleted  node
		else:
			How  to  modify  (i - 1)th  node  link  to  (i + 1)th node
			How  to  delete  ith  node
			How  to  return  data  of  the  deleted  node
# End  of  the  class
How  to  create  linked  list
while  True:
	i = int(input('Enter  value  of  i  :  '))
	How  to  delete  ith  node
	if  ???:
			print(F'Node  {i}  does  not  exist')
	else:
			print('Data  of  deleted  node  is  ' ,  ???)
	print('Linked  List  :  ' , end = '')
	How  to  print  linked  list
	ch = input('Would  you  like  to  delete  another  node (Y  or   N) ?  :  ')
	if  ch == 'n'  or  ch == 'N':
		break