#  Write  a  program   to  determine  length  of  linked  list
from prog2 import*
class  sll(linked_list):
	def  length(a):
			p=a.first
			ctr=0
			while p!=None:
				ctr+=1
				p=p.link
			return ctr #return  number  of  nodes  in  the  linked  list
# End  of  the  class
if  __name__  ==  '__main__':
	a=sll()
	a.create()#How  to  create  linked  list
	print('Number  of  nodes : ' , a.length())
'''
Enter  values  terminated  by  ctrl+z
10
20
30
40
^Z
Number  of  nodes :  4
'''


'''
Write  a  progam  to  determine  data  of  ith  node

1) What  does  method  do  when  ith  node  exists ?  --->  Return  data  of  ith  node

2) What  does  method  do  when  ith  node  does  not  exist ?  --->  Return  None
'''
from prog3 import *
class   linkedlist(sll):
	def  find(a , i):
		if i < 1 or i > a.length():
			return None 
		p=a.first
		for j in range (i-1):
			p=p.link
		return p.data
# End  of  the  class
a=linkedlist()
a.create()#How  to  create  linked  list
while  True:
	i = int(input("Enter  value  of  'i':  "))
	x=a.find(i)#How  to   obtain  data  of  ith  node
	if x==None:
		print(F'Node  {i}  does  not  exist')
	else:
		print(F'Data   of  node  {i}  is  :  {x}')
	ch = input('Do  you  wish  to  continue (y / n) :  ')
	if  ch == 'N'  or  ch == 'n':
			break
# End  of  while  loop
print('Good  Bye')
'''
o/p:
Enter  values  terminated  by  ctrl+z
10
20
30
40
^Z
Enter  value  of  'i':  3
Data   of  node  3  is  :  30
Do  you  wish  to  continue (y / n) :  y
Enter  value  of  'i':  5

'''




'''
Write  a  method  to  search  for  a  value  in  the  linked  list.

1) What  action  to  be  made  when  'x'  is  not  in  the  node  of  linked  list ?  --->  Move  reference  to  the  next  node

2) What  action  to  be  made  when  'x'  is  in  the  current  node  ?  --->  Return  address  of  that  node

3) What  action  to  be  made  when  'x'  is  not  found  in  the  linked  list  ?  --->  return  None  outside  the  loop
'''
from prog2 import*
class  sll(linked_list):
	def  search(a , x):
		p=a.first
		while p!=None:
			if p.data==x:
				return p 
			else:
				p=p.link
		return None
# End  of  the  class
a=sll()
a.create()#How  to  create  linked  list
while  True:
	x = eval(input("Enter  value  to  be  searched :  "))
	p=a.search(x)#How  to  call  search()  method
	if  p==None:
		print(F'{x}  is  not  found')
	else:
		print(F'Found  at  address  :  {p.link}')
	ch = input('Do  you  wish  to  continue (y / n) :  ')
	if  ch == 'N'  or  ch == 'n':
			break
# End  of  while  loop
print('Good  Bye')


'''
o/p:
Enter  values  terminated  by  ctrl+z
10
10.8
3+4j
'hyd'
22
^Z
Enter  value  to  be  searched :  'hyd'
Found  at  address  :  <prog2.node object at 0x000002A35050E650>
Do  you  wish  to  continue (y / n) :  y
Enter  value  to  be  searched :  5
5  is  not  found
Do  you  wish  to  continue (y / n) :  n
Good  Bye


'''


'''
Write  a  method  to  insert  a  node  in  the  linked  list
1) How  many  links  have  to  be  modified  for  insertion ?  --->  Two  links

2) How  to  insert  a  node  at  the  begining  of  linked list ?  --->  Modify  new  node  link  to  1st  node modify  the  reference  a . first  to  new  node

3) How  to  insert  a  node  at  the  end  of  linked list ?  --->  Modify  new  node  link  to  None and modify  last  node  link  to  new  node

4) How  to  insert  a  node  after  ith  node ?  --->  Modify  new  node  link  to  (i + 1)th  node  and
																		        modify  ith  node  link   to  new  node

5) In  which  order  can  links  be  modified ?  --->  Modify  new  node  link  first  and  then  existing  node  link

6) Is  logic  same  for  middle  insertion  and  insertion  at  the  end  ? --->  Yes

7) What  is  the  difference  between  insertion  at  the  begining  and  insertion  anywhere  else ?  --->
															a . first  is  modified  when  node  is   inserted  at  the  begining  and
															a . first  reference  remains  unchanged  when  node  is   inserted  anywhere  else
'''
from prog3 import*
class  linkedlist(sll):
	def  insert(a , i , x):
		if  i<0 or i>a.length():
				print(F'Node  {i}  does  not  exist')
		elif  i==0:#insertion  at  the  begining  of  LL
				new=node(x)#How  to  create  a  new  node
				new.link=a.first#How  to  insert  new  node  at  the  begining  of  LL
				a.first=new
		else:
			new=node(x)#How  to  create  a  new  node
			p=a.first#How  to  insert  new  node  after  ith  node  of  LL
			for  j in range(i-1):
				p=p.link
			new.link=p.link
			p.link= new
