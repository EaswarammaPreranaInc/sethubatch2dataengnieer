'''
Write  a  funciton  to  concatenate  two  linked  lists

How  to  concatenate  two  linked list's ?  ---> Modify  last  node  link  of  1st  linked list  to  first  node  of  2nd  linked list
'''
from LinkedList import *
class  sll(linked_list):
	def  concat(a , b):
		if  a.first==None:      # 1st linked  list  is  empty:
			a.first=b.first     # 2nd  linked  list  is  the   result
		else:
			p=a.first
			while p.link!=None:
				p=p.link
			p.link=b.first      #How  to  attach  last  node  of  1st  LL  with  first  node  of  2nd  LL
#  End  of  the  class
a=sll() 
a.create()#How  to  create  1st  LL
b=sll()
b.create() #How  to  create  2nd  LL
a.concat(b) #How  to  concatenate  the  2  LL's
print('Linked  List  :  ' , end = '')
a.disp() #How  to  print  final  linked  list


#  Write  a  method  to  copy  a  linked  list
from LinkedList import *
class  sll(linked_list):
	def  copy(a):
		b=linked_list() #How  to  create  a  local  object  for  2nd  linked  list
		p=a.first   
		while p!=None:
				new=node(p.data)  
				p=p.link  
				b.append(new)   #How  to  copy  each  node  of  1st  LL  to  2nd  LL  until   LL  is  exhausted
		return b    #How  to   return  2nd  linked  list
#  End  of  the  clas
a=sll() 
a.create()  #How  to  create  1st  linked  list
b=sll()
b=a.copy()  #How  to  copy  1st  linked  list  to  2nd  linked  list
print('Original  linked   list  :  ' , end = '')
a.disp()  #How  to  print  1st  linked  list
print('Copied  linked   list  :  ' , end = '')
b.disp()  #How  to  print  2nd  linked  list


#  Write  destructor  to  delete  whole  linked  list
from LinkedList import *
class  sll(linked_list):
	def    __del__(a):
		while a.first!=None:
			p=a.first   
			a.first=a.first.link
			p=p.link	#How  to  remove  each  node  of  LL  until  LL  is  empty
			del p 
		print('Linked  list  is  empty')
#  End  of  the  clas
a=sll()
a.create()  #How  to  create  linked  list


'''
Write  a  method  to  reverse  linked  list

1) How  to  reverse  the  linked  list ?  ---> Modify  4th  node  link  to  3rd  node,
															        modify  3rd  node  link  to  2nd  node,
															        modify  2nd  node  link  to  1st  node,
															        modify  1st  node  link  to  NULL  and
															        modify  first  pointer  to  last  node

2) How  many  references  are  needed  to  reverse  a  linked  list  ?  ---> Three  i.e.  prev , cur , next

3) Where  does  ref  cur   points  to  (in  general) ?  ---> Current  node  i.e.  ith  node
    Where  does  ref  prev   points  to ?  ---> Previous  node  i.e.  (i - 1)th  node
    Where  does  ref  next  points  to ?  ---> Next  node  i.e.  (i + 1)th  node
'''
from LinkedList import *
class  sll(linked_list):
		def  reverse(a):
				cur=None  
				next=a.first
				while(next!=None):
					prev=cur
					cur=next
					next=next.link
					cur.link=prev  #How  to  reverse  each  node  of  linked  list
				a.first=cur  #How  to  modify  ref  a . frist   to   last  node  of  linked  list
# End  of  the  class
a=sll()
a.create()  #How  to  create  linked  list
print('Input  Linked  List')
a.disp()    #How  to  print  linked  list
a.reverse() #How  to  reverse  linked  list
print('Reverse  Linked  List')
a.disp()    #How  to  print  reverse  linked  list



