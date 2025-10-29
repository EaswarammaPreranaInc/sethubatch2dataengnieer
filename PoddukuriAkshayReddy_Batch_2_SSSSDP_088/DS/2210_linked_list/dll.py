

    
    
    
#  Write  a  method  to  determine  length  of  circular  linked  list
class  cll(linkedlist):
	def  length(a):
			How  to  return  number  of  nodes  in  circular  linked  list
# End  of  the  class
if  _name_  ==  '_main_':
	How  to   create  circular  linked   list
	print('Number  of  nodes : ' , ???)

    
    
    
class  circular_linked_list(cll):
	def  find(a , i):
			return   data  of  ith  node  and  None  when  ith  node  does  not  exist
# End  of  the  class
How  to   create  circular  linked   list
while  True:
	i = int(input("Enter  value  of  'i':  "))
	How  to  obtain  data  of  ith  node
	if  ???
		print(F'Node  {i}  does  not  exist')
	else:
		print(F'Data   of  node  {i}  is  :  {x}')
	ch = input('Do  you  wish  to  continue (y / n) :  ')
	if  ch == 'N'  or  ch == 'n':
			break
# End  of  while  loop
print('Good  Bye')

    
    
# Write  a  method  to  search  for  a  value  in  the  linked  list.
class  circular_linked_list(linkedlist):
	def  search(a , x):
			How  to   return  the  node  when  'x'  is   found  in  the  linked  list  and  None  otherwise
# End  of  the  class
How  to   create  circular  linked   list
while  True:
	x = eval(input("Enter  value  to  be  searched :  "))
	How  to  search  for  'x'  in  the  linked  list
	if ??
		print(F'{x}  is  not  found')
	else:
		print(F'Found  at  address  :  ??? ')
	ch = input('Do  you  wish  to  continue (y / n) :  ')
	if  ch == 'N'  or  ch == 'n':
			break
# End  of  while  loop
print('Good  Bye')

    
    
#  Write  a  method  to  insert  a  node  in  the  linked  list
class  circular_linked_list(cll):
	def  insert(a , i , x):
		if  'i'  is  an  invalid  node  number:
				print(F'Node  {i}  does  not  exist')
		elif  cll  is  empty:
				How  to  create  a  new  node
				How  to  insert  a  node  into  empty  cll
		elif  insertion  at  the  begining:
				How  to  create  a  new  node
				How  to  insert  a  node  at  the  begining  of  cll
		else:
			How  to  create  a  new  node
			How  to  insert  a  node  after  ith  node  of  cll
# End  of  the  class
How  to   create  circular  linked   list
while  True:
	i = int(input("Enter  value  of  'i' :  "))
	x = eval(input('Enter  value  to  be  inserted  :  '))
	How  to  insert  'x'  after  ith  node
	How  to  print linked  list
	ch = input('Would  you  like  to  insert  another  node (Y  or   N) ?  :  ')
	if  ch == 'n'  or  ch == 'N':
		break

    
# Write  a  method  to  delete  ith  node  of  linked  list
class  circular_linked_list(cll):
	def  delete(a , i):
		if  'i'  is  an  invalid  node  number:
				return  None
		elif  cll  has  single  node
				How  to  delete  the  single  node  and  return  data  of  deleted  node
		elif  deletion  of  first  node:
				How  to  delete  the  fist  node  and  return  data  of  deleted  node
		else:
			How  to  delete  ith  node  and  return  data  of  deleted  node
# End  of  the  class
How  to   create  circular  linked   list
while  True:
	i = int(input('Enter  value  of  i  :  '))
	How  to  delete   ith  node
	if  ???
			print(F'Node  {i}  does  not  exist')
	else:
			print('Data  of  deleted  node  is  ' ,  x)
	How  to  print  linked  list
	ch = input('Would  you  like  to  delete  another  node (Y  or   N) ?  :  ')
	if  ch == 'n'  or  ch == 'N':
		break



#  Tricky 
#  Write  destructor  to  delete  whole  linked  list
class  circular_linked_list(linkedlist):
	def    _del_(a):
			if  linked  list  is  empty:
					print('Linked  list  is  already  empty')
			else:
					How  to  delete  each  node  of  cll
					print('Linked  list  is  empty')
#  End  of  the  clas
How  to   create  circular  linked   list

    
    
#  Write  a  method  to  copy  a  linked  list
class  circular_linked_list(linkedlist):
	def  copy(a):
		How  to  create  a  new  cll object  to  hold  the  result
		if  input  cll  is  empty
			output  cll  is   empty
		else:
			How  to  copy  each  node  of  cll  held  by  object  'a'  to 'b'
			# End  of  while  loop
		return  output  cll
#  End  of  the  clas
How  to   create  circular  linked   list
How  to  copy  linked  list
How  to  print  input  cll
How  to  print  output  cll



#  Write  methods  to  create  and  print  linked  list
class  node:
		def   _init_(new  , x):
				How   to   add  data  field  to   new  node  with  'x'
		# new  = node(25)
class  linkedlist:
		def   _init_(a):
				How  to  add  'l'  and  'r'  to  object  'a'
		# a = linkedlist()
		def  isempty(a):
				return  True  when  dll  is  empty  and  False  otherwise
		# a . isempty()  --->  True / False
		def  disp_left_right(a):
				if  dll  is  empty:
						print('Linked  List  is  empty')
				else:
						How  to  print  data  field  of  each  node  from  left  to  right  in  same  line
		def  disp_right_left(a):
				if  dll  is  empty:
						print('Linked  List  is  empty')
				else:
						How  to  print  data  field  of  each  node  from  right  to  left  in  same  line
		def  append(a , new):
				if  dll  is  empty:
						How  to  append  new  node  to  empty  dll
				else:
						How  to append  new  node  to  existing  dll
		def  create(a):
				How  to   create  dll  i.e.  Append   each  node  to  dll
# End  of  the  class
if  _name_ == '_main_':
	How  to  create  dll
	print('Linked  List   from  left  to  right  :  ' , end = '')
	How  to  print  dll  from  left  to  right
	print('Linked  List   from  right  to  left  :  ' , end = '')