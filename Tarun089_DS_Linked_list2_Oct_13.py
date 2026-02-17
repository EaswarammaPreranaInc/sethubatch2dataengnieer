
#  Write  a  program   to  determine  length  of  linked  list

from  prog2   import  *     #  In  view  of  linked_list  class
class  sll(linked_list):    #  constructor , isempty() , disp() , append()  and  create()  are  inherited
	def  length(a):
			p = a . first   #  Ref  'p'  points  to  first  node  of  linked  list
			ctr = 0
			while   p  != None:  #  Repeat  until  ref  'p'  becomes  None
				ctr += 1    #  Counts  each  node  of  linked  list
				p = p . link  #  Moves  ref  'p'  to  next  node
			return  ctr
# End  of  the  class
if  _name_  ==  '_main_':
	a = sll()               #  Constructor  of  parent  class  (i.e.  linked_list  class)  initializes   object  with  first = None
	a . create()            #  Creates  a  linked  list  whose  address  is  stored  in  object  'a'
	print('Number  of  nodes : ' , a . length())






'''
Write  a  progam  to  determine  data  of  ith  node

1) What  does  method  do  when  ith  node  exists ?  --->  Return  data  of  ith  node

2) What  does  method  do  when  ith  node  does  not  exist ?  --->  Return  None
'''
from  prog4  import  *          #  In  view  of  sll  class
class  linkedlist(sll):         #  constructor , isempty() , disp() , append() , create()  and  len()  are  inherited
	def  find(a , i):
			if  i < 1  or  i > a . length():
				return  None    #  Executed  when  'i'  is  not  between  1  and  length()
			p = a . first       #  Ref  'p' points  to  first  node  of  linked  list
			for  j  in  range(i - 1):  #  Moves  ref  'p'  to  ith  node  by  executing  loop  (i - 1)  times
				p = p . link
			return  p . data    #  Data  of  ith  node
# End  of  the  class
a = linkedlist()                #  Constructor  of   grand  parent  class  (i.e.  linked_list  class)  initializes   object  with  first = None
a . create()                    #  Creates  a  linked  list  whose  address  is  stored  in  object  'a'
while  True:
	i = int(input("Enter  value  of  'i':  "))
	x = a . find(i)             #  Returns  data  of  ith  node  (or)  None
	if  x == None:
		print(F'Node  {i}  does  not  exist')
	else:
		print(F'Data   of  node  {i}  is  :  {x}')
	ch = input('Do  you  wish  to  continue (y / n) :  ')
	if  ch == 'N'  or  ch == 'n':
			break
# End  of  while  loop
print('Good  Bye')







'''
Write  a  method  to  search  for  a  value  in  the  linked  list.

1) What  action  to  be  made  when  'x'  is  not  in  the  node  of  linked  list ?  --->  Move  reference  to  the  next  node

2) What  action  to  be  made  when  'x'  is  in  the  current  node  ?  --->  Return  the  node   where  'x'  is  found

3) What  action  to  be  made  when  'x'  is  not  found  in  the  linked  list  ?  --->  return  None  outside  the  loop
'''
from  prog2  import  *      #  In  view  of  linked_list  class
class  singly_linked_list(linked_list):  #  constructor , isempty() , disp() , append()  and  create()  are  inherited
	def  search(a , x):
			p = a . first   #  Ref  'p' points  to  first  node  of  linked  list
			while  p != None:  #  Repeat  until  ref  'p'  becomes  None
				if  p . data == x:   # Compares  'x'  with  data  of  each  node  in  linked  list
						return  p  #  That  object  where  'x' is  found
				else:
						p = p . link   #  Moves  ref  'p'  to  next  node
			# End  of  while  loop
			return  None    #  'x'  is  not  found  in  the  linked   list
# End  of  the  class
a = singly_linked_list()    #  Constructor  of  parent  class  (i.e.  linked_list  class)  initializes   object  with  first = None
a . create()                #  Creates  a  linked  list  whose  address  is  stored  in  object  'a'
while  True:
	x = eval(input("Enter  value  to  be  searched :  "))
	p = a . search(x)       #  Returns  that  node  where   'x'  is  found  and  None  otherwise
	if  p == None:
		print(F'{x}  is  not  found')
	else:
		print(F'Found  at  that  node  whose  address  :  {id(p)}')
	ch = input('Do  you  wish  to  continue (y / n) :  ')
	if  ch == 'N'  or  ch == 'n':
			break
