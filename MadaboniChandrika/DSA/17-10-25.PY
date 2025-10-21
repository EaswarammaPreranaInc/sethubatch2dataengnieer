#1st program
'''
Write  a  function  to  concatenate  two  linked  lists

How  to  concatenate  two  linked list's ?  ---> Modify  last  node  link  of  1st  linked list  to  first  node  of  2nd  linked list
'''
from prog2 import *
class  sll(linked_list):
	def  concat(a , b):
		if a.first==None:#linked  list  is  empty
			return b #2nd  linked  list  is  the   result
		else:
			last=a.first
			while last.link!=None:
				last=last.link
			last.link=b.link
			return a	#How  to  attach  last  node  of  1st  LL  with  first  node  of  2nd  LL
#  End  of  the  class
ll1=sll()
ll1.create()#How  to  create  1st  LL
ll2=sll()
ll2.create()#How  to  create  2nd  LL
x=sll.concat(ll1,ll2)#How  to  concatenate  the  2  LL's
print('Linked  List  :  ' , end = '')
x.disp()#How  to  print  final  linked  list


#2nd program
#  Write  a  method  to  copy  a  linked  list
class  sll(linked_list):
	def  copy(a):
			b=linked_list()#How  to  create  a  local  object  for  2nd  linked  list
			p=a.first#How  to  copy  each  node  of  1st  LL  to  2nd  LL  until   LL  is  exhausted
			while p is not None:
				b.append(p.data)   # assuming append() already exists in linked_list
				p = p.link
			return b #How  to   return  2nd  linked  list
#  End  of  the  clas
L1 = linked_list()#How  to  create  1st  linked  list
L1.copy()#How  to  copy  1st  linked  list  to  2nd  linked  list
print('Original  linked   list  :  ' , end = '')
L1.disp()#How  to  print  1st  linked  list
print('Copied  linked   list  :  ' , end = '')
L2 = sll.copy(L1)
L2.disp()#How  to  print  2nd  linked  list


#3rd program
#  Write  destructor  to  delete  whole  linked  list
from prog2 import *
class  sll(linked_list):
	def    __del__(a):
			p=a.first
			while p !=None:
				q=p
				p=p.link
				del q
			a.first=None		#How  to  remove  each  node  of  LL  until  LL  is  empty
			print('Linked  list  is  empty')
#  End  of  the  clas
L1=sll()
L1.create()#How  to  create  linked  list


#4th program
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
from prog3 import*
class  sll(linked_list):
		def  reverse(a):
				prev=None
				cur=a.first
				while cur !=None:
					next=cur.link
					cur.link=prev
					prev=cur
					cur=next
				a.first=prev	#How  to  reverse  each  node  of  linked  list
				#How  to  modify  ref  a . frist   to   last  node  of  linked  list
# End  of  the  class
a=sll()
a.create()#How  to  create  linked  list
print('Input  Linked  List')

a.reverse()# How  to  reverse  linked  list
print('Reverse  Linked  List')
a.disp()#How  to  print  reverse  linked  list


