'''
Write  a  progam  to  determine  data  of  ith  node

1) What  does  method  do  when  ith  node  exists ?  --->  Return  data  of  ith  node

2) What  does  method  do  when  ith  node  does  not  exist ?  --->  Return  None
'''
from  len_sll import *;

class   linkedlist(len_sll):
    def  find(a , i):
        if i<1 or i>a.length():
            return None
        p=a.first
        for j in range(i-1):
            p=p.link
        return p.data
        
        
         #return  data  of  ith  node and  return  None  when  ith  node  does  not  exist
# End  of  the  class
if __name__=='__main__':
	ll=linkedlist()
	ll.create() #How  to  create  linked  list
	while  True:
		i = int(input("Enter  value  of  'i':  "))
		x=ll.find(i) #How  to   obtain  data  of  ith  node
		if  i==None:
			print(F'Node  {i}  does  not  exist')
		else:
			print(F'Data   of  node  {i}  is  : {x}')
		ch = input('Do  you  wish  to  continue (y / n) :  ')
		if  ch == 'N'  or  ch == 'n':
				break
	# End  of  while  loop
	print('Good  Bye')