
#1st program
from linkedlist import *
#  Write  a  program   to  determine  length  of  linked  list
class  sll(linked_list):
	def  length(a):
		count  =  0
		p  =  a . first
		while  p  !=  None:
			count  +=  1
			p  =  p . link
		return  count
# End  of  the  class
if  __name__  ==  '__main__':
	a=sll()
	a.create()#How  to  create  linked  list
	print('Number  of  nodes : ' , a.length())


#2nd program
'''
Write  a  progam  to  determine  data  of  ith  node

1) What  does  method  do  when  ith  node  exists ?  --->  Return  data  of  ith  node

2) What  does  method  do  when  ith  node  does  not  exist ?  --->  Return  None
'''
from sll import *
class   linkedlist(sll):
	def  find(a , i):
			if i>1 and i<a.length():
				p= a.first
				for j in range(i-1):
					p= p.link
				return p.data#return  data  of  ith  node
			else:
				return  None  
# End  of  the  class
a= linkedlist()
a.create()#How  to  create  linked  list
while  True:
	i = int(input("Enter  value  of  'i':  "))
	a.find(i)#How  to   obtain  data  of  ith  node
	if  a.find(i)==None:
		print(F'Node  {i}  does  not  exist')
	else:
		print(F'Data   of  node  {i}  is  :  ' , a.find(i))
	ch = input('Do  you  wish  to  continue (y / n) :  ')
	if  ch == 'N'  or  ch == 'n':
			break
# End  of  while  loop
print('Good  Bye')


#3rd program

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


#4th program
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
	

#5th program
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
	