# End  of  while  loop
print('Good  Bye')





'''
Write  a  method  to  insert  a  node  in  the  linked  list
1) How  many  links  have  to  be  modified  for  insertion ?  --->  Two  links

2) How  to  insert  a  node  at  the  begining  of  linked list ?  --->  Modify  new  node  link  to  1st  node and modify  the  reference  a . first  to  new  node

3) How  to  insert  a  node  at  the  end  of  linked list ?  --->  Modify  new  node  link  to  None and modify  last  node  link  to  new  node

4) How  to  insert  a  node  after  ith  node ?  --->  Modify  new  node  link  to  (i + 1)th  node  and  modify  ith  node  link   to  new  node

5) In  which  order  can  links  be  modified ?  --->  Modify  new  node  link  first  and  then  existing  node  link

6) Is  logic  same  for  middle  insertion  and  insertion  at  the  end  ? --->  Yes

7) What  is  the  difference  between  insertion  at  the  begining  and  insertion  anywhere  else ?  --->
a . first  is  modified  when  node  is   inserted  at  the  begining  and
a . first  reference  remains  unchanged  when  node  is   inserted  anywhere  else
'''
from  prog4  import  *      #  In  view  of  sll  and  node  classes
class  linkedlist(sll):     #  constructor , isempty() , disp() , append() , create()  and  len()  are  inherited
	def  insert(a , i , x):
		if  i < 0  or  i > a . length(): 
				print(F'Node  {i}  does  not  exist')
		elif  i == 0:         #  Insertion  at  the   begining   (or)  Empty  linked  list
				new = node(x) #  Constructor  of  node  class  initialzes  object  with  data = x , link = None
				new . link = a . first  #  Attaches  new  node  and  first  node
				a . first = new  #  new  node  becomes  first  node
		else:               #  Insertion  in  the  middle  (or) at  the  end
			new  = node(x)  #  Constructor  of  node  class  initialzes  object  with  data = x , link = None
			p = a . first   #  Ref  'p' points  to  first  node  of  linked  list
			for  j  in  range(i - 1):  #  Moves  ref  'p'  to  ith  node  by  executing  loop  (i - 1)  times
					p = p . link
			new . link = p . link  # new  node  link  points to  (i + 1)th  node
			p . link = new  #  ith   node  link  points to  new  node
# End  of  the  class
a = linkedlist()            #  Constructor  of   grand  parent  class  (i.e.  linked_list  class)  initializes   object  with  first = None
a . create()                #  Creates  a  linked  list  whose  address  is  stored  in  object  'a'
while  True:
	i = int(input("Enter  value  of  'i' :  (0 - At  the  begin) "))
	x = eval(input('Enter  value  to  be  inserted  :  '))
	a . insert(i , x)       #  Inserts  'x'  after  ith  node
	a . disp()              #  Prints  linked  list
	ch = input('Would  you  like  to  insert  another  node (Y  or   N) ?  :  ')
	if  ch == 'n'  or  ch == 'N':
		break





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

from  prog4  import  *      
class linkedlist(sll):
    def delete(self, i):
        if i < 1 or i > self.length():  # Invalid node number
            return None
        # Delete first node
        if i == 1:
            temp = self.first
            self.first = temp.link  # Logical and physical deletion
            return temp.data
        # Delete middle or last node
        p = self.first
        for _ in range(i - 2):  # Move to (i-1)th node
            p = p.link
        temp = p.link  # Node to delete
        p.link = temp.link  # Modify (i-1)th node link
        return temp.data

# Main program
if __name__ == '__main__':
    a = linkedlist()
    a.create()
    while True:
        i = int(input('Enter value of i (node to delete): '))
        deleted_data = a.delete(i)
        if deleted_data is None:
            print(f'Node {i} does not exist')
        else:
            print('Data of deleted node is', deleted_data)
        print('Linked List:', end=' ')
        a.disp()
        ch = input('Would  you  like  to  delete  another  node (Y  or   N) ?  :  ')
        if  ch == 'n'  or  ch == 'N':
		break
