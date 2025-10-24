#  Write  a  method  to  determine  length  of  circular  linked  list
from cll import  linkedlist , node
class  cll(linkedlist):
	def  length(a):
			ctr=0
			p=a.first 
			while True:
						ctr+=1
						p=p.link
						if p==a.first:
							break 
			return ctr   #How  to  return  number  of  nodes  in  circular  linked  list
# End  of  the  class
if  __name__  ==  '__main__':
	a=cll()
	a.create()  #How  to   create  circular  linked   list
	print('Number  of  nodes : ' , a.length())
from  cllLength  import  *
class  circular_linked_list(cll):
	def  find(a , i):
		if i < 0  or  i >= a.length():
			return None
		else:
			p=a.first
			for j in range(i-1):
				p=p.link
			return p.data

			 # return   data  of  ith  node  and  None  when  ith  node  does  not  exist
# End  of  the  class
a=circular_linked_list()
a.create()  #How  to   create  circular  linked   list
while  True:
	i = int(input("Enter  value  of  'i':  "))
	x = a.find(i)
	if  x==None:
		print(F'Node  {i}  does  not  exist')
	else:
		print(F'Data   of  node  {i}  is  :  {x}')
	ch = input('Do  you  wish  to  continue (y / n) :  ')
	if  ch == 'N'  or  ch == 'n':
			break
# End  of  while  loop
print('Good  Bye')

# Write  a  method  to  search  for  a  value  in  the  linked  list.
from cll  import  *
class  circular_linked_list(linkedlist):
	def  search(a , x):
			p=a.first
			while True:
				if  p.data == x:
					return p   #How  to   return  the  node  when  'x'  is   found  in  the  linked  list
				p=p.link
				if  p == a.first:
					break
			return None     #How  to   return  the  node  when  'x'  is   found  in  the  linked  list  and  None  otherwise
# End  of  the  class
a=circular_linked_list()
a.create()  #How  to   create  circular  linked   list
while  True:
	x = eval(input("Enter  value  to  be  searched :  "))
	y=a.search(x)  #How  to  search  for  'x'  in  the  linked  listn
	if y==None:
		print(F'{x}  is  not  found')
	else:
		print(F'Found  at  address  :  {y} ')
	ch = input('Do  you  wish  to  continue (y / n) :  ')
	if  ch == 'N'  or  ch == 'n':
			break
# End  of  while  loop
print('Good  Bye')

#  Write  a  method  to  insert  a  node  in  the  linked  list
from cllLength import  *
class  circular_linked_list(cll):
	def  insert(a , i , x):
		if  i<0  or  i>a.length():  #'i'  is  an  invalid  node  number:
				print(F'Node  {i}  does  not  exist')
		elif  a.isempty():  #cll  is  empty:
				new=node(x)  #How  to  create  a  new  node
				a.insert(new)  #How  to  insert  a  node  into  empty  cll
		elif  i==1:  #insertion  at  the  begining:
				new=node(x)  #How  to  create  a  new  node
				new.link=a.first  
				a.first=new
				 
				 #How  to  insert  a  node  at  the  begining  of  cll
		else:
			new=node(x)  #How  to  create  a  new  node
			p=a.first
			for j in range(i-1):
				p=p.link
			new.link=p.link
			p.link=new
			
			#How  to  insert  a  node  after  ith  node  of  cll
# End  of  the  class
a=circular_linked_list()
a.create()  #How  to   create  circular  linked   list
while  True:
	i = int(input("Enter  value  of  'i' :  "))
	x = eval(input('Enter  value  to  be  inserted  :  '))
	a.insert(i , x)  #How  to  insert  'x'  after  ith  node
	a.disp()  #How  to  print linked  list
	ch = input('Would  you  like  to  insert  another  node (Y  or   N) ?  :  ')
	if  ch == 'n'  or  ch == 'N':
		break
	


# Write  a  method  to  delete  ith  node  of  linked  list
from cllLength import  *
class  circular_linked_list(cll):
	def  delete(a , i):
		if i<1  or  i>a.length():  #'i'  is  an  invalid  node  number:
				return  None
		elif  a.length()==1:  #cll  has  single  node
				a.first=None    #How  to  delete  the  single  node  and  return  data  of  deleted  node
		elif  i==1:  #deletion  of  first  node:
				a.first=a.first.link  #How  to  delete  the  fist  node  and  return  data  of  deleted  node
		else:
			p=a.first   #How  to  delete  ith  node  and  return  data  of  deleted  node
			for  j  in  range(i-2):
				p=p.link
			x=p.link.data
			p.link=p.link.link
			return  x
# End  of  the  class
a=circular_linked_list()
a.create()  #How  to   create  circular  linked   list
while  True:
	i = int(input('Enter  value  of  i  :  '))
	x=a.delete(i) #How  to  delete   ith  node
	if  x==None:
			print(F'Node  {i}  does  not  exist')
	else:
			print('Data  of  deleted  node  is  ' ,  x)
	a.disp()  #How  to  print  linked  list
	ch = input('Would  you  like  to  delete  another  node (Y  or   N) ?  :  ')
	if  ch == 'n'  or  ch == 'N':
		break

#  Tricky 
#  Write  destructor  to  delete  whole  linked  list
from cll import  *
class  circular_linked_list(linkedlist):
	def    __del__(a):
		if  a.isempty():  #linked  list  is  empty:
					print('Linked  list  is  already  empty')
		else:
					p=a.first   #How  to  delete  each  node  of  cll
					while a.first != None:
						a.first=a.first.link
						del p
						p=p.link
						
					print('Linked  list  is  empty')
#  End  of  the  clas
a=circular_linked_list()
a.create()  #How  to   create  circular  linked   list


#  Write  a  method  to  copy  a  linked  list
from cll import  *
class  circular_linked_list(linkedlist):
	def  copy(a):
		b=circular_linked_list()  #How  to  create  a  new  cll object  to  hold  the  result
		if a.isempty():  #input  cll  is  empty
			return None# output  cll  is   empty
		else:
			p=a.first  #How  to  copy  each  node  of  cll  held  by  object  'a'  to 'b'
            
			while p.link!=a.first:
							new=node(p.data)  #How  to  create  a  new  node
							p=p.link
							  #How  to  create  a  new  node
							b.append(new)  #How  to  insert  a  node  into  empty  cll
			# End  of  while  loop
		return b
#  End  of  the  clas
a=circular_linked_list()
a.create()  #How  to   create  circular  linked   list
b=a.copy()  #How  to  copy  linked  list
a.disp()  #How  to  print  input  cll
b.disp()  #How  to  print  output  cll










