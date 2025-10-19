'''
Write  a  method  to  search  for  a  value  in  the  linked  list.

1) What  action  to  be  made  when  'x'  is  not  in  the  node  of  linked  list ?  --->  Move  reference  to  the  next  node

2) What  action  to  be  made  when  'x'  is  in  the  current  node  ?  --->  Return  address  of  that  node

3) What  action  to  be  made  when  'x'  is  not  found  in  the  linked  list  ?  --->  return  None  outside  the  loop
'''
from  single_linked_list  import *

class  sll_search(linked_list):
    def  search(a , x):
        p=a.first
        while p!=None: 
            if p.data==x:
                return p
            else:
                p=p.link
    
	    #return  address  of  that  node  where  'x'  is  found  and  None  otherwise
# End  of  the  class

sh=sll_search() 
sh.create()#How  to  create  linked  list
while  True:
	x = eval(input("Enter  value  to  be  searched :  "))
	s=sh.search(x) #How  to  call  search()  method
	if  x== None:
		print(F'{x}  is  not  found')
	else:
		print(F'Found  at  address  :{s}')
	ch = input('Do  you  wish  to  continue (y / n) :  ')
	if  ch == 'N'  or  ch == 'n':
			break
# End  of  while  loop
print('Good  Bye')