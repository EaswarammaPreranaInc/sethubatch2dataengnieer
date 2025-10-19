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
from  len_sll import *
class  linkedlist(len_sll):
    def  insert(a , i , x):
        if  i<0 or i>a.length():
            print(F'Node  {i}  does  not  exist')
        elif  i==0:
            new=node(x)
            new.link=a.first
            a.first=new #How  to  create  a  new  node  #How  to  insert  new  node  at  the  begining  of  LL
        else:
            new=node(x) #How  to  create  a  new  node
            p=a.first
            for i in range(i-1):
                p=p.link
            new.link=p.link
            p.link=new  

			#How  to  insert  new  node  after  ith  node  of  LL
# End  of  the  class
if __name__=='__main__':
	ll=linkedlist()
	ll.create() #How  to  create  a  linked  list
	while  True:
		i = int(input("Enter  value  of  'i' :  "))
		x = eval(input('Enter  value  to  be  inserted  :  '))
		ll.insert(i,x) #How  to  insert   new  node  after   ith  node
		print('Linked  List  :  ' , end = '')
		ll.disp() #How  to  print  linked  list
		ch = input('Would  you  like  to  insert  another  node (Y  or   N) ?  :  ')
		if  ch == 'n'  or  ch == 'N':
			break