# End  of  the  class
a=linkedlist()
a.create()#How  to  create  a  linked  list
while  True:
	i = int(input("Enter  value  of  'i' :  "))
	x = eval(input('Enter  value  to  be  inserted  :  '))
	a.insert(i,x)#How  to  insert   new  node  after   ith  node
	print('Linked  List  :  ' , end = '')
	a.disp()#How  to  print  linked  list
	ch = input('Would  you  like  to  insert  another  node (Y  or   N) ?  :  ')
	if  ch == 'n'  or  ch == 'N':
		break
	

'''
o/p:
Enter  values  terminated  by  ctrl+z
2
3
4
^Z
Enter  value  of  'i' :  3
Enter  value  to  be  inserted  :  33
Linked  List  :  2      3       4       33
Would  you  like  to  insert  another  node (Y  or   N) ?  :  y
Enter  value  of  'i' :  0
Enter  value  to  be  inserted  :  22
Linked  List  :  22     2       3       4       33

'''    



'''
Write  a method  to  delete  ith  node  of  linked  list

1) How  many  links  have  to  be  modifed  for  deletion ?  --->  Single  link

2) How  to  remove  ith  node  of  linked list ?  --->  Modify  (i - 1)th  node  link  to  (i + 1)th  node

3) How  to  remove  first  node  of  linked list ?  --->  Move  a . first  to  2nd  node

4) How  to  remove  last  node  of  linked list ?  --->  Modify  last  but  one  node  link  to  None

5) How  to  remove  the  node  when  there  is  a  single  node  in  linked  list  ?  --->  Reinitialize  a . first  to  None

6) Logic  for  middle  node  and  last  node  deletion  is  same

7) Similarly  logic  for  first  node  and  single  node  deletion  is  same
'''
from prog3 import*
class  linkedlist(sll):
	def  delete(a , i):
		if  i<1 or i> a.length():
			return None
		elif i==1:
			p=a.first
			a.first=a.first.link
			#How  to  delete  first  node  logically
			x=p.data
			del p#How  to  delete  first  node  physically
			return x#How  to  return  data  of  the  deleted  node
		else:
			p=a.first
			for j in range(i-2):
				p=p.link
				next=p.link
				p.link=next.link#How  to  modify  (i - 1)th  node  link  to  (i + 1)th node
				x=next.data
				del next#How  to  delete  ith  node
				return x#How  to  return  data  of  the  deleted  node
# End  of  the  class
a=linkedlist()
a.create()#How  to  create  linked  list
while  True:
	i = int(input('Enter  value  of  i  :  '))
	x=a.delete(i)#How  to  delete  ith  node
	if  x==None:
			print(F'Node  {i}  does  not  exist')
	else:
			print('Data  of  deleted  node  is  ' ,x)
	print('Linked  List  :  ' , end = '')
	a.disp()#How  to  print  linked  list
	ch = input('Would  you  like  to  delete  another  node (Y  or   N) ?  :  ')
	if  ch == 'n'  or  ch == 'N':
		break
	

'''
o/p:
Enter  values  terminated  by  ctrl+z
12
23
34
55
^Z
Enter  value  of  i  :  3
Data  of  deleted  node  is   34
Linked  List  :  12     23      55
'''    



'''
Write  a  funciton  to  concatenate  two  linked  lists

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


'''
o/p:
Enter  values  terminated  by  ctrl+z
^Z
Enter  values  terminated  by  ctrl+z
12
3
4
^Z
Linked  List  :  12     3       4
'''



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

'''
o/p:
Enter  values  terminated  by  ctrl+z
1
2
3
4
^Z
Linked  list  is  empty
'''




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


'''
o/p:
Enter  values  terminated  by  ctrl+z
12
23
34
56
^Z
Input  Linked  List
Reverse  Linked  List
56      34      23      12

'''
