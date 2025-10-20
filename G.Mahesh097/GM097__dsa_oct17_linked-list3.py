
'''
Write  a  funciton  to  concatenate  two  linked  lists

How  to  concatenate  two  linked list's ?  ---> Modify  last  node  link  of  1st  linked list  to  first  node  of  2nd  linked list
'''
from prog2 import *
class  sll(linked_list):
	def  concat(a , b):
		if  a.isempty():
			a.first=b.first		# 2nd  linked  list  is  the   result
		else:
			last=a.first
			while last.link!=None:
				last=last.link
			last.link=b.first	# How  to  attach  last  node  of  1st  LL  with  first  node  of  2nd  LL
#  End  of  the  class
a=sll()
a.create()  # How  to  create  1st  LL
b=sll()
b.create()  # How  to  create  2nd  LL
a.concat(b) # How  to  concatenate  the  2  LL's
print('Linked  List  :  ' , end = '')
a.disp()    # How  to  print  final  linked  list

'''
output:
enter values terminated by ctrl+z  10 20 30 40 50
enter values terminated by ctrl+z  60 70 80
Linked  List  :  10	20	30	40	50	60	70	80	
'''






#  Write  a  method  to  copy  a  linked  list

class  sll(linked_list):
	def  copy(a):
			b=sll() # How  to  create  a  local  object  for  2nd  linked  list
			p=a.first
			while p!=None:
				new=node(p.data)
				b.append(new)
				p=p.link  # How  to  copy  each  node  of  1st  LL  to  2nd  LL  until   LL  is  exhausted
			return b  # How  to   return  2nd  linked  list
#  End  of  the  clas
a=sll()
a.create()  # How  to  create  1st  linked  list
b=a.copy()  # How  to  copy  1st  linked  list  to  2nd  linked  list
print('Original  linked   list  :  ' , end = '')
a.disp()  # How  to  print  1st  linked  list
print('Copied  linked   list  :  ' , end = '')
b.disp()  # How  to  print  2nd  linked  list

'''
output:
enter values terminated by ctrl+z
Original  linked   list  :  10	20	40	50	
Copied  linked   list  :  10	20	40	50	
'''





#  Write  destructor  to  delete  whole  linked  list

class  sll(linked_list):
	def __del__(a):
        while not a.isempty():
            temp=a.first
			a.first=a.first.link
			del temp # How  to  remove  each  node  of  LL  until  LL  is  empty
		print('Linked  list  is  empty')
#  End  of  the  clas
a=sll()
a.create()
a.disp()
del a # How  to  create  linked  list

'''
output:
enter values terminated by ctrl+z
10	20	30	40	50	
Linked  list  is  empty
'''





'''
Write  a  method  to  reverse  linked  list

1) How  to  reverse  the  linked  list ?  --->  Modify  4th  node  link  to  3rd  node,
                                                modify  3rd  node  link  to  2nd  node,
                                                modify  2nd  node  link  to  1st  node,
										        modify  1st  node  link  to  NULL  and
										        modify  first  pointer  to  last  node

2) How  many  references  are  needed  to  reverse  a  linked  list  ?  ---> Three  i.e.  prev , cur , next

3) Where  does  ref  cur   points  to  (in  general) ?  ---> Current  node  i.e.  ith  node
    Where  does  ref  prev   points  to ?  ---> Previous  node  i.e.  (i - 1)th  node
    Where  does  ref  next  points  to ?  ---> Next  node  i.e.  (i + 1)th  node
'''
class  sll(linked_list):
    def  reverse(a):
        prev=None
        cur=a.first
        while cur!=None:
            next=cur.link
            cur.link=prev
            prev=cur
            cur=next  # How  to  reverse  each  node  of  linked  list
        a.first=prev  # How  to  modify  ref  a . frist   to   last  node  of  linked  list
# End  of  the  class
a=sll()
a.create()  # How  to  create  linked  list
print('Input  Linked  List: ',a.disp())  # How  to  print  linked  list
a.reverse()  # How  to  reverse  linked  list
print('Reverse  Linked  List: ',a.disp())  # How  to  print  reverse  linked  list

'''
output:
enter values terminated by ctrl+z
Input  Linked  List: 10	20	30	40	50	
Reverse  Linked  List: 50	40	30	20	10	 
'''