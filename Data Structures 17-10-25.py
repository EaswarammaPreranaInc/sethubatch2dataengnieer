'''
Write  a  funciton  to  concatenate  two  linked  lists

How  to  concatenate  two  linked list's ?  ---> Modify  last  node  link  of  1st  linked list  to  first  node  of  2nd  linked list
'''
class  sll(linked_list):
	def  concat(a , b):
		if  a . isempty() # first  linked  list  is  empty:
			a . first = b.first() # 2nd  linked  list  is  the   result
		else:
			# How  to  attach  last  node  of  1st  LL  with  first  node  of  2nd  LL
			p = a.first
            		while p.link != None:   
                		p = p.link
            		p.link = b.first  
#  End  of  the  class
# How  to  create  1st  LL
a = linked_list()
a . create() 
# How  to  create  2nd  LL
b = linked_list()
b . create()
How  to  concatenate  the  2  LL's
print('Linked  List  :  ' , end = '')
concat(a , b) # How  to  print  final  linked  list


#  Write  a  method  to  copy  a  linked  list
class  sll(linked_list):
	def  copy(a):
			b = linked_list() # How  to  create  a  local  object  for  2nd  linked  list
			# How  to  copy  each  node  of  1st  LL  to  2nd  LL  until   LL  is  exhausted
			if a.isempty():
				return b
			# How  to   return  2nd  linked  list	
			p = a.first
			while p != None:
				new = node(p.data)     
				b.append(new)          
				p = p.link 
			return b
#  End  of  the  clas
# How  to  create  1st  linked  list
a = linked_list()
# How  to  copy  1st  linked  list  to  2nd  linked  list
c = sll.copy(a)
print('Original  linked   list  :  ' , end = '')
# How  to  print  1st  linked  list
a . disp()
print('Copied  linked   list  :  ' , end = '')
# How  to  print  2nd  linked  list
c . disp()


#  Write  destructor  to  delete  whole  linked  list
class  sll(linked_list):
	def    __del__(a):
			How  to  remove  each  node  of  LL  until  LL  is  empty
			while not a.isempty():
            			temp = a.first          
            			a.first = a.first.link  
            			del temp             
			print('Linked  list  is  empty')
#  End  of  the  clas
# How  to  create  linked  list
a = linked_list()